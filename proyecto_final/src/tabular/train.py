"""
train.py
Entrenamiento y evaluación del MLP para clasificación tabular.
Usa los tensores directamente (sin DataLoader).
"""

import torch
import torch.nn as nn

from sklearn.metrics import confusion_matrix

from preprocess import preprocess_pipeline
from model import MLP


# ─────────────────────────────────────────────
# 1. Configuración
# ─────────────────────────────────────────────

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", ".."))

DATA_PATH = os.path.join(
    ROOT_DIR, "data", "proyecto_final", "tabular", "phpnThNfi.arff"
)
INPUT_DIM  = 5
LR         = 0.001
EPOCHS     = 20


# ─────────────────────────────────────────────
# 2. Entrenamiento
# ─────────────────────────────────────────────

def train(model, X_train, y_train, criterion, optimizer, epochs: int):
    """
    Bucle de entrenamiento completo.

    En cada época:
      1. Pone el modelo en modo entrenamiento (activa dropout/batchnorm si existieran).
      2. Forward pass: obtiene logits para todo el conjunto de train.
      3. Calcula la pérdida con CrossEntropyLoss (espera logits, no probabilidades).
      4. Resetea gradientes acumulados del paso anterior.
      5. Backward pass: calcula gradientes mediante autodiferenciación.
      6. Actualiza pesos con Adam.

    Parameters
    ----------
    model     : MLP
    X_train   : torch.Tensor  (n_train, input_dim)
    y_train   : torch.Tensor  (n_train,)  – etiquetas enteras
    criterion : nn.CrossEntropyLoss
    optimizer : torch.optim.Adam
    epochs    : int
    """
    print("\n" + "=" * 45)
    print("  ENTRENAMIENTO")
    print("=" * 45)

    for epoch in range(1, epochs + 1):
        model.train()

        # Forward: logits de forma (n_train, num_classes)
        logits = model(X_train)

        # Pérdida: CrossEntropyLoss aplica softmax internamente
        loss = criterion(logits, y_train)

        # Backward
        optimizer.zero_grad()   # limpia gradientes del paso anterior
        loss.backward()         # calcula ∂loss/∂params
        optimizer.step()        # actualiza params: θ ← θ − lr·∇θ

        print(f"  Época {epoch:>2}/{epochs}  |  Loss: {loss.item():.4f}")

    print("=" * 45)


# ─────────────────────────────────────────────
# 3. Evaluación
# ─────────────────────────────────────────────

def evaluate(model, X_test, y_test):
    """
    Calcula la accuracy sobre el conjunto de prueba y devuelve las
    predicciones para análisis posterior (matriz de confusión).

    Se usa torch.no_grad() para desactivar el cálculo de gradientes,
    reduciendo el uso de memoria y acelerando la inferencia.

    Parameters
    ----------
    model  : MLP
    X_test : torch.Tensor  (n_test, input_dim)
    y_test : torch.Tensor  (n_test,)

    Returns
    -------
    accuracy : float            – proporción de aciertos (0–1)
    preds    : torch.Tensor     – clases predichas (n_test,)
    """
    model.eval()

    with torch.no_grad():
        logits = model(X_test)                      # (n_test, num_classes)
        preds  = torch.argmax(logits, dim=1)        # clase con mayor logit
        correct = (preds == y_test).sum().item()    # predicciones correctas
        accuracy = correct / len(y_test)

    return accuracy, preds


# ─────────────────────────────────────────────
# 4. Matriz de confusión
# ─────────────────────────────────────────────

def report_confusion_matrix(y_test, preds):
    """
    Convierte los tensores a numpy, calcula e imprime la matriz de confusión
    junto con un desglose de aciertos y totales por clase.

    La matriz cm[i][j] indica cuántas muestras de la clase real i
    fueron predichas como clase j. Los aciertos están en la diagonal.

    Parameters
    ----------
    y_test : torch.Tensor  (n_test,)  – etiquetas reales
    preds  : torch.Tensor  (n_test,)  – etiquetas predichas
    """
    # Convertir tensores a arrays de numpy para sklearn
    y_true = y_test.cpu().numpy()
    y_pred = preds.cpu().numpy()

    cm = confusion_matrix(y_true, y_pred)

    print("\n" + "=" * 45)
    print("  MATRIZ DE CONFUSIÓN")
    print("=" * 45)
    print(cm)

    # — Desglose por clase: aciertos y totales —
    print("\n  Detalle por clase:")
    print(f"  {'Clase':>6}  {'Aciertos':>9}  {'Total':>7}  {'% Clase':>8}")
    print("  " + "─" * 37)

    for i, row in enumerate(cm):
        hits  = row[i]           # diagonal: predicciones correctas de la clase i
        total = row.sum()        # todas las muestras reales de la clase i
        pct   = hits / total * 100 if total > 0 else 0.0
        print(f"  {i:>6}  {hits:>9}  {total:>7}  {pct:>7.1f}%")

    print("=" * 45)


# ─────────────────────────────────────────────
# 4. Pipeline principal
# ─────────────────────────────────────────────

def main():
    # — Datos —
    data = preprocess_pipeline(filepath=DATA_PATH)

    X_train     = data["X_train"]
    X_test      = data["X_test"]
    y_train     = data["y_train"]
    y_test      = data["y_test"]
    num_classes = data["num_classes"]

    # — Modelo —
    model = MLP(input_dim=INPUT_DIM, num_classes=num_classes)
    print(f"\n[✓] Modelo creado:\n{model}")

    # — Loss y optimizador (con manejo de desbalance) —

    # Calcular frecuencia de clases en entrenamiento
    class_counts = torch.bincount(y_train)

    # Calcular pesos inversos (más peso a la clase minoritaria)
    weights = 1.0 / class_counts.float()

    # Normalizar pesos (opcional pero recomendable)
    weights = weights / weights.sum()

    # Definir función de pérdida con pesos
    criterion = nn.CrossEntropyLoss(weight=weights)

    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    # — Entrenamiento —
    train(model, X_train, y_train, criterion, optimizer, epochs=EPOCHS)

    # — Evaluación —
    accuracy, preds = evaluate(model, X_test, y_test)

    print(f"\n  Accuracy en test : {accuracy * 100:.2f}%")
    print("─" * 45)

    # — Matriz de confusión —
    report_confusion_matrix(y_test, preds)
    print()


if __name__ == "__main__":
    main()
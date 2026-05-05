"""
train.py
Entrenamiento y evaluación del MLP para clasificación tabular.
Usa los tensores directamente (sin DataLoader).
"""

import os
import torch
import torch.nn as nn
from sklearn.metrics import confusion_matrix

from preprocess import preprocess_pipeline
from model import MLP


# ─────────────────────────────────────────────
# 1. Configuración
# ─────────────────────────────────────────────

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR  = os.path.abspath(os.path.join(BASE_DIR, "..", "..", ".."))
DATA_PATH = os.path.join(ROOT_DIR, "data", "proyecto_final", "tabular", "phpnThNfi.arff")

INPUT_DIM = 5
LR        = 0.001
EPOCHS    = 20


# ─────────────────────────────────────────────
# 2. Pesos de clase para manejo de desbalance
# ─────────────────────────────────────────────

def compute_class_weights(y_train: torch.Tensor) -> torch.Tensor:
    """
    Calcula pesos de clase proporcionales al desbalance del dataset.

    La fórmula estándar es:
        peso_i = n_total / (n_clases × n_i)

    Esto asigna mayor peso a las clases minoritarias sin normalizar
    a suma 1, preservando la escala relativa de la pérdida.
    Equivale al parámetro class_weight='balanced' de scikit-learn.

    Parameters
    ----------
    y_train : torch.Tensor  – etiquetas de entrenamiento

    Returns
    -------
    torch.Tensor con un peso por clase
    """
    class_counts = torch.bincount(y_train)          # [n_clase0, n_clase1]
    n_total      = len(y_train)
    n_classes    = len(class_counts)

    # peso_i = n_total / (n_clases * n_i)  →  clase minoritaria recibe más peso
    weights = n_total / (n_classes * class_counts.float())

    print(f"[✓] Pesos de clase calculados:")
    for i, (w, c) in enumerate(zip(weights, class_counts)):
        print(f"    Clase {i}: {c.item()} muestras → peso {w.item():.4f}")

    return weights


# ─────────────────────────────────────────────
# 3. Entrenamiento
# ─────────────────────────────────────────────

def train(model, X_train, y_train, criterion, optimizer, epochs: int):
    """
    Bucle de entrenamiento completo.

    En cada época:
      1. Pone el modelo en modo entrenamiento.
      2. Forward pass: obtiene logits para todo el conjunto de train.
      3. Calcula la pérdida con CrossEntropyLoss ponderada.
      4. Resetea gradientes acumulados del paso anterior.
      5. Backward pass: calcula gradientes.
      6. Actualiza pesos con Adam.

    Parameters
    ----------
    model     : MLP
    X_train   : torch.Tensor  (n_train, input_dim)
    y_train   : torch.Tensor  (n_train,)
    criterion : nn.CrossEntropyLoss
    optimizer : torch.optim.Adam
    epochs    : int
    """
    print("\n" + "=" * 45)
    print("  ENTRENAMIENTO")
    print("=" * 45)

    for epoch in range(1, epochs + 1):
        model.train()

        logits = model(X_train)             # forward pass
        loss   = criterion(logits, y_train) # pérdida ponderada

        optimizer.zero_grad()   # limpia gradientes del paso anterior
        loss.backward()         # calcula ∂loss/∂params
        optimizer.step()        # θ ← θ − lr·∇θ

        print(f"  Época {epoch:>2}/{epochs}  |  Loss: {loss.item():.4f}")

    print("=" * 45)


# ─────────────────────────────────────────────
# 4. Evaluación
# ─────────────────────────────────────────────

def evaluate(model, X_test, y_test):
    """
    Calcula la accuracy sobre el conjunto de prueba.

    Parameters
    ----------
    model  : MLP
    X_test : torch.Tensor  (n_test, input_dim)
    y_test : torch.Tensor  (n_test,)

    Returns
    -------
    accuracy : float
    preds    : torch.Tensor
    """
    model.eval()

    with torch.no_grad():
        logits  = model(X_test)
        preds   = torch.argmax(logits, dim=1)
        correct = (preds == y_test).sum().item()
        accuracy = correct / len(y_test)

    return accuracy, preds


# ─────────────────────────────────────────────
# 5. Matriz de confusión
# ─────────────────────────────────────────────

def report_confusion_matrix(y_test, preds):
    """
    Calcula e imprime la matriz de confusión con desglose por clase.

    cm[i][j] = muestras de clase real i predichas como clase j.
    Los aciertos están en la diagonal principal.

    Parameters
    ----------
    y_test : torch.Tensor  (n_test,)
    preds  : torch.Tensor  (n_test,)
    """
    y_true = y_test.cpu().numpy()
    y_pred = preds.cpu().numpy()

    cm = confusion_matrix(y_true, y_pred)

    print("\n" + "=" * 45)
    print("  MATRIZ DE CONFUSIÓN")
    print("=" * 45)
    print(cm)

    print("\n  Detalle por clase:")
    print(f"  {'Clase':>6}  {'Aciertos':>9}  {'Total':>7}  {'% Clase':>8}")
    print("  " + "─" * 37)

    for i, row in enumerate(cm):
        hits  = row[i]
        total = row.sum()
        pct   = hits / total * 100 if total > 0 else 0.0
        print(f"  {i:>6}  {hits:>9}  {total:>7}  {pct:>7.1f}%")

    print("=" * 45)


# ─────────────────────────────────────────────
# 6. Pipeline principal
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

    # — Pesos de clase (manejo de desbalance) —
    # Se usa la fórmula estándar: peso_i = n_total / (n_clases * n_i)
    # Esto penaliza más los errores en la clase minoritaria durante el entrenamiento.
    weights   = compute_class_weights(y_train)
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
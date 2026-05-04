"""
train.py
Entrenamiento y evaluación de la CNN para clasificación de imágenes.
Itera sobre batches via DataLoader. Usa GPU automáticamente si está disponible.
"""

import torch
import torch.nn as nn

from dataset import build_image_pipeline
from model import CNN


# ─────────────────────────────────────────────
# 1. Configuración
# ─────────────────────────────────────────────

LR     = 0.001
EPOCHS = 10

# Selecciona GPU (CUDA o MPS en Apple Silicon) si está disponible,
# de lo contrario usa CPU. Mover modelo y tensores al mismo device
# es obligatorio para que PyTorch pueda operar sobre ellos.
DEVICE = (
    "cuda" if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available()
    else "cpu"
)


# ─────────────────────────────────────────────
# 2. Entrenamiento
# ─────────────────────────────────────────────

def train(model, train_loader, criterion, optimizer, epochs: int, device: str):
    """
    Bucle de entrenamiento por batches.

    En cada época se itera sobre todos los batches del train_loader.
    Por cada batch:
      1. Mover imágenes y etiquetas al device (GPU/CPU).
      2. Forward pass: obtener logits.
      3. Calcular pérdida con CrossEntropyLoss.
      4. Limpiar gradientes acumulados (zero_grad).
      5. Backward pass: calcular gradientes.
      6. Actualizar pesos con Adam.

    La pérdida reportada por época es el promedio sobre todos los batches,
    lo que permite comparar épocas independientemente del tamaño del dataset.

    Parameters
    ----------
    model        : CNN
    train_loader : DataLoader
    criterion    : nn.CrossEntropyLoss
    optimizer    : torch.optim.Adam
    epochs       : int
    device       : str  – 'cuda', 'mps' o 'cpu'
    """
    print("\n" + "=" * 50)
    print("  ENTRENAMIENTO")
    print("=" * 50)

    model.train()

    for epoch in range(1, epochs + 1):
        running_loss = 0.0

        for images, labels in train_loader:
            # Mover batch al device seleccionado
            images = images.to(device)
            labels = labels.to(device)

            # Forward: (batch, num_classes) logits
            logits = model(images)

            # Pérdida batch
            loss = criterion(logits, labels)

            # Backward
            optimizer.zero_grad()   # limpia gradientes del paso anterior
            loss.backward()         # calcula ∂loss/∂params
            optimizer.step()        # θ ← θ − lr·∇θ

            running_loss += loss.item()

        # Pérdida promedio de la época
        avg_loss = running_loss / len(train_loader)
        print(f"  Época {epoch:>2}/{epochs}  |  Loss: {avg_loss:.4f}")

    print("=" * 50)


# ─────────────────────────────────────────────
# 3. Evaluación
# ─────────────────────────────────────────────

def evaluate(model, test_loader, device: str) -> float:
    """
    Calcula la accuracy del modelo sobre el conjunto de prueba.

    Itera sobre todos los batches del test_loader acumulando aciertos.
    torch.no_grad() desactiva el cálculo del grafo de gradientes,
    reduciendo el uso de memoria y acelerando la inferencia.

    Parameters
    ----------
    model       : CNN
    test_loader : DataLoader
    device      : str

    Returns
    -------
    float – accuracy global (0–1)
    """
    model.eval()

    total_correct = 0
    total_samples = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)

            logits  = model(images)                      # (batch, num_classes)
            preds   = torch.argmax(logits, dim=1)        # clase con mayor logit
            total_correct += (preds == labels).sum().item()
            total_samples += labels.size(0)

    return total_correct / total_samples


# ─────────────────────────────────────────────
# 4. Pipeline principal
# ─────────────────────────────────────────────

def main():
    print(f"\n[✓] Device seleccionado: {DEVICE}")

    # — Datos —
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", ".."))

    DATA_PATH = os.path.join(
        ROOT_DIR, "data", "proyecto_final", "imagenes", "potato_subset"
    )

    pipeline = build_image_pipeline(data_path=DATA_PATH)
    train_loader = pipeline["train_loader"]
    test_loader  = pipeline["test_loader"]
    num_classes  = pipeline["num_classes"]

    # — Modelo → device —
    model = CNN(num_classes=num_classes).to(DEVICE)
    print(f"\n[✓] Modelo creado y enviado a '{DEVICE}':\n{model}")

    # — Loss y optimizador —
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    # — Entrenamiento —
    train(model, train_loader, criterion, optimizer, epochs=EPOCHS, device=DEVICE)

    # — Evaluación —
    accuracy = evaluate(model, test_loader, device=DEVICE)

    print(f"\n  Accuracy en test : {accuracy * 100:.2f}%")
    print("─" * 50 + "\n")


if __name__ == "__main__":
    main()
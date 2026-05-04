"""
model.py
Definición de la arquitectura CNN para clasificación de imágenes.
Input esperado: tensores de forma (batch, 3, 128, 128).
"""

import torch.nn as nn


class CNN(nn.Module):
    """
    Red Neuronal Convolucional (CNN) para clasificación de imágenes.

    Flujo de dimensiones por capa (asumiendo batch_size=B):
        Entrada          →  (B,  3, 128, 128)
        Conv1 + ReLU     →  (B, 16, 128, 128)
        MaxPool1         →  (B, 16,  64,  64)
        Conv2 + ReLU     →  (B, 32,  64,  64)
        MaxPool2         →  (B, 32,  32,  32)
        Flatten          →  (B, 32·32·32) = (B, 32768)
        Linear1 + ReLU   →  (B, 64)
        Linear2 (salida) →  (B, num_classes)

    Parameters
    ----------
    num_classes : int – número de categorías a predecir
    """

    def __init__(self, num_classes: int) -> None:
        super().__init__()

        # ── Bloque convolucional 1 ────────────────────────────────────────
        # Conv2d: detecta patrones locales (bordes, texturas) en la imagen.
        #   - in_channels=3   : imagen RGB
        #   - out_channels=16 : aprende 16 filtros diferentes
        #   - kernel_size=3   : ventana 3×3 sobre la imagen
        #   - padding=1       : agrega un borde de ceros para preservar
        #                       el tamaño espacial (128×128 → 128×128)
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16,
                               kernel_size=3, padding=1)
        self.relu1 = nn.ReLU()

        # MaxPool2d: reduce la resolución espacial a la mitad tomando
        # el valor máximo de cada ventana 2×2 (stride=2 por defecto).
        # Efecto: (16, 128, 128) → (16, 64, 64)
        # Proporciona invariancia a pequeñas traslaciones y reduce cómputo.
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)

        # ── Bloque convolucional 2 ────────────────────────────────────────
        # Ahora el input tiene 16 canales (salida de pool1).
        # 32 filtros permiten aprender representaciones más abstractas
        # (combinaciones de los patrones detectados en el bloque anterior).
        # padding=1 preserva el tamaño: (32, 64, 64) → (32, 64, 64)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32,
                               kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()

        # MaxPool2d: reduce de nuevo a la mitad.
        # Efecto: (32, 64, 64) → (32, 32, 32)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        # ── Cabeza clasificadora (capas densas) ───────────────────────────
        # Flatten: convierte el volumen 3D (32, 32, 32) en un vector 1D.
        # Tamaño resultante: 32 × 32 × 32 = 32 768 valores por imagen.
        self.flatten = nn.Flatten()

        # Linear 1: proyecta las 32 768 features a un espacio de 64 dims.
        # Actúa como combinación lineal aprendida de todas las activaciones.
        self.fc1  = nn.Linear(32 * 32 * 32, 64)
        self.relu3 = nn.ReLU()

        # Linear 2 (capa de salida): produce un logit por clase.
        # No se aplica Softmax aquí porque nn.CrossEntropyLoss lo incorpora
        # internamente como LogSoftmax + NLLLoss, lo que es numéricamente
        # más estable. Para inferencia, argmax(logits) == argmax(softmax(logits)).
        self.fc2 = nn.Linear(64, num_classes)

    def forward(self, x):
        """
        Paso hacia adelante.

        Parameters
        ----------
        x : torch.Tensor  shape (batch_size, 3, 128, 128)

        Returns
        -------
        torch.Tensor  shape (batch_size, num_classes)  – logits crudos
        """
        x = self.pool1(self.relu1(self.conv1(x)))   # → (B, 16, 64, 64)
        x = self.pool2(self.relu2(self.conv2(x)))   # → (B, 32, 32, 32)
        x = self.flatten(x)                         # → (B, 32768)
        x = self.relu3(self.fc1(x))                 # → (B, 64)
        x = self.fc2(x)                             # → (B, num_classes)
        return x
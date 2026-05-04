"""
model.py
Definición de la arquitectura MLP para clasificación tabular.
"""

import torch.nn as nn


class MLP(nn.Module):
    """
    Perceptrón Multicapa (MLP) para clasificación multiclase.

    Arquitectura:
        Input → Linear(input_dim, 16) → ReLU
              → Linear(16, 8)         → ReLU
              → Linear(8, num_classes)

    Parameters
    ----------
    input_dim  : int – número de features de entrada (ej. 5 para V1–V5)
    num_classes: int – número de clases del problema
    """

    def __init__(self, input_dim: int, num_classes: int) -> None:
        super().__init__()

        # Capa 1: proyecta el espacio de entrada a 16 neuronas.
        # Permite que la red aprenda combinaciones lineales de los features.
        self.fc1 = nn.Linear(input_dim, 16)

        # Activación no lineal tras la primera capa.
        # ReLU introduce no linealidad sin saturar el gradiente
        # en la región positiva, acelerando la convergencia.
        self.relu1 = nn.ReLU()

        # Capa 2: comprime la representación de 16 → 8 neuronas.
        # Fuerza al modelo a extraer las características más relevantes.
        self.fc2 = nn.Linear(16, 8)

        # Segunda activación no lineal.
        self.relu2 = nn.ReLU()

        # Capa de salida: produce un logit por clase.
        # No se aplica activación aquí (ver docstring de forward).
        self.fc3 = nn.Linear(8, num_classes)

    def forward(self, x):
        """
        Paso hacia adelante de la red.

        Devuelve logits crudos (sin Softmax) porque:
          - nn.CrossEntropyLoss combina internamente LogSoftmax + NLLLoss,
            por lo que aplicar Softmax aquí sería redundante y numéricamente
            menos estable (pérdida de precisión en valores extremos).
          - Durante la inferencia, argmax(logits) == argmax(softmax(logits)),
            por lo que la predicción de clase no requiere la probabilidad real.

        Parameters
        ----------
        x : torch.Tensor  shape (batch_size, input_dim)

        Returns
        -------
        torch.Tensor  shape (batch_size, num_classes)  – logits
        """
        x = self.relu1(self.fc1(x))   # (batch, input_dim) → (batch, 16)
        x = self.relu2(self.fc2(x))   # (batch, 16)        → (batch,  8)
        x = self.fc3(x)               # (batch,  8)        → (batch, num_classes)
        return x
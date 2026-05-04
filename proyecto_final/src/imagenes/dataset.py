"""
dataset.py
Carga, transformación y partición del dataset de imágenes de papa (potato_subset)
usando torchvision.ImageFolder y DataLoader de PyTorch.
"""

import os
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms


# ─────────────────────────────────────────────
# 1. Configuración
# ─────────────────────────────────────────────

DATA_PATH  = "../../data/proyecto_final/imagenes/potato_subset"
IMG_SIZE   = (128, 128)
BATCH_SIZE = 32
TRAIN_RATIO = 0.8


# ─────────────────────────────────────────────
# 2. Transformaciones
# ─────────────────────────────────────────────

def build_transforms():
    """
    Define el pipeline de transformaciones aplicado a cada imagen.

    Pasos:
      1. Resize     – redimensiona a (128, 128) para unificar el tamaño de entrada.
      2. ToTensor   – convierte PIL Image (H×W×C, uint8 0-255)
                      a torch.Tensor (C×H×W, float32 0-1).
      3. Normalize  – centra cada canal en 0 con std 1 usando
                      mean=0.5 y std=0.5  →  pixel_norm = (pixel - 0.5) / 0.5
                      El rango resultante es [-1, 1], que favorece la convergencia.

    Returns
    -------
    transforms.Compose
    """
    return transforms.Compose([
        transforms.Resize(IMG_SIZE),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5],
                             std=[0.5,  0.5,  0.5]),
    ])


# ─────────────────────────────────────────────
# 3. Carga del dataset con ImageFolder
# ─────────────────────────────────────────────

def load_dataset(data_path: str, transform) -> datasets.ImageFolder:
    """
    Carga el dataset desde disco usando ImageFolder.

    ImageFolder espera la siguiente estructura de directorios:
        data_path/
            clase_A/  imagen1.jpg  imagen2.jpg …
            clase_B/  imagen1.jpg  …

    Detecta automáticamente las clases (subdirectorios) y asigna
    un índice entero a cada una.

    Parameters
    ----------
    data_path : str               – ruta raíz del dataset
    transform : transforms.Compose – pipeline de preprocesamiento

    Returns
    -------
    datasets.ImageFolder
    """
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"No se encontró el directorio: {data_path}")

    dataset = datasets.ImageFolder(root=data_path, transform=transform)

    print(f"[✓] Dataset cargado desde: {data_path}")
    print(f"    Clases detectadas ({len(dataset.classes)}): {dataset.classes}")
    print(f"    Total de imágenes : {len(dataset)}")

    return dataset


# ─────────────────────────────────────────────
# 4. División train / test
# ─────────────────────────────────────────────

def split_dataset(dataset, train_ratio: float = TRAIN_RATIO):
    """
    Divide el dataset en conjuntos de entrenamiento y prueba.

    Usa random_split de PyTorch, que garantiza que no haya
    solapamiento entre ambos subconjuntos.

    Parameters
    ----------
    dataset     : ImageFolder
    train_ratio : float  – proporción de muestras para entrenamiento (default 0.8)

    Returns
    -------
    train_dataset, test_dataset
    """
    total      = len(dataset)
    train_size = int(total * train_ratio)
    test_size  = total - train_size

    train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

    print(f"\n[✓] División del dataset:")
    print(f"    Train : {train_size} imágenes ({train_ratio*100:.0f}%)")
    print(f"    Test  : {test_size}  imágenes ({(1-train_ratio)*100:.0f}%)")

    return train_dataset, test_dataset


# ─────────────────────────────────────────────
# 5. DataLoaders
# ─────────────────────────────────────────────

def build_dataloaders(train_dataset, test_dataset, batch_size: int = BATCH_SIZE):
    """
    Crea DataLoaders para entrenamiento y prueba.

    - train_loader : shuffle=True  → mezcla los datos en cada época
                                     para evitar que el modelo aprenda
                                     el orden de los ejemplos.
    - test_loader  : shuffle=False → el orden no afecta la evaluación
                                     y facilita la reproducibilidad.

    Parameters
    ----------
    train_dataset : Subset  – conjunto de entrenamiento
    test_dataset  : Subset  – conjunto de prueba
    batch_size    : int     – número de imágenes por lote

    Returns
    -------
    train_loader, test_loader : DataLoader
    """
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader  = DataLoader(test_dataset,  batch_size=batch_size, shuffle=False)

    print(f"\n[✓] DataLoaders creados (batch_size={batch_size}):")
    print(f"    Batches train : {len(train_loader)}")
    print(f"    Batches test  : {len(test_loader)}")

    return train_loader, test_loader


# ─────────────────────────────────────────────
# 6. Pipeline principal
# ─────────────────────────────────────────────

def build_image_pipeline(
    data_path: str   = DATA_PATH,
    batch_size: int  = BATCH_SIZE,
    train_ratio: float = TRAIN_RATIO,
):
    """
    Ejecuta el pipeline completo:
        transformaciones → carga → división → DataLoaders.

    Parameters
    ----------
    data_path   : str   – ruta raíz del dataset
    batch_size  : int   – tamaño de lote
    train_ratio : float – proporción de entrenamiento

    Returns
    -------
    dict con:
        train_loader : DataLoader
        test_loader  : DataLoader
        classes      : list[str]
        num_classes  : int
    """
    print("\n" + "=" * 50)
    print("  PIPELINE DE IMÁGENES")
    print("=" * 50)

    transform                    = build_transforms()
    dataset                      = load_dataset(data_path, transform)
    train_dataset, test_dataset  = split_dataset(dataset, train_ratio)
    train_loader, test_loader    = build_dataloaders(
                                       train_dataset, test_dataset, batch_size
                                   )

    num_classes = len(dataset.classes)

    print("\n" + "─" * 50)
    print(f"  Num. clases : {num_classes}")
    print(f"  Clases      : {dataset.classes}")
    print(f"  Train size  : {len(train_dataset)}")
    print(f"  Test size   : {len(test_dataset)}")
    print("─" * 50 + "\n")

    return {
        "train_loader" : train_loader,
        "test_loader"  : test_loader,
        "classes"      : dataset.classes,
        "num_classes"  : num_classes,
    }


# ─────────────────────────────────────────────
# Punto de entrada
# ─────────────────────────────────────────────

if __name__ == "__main__":
    BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR  = os.path.abspath(os.path.join(BASE_DIR, "..", "..", ".."))

    DATA_PATH_ABS = os.path.join(
    ROOT_DIR, "data", "proyecto_final", "imagenes", "potato_subset"
    )
    build_image_pipeline(data_path=DATA_PATH_ABS)
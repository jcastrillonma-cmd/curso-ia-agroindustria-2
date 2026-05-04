"""
preprocess.py
Pipeline de preprocesamiento para dataset phpnThNfi.arff
"""

import os
import pandas as pd
import torch
from scipy.io import arff
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


# ─────────────────────────────────────────────
# 1. Carga del dataset
# ─────────────────────────────────────────────

def load_arff(filepath: str) -> pd.DataFrame:
    """Carga un archivo .arff y lo convierte a DataFrame de pandas."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No se encontró el archivo: {filepath}")

    data, meta = arff.loadarff(filepath)
    df = pd.DataFrame(data)
    print(f"[✓] Dataset cargado: {df.shape[0]} filas × {df.shape[1]} columnas")
    return df


# ─────────────────────────────────────────────
# 2. Limpieza de la variable objetivo
# ─────────────────────────────────────────────

def clean_target(df: pd.DataFrame, target_col: str = "Class") -> pd.DataFrame:
    """
    Convierte la columna objetivo de bytes a string.
    Ejemplo: b'2' → '2'
    """
    df = df.copy()
    df[target_col] = df[target_col].apply(
        lambda v: v.decode("utf-8") if isinstance(v, bytes) else str(v)
    )
    print(f"[✓] Variable objetivo '{target_col}' limpiada. "
          f"Clases únicas: {sorted(df[target_col].unique())}")
    return df


# ─────────────────────────────────────────────
# 3. Separación de features y target
# ─────────────────────────────────────────────

def split_features_target(
    df: pd.DataFrame,
    feature_cols: list[str],
    target_col: str = "Class",
) -> tuple[pd.DataFrame, pd.Series]:
    """Separa el DataFrame en X (features) e y (target)."""
    X = df[feature_cols].astype(float)
    y = df[target_col]
    print(f"[✓] Features: {feature_cols}")
    print(f"[✓] Target  : '{target_col}'")
    return X, y


# ─────────────────────────────────────────────
# 4. Codificación de la variable objetivo
# ─────────────────────────────────────────────

def encode_target(y: pd.Series) -> tuple[pd.Series, LabelEncoder]:
    """Aplica LabelEncoder a la variable objetivo."""
    le = LabelEncoder()
    y_encoded = pd.Series(le.fit_transform(y), name=y.name)
    print(f"[✓] Clases codificadas: { {k: v for k, v in zip(le.classes_, le.transform(le.classes_))} }")
    return y_encoded, le


# ─────────────────────────────────────────────
# 5. División train / test
# ─────────────────────────────────────────────

def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple:
    """Divide los datos en conjuntos de entrenamiento (80%) y prueba (20%)."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    print(f"[✓] Train: {X_train.shape[0]} muestras | Test: {X_test.shape[0]} muestras")
    return X_train, X_test, y_train, y_test


# ─────────────────────────────────────────────
# 6. Escalado de features
# ─────────────────────────────────────────────

def scale_features(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, StandardScaler]:
    """
    Ajusta StandardScaler sobre el conjunto de entrenamiento
    y transforma ambos conjuntos.
    """
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=X_train.columns,
    )
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test),
        columns=X_test.columns,
    )
    print("[✓] Features escaladas con StandardScaler (fit sobre train).")
    return X_train_scaled, X_test_scaled, scaler


# ─────────────────────────────────────────────
# 7. Conversión a tensores de PyTorch
# ─────────────────────────────────────────────

def to_tensors(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """Convierte DataFrames y Series de pandas a tensores de PyTorch."""
    X_train_t = torch.tensor(X_train.values, dtype=torch.float32)
    X_test_t  = torch.tensor(X_test.values,  dtype=torch.float32)
    y_train_t = torch.tensor(y_train.values, dtype=torch.long)
    y_test_t  = torch.tensor(y_test.values,  dtype=torch.long)
    print("[✓] Datos convertidos a tensores de PyTorch.")
    return X_train_t, X_test_t, y_train_t, y_test_t


# ─────────────────────────────────────────────
# 8. Pipeline completo
# ─────────────────────────────────────────────

def preprocess_pipeline(
    filepath: str,
    feature_cols: list[str] | None = None,
    target_col: str = "Class",
    test_size: float = 0.2,
    random_state: int = 42,
) -> dict:
    """
    Ejecuta el pipeline completo de preprocesamiento.

    Returns
    -------
    dict con:
        X_train, X_test, y_train, y_test : torch.Tensor
        scaler                            : StandardScaler ajustado
        label_encoder                     : LabelEncoder ajustado
        num_classes                       : int
    """
    if feature_cols is None:
        feature_cols = ["V1", "V2", "V3", "V4", "V5"]

    print("\n" + "=" * 50)
    print("  PIPELINE DE PREPROCESAMIENTO")
    print("=" * 50)

    df                        = load_arff(filepath)
    df                        = clean_target(df, target_col)
    X, y                      = split_features_target(df, feature_cols, target_col)
    y, le                     = encode_target(y)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size, random_state)
    X_train, X_test, scaler   = scale_features(X_train, X_test)
    X_train_t, X_test_t, y_train_t, y_test_t = to_tensors(
        X_train, X_test, y_train, y_test
    )

    num_classes = len(le.classes_)

    print("\n" + "─" * 50)
    print(f"  Tamaño train : {X_train_t.shape}")
    print(f"  Tamaño test  : {X_test_t.shape}")
    print(f"  Num. clases  : {num_classes}")
    print("─" * 50 + "\n")

    return {
        "X_train": X_train_t,
        "X_test":  X_test_t,
        "y_train": y_train_t,
        "y_test":  y_test_t,
        "scaler":  scaler,
        "label_encoder": le,
        "num_classes": num_classes,
    }


# ─────────────────────────────────────────────
# Punto de entrada
# ─────────────────────────────────────────────

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", ".."))

    DATA_PATH = os.path.join(
    ROOT_DIR, "data", "proyecto_final", "tabular", "phpnThNfi.arff"
    )

    result = preprocess_pipeline(filepath=DATA_PATH)
# Proyecto Final — Inteligencia Artificial para Agroindustria

**Estudiante:** Juan David Castrillón Martínez
**Curso:** Inteligencia Artificial para Agroindustria
**Repositorio:** [github.com/jcastrillonma-cmd/curso-ia-agroindustria-2](https://github.com/jcastrillonma-cmd/curso-ia-agroindustria-2)

---

## Descripción general

Este proyecto desarrolla dos modelos de clasificación supervisada usando PyTorch:

- **Componente tabular:** clasificación binaria sobre el dataset `phpnThNfi.arff` usando un Perceptrón Multicapa (MLP).
- **Componente de imágenes:** clasificación multiclase de hojas de papa usando una Red Neuronal Convolucional (CNN).

---

## Estructura del repositorio

```
proyecto_final/
├── README.md
├── informe/
│   ├── main.tex
│   └── main.pdf
├── src/
│   ├── tabular/
│   │   ├── preprocess.py
│   │   ├── model.py
│   │   └── train.py
│   └── imagenes/
│       ├── dataset.py
│       ├── model.py
│       └── train.py
└── resultados/
    ├── tabular/
    │   └── resultados.txt
    └── imagenes/
        └── resultados.txt
```

Los datasets oficiales del curso deben estar ubicados en:

```
data/
└── proyecto_final/
    ├── tabular/
    │   └── phpnThNfi.arff
    └── imagenes/
        └── potato_subset/
            ├── Potato___Early_blight/
            ├── Potato___Late_blight/
            └── Potato___healthy/
```

---

## Componente tabular

**Dataset:** `phpnThNfi.arff` — 4839 muestras, 5 variables de entrada (V1–V5), variable objetivo binaria (clases 1 y 2).

**Modelo:** Perceptrón Multicapa (MLP)

```
Entrada (5) → Linear(5, 16) → ReLU → Linear(16, 8) → ReLU → Linear(8, 2)
```

**Resultados:**

| Métrica | Valor |
|---|---|
| Accuracy en test | 67.98% |
| Aciertos clase 0 | 622 / 916 (67.9%) |
| Aciertos clase 1 | 36 / 52 (69.2%) |

El dataset presenta desbalance significativo (ratio ~17:1). Se aplicaron pesos de clase con la fórmula estándar `n_total / (n_clases × n_i)` para que el modelo aprenda ambas clases de forma equilibrada.

### Instrucciones de ejecución

```bash
cd proyecto_final/src/tabular
python train.py
```

---

## Componente de imágenes

**Dataset:** `potato_subset` — 456 imágenes de hojas de papa en 3 clases:
- `Potato___Early_blight`
- `Potato___Late_blight`
- `Potato___healthy`

**Modelo:** Red Neuronal Convolucional (CNN)

```
Conv2d(3,16) → ReLU → MaxPool →
Conv2d(16,32) → ReLU → MaxPool →
Flatten → Linear(32768, 64) → ReLU → Linear(64, 3)
```

**Resultados:**

| Métrica | Valor |
|---|---|
| Accuracy en test | 92.39% |
| Loss época 1 | 0.7736 |
| Loss época 10 | 0.0226 |

### Instrucciones de ejecución

```bash
cd proyecto_final/src/imagenes
python train.py
```

---

## Requisitos

```bash
pip install torch torchvision scikit-learn pandas scipy
```

Python 3.10 o superior requerido.

---

## Informe

El informe completo en LaTeX y su PDF compilado se encuentran en la carpeta `informe/`.
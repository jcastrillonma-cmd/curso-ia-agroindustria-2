# Proyecto final

En esta carpeta se encuentra la guía general del proyecto final del curso de **Inteligencia Artificial para Agroindustria**.

El proyecto final es un trabajo **integrado**. Cada estudiante deberá desarrollar **dos componentes obligatorios** dentro de un mismo proyecto:

1. un componente de clasificación tabular,
2. un componente de clasificación de imágenes.

No se debe escoger una modalidad única. Se deben desarrollar **ambas partes**.

---

## Objetivo general

El objetivo del proyecto final es que el estudiante desarrolle un trabajo aplicado de inteligencia artificial usando los **dos datasets oficiales del curso**, integrando:

- comprensión del problema,
- explicación matemática básica del método,
- explicación conceptual del funcionamiento,
- ejemplo o ejercicio de apoyo,
- implementación en **PyTorch** o **TensorFlow**,
- documentación técnica en **LaTeX**,
- compilación final en **PDF**,
- entrega en el **GitHub del estudiante**.

---

## Componentes obligatorios

### 1. Componente tabular

El estudiante deberá trabajar con el dataset tabular oficial del curso y desarrollar un modelo de clasificación.

### 2. Componente de imágenes

El estudiante deberá trabajar con el subconjunto oficial de imágenes de hojas de papa y desarrollar un modelo de clasificación de imágenes.

En ambos componentes el estudiante deberá:

- estudiar el método utilizado,
- explicar brevemente su base matemática,
- explicar cómo funciona,
- presentar un ejemplo o ejercicio de apoyo,
- implementar el modelo,
- entrenarlo y evaluarlo,
- analizar los resultados obtenidos.

---

## Ubicación de los datasets oficiales

Los datasets oficiales del proyecto final están ubicados en las siguientes rutas del repositorio:

### Dataset tabular

```text
data/proyecto_final/tabular/phpnThNfi.arff
```

### Dataset de imágenes

```text
data/proyecto_final/imagenes/potato_subset/
```

La descripción general de ambos datasets está en:

```text
proyecto_final/datasets/datasets_oficiales.md
```

---

## Temáticas mínimas a estudiar

Para desarrollar correctamente el proyecto final, el estudiante deberá estudiar como mínimo los siguientes temas.

### Para el componente tabular

- clasificación supervisada,
- variables de entrada y variable objetivo,
- partición de datos en entrenamiento y prueba,
- función de pérdida,
- métricas básicas de clasificación,
- implementación de modelos en **PyTorch** o **TensorFlow**.

### Para el componente de imágenes

- representación de imágenes como tensores,
- clasificación supervisada de imágenes,
- preprocesamiento básico de imágenes,
- entrenamiento y evaluación de modelos,
- métricas básicas de clasificación,
- implementación de modelos en **PyTorch** o **TensorFlow**.

### Para el informe y la entrega

- estructura básica de un informe técnico,
- redacción del proyecto en **LaTeX**,
- compilación del informe a **PDF**,
- organización del repositorio en **GitHub**,
- instrucciones de ejecución y reproducibilidad.

---

## Qué debe entregar el estudiante

La entrega final deberá realizarse en el **repositorio personal de GitHub del estudiante**.

Ese repositorio deberá contener:

- código fuente del componente tabular,
- código fuente del componente de imágenes,
- documento del proyecto en LaTeX,
- PDF compilado,
- `README.md`,
- resultados,
- instrucciones de ejecución.

---

## Ruta de trabajo recomendada

Se recomienda seguir esta ruta dentro de `proyecto_final/`:

1. Leer `guia/enunciado_proyecto_final.md`
2. Leer `guia/entrega.md`
3. Leer `guia/rubrica.md`
4. Leer `datasets/datasets_oficiales.md`
5. Revisar `asignacion/README.md`
6. Revisar `asignacion/notas_tecnicas.md`
7. Ubicar los datasets oficiales en `data/proyecto_final/`

---

## Estructura de esta carpeta

```text
proyecto_final/
├── README.md
├── guia/
│   ├── enunciado_proyecto_final.md
│   ├── entrega.md
│   └── rubrica.md
├── datasets/
│   ├── README.md
│   └── datasets_oficiales.md
└── asignacion/
    ├── README.md
    └── notas_tecnicas.md
```

---

## Observación final

El estudiante debe trabajar únicamente con los datasets oficiales del curso y desarrollar **los dos componentes obligatorios** dentro del mismo proyecto final.

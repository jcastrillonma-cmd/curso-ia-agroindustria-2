# Enunciado del proyecto final

## Curso
Inteligencia Artificial para Agroindustria

## Propósito

El proyecto final tiene como propósito que el estudiante desarrolle un trabajo aplicado de inteligencia artificial usando los **dos datasets oficiales del curso**, articulando estudio teórico, comprensión matemática, implementación computacional, evaluación de resultados y documentación técnica.

El proyecto final es **integrado**. Cada estudiante deberá desarrollar **dos componentes obligatorios** dentro de un mismo trabajo:

1. un componente de clasificación tabular,
2. un componente de clasificación de imágenes.

No se debe escoger una sola modalidad. Se deben desarrollar **ambos componentes**.

---

## Paso 1. Revisar los datasets oficiales

Antes de seleccionar modelos o programar, el estudiante deberá revisar cuidadosamente los datasets oficiales del curso.

### Dataset tabular

Ruta en el repositorio:

```text
data/proyecto_final/tabular/phpnThNfi.arff
```

Tarea inicial:

- identificar las variables de entrada,
- identificar la variable objetivo,
- revisar el tipo de datos,
- verificar el tamaño del dataset,
- reconocer que se trata de un problema de clasificación.

### Dataset de imágenes

Ruta en el repositorio:

```text
data/proyecto_final/imagenes/potato_subset/
```

Clases del subconjunto:

- `Potato___Early_blight`
- `Potato___healthy`
- `Potato___Late_blight`

Tarea inicial:

- revisar la estructura de carpetas,
- identificar las clases,
- inspeccionar visualmente varias imágenes,
- reconocer que se trata de un problema de clasificación multiclase.

---

## Paso 2. Revisar la bibliografía base

Antes de implementar, el estudiante deberá revisar documentación y material de apoyo sobre aprendizaje supervisado, clasificación y evaluación de modelos.

### Documentos base sugeridos

- scikit-learn:  
  https://scikit-learn.org/stable/supervised_learning.html\#

- The Elements of Statistical Learning:  
  https://hastie.su.domains/ElemStatLearn/\?spm\=a2ty_o01.29997173.0.0.4d5b5171Qvbi9L

- An Introduction to Statistical Learning:  
  https://www.statlearning.com/\?spm\=a2ty_o01.29997173.0.0.4d5b5171Qvbi9L

### Qué debe hacer con esta bibliografía

El estudiante no debe limitarse a citar estos documentos. Debe usarlos para:

- identificar métodos adecuados de clasificación,
- comprender la lógica matemática básica de esos métodos,
- reconocer criterios de entrenamiento y evaluación,
- diferenciar entre modelo, entrenamiento, predicción y evaluación.

---

## Paso 3. Estudiar los temas del componente tabular

Para el componente tabular, el estudiante deberá estudiar como mínimo los siguientes temas:

- aprendizaje supervisado,
- clasificación binaria o multiclase,
- variables predictoras y variable objetivo,
- partición en entrenamiento y prueba,
- normalización o preprocesamiento básico,
- función de pérdida,
- métricas de clasificación,
- interpretación de resultados.

### Teoría matemática mínima para estudiar

El estudiante deberá comprender, de forma básica y clara:

- representación del problema en términos de entradas y salidas,
- función del modelo \(f(x)\),
- criterio de error o pérdida,
- proceso general de entrenamiento,
- noción de ajuste del modelo,
- noción de generalización,
- métricas como accuracy, precision, recall y F1-score.

### Herramientas de aprendizaje automático sugeridas

Para este componente, el estudiante podrá apoyarse conceptualmente en métodos como:

- regresión logística,
- árboles de decisión,
- random forest,
- support vector machines,
- perceptrón multicapa.

La implementación final del proyecto deberá hacerse en **PyTorch** o **TensorFlow**.

---

## Paso 4. Estudiar los temas del componente de imágenes

Para el componente de imágenes, el estudiante deberá estudiar como mínimo los siguientes temas:

- representación de imágenes como arreglos o tensores,
- clasificación supervisada de imágenes,
- clases y etiquetas,
- partición en entrenamiento y prueba,
- preprocesamiento básico,
- entrenamiento de modelos,
- evaluación de desempeño.

### Teoría matemática mínima para estudiar

El estudiante deberá comprender, de forma básica y clara:

- cómo se representa una imagen numéricamente,
- cómo un modelo transforma una entrada en una salida de clasificación,
- función de pérdida para clasificación,
- proceso general de entrenamiento,
- métricas básicas de evaluación,
- interpretación de la matriz de confusión.

### Herramientas de aprendizaje automático sugeridas

Para este componente, el estudiante podrá trabajar con:

- perceptrón multicapa,
- redes neuronales convolucionales básicas,
- arquitecturas simples de clasificación implementadas en **PyTorch** o **TensorFlow**.

No se exige usar modelos complejos ni arquitecturas avanzadas. Se valorará más la claridad del desarrollo que la complejidad técnica.

---

## Paso 5. Qué debe hacer con cada dataset

### Componente tabular

El estudiante deberá:

1. cargar y explorar el dataset tabular;
2. identificar entradas y variable objetivo;
3. preparar los datos;
4. seleccionar un método de clasificación;
5. explicar brevemente su fundamento matemático;
6. implementar el modelo en **PyTorch** o **TensorFlow**;
7. entrenar el modelo;
8. evaluar resultados con métricas;
9. interpretar los resultados obtenidos.

### Componente de imágenes

El estudiante deberá:

1. revisar las carpetas y clases del subconjunto;
2. preparar las imágenes para entrenamiento y prueba;
3. seleccionar un método de clasificación;
4. explicar brevemente su fundamento matemático;
5. implementar el modelo en **PyTorch** o **TensorFlow**;
6. entrenar el modelo;
7. evaluar resultados con métricas;
8. interpretar los resultados obtenidos.

---

## Paso 6. Qué debe explicar en el informe

El informe final deberá mostrar con claridad:

- descripción del problema tabular,
- descripción del problema de imágenes,
- teoría matemática básica de los métodos usados,
- explicación conceptual del funcionamiento,
- ejemplo o ejercicio de apoyo,
- metodología de implementación,
- resultados obtenidos,
- análisis breve de resultados,
- conclusiones.

El informe deberá redactarse en **LaTeX** y compilarse a **PDF**.

---

## Entrega obligatoria

La entrega final deberá realizarse en el **GitHub del estudiante**.

Cada estudiante deberá crear y mantener su propio repositorio para el proyecto. En ese repositorio deberá incluir:

- código fuente del componente tabular,
- código fuente del componente de imágenes,
- documento en LaTeX,
- PDF compilado,
- `README.md`,
- resultados,
- instrucciones de ejecución.

---

## Alcance

Este proyecto está pensado para desarrollarse en un tiempo corto. Por tanto:

- no se exige construir una aplicación completa,
- no se exige usar múltiples modelos complejos,
- no se exige trabajar con datasets externos,
- no se exige alcanzar resultados de nivel profesional,
- se valorará más la comprensión, la claridad, la reproducibilidad y el desarrollo correcto del trabajo.

---

## Observación final

Se debe trabajar únicamente con los datasets oficiales definidos para el curso y desarrollar **los dos componentes obligatorios** dentro del mismo proyecto final.

# Guía de entrega del proyecto final

## Forma de entrega

La entrega final deberá realizarse **exclusivamente en el GitHub del estudiante**.

Cada estudiante deberá crear o usar un repositorio propio de GitHub para desarrollar y entregar su proyecto final. No se aceptará una entrega separada por fuera de ese repositorio, salvo que el profesor indique lo contrario.

## Qué debe estar en el repositorio del estudiante

El repositorio de GitHub del estudiante deberá contener como mínimo:

1. Un archivo `README.md`.
2. El código fuente del proyecto.
3. El desarrollo del documento en LaTeX.
4. El archivo PDF compilado del informe.
5. Los resultados obtenidos.
6. Las instrucciones necesarias para ejecutar el proyecto.
7. Evidencia del componente tabular.
8. Evidencia del componente de clasificación de imágenes.

## Estructura mínima sugerida

```text
proyecto_final_estudiante/
├── README.md
├── informe/
│   ├── main.tex
│   └── main.pdf
├── src/
│   ├── tabular/
│   │   └── modelo_tabular.py
│   └── imagenes/
│       └── modelo_imagenes.py
├── data/
│   └── descripcion.txt
└── results/
    ├── tabular/
    └── imagenes/
```

## Contenido mínimo del README.md

El archivo `README.md` del repositorio del estudiante deberá incluir:

- título del proyecto,
- nombre del estudiante,
- descripción breve del problema,
- descripción del componente tabular,
- descripción del componente de imágenes,
- tecnologías utilizadas,
- instrucciones de ejecución,
- resumen breve de resultados.

## Contenido mínimo del informe en LaTeX

El informe deberá estar escrito en LaTeX y compilado a PDF. Como mínimo, deberá contener:

- título,
- introducción,
- descripción del problema,
- explicación matemática breve,
- explicación conceptual del método,
- ejemplo o ejercicio de apoyo,
- metodología,
- resultados,
- discusión breve,
- conclusiones.

## Requisitos técnicos

- El programa debe estar implementado en **PyTorch** o **TensorFlow**.
- El código debe ejecutarse de manera reproducible.
- El informe debe estar en formato **LaTeX** y su correspondiente **PDF** debe estar incluido en el repositorio.
- El estudiante debe trabajar con los datasets oficiales del curso.
- El estudiante debe desarrollar los dos componentes obligatorios del proyecto final.

## Recomendaciones

- Usar nombres de archivos claros.
- Mantener una estructura ordenada de carpetas.
- Evitar subir archivos innecesarios.
- Explicar de forma breve cómo ejecutar el código.
- Verificar que el PDF final sí esté presente en el repositorio.

## Observación final

El repositorio del estudiante constituye la evidencia principal de entrega del proyecto final.

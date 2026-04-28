

## 01 - Preparación de datos
- Fecha de ejecución: 2026-03-24 19:54:47.184185
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/raw/datosbase.csv
- Archivo generado: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Transformaciones aplicadas:
  - Selección de columnas: created_at, entry_id, field2, field4
  - Eliminación de columnas no relevantes
  - Renombrado de variables:
      field2 → co2_ppm
      field4 → ch4_ppm
  - Conversión de created_at a datetime
- Registros con fecha inválida: 0
- Justificación técnica:
  Se conservan únicamente las variables en ppm relevantes para el análisis de emisiones, garantizando consistencia y trazabilidad.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-24 19:57:10.955603
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Cálculo de tiempo relativo por día (minutos desde inicio)
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes, y el tiempo relativo facilita la comparación entre días.


## 03 - Generación de gráficos diarios
- Fecha de ejecución: 2026-03-24 20:00:12.478306
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Transformaciones aplicadas:
  - Generación de gráficos de CO2 por día
  - Generación de gráficos de CH4 por día
  - Generación de gráficos conjuntos CO2 vs CH4
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados:
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Justificación técnica:
  La visualización permite identificar patrones dinámicos, picos, zonas estables y posibles relaciones inversas entre CO2 y CH4 en cada jornada.


## 03 - Generación de gráficos diarios
- Fecha de ejecución: 2026-03-24 20:03:09.476242
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Transformaciones aplicadas:
  - Generación de gráficos de CO2 por día
  - Generación de gráficos de CH4 por día
  - Generación de gráficos conjuntos CO2 vs CH4
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados:
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Justificación técnica:
  La visualización permite identificar patrones dinámicos, picos, zonas estables y posibles relaciones inversas entre CO2 y CH4 en cada jornada.


## 03 - Generación de gráficos diarios
- Fecha de ejecución: 2026-03-24 20:04:29.405374
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Transformaciones aplicadas:
  - Generación de gráficos de CO2 por día
  - Generación de gráficos de CH4 por día
  - Generación de gráficos conjuntos CO2 vs CH4
  - Uso de tiempo relativo como eje temporal
  - Generación de gráficos comparativos entre días (CO2 y CH4)
- Número de días procesados: 10
- Archivos generados:
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-24 20:06:15.718204
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.


## 04 - Cálculo de pendientes
- Fecha de ejecución: 2026-03-24 20:09:24.512594
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Archivo generado: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/resumen_pendientes.csv
- Método aplicado:
  - Regresión lineal (numpy.polyfit grado 1)
  - Cálculo de pendiente global por día
- Número de días procesados: 10
- Variables analizadas:
  - CO2 (ppm)
  - CH4 (ppm)
- Justificación técnica:
  La pendiente global permite cuantificar la tendencia general de las emisiones durante cada jornada, facilitando la comparación entre días.


## 05 - Reporte analítico
- Fecha de ejecución: 2026-03-24 20:11:02.507870
- Archivo generado: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/reports/analisis_por_dia.md
- Contenido:
  - Análisis descriptivo por día
  - Integración de métricas (pendientes)
  - Interpretación técnica básica
- Justificación técnica:
  El reporte permite traducir los datos y métricas en una interpretación comprensible del comportamiento del sistema.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:14:57.383585
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:16:10.939344
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-26 21:16:59.571599
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:18:43.630433
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-26 21:18:50.570133
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:23:41.973328
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:24:29.251875
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-26 21:24:36.617235
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:26:49.160825
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-26 21:26:55.646438
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:28:29.810139
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:29:28.455037
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-26 21:29:35.469667
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:36:18.628715
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-26 21:36:24.956400
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:39:50.260087
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-26 21:39:55.659034
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.


## 02 - Segmentación diaria
- Fecha de ejecución: 2026-03-26 21:42:38.293719
- Archivo origen: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/interim/datos_filtrados_ppm.csv
- Archivo generado (general): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_limpios.csv
- Transformaciones aplicadas:
  - Creación de columna 'fecha' a partir de created_at
  - Ordenamiento temporal de los datos
  - Filtrado de valores atípicos por cambios abruptos
  - Aplicación de umbral diferencial para CO2 y CH4
  - Interpolación de valores faltantes
  - Cálculo de tiempo relativo por día
  - Segmentación en archivos individuales por fecha
- Número de días detectados: 10
- Archivos generados:
  - 2025-08-10.csv
  - 2025-08-18.csv
  - 2025-08-19.csv
  - 2025-08-20.csv
  - 2025-08-22.csv
  - 2025-08-25.csv
  - 2025-09-09.csv
  - 2025-09-11.csv
  - 2025-09-13.csv
  - 2025-09-17.csv
- Justificación técnica:
  Se eliminaron valores atípicos asociados a errores de medición mediante un criterio de cambio abrupto entre observaciones consecutivas.
  La interpolación permitió mantener la continuidad de la serie temporal sin afectar la tendencia general.
  La segmentación diaria permite analizar el comportamiento del sistema por jornadas independientes.


## 03 - Generación de gráficos
- Fecha de ejecución: 2026-03-26 21:42:43.851064
- Carpeta de entrada: /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/data/processed/datos_por_dia
- Carpeta de salida (diarios): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/diarios
- Carpeta de salida (comparativos): /workspaces/curso-ia-agroindustria-2/proyecto_gases_hi/figures/comparativos
- Transformaciones aplicadas:
  - Gráficos diarios de CO2
  - Gráficos diarios de CH4
  - Gráficos conjuntos CO2 vs CH4
  - Gráficos comparativos entre días
  - Uso de tiempo relativo como eje temporal
- Número de días procesados: 10
- Archivos generados (diarios):
  - 2025-08-10_co2.png
  - 2025-08-10_ch4.png
  - 2025-08-10_conjunto.png
  - 2025-08-18_co2.png
  - 2025-08-18_ch4.png
  - 2025-08-18_conjunto.png
  - 2025-08-19_co2.png
  - 2025-08-19_ch4.png
  - 2025-08-19_conjunto.png
  - 2025-08-20_co2.png
  - 2025-08-20_ch4.png
  - 2025-08-20_conjunto.png
  - 2025-08-22_co2.png
  - 2025-08-22_ch4.png
  - 2025-08-22_conjunto.png
  - 2025-08-25_co2.png
  - 2025-08-25_ch4.png
  - 2025-08-25_conjunto.png
  - 2025-09-09_co2.png
  - 2025-09-09_ch4.png
  - 2025-09-09_conjunto.png
  - 2025-09-11_co2.png
  - 2025-09-11_ch4.png
  - 2025-09-11_conjunto.png
  - 2025-09-13_co2.png
  - 2025-09-13_ch4.png
  - 2025-09-13_conjunto.png
  - 2025-09-17_co2.png
  - 2025-09-17_ch4.png
  - 2025-09-17_conjunto.png
- Archivos generados (comparativos):
  - co2_todos_los_dias.png
  - ch4_todos_los_dias.png
- Justificación técnica:
  La visualización permite comparar dinámicas diarias, identificar picos, zonas estables y posibles relaciones entre CO2 y CH4.

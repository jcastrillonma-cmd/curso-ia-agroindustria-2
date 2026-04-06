#!/usr/bin/env bash
set -euo pipefail

# 1. Crear estructura (redundancia de seguridad)
mkdir -p data/raw data/processed scripts reports

# 2. Descargar datos (NOTA: Cambia la URL por una real si tienes una)
# Si no tienes URL, puedes comentar la línea de curl y copiar manualmente un archivo a data/raw
DATA_URL="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv" # Ejemplo genérico
DATA_FILE="data/raw/datos_sensores.csv"

if [ ! -f "$DATA_FILE" ]; then
  echo "Descargando datos..."
  # Usamos curl -L para seguir redirecciones si es necesario
  curl -L -o "$DATA_FILE" "$DATA_URL"
fi

# 3. Validar datos y generar reporte
echo "=== Reporte de Validación ===" > reports/validacion_inicial.txt
echo "Fecha: $(date)" >> reports/validacion_inicial.txt
echo "Filas: $(wc -l < $DATA_FILE)" >> reports/validacion_inicial.txt
echo "Columnas: $(head -n1 $DATA_FILE | tr ',' '\n' | wc -l)" >> reports/validacion_inicial.txt
# El '|| true' evita que el script falle si no encuentra ",,"
echo "Valores faltantes: $(grep -c ",," $DATA_FILE || true)" >> reports/validacion_inicial.txt

echo "Setup completado. Ver reports/validacion_inicial.txt"

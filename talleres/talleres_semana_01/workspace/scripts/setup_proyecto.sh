#!/usr/bin/env bash
set -euo pipefail

RAW_DIR="data/raw"
REPORTS_DIR="reports"
DATA_FILE="$RAW_DIR/sensores.csv"
REPORT_FILE="$REPORTS_DIR/validacion_inicial.txt"

mkdir -p "$RAW_DIR" "$REPORTS_DIR"
if [ ! -f "$DATA_FILE" ]; then
cat > "$DATA_FILE" <<'CSV'
id_sensor,fecha,temperatura,humedad
SENSOR_01,2026-01-01 00:00:00,24.1,60
SENSOR_01,2026-01-01 00:01:00,24.0,61
SENSOR_02,2026-01-01 00:00:00,25.3,55
SENSOR_03,2026-01-01 00:00:00,23.7,,
SENSOR_02,2026-01-01 00:01:00,25.1,56
CSV
fi
rows="$(wc -l < "$DATA_FILE")"
cols="$(head -n1 "$DATA_FILE" | tr ',' '\n' | wc -l)"
missing="$(grep -c ",," "$DATA_FILE" || true)"
{
echo "=== Reporte de Validación Inicial (Semana 1) ==="
echo "Fecha: $(date)"
echo "Archivo: $DATA_FILE"
echo "Filas (incluye header): $rows"
echo "Columnas: $cols"
echo "Faltantes (patrón ',,'): $missing"
echo ""
echo "Muestra (primeras 5 líneas):"
head -n 5 "$DATA_FILE"
} > "$REPORT_FILE"

echo "OK: generado $REPORT_FILE"

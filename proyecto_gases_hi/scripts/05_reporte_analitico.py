from pathlib import Path
import pandas as pd
from datetime import datetime

# =========================
# Rutas
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]

input_dir = BASE_DIR / "data/processed/datos_por_dia"
pendientes_path = BASE_DIR / "data/processed/resumen_pendientes.csv"
output_path = BASE_DIR / "reports/analisis_por_dia.md"
bitacora_path = BASE_DIR / "reports/bitacora_limpieza.md"

# =========================
# Cargar pendientes
# =========================
df_pendientes = pd.read_csv(pendientes_path)

# =========================
# Archivos diarios
# =========================
archivos = sorted(input_dir.glob("*.csv"))

# =========================
# Función de interpretación
# =========================
def interpretar_tendencia(pendiente):
    if pendiente > 0:
        return "tendencia creciente"
    elif pendiente < 0:
        return "tendencia decreciente"
    else:
        return "comportamiento estable"

# =========================
# Generar reporte
# =========================
with open(output_path, "w", encoding="utf-8") as f:

    f.write("# Análisis técnico por día\n\n")
    f.write(f"Fecha de generación: {datetime.now()}\n\n")

    for archivo in archivos:
        df = pd.read_csv(archivo)
        fecha = archivo.stem

        # Datos básicos
        co2_inicio = df["co2_ppm"].iloc[0]
        co2_fin = df["co2_ppm"].iloc[-1]
        co2_max = df["co2_ppm"].max()
        co2_min = df["co2_ppm"].min()

        ch4_inicio = df["ch4_ppm"].iloc[0]
        ch4_fin = df["ch4_ppm"].iloc[-1]
        ch4_max = df["ch4_ppm"].max()
        ch4_min = df["ch4_ppm"].min()

        # Pendientes
        fila = df_pendientes[df_pendientes["fecha"] == fecha]

        if not fila.empty:
            pendiente_co2 = fila["pendiente_co2"].values[0]
            pendiente_ch4 = fila["pendiente_ch4"].values[0]
        else:
            pendiente_co2 = None
            pendiente_ch4 = None

        tendencia_co2 = interpretar_tendencia(pendiente_co2) if pendiente_co2 is not None else "no disponible"
        tendencia_ch4 = interpretar_tendencia(pendiente_ch4) if pendiente_ch4 is not None else "no disponible"

        # =========================
        # Escritura
        # =========================
        f.write(f"## Día {fecha}\n\n")

        f.write("### CO2\n")
        f.write(f"- Valor inicial: {co2_inicio:.2f} ppm\n")
        f.write(f"- Valor final: {co2_fin:.2f} ppm\n")
        f.write(f"- Máximo: {co2_max:.2f} ppm\n")
        f.write(f"- Mínimo: {co2_min:.2f} ppm\n")
        f.write(f"- Pendiente: {pendiente_co2:.4f}\n")
        f.write(f"- Comportamiento: {tendencia_co2}\n\n")

        f.write("### CH4\n")
        f.write(f"- Valor inicial: {ch4_inicio:.2f} ppm\n")
        f.write(f"- Valor final: {ch4_fin:.2f} ppm\n")
        f.write(f"- Máximo: {ch4_max:.2f} ppm\n")
        f.write(f"- Mínimo: {ch4_min:.2f} ppm\n")
        f.write(f"- Pendiente: {pendiente_ch4:.4f}\n")
        f.write(f"- Comportamiento: {tendencia_ch4}\n\n")

        # Interpretación básica
        f.write("### Interpretación\n")
        f.write("Se observa el comportamiento dinámico de las emisiones durante la jornada. ")
        f.write("Los cambios en las concentraciones pueden estar asociados a la actividad metabólica del sistema. ")

        if pendiente_co2 > 0 and pendiente_ch4 < 0:
            f.write("Se evidencia un comportamiento inverso entre CO2 y CH4.\n\n")
        else:
            f.write("No se observa una relación inversa clara entre CO2 y CH4.\n\n")

# =========================
# Bitácora
# =========================
with open(bitacora_path, "a", encoding="utf-8") as f:
    f.write("\n\n## 05 - Reporte analítico\n")
    f.write(f"- Fecha de ejecución: {datetime.now()}\n")
    f.write(f"- Archivo generado: {output_path}\n")
    f.write("- Contenido:\n")
    f.write("  - Análisis descriptivo por día\n")
    f.write("  - Integración de métricas (pendientes)\n")
    f.write("  - Interpretación técnica básica\n")
    f.write("- Justificación técnica:\n")
    f.write("  El reporte permite traducir los datos y métricas en una interpretación comprensible del comportamiento del sistema.\n")
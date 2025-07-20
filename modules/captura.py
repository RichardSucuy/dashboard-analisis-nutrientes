from modules.captura_dashboard import capturar_dashboard_png

def ejecutar_captura_dashboard():
    try:
        url = "http://localhost:8501"
        capturar_dashboard_png(url, output_file="dashboard.png")
    except Exception as e:
        print("❌ Error al capturar el dashboard:", e)

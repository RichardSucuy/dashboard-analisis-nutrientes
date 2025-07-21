import subprocess
import os


def run_streamlit():
    # Ruta completa al script de Streamlit (cambia aquí si tu archivo principal tiene otro nombre)
    script_path = os.path.join(os.path.dirname(__file__), "app.py")

    # Usa el Python actual para ejecutar Streamlit como módulo, más compatible
    subprocess.run(["streamlit", "run", script_path])

if __name__ == "__main__":
    run_streamlit()

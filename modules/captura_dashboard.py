from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pdfkit
import os
import sys

def capturar_dashboard_png(url_dashboard, output_file="dashboard.png", ancho=1920, alto=1080):
    try:
        options = Options()
        options.headless = True
        options.add_argument(f"--window-size={ancho},{alto}")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        print("🔄 Cargando dashboard...")
        driver.get(url_dashboard)
        time.sleep(5)  # Espera que cargue todo

        driver.save_screenshot(output_file)
        print(f"✅ Captura PNG guardada como {output_file}")
        driver.quit()
    except Exception as e:
        print(f"❌ Error capturando PNG: {e}")

def capturar_dashboard_pdf(url_dashboard, output_file="dashboard.pdf"):
    try:
        # Ajusta esta ruta según tu sistema operativo
        wkhtml_path = "/usr/local/bin/wkhtmltopdf" if os.name != "nt" else "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"

        if not os.path.isfile(wkhtml_path):
            raise FileNotFoundError(f"wkhtmltopdf no encontrado en: {wkhtml_path}")

        config = pdfkit.configuration(wkhtmltopdf=wkhtml_path)
        pdfkit.from_url(url_dashboard, output_file, configuration=config)
        print(f"✅ Captura PDF generada como {output_file}")
    except Exception as e:
        print(f"❌ Error capturando PDF: {e}")

if __name__ == "__main__":
    url = "http://localhost:8501"
    print("📸 Iniciando captura del dashboard...")

    capturar_dashboard_png(url)
    capturar_dashboard_pdf(url)


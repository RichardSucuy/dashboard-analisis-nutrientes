@echo off
echo 🛠️ Iniciando entorno para el dashboard...

REM Crear entorno virtual si no existe
IF NOT EXIST "venvsuelo" (
    echo 🔧 Creando entorno virtual...
    python -m venv venv
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

REM Instalar requerimientos si no están instalados
echo 📦 Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt

REM Ejecutar la aplicación Streamlit
echo 🚀 Levantando el dashboard en tu navegador...
streamlit run app.py

pause

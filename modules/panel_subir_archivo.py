# En un nuevo archivo: modules/panel_subir_archivo.py

import streamlit as st
from modules.data_loader import cargar_archivo

def mostrar_panel_subir_archivo():
    st.title("📁 Cargar archivo Excel de análisis")

    archivo_excel = st.file_uploader("Selecciona el archivo .xlsx", type=["xlsx"])

    if archivo_excel:
        df_suelo, df_foliar, error = cargar_archivo(archivo_excel)

        if error:
            st.error(f"Error al cargar el archivo: {error}")
        else:
            st.session_state["df_suelo"] = df_suelo
            st.session_state["df_foliar"] = df_foliar
            st.success("Archivo cargado correctamente. Puedes continuar.")
            st.subheader("Vista previa - Suelo")
            st.dataframe(df_suelo.head(), use_container_width=True)
            st.subheader("Vista previa - Foliar")
            st.dataframe(df_foliar.head(), use_container_width=True)

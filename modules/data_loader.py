import pandas as pd
import streamlit as st

@st.cache_data
def cargar_archivo(archivo_bytes):
    try:
        df_suelo_raw = pd.read_excel(archivo_bytes, sheet_name="DATA_SUELO", skiprows=1).fillna("")
        df_foliar_raw = pd.read_excel(archivo_bytes, sheet_name="DATA_FOLIAR", skiprows=1).fillna("")

        # Quitar columna vacía si existe al inicio
        df_suelo = df_suelo_raw.iloc[:, 1:] if df_suelo_raw.columns[0].startswith("Unnamed") else df_suelo_raw
        df_foliar = df_foliar_raw.iloc[:, 1:] if df_foliar_raw.columns[0].startswith("Unnamed") else df_foliar_raw

        return df_suelo, df_foliar, ""
    except Exception as e:
        return None, None, str(e)

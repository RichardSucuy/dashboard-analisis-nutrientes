import streamlit as st
from modules.interface import encabezado_panel
from modules.filtros import filtros_interactivos
from modules.nutrientes import MAPEO_COLUMNAS_LOGICA, MAPEO_COLUMNAS
from modules.tablas import construir_tabla_html, generar_tabla_promedios, mostrar_tabla_rangos_editable_suelo
from modules.graficos import graficar_radar_suelo
from modules.utils import calcular_diferencia_porcentual
import pandas as pd
from modules.tablas import mostrar_tabla_relacion_bases
import json
from modules.tablas import mostrar_tabla_saturacion_bases
from modules.secciones_adicionales import mostrar_caja_comentarios, mostrar_caja_contacto
from modules.mapa import mostrar_mapa
from modules.captura import ejecutar_captura_dashboard
import time
import os


def mostrar_panel_suelo():
    # st.title("🟢 Panel de análisis del suelo")
    encabezado_panel("Suelo")
    if st.button("📸 Capturar Dashboard como imagen"):
        try:
            ejecutar_captura_dashboard()

            # Esperar hasta que el archivo exista (máximo 5 segundos)
            timeout = 5  # segundos
            start_time = time.time()
            while not os.path.exists("dashboard.png"):
                time.sleep(0.5)
                if time.time() - start_time > timeout:
                    raise FileNotFoundError("El archivo dashboard.png no fue creado a tiempo")

            st.success("✅ Captura realizada correctamente.")

            with open("dashboard.png", "rb") as file:
                st.download_button(
                    label="⬇️ Descargar imagen PNG",
                    data=file,
                    file_name="dashboard.png",
                    mime="image/png"
                )
        except Exception as e:
            st.error(f"❌ Error al capturar el dashboard: {e}")


    if "df_suelo" not in st.session_state:
        st.warning("Primero debes cargar un archivo válido desde el menú 📁 Subir archivo.")
        return

    df_suelo = st.session_state["df_suelo"]
    columnas_filtro = ["CULTIVO", "AÑO", "PRODUCTOR", "PROPIEDAD", "LOTE", "CODIGO MUESTRA", "FECHA ANALISIS"]

    if "filtros_suelo" not in st.session_state:
        st.session_state["filtros_suelo"] = {col: [] for col in columnas_filtro}

    seleccionados = filtros_interactivos(
        df_suelo,
        columnas_filtro,
        st.session_state["filtros_suelo"],
        panel="Suelo"
    )

    df_filtrado = aplicar_filtros(df_suelo, seleccionados)
    mostrar_promedios(df_filtrado)
    mostrar_tabla_rangos_editable_suelo()
    mostrar_dop_y_graficos(df_filtrado)
    
    # Crea 4 columnas horizontales para alinear los bloques
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:

        valores_promedio = st.session_state.get("valores_promedio_suelo", {})
        mostrar_tabla_relacion_bases(valores_promedio)

    with col2:

        mostrar_tabla_saturacion_bases()

    with col3:

        mostrar_mapa()

    with col4:
        mostrar_caja_comentarios()
        mostrar_caja_contacto()


    # st.subheader("🔎 Datos filtrados")
    # st.dataframe(df_filtrado, use_container_width=True)

def aplicar_filtros(df, seleccionados):
    for col, valores in seleccionados.items():
        if valores:
            df = df[df[col].isin(valores)]
    return df

def mostrar_promedios(df_filtrado):
    st.subheader("📊 Promedio de nutrientes")
    tabla_promedios = generar_tabla_promedios(df_filtrado)
    html_tabla = construir_tabla_html(tabla_promedios)
    st.markdown(html_tabla, unsafe_allow_html=True)
    st.session_state["tabla_promedios"] = tabla_promedios

    # Guardar diccionario de promedios para cálculos posteriores
    valores_promedio_dict = tabla_promedios.iloc[0].to_dict()
    st.session_state["valores_promedio_suelo"] = valores_promedio_dict

def mostrar_dop_y_graficos(df_filtrado):
    tabla_promedios = st.session_state.get("tabla_promedios")
    referenciales = st.session_state.get("valores_referenciales_suelo", {})
    if not referenciales or tabla_promedios is None:
        st.warning("No se encontraron valores referenciales o promedios.")
        return

    mapeo_inverso = {v.strip(): k for k, v in MAPEO_COLUMNAS_LOGICA.items()}
    valores_promedio_raw = tabla_promedios.iloc[0].to_dict()
    valores_promedio = {
        mapeo_inverso[nombre.strip()]: valor
        for nombre, valor in valores_promedio_raw.items()
        if nombre.strip() in mapeo_inverso
    }

    claves_comunes = [k for k in referenciales.keys() if k in valores_promedio]
    dop = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_comunes)

    # if claves_comunes:
    #     columnas = st.columns(len(claves_comunes), gap="small")
    #     for col, clave, dop_val in zip(columnas, claves_comunes, dop):
    #         if isinstance(dop_val, float) and not pd.isna(dop_val):
    #             dop_str = f"{dop_val:+.2f}%"
    #             color = "#e26410" if dop_val > 0 else "#4883bf"
    #             html = f"<div style='text-align:center; color:{color}; font-size: 0.9em;'><b>{dop_str}</b></div>"
    #         else:
    #             html = "<div style='text-align:center; font-size: 0.9em;'><span class='valor-vacio'>0.0</span></div>"
    #         col.markdown(html, unsafe_allow_html=True)
    # else:
    #     st.warning("No hay nutrientes en común entre promedios y referenciales.")

    etiquetas = MAPEO_COLUMNAS_LOGICA



    # --- Gráficos radiales en fila horizontal ---
    col1, col2, col3 = st.columns(3)

    # Gráfico 1
    claves_g1 = ["acinter", "mo", "phkcl", "ce"]
    dop_g1 = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_g1)
    valores_dop_g1 = dict(zip(claves_g1, dop_g1))
    grafico_1 = graficar_radar_suelo(valores_dop_g1, referenciales, claves_g1, "🟢 G1: MO, pH(KCl), CE, Ac. Inter.", etiquetas)

    # Gráfico 1
    with col1:
        # st.markdown("##### G1: Propiedades básicas")
        st.plotly_chart(grafico_1, use_container_width=True)

    # Gráfico 2
    claves_g2 = ["no3nh4", "azufre", "calcio", "magnesio", "potasio", "fosforo"]
    dop_g2 = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_g2)
    valores_dop_g2 = dict(zip(claves_g2, dop_g2))
    grafico_2 = graficar_radar_suelo(valores_dop_g2, referenciales, claves_g2, "🟧 G2: Macronutrientes", etiquetas)

    with col2:
        # st.markdown("##### G2: Macronutrientes")
        st.plotly_chart(grafico_2, use_container_width=True)

    # Gráfico 3
    claves_g3 = ["hierro", "boro", "zinc", "cobre", "manganeso"]
    dop_g3 = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_g3)
    valores_dop_g3 = dict(zip(claves_g3, dop_g3))
    grafico_3 = graficar_radar_suelo(valores_dop_g3, referenciales, claves_g3, "🟦 G3: Micronutrientes", etiquetas)

    with col3:
        # st.markdown("##### G3: Micronutrientes")
        st.plotly_chart(grafico_3, use_container_width=True)

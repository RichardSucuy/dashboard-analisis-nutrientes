import streamlit as st
from modules.interface import encabezado_panel
from modules.filtros import filtros_interactivos
from modules.nutrientes import MAPEO_COLUMNAS_LOGICA
from modules.tablas import construir_tabla_html, generar_tabla_promedios, mostrar_tabla_rangos_editable
from modules.graficos import graficar_radar_suelo, graficar_relaciones_cationicas
from modules.utils import calcular_diferencia_porcentual
import pandas as pd
from modules.tablas import mostrar_tabla_relacion_bases
import json
from modules.tablas import mostrar_tabla_saturacion_bases
from modules.secciones_adicionales import mostrar_caja_comentarios, mostrar_caja_contacto
from modules.mapa import mostrar_mapa

import time
import os
from modules.rangos import rangos_suelo_json
from modules.utils import boton_imprimir_pdf

def mostrar_panel_suelo():
    # st.title("🟢 Panel de análisis del suelo")
    encabezado_panel("Suelo")



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
    mostrar_tabla_rangos_editable(rangos_suelo_json, "valores_referenciales_suelo")
    

    mostrar_dop_y_graficos(df_filtrado)





    # Crea 4 columnas horizontales para alinear los bloques
    col1, col2, col3= st.columns([1, 1, 1])

    with col1:
        mostrar_tabla_saturacion_bases(df_filtrado)
        valores_promedio = st.session_state.get("valores_promedio_suelo", {})
        mostrar_tabla_relacion_bases(valores_promedio)
        

    with col2:

        mostrar_mapa(df_filtrado)

    with col3:
        st.markdown("💬 COMENTARIOS")
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
    st.subheader("🧫 Datos de Laboratorio")
    tabla_promedios = generar_tabla_promedios(df_filtrado)
    print(tabla_promedios.columns.tolist())
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

    etiquetas = MAPEO_COLUMNAS_LOGICA

    # --- Gráficos radiales en fila horizontal ---
    col1, col2, col3 = st.columns(3)

    # Gráfico 1
    claves_g1 = ["mo", "phkcl", "ce", "acinter"]
    dop_g1 = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_g1)
    valores_dop_g1 = dict(zip(claves_g1, dop_g1))
    grafico_1 = graficar_radar_suelo(valores_dop_g1, referenciales, claves_g1, "Propiedades quimicas del suelo", etiquetas)

    # Gráfico 1
    with col1:
        # st.markdown("##### G1: Propiedades básicas")
        st.plotly_chart(grafico_1, use_container_width=True)

    # Gráfico 2
    claves_g2 = ["no3nh4", "azufre", "calcio", "magnesio", "potasio", "fosforo"]
    dop_g2 = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_g2)
    valores_dop_g2 = dict(zip(claves_g2, dop_g2))
    grafico_2 = graficar_radar_suelo(valores_dop_g2, referenciales, claves_g2, "Fertilidad macronutrientes en suelo", etiquetas)

    with col2:
        # st.markdown("##### G2: Macronutrientes")
        st.plotly_chart(grafico_2, use_container_width=True)

    # Gráfico 3
    claves_g3 = ["hierro", "boro", "zinc", "cobre", "manganeso"]
    dop_g3 = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_g3)
    valores_dop_g3 = dict(zip(claves_g3, dop_g3))
    grafico_3 = graficar_radar_suelo(valores_dop_g3, referenciales, claves_g3, "Fertilidad micronutrientes en suelo", etiquetas)

    with col3:
        # st.markdown("##### G3: Micronutrientes")
        st.plotly_chart(grafico_3, use_container_width=True)

    # === G5: Relaciones Catiónicas ===

    #Extraer valores promedio desde el dict valores_promedio
    ca = valores_promedio.get("calcio", 0)
    mg = valores_promedio.get("magnesio", 0)
    k = valores_promedio.get("potasio", 0)

    # Verificar que haya datos válidos
    if ca > 0 and mg > 0 and k > 0:
        fig_g5 = graficar_relaciones_cationicas(ca, mg, k, "Relaciones de bases (Ca, Mg, K)")
        st.plotly_chart(fig_g5, use_container_width=True)
    else:
        st.warning("No hay suficientes datos para graficar relaciones catiónicas (Ca, Mg, K).")

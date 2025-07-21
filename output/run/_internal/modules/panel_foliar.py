import streamlit as st
from modules.interface import encabezado_panel
from modules.filtros import filtros_interactivos
from modules.utils import calcular_diferencia_porcentual
from modules.graficos import graficar_radar_suelo  # reutilizamos el mismo
from modules.secciones_adicionales import mostrar_caja_comentarios, mostrar_caja_contacto
from modules.mapa import mostrar_mapa

from modules.rangos import rangos_foliar_json
from modules.tablas import mostrar_tabla_rangos_editable
from modules.nutrientes import MAPEO_COLUMNAS_FOLIAR, columnas_foliar_saltos, MAPEO_COLUMNAS_FOLIAR_LOGICA2

from modules.tablas import generar_tabla_promedios_foliar, construir_tabla_html_foliar
# from modules.utils import boton_imprimir_pdf

def mostrar_panel_foliar():
    encabezado_panel("Foliar")


    if "df_foliar" not in st.session_state:
        st.warning("Primero debes cargar un archivo válido desde el menú 📁 Subir archivo.")
        return

    df_foliar = st.session_state["df_foliar"]
    print(df_foliar.columns.tolist())
    columnas_filtro = ["CULTIVO", "AÑO", "PRODUCTOR", "PROPIEDAD", "LOTE", "CODIGO MUESTRA", "FECHA ANALISIS"]

    if "filtros_foliar" not in st.session_state:
        st.session_state["filtros_foliar"] = {col: [] for col in columnas_filtro}

    seleccionados = filtros_interactivos(
        df_foliar,
        columnas_filtro,
        st.session_state["filtros_foliar"],
        panel="Foliar"
    )

    df_filtrado = aplicar_filtros(df_foliar, seleccionados)
           
    mostrar_promedios_foliar(df_filtrado)

    mostrar_tabla_rangos_editable(rangos_foliar_json, "valores_referenciales_foliar")

    
    mostrar_dop_y_graficos_foliar(df_filtrado)

    # Crea 4 columnas horizontales para alinear los bloques
    col1, col2= st.columns([1, 1])

    with col1:

        mostrar_mapa(df_filtrado)

    with col2:

        mostrar_caja_comentarios()
        mostrar_caja_contacto()

    # # Mostrar el botón solo en Panel Suelo
    # boton_imprimir_pdf(escala=0.5, orientacion="portrait")

def aplicar_filtros(df, seleccionados):
    for col, valores in seleccionados.items():
        if valores:
            df = df[df[col].isin(valores)]
    return df

def mostrar_promedios_foliar(df_filtrado):
    st.subheader("🧫 Datos de Laboratorio")
    tabla_promedios = generar_tabla_promedios_foliar(df_filtrado, MAPEO_COLUMNAS_FOLIAR)
    # st.text("Columnas detectadas en tabla_promedios:")
    # st.write(tabla_promedios.columns.tolist())

    html_tabla = construir_tabla_html_foliar(tabla_promedios, columnas_foliar_saltos)
    st.markdown(html_tabla, unsafe_allow_html=True)
    st.session_state["tabla_promedios_foliar"] = tabla_promedios

    # Guardar diccionario para cálculos posteriores
    valores_promedio_dict = tabla_promedios.iloc[0].to_dict()
    st.session_state["valores_promedio_foliar"] = valores_promedio_dict


def mostrar_dop_y_graficos_foliar(df_filtrado):
    # Accedemos a la tabla de promedios
    tabla_promedios = st.session_state.get("tabla_promedios_foliar")
    referenciales = st.session_state.get("valores_referenciales_foliar", {})

    if not referenciales or tabla_promedios is None:
        st.warning("No se encontraron valores referenciales o promedios.")
        return

    # Obtenemos los valores reales y los asociamos a las claves internas
    valores_promedio_raw = tabla_promedios.iloc[0].to_dict()
    valores_promedio = {}

    for clave_logica, etiqueta_excel in MAPEO_COLUMNAS_FOLIAR_LOGICA2.items():
        if etiqueta_excel in valores_promedio_raw:
            valores_promedio[clave_logica] = valores_promedio_raw[etiqueta_excel]


    etiquetas = MAPEO_COLUMNAS_FOLIAR_LOGICA2

    col1, col2 = st.columns(2)

    # Gráfico 1: Macronutrientes principales
    claves_g1 = [ "nitrogeno",  "azufre", "calcio", "magnesio", "potasio", "fosforo"]
    dop_g1 = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_g1)
    valores_dop_g1 = dict(zip(claves_g1, dop_g1))
    grafico_1 = graficar_radar_suelo(valores_dop_g1, referenciales, claves_g1, "Macronutrientes foliar", etiquetas)

    with col1:
        st.plotly_chart(grafico_1, use_container_width=True)

    # Gráfico 2: Micronutrientes
    claves_g2 = ["hierro", "boro", "zinc", "cobre", "manganeso", ]
    dop_g2 = calcular_diferencia_porcentual(valores_promedio, referenciales, claves_g2)
    valores_dop_g2 = dict(zip(claves_g2, dop_g2))
    grafico_2 = graficar_radar_suelo(valores_dop_g2, referenciales, claves_g2, "Micronutrientes foliar", etiquetas)

    with col2:
        st.plotly_chart(grafico_2, use_container_width=True)


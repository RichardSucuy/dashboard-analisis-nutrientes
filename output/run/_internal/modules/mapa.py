# import streamlit as st
# import folium
# import pandas as pd
# from streamlit_folium import st_folium

# def mostrar_mapa(df_filtrado):
#     st.markdown("🌍 COORDENADAS")

#     # Convertir nombres de columnas a minúsculas
#     columnas = [c.lower() for c in df_filtrado.columns]

#     if "latitud" not in columnas or "longitud" not in columnas:
#         st.error("⚠️ El archivo cargado no contiene columnas 'latitud' y 'longitud'.")
#         return

#     # Extraer valores sin errores
#     df = df_filtrado.copy()
#     df["latitud"] = pd.to_numeric(df["latitud"], errors="coerce")
#     df["longitud"] = pd.to_numeric(df["longitud"], errors="coerce")

#     lat = df["latitud"].mean(skipna=True)
#     lon = df["longitud"].mean(skipna=True)

#     # Validación por si no hay valores válidos
#     if pd.isna(lat) or pd.isna(lon):
#         lat = -3.2535
#         lon = -79.8610
#         st.info("🔁 No hay coordenadas válidas en la selección. Se muestra ubicación por defecto.")

#     # Entradas editables
#     col1, col2 = st.columns(2)
#     with col1:
#         lat = st.number_input(
#             "Latitud", 
#             min_value=-90.0, 
#             max_value=90.0, 
#             value=lat, 
#             step=0.00001,  # más preciso que 0.0001 (~1 metro)
#             format="%.6f",  # mostrar hasta 6 decimales
#             key="input_lat"
#         )

#     with col2:
#         lon = st.number_input(
#             "Longitud", 
#             min_value=-180.0, 
#             max_value=180.0, 
#             value=lon, 
#             step=0.00001, 
#             format="%.6f", 
#             key="input_lon"
#         )

#     zoom = st.slider("Zoom del mapa", min_value=1, max_value=20, value=13)

#     # Crear mapa
#     mapa = folium.Map(location=[lat, lon], zoom_start=zoom, tiles=None)
#     folium.TileLayer(
#         tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
#         attr='ESRI World Imagery',
#         name='ESRI',
#         overlay=True,
#         control=True
#     ).add_to(mapa)

#     folium.Marker([lat, lon], popup="Ubicación de muestra", icon=folium.Icon(color="red", icon="map-marker")).add_to(mapa)

#     # Contenedor controlado para evitar expansión inicial
#     with st.container():
#         # Ajuste CSS inline para controlar el iframe del mapa
#         st.markdown("""
#             <style>
#             iframe {
#                 max-width: 100% !important;
#                 height: 250px !important;
#                 border-radius: 10px;
#                 display: block;
#                 margin: 0 auto;
#             }

#             /* Eliminar espacio vacío hacia abajo */
#             .element-container:has(> iframe) {
#                 margin-bottom: -20px;
#             }
#             </style>
#         """, unsafe_allow_html=True)

#         st_folium(mapa, width=None, height=250, key=f"mapa-{lat:.4f}-{lon:.4f}")


import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium
from PIL import Image
import socket

def mostrar_mapa(df_filtrado):
    st.markdown("🌍 COORDENADAS")

    columnas = [c.lower() for c in df_filtrado.columns]

    if "latitud" not in columnas or "longitud" not in columnas:
        st.error("⚠️ El archivo cargado no contiene columnas 'latitud' y 'longitud'.")
        return

    df = df_filtrado.copy()
    df["latitud"] = pd.to_numeric(df["latitud"], errors="coerce")
    df["longitud"] = pd.to_numeric(df["longitud"], errors="coerce")

    lat = df["latitud"].mean(skipna=True)
    lon = df["longitud"].mean(skipna=True)

    if pd.isna(lat) or pd.isna(lon):
        lat, lon = -3.2535, -79.8610
        st.info("🔁 No hay coordenadas válidas en la selección. Se muestra ubicación por defecto.")

    col1, col2 = st.columns(2)
    with col1:
        lat = st.number_input("Latitud", min_value=-90.0, max_value=90.0, value=lat, step=0.00001, format="%.6f", key="input_lat")
    with col2:
        lon = st.number_input("Longitud", min_value=-180.0, max_value=180.0, value=lon, step=0.00001, format="%.6f", key="input_lon")

    zoom = st.slider("Zoom del mapa", min_value=1, max_value=20, value=13)

    # 🛡️ INTENTAR conexión a Internet (timeout corto)
    def hay_internet():
        try:
            socket.create_connection(("www.google.com", 80), timeout=3)
            return True
        except OSError:
            return False

    if hay_internet():
        try:
            mapa = folium.Map(location=[lat, lon], zoom_start=zoom, tiles=None)
            folium.TileLayer(
                tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                attr='ESRI World Imagery',
                name='ESRI',
                overlay=True,
                control=True
            ).add_to(mapa)
            folium.Marker([lat, lon], popup="Ubicación de muestra", icon=folium.Icon(color="red", icon="map-marker")).add_to(mapa)

            with st.container():
                st.markdown("""
                    <style>
                    iframe {
                        max-width: 100% !important;
                        height: 250px !important;
                        border-radius: 10px;
                        display: block;
                        margin: 0 auto;
                    }
                    .element-container:has(> iframe) {
                        margin-bottom: -20px;
                    }
                    </style>
                """, unsafe_allow_html=True)
                st_folium(mapa, width=None, height=250, key=f"mapa-{lat:.4f}-{lon:.4f}")

        except Exception as e:
            st.warning("⚠️ Ocurrió un error al cargar el mapa. Se mostrará una imagen de respaldo.")
            imagen = Image.open("assets/ecuador.png")
            st.image(imagen, caption="🌍 Ubicación referencial: Ecuador", use_container_width=True)


    else:
        st.warning("⚠️ No hay conexión a Internet. Mostrando imagen local.")
        imagen = Image.open("assets/ecuador.png")
        st.image(imagen, caption="🌍 Ubicación referencial: Ecuador", use_container_width=True)


import streamlit as st
import folium
from streamlit_folium import st_folium

def mostrar_mapa():
    st.markdown("### 🌍 COORDENADAS")

    # Entradas para latitud, longitud y zoom
    lat = st.number_input("Latitud", min_value=-90.0, max_value=90.0, value=-3.2534992569698824, step=0.0001)
    lon = st.number_input("Longitud", min_value=-180.0, max_value=180.0, value=-79.86107524349622, step=0.0001)
    zoom = st.number_input("Zoom", min_value=1, max_value=20, value=13)

    # Crear mapa
    mapa = folium.Map(location=[lat, lon], zoom_start=zoom, tiles=None)
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='ESRI World Imagery',
        name='ESRI',
        overlay=True,
        control=True
    ).add_to(mapa)

    folium.Marker([lat, lon], popup="Ubicación de muestra").add_to(mapa)

    st_folium(mapa, width=300, height=250)

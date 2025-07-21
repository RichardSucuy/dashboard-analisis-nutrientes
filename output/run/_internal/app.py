
# from modules.panel_foliar import mostrar_panel_foliar
from modules.panel_suelo import mostrar_panel_suelo
from modules.panel_foliar import mostrar_panel_foliar
from modules.interface import sidebar_nav
from modules.interface import cargar_css

from modules.panel_subir_archivo import mostrar_panel_subir_archivo
import streamlit as st


cargar_css()

st.set_page_config(layout="wide")

menu_seleccionado = sidebar_nav()

if menu_seleccionado == "Panel Suelo":
    mostrar_panel_suelo()


if menu_seleccionado == "Subir archivo":
    mostrar_panel_subir_archivo()
elif menu_seleccionado == "Panel Foliar":
    mostrar_panel_foliar()


import streamlit as st


def cargar_css():
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def encabezado_panel(panel):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: flex-end;">
            <span style="color: #888; font-weight: bold; font-size: 1.2em;" id="panel_name">
                {'🟫 Suelo' if panel=='Suelo' else '🌿 Foliar'}
            </span>
        </div>
        """, unsafe_allow_html=True)

def sidebar_nav():
    st.sidebar.markdown(
        "<h2 style='text-align:center; color:#3366cc; margin-bottom:30px;'>🌱 Dashboard</h2>",
        unsafe_allow_html=True
    )
    menu = st.sidebar.radio(
        "Ir a:",
        ["Subir archivo", "Panel Suelo", "Panel Foliar"],
        format_func=lambda x: {"Subir archivo":"📁 Subir archivo", "Panel Suelo":"🟫 Suelo", "Panel Foliar":"🌿 Foliar"}[x],
    )
    return menu

def footer():
    st.markdown("""
        <hr style="margin-top: 30px; margin-bottom: 0; border:0; border-top: 1px solid #eee;">
        <div style='text-align:center; color:#bbb; font-size: 0.9em;'>
            Minimal dashboard · hecho con <b>Streamlit</b>
        </div>
    """, unsafe_allow_html=True)

import streamlit as st

def mostrar_caja_comentarios():
    # st.markdown("<h3 style='margin-bottom: 0.5rem;'>💬 Comentarios</h3>", unsafe_allow_html=True)
    comentario = st.text_area(
        label="💬 Comentarios",
        placeholder="",
        height=200,
        key="comentarios_suelo"
    )
    return comentario

def mostrar_caja_contacto():
    st.markdown("📇 DATOS DE CONTACTO")

    nombre = st.text_input("Nombre completo", key="contacto_nombre")
    celular = st.text_input("Celular", key="contacto_celular")
    correo = st.text_input("Correo electrónico", key="contacto_correo")

    return {"nombre": nombre, "celular": celular, "correo": correo}

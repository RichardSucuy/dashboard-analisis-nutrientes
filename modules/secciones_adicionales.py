import streamlit as st

def mostrar_caja_comentarios():
    st.markdown("### 💬 Comentarios")
    comentario = st.text_area(
        label="",
        placeholder="Escribe tus observaciones o conclusiones aquí...",
        height=100,
        key="comentarios_suelo"
    )
    return comentario

def mostrar_caja_contacto():
    st.markdown("### 📇 Datos de Contacto")

    nombre = st.text_input("Nombre completo", key="contacto_nombre")
    celular = st.text_input("Celular", key="contacto_celular")
    correo = st.text_input("Correo electrónico", key="contacto_correo")

    return {"nombre": nombre, "celular": celular, "correo": correo}

import streamlit as st

def filtros_interactivos(df, filtros, seleccionados, panel):
    filtro_cols = st.columns(len(filtros), gap="small")
    for idx, col in enumerate(filtros):
        temp_df = df.copy()
        for otro_col in filtros:
            if otro_col != col and seleccionados[otro_col]:
                temp_df = temp_df[temp_df[otro_col].isin(seleccionados[otro_col])]
        opciones = sorted([
            v for v in temp_df[col].unique() if str(v).strip() != "" and v != 0.0
        ])
        seleccion_validada = [v for v in seleccionados[col] if v in opciones]
        with filtro_cols[idx]:
            st.markdown(f"<div style='text-align:center;font-weight:bold;margin-bottom:2px'>{col.title()}</div>", unsafe_allow_html=True)
            seleccion = st.multiselect(
                "",
                opciones,
                default=seleccion_validada,
                key=panel + col
            )
        seleccionados[col] = seleccion
    return seleccionados

import pandas as pd
from modules.nutrientes import MAPEO_COLUMNAS
import streamlit as st
from modules.utils import calcular_relaciones_bases

import streamlit as st
from modules.nutrientes import MAPEO_COLUMNAS_LOGICA


def generar_tabla_promedios(df):
    df.columns = df.columns.str.strip()  # limpiar espacios invisibles

    # Invertimos el mapeo para encontrar columnas en el Excel
    mapeo_invertido = {v.strip(): k for k, v in MAPEO_COLUMNAS.items()}

    columnas_en_excel = [col for col in df.columns if col.strip() in mapeo_invertido]
    if not columnas_en_excel:
        return pd.DataFrame([["No hay columnas de nutrientes válidas"]], columns=["⚠️ Vacío"])

    # Convertimos a numérico solo las columnas que nos interesan
    df_nutrientes = df[columnas_en_excel].apply(pd.to_numeric, errors="coerce")
    promedios = df_nutrientes.mean().round(2)

    # Renombramos usando las claves originales (nutriente corto)
    promedios.index = [mapeo_invertido[col.strip()] for col in promedios.index]

    return promedios.to_frame().T


def construir_tabla_html(df):
    columnas = df.columns.tolist()

    columnas_con_saltos = {
        "M.O. %": "M.O.\n%",
        "CIC meq/100g": "CIC\nmeq/100g",
        "Ac. Inter. meq/100g": "Ac. Inter.\nmeq/100g",
        "Al Inter. meq/100g": "Al Inter.\nmeq/100g",
        "(CE) mS/cm": "(CE)\nmS/cm",
        "pH  (en H2O)": "pH\n(en H2O)",
        "pH  (en KCl)": "pH\n(en KCl)",
        "(NO3-N) mg/kg": "(NO3-N)\nmg/kg",
        "(NH4-N) mg/kg": "(NH4-N)\nmg/kg",
        "(NO3+NH4) N mg/kg": "(NO3+NH4)\nN mg/kg",
        "(P) mg/kg": "(P)\nmg/kg",
        "(K) mg/kg": "(K)\nmg/kg",
        "(Mg) mg/kg": "(Mg)\nmg/kg",
        "(Ca) mg/kg": "(Ca)\nmg/kg",
        "(SO4-S) mg/kg": "(SO4-S)\nmg/kg",
        "(Fe) mg/kg": "(Fe)\nmg/kg",
        "(Mn) mg/kg": "(Mn)\nmg/kg",
        "(Cu) mg/kg": "(Cu)\nmg/kg",
        "(Zn)  mg/kg": "(Zn)\nmg/kg",
        "(B)  mg/kg": "B\nmg/kg",
        "(Na)  mg/kg": "Na\nmg/kg",
        "(Cl¯)  mg/kg": "Cl¯\nmg/kg",
        "Sales Totales mg/kg": "Sales total \nmg/kg"
    }



    columnas = [columnas_con_saltos.get(col, col) for col in columnas]

    valores = df.iloc[0].tolist()  # solo una fila

    html = '<table class="vertical-headers" style="width: 100%;">\n'

    html += '  <tr>\n'
    for col in columnas:
        html += f'    <th><div>{col}</div></th>\n'

    html += '  </tr>\n'
    html += '  <tr>\n'
    for val in valores:
        if pd.isna(val):
            html += '<td><span class="valor-vacio">0.0</span></td>\n'
        else:
            html += f'<td>{val}</td>\n'

    html += '  </tr>\n'
    html += '</table>'

    return html



def generar_tabla_promedios_foliar(df, mapeo_columnas):
    df.columns = df.columns.str.strip()  # limpiar espacios invisibles

    # Invertimos el mapeo para encontrar columnas en el Excel
    mapeo_invertido = {v.strip(): k for k, v in mapeo_columnas.items()}

    columnas_en_excel = [col for col in df.columns if col.strip() in mapeo_invertido]
    if not columnas_en_excel:
        return pd.DataFrame([["No hay columnas de nutrientes válidas"]], columns=["⚠️ Vacío"])

    # st.write("Columnas en Excel:", df.columns.tolist())
    # st.write("Columnas válidas encontradas:", columnas_en_excel)


    # Convertimos a numérico solo las columnas que nos interesan
    df_nutrientes = df[columnas_en_excel].apply(pd.to_numeric, errors="coerce")
    promedios = df_nutrientes.mean().round(2)

    # Renombramos usando las claves originales (nutriente corto)
    promedios.index = [mapeo_invertido[col.strip()] for col in promedios.index]

    return promedios.to_frame().T


def construir_tabla_html_foliar(df, columnas_con_saltos={}):
    columnas = df.columns.tolist()

    # Aplica saltos si se proporcionan, de lo contrario deja los nombres como están
    columnas = [columnas_con_saltos.get(col, col) for col in columnas]

    valores = df.iloc[0].tolist()  # solo una fila

    html = '<table class="vertical-headers" style="width: 100%;">\n'

    html += '  <tr>\n'
    for col in columnas:
        html += f'    <th><div>{col}</div></th>\n'

    html += '  </tr>\n'
    html += '  <tr>\n'
    for val in valores:
        if pd.isna(val):
            html += '<td><span class="valor-vacio">0.0</span></td>\n'
        else:
            html += f'<td>{val}</td>\n'

    html += '  </tr>\n'
    html += '</table>'

    return html


def mostrar_tabla_rangos_editable(rangos_json: dict, clave_session_state: str):
    import streamlit as st

    nutrientes = list(rangos_json.keys())
    nombres = [rangos_json[n]["nombre"] for n in nutrientes]

    st.markdown("### Rangos de nutrientes")

    columnas = st.columns(len(nutrientes), gap="small")

    min_vals = []
    max_vals = []
    referenciales = []
    # ======= FILA 1: Máximos =======
    for col, nutriente in zip(columnas, nutrientes):
        max_default = rangos_json[nutriente].get("max", 0.0)
        max_val = col.number_input(
            label="",
            value=max_default,
            key=f"max_{nutriente}",
            label_visibility="collapsed"
        )
        max_vals.append(max_val)

    # ======= FILA 2: Mínimos =======
    for col, nutriente in zip(columnas, nutrientes):
        min_default = rangos_json[nutriente].get("min", 0.0)
        min_val = col.number_input(
            label="",
            value=min_default,
            key=f"min_{nutriente}",
            label_visibility="collapsed"
        )
        min_vals.append(min_val)


    # ======= FILA 3: Valor referencial =======
    for col, min_val, max_val in zip(columnas, min_vals, max_vals):
        ref = round((min_val + max_val) / 2, 2)
        referenciales.append(ref)
        col.markdown(
            f"<div style='text-align:left; margin-top:6px; font-size: 0.9em; color:#333;'><b>{ref}</b></div>",
            unsafe_allow_html=True
        )

    # Guardar resultados en session_state
    st.session_state[clave_session_state] = dict(zip(nutrientes, referenciales))


def mostrar_tabla_relacion_bases(valores_promedio: dict):
# def mostrar_relacion_bases(valores_promedio: dict):
    st.markdown("<h3 style='margin-bottom: 0.2rem; margin-top: 0.5rem;'>Relación de Bases</h3>", unsafe_allow_html=True)

    col_titles = ["Ca/Mg", "Ca/K", "Mg/K", "Ca+Mg/K"]
    col_rangos = st.columns(len(col_titles), gap="small")

    # ==== FILA DE TÍTULO "Rangos" CENTRADO ====
    cols_titulo = st.columns(len(col_titles), gap="small")
    for i, col in enumerate(cols_titulo):
        if i == len(col_titles)//2 - 1:
            col.markdown("<div style='text-align:center; font-weight:bold; margin-top:-0.5rem;'>Rangos</div>", unsafe_allow_html=True)


    # ==== FILA 1: MÁXIMOS ====
    col_rangos = st.columns(len(col_titles), gap="small")
    for col, nombre in zip(col_rangos, col_titles):
        col.number_input(f"Máx {nombre}", value=0.0, key=f"base_max_{nombre}", label_visibility="collapsed")

    # ==== FILA 2: MÍNIMOS ====
    for col, nombre in zip(col_rangos, col_titles):
        col.number_input(f"Mín {nombre}", value=0.0, key=f"base_min_{nombre}", label_visibility="collapsed")

    # (Opcional: mostrar resultados u otros elementos)
    st.markdown("<div style='text-align:center; font-weight:bold; margin-top:10px;'>Nutrientes involucrados</div>", unsafe_allow_html=True)


    # Invertir el mapeo visual ➝ clave lógica
    MAPEO_INVERSO = {v.strip(): k for k, v in MAPEO_COLUMNAS_LOGICA.items()}

    # Transformar las claves del diccionario
    valores_promedio = {
        MAPEO_INVERSO.get(k.strip(), k.strip()): v
        for k, v in valores_promedio.items()
}

    # Mapear nombres visuales
    etiquetas = {
        "Ca/Mg": "Ca/Mg ",
        "Ca/K": "Ca/K ",
        "Mg/K": "Mg/K ",
        "Ca+Mg/K": "Ca+Mg/K "
    }

    relaciones = calcular_relaciones_bases(
        ca=valores_promedio.get("calcio", 0),
        mg=valores_promedio.get("magnesio", 0),
        k=valores_promedio.get("potasio", 0)
    )

    col_resultados = st.columns(len(col_titles), gap="small")
    for col, nombre in zip(col_resultados, col_titles):
        valor = relaciones.get(nombre, 0.0)
        html = f"""
        <div style='text-align:left; font-size: 0.8em;'>
            <b>{etiquetas[nombre]}</b><br>
            <span style='font-size: 0.9em; color:#333;'>{valor}</span>
        </div>
        """
        col.markdown(html, unsafe_allow_html=True)




import streamlit as st
import pandas as pd

def mostrar_tabla_saturacion_bases(df_filtrado):
    st.markdown("### 🧪 Saturación de Bases (%)")

    nutrientes = ["% Ca:", "% Mg:", "% K:", "% Na:"]
    porcentajes = {}
    cols = st.columns(len(nutrientes))

    valores = {}
    if len(df_filtrado) > 1:
        for n in nutrientes:
            val = pd.to_numeric(df_filtrado[n], errors="coerce").mean(skipna=True)
            valores[n] = round(val, 2) if not pd.isna(val) else "vacío"
    elif len(df_filtrado) == 1:
        fila = df_filtrado.iloc[0]
        for n in nutrientes:
            val = fila.get(n, None)
            try:
                val = pd.to_numeric(val, errors="coerce")
                if pd.isna(val):
                    valores[n] = "vacío"
                else:
                    valores[n] = round(val, 2)
            except Exception:
                valores[n] = "vacío"

    else:
        valores = {n: "~" for n in nutrientes}

    for col, nutriente in zip(cols, nutrientes):
        valor = valores[nutriente]
        if valor == "vacío":
            col.markdown(
                f'<div style="text-align:center; font-size:1.2em;"><span class="valor-vacio">0.0</span></div>',
                unsafe_allow_html=True
            )

        else:
            porcentajes[nutriente] = col.number_input(
                label=f"{nutriente}",
                min_value=0.0,
                max_value=100.0,
                value=valor,
                step=0.1,
                key=f"porcentaje_{nutriente}"
            )

    suma_total = sum(porcentajes.values()) if porcentajes else 0.0
    st.markdown(
        f"<div style='text-align:center; font-weight:bold; margin-top:10px;'>🔢 Total: {suma_total:.2f}%</div>",
        unsafe_allow_html=True
    )

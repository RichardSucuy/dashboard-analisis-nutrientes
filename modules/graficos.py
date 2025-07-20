# modules/graficos.py
import plotly.graph_objects as go

def _transformar_dop_para_grafico(dop: float) -> float:
    """Transforma un valor Dop (%) en su representación radial."""
    if dop is None:
        return 0
    try:
        if dop < 0:
            # Déficit: va por debajo del óptimo (100), se acerca al centro.
            return abs(dop)
        else:
            # Exceso: supera la banda óptima (100%) hacia afuera.
            return 100 + dop
    except Exception:
        return 0

def graficar_radar_suelo(
    valores_dop: dict,
    valores_referenciales: dict,
    claves: list,
    titulo: str,
    etiquetas: dict | None = None,
):
    """
    Gráfico radial comparando Óptimo (100%) vs Resultado transformado a escala Dop.
    
    Parámetros
    ----------
    valores_dop : dict
        Clave nutriente -> Dop real (% con signo, ej. -30.93, +12.5)
    valores_referenciales : dict
        Clave nutriente -> valor referencial numérico (no se usa directo en radial,
        pero puede servir para tooltips o validaciones futuras).
    claves : list
        Lista ordenada de claves internas a graficar (ej. ["mo", "phkcl", "ce", "acinter"]).
    titulo : str
        Título del gráfico.
    etiquetas : dict opcional
        Mapeo clave -> etiqueta amigable para mostrar en el eje. Si no se da, usa la clave en mayúsculas.
    """

    # Etiquetas visibles
    if etiquetas:
        theta_labels = [etiquetas.get(k, k.upper()) for k in claves]
    else:
        theta_labels = [k.upper() for k in claves]

    # Dop reales (lo que verás en hover)
    dop_vals = [valores_dop.get(k, 0) for k in claves]

    # Transformados a escala radial
    r_dop = [_transformar_dop_para_grafico(d) for d in dop_vals]

    # Óptimo fijo a 100
    r_optimo = [100 for _ in claves]

    # Determinar rango radial máximo (si hay excesos grandes, expandimos)
    maximo_rango = max(r_optimo + r_dop + [100]) * 1.1  # margen 10%

    # Texto hover personalizado (muestra Dop real + estado)
    hover_text = []
    for k, dop in zip(claves, dop_vals):
        estado = "Déficit" if dop < 0 else "Exceso" if dop > 0 else "Óptimo"
        hover_text.append(f"{k}: {dop:+.2f}% ({estado})")

    fig = go.Figure()

# Repetir el primer punto al final para cerrar el polígono
    r_dop.append(r_dop[0])
    r_optimo.append(r_optimo[0])
    theta_labels.append(theta_labels[0])
    hover_text.append(hover_text[0])

    # Polígono Óptimo
    fig.add_trace(go.Scatterpolar(
        r=r_optimo,
        theta=theta_labels,
        name='Óptimo',
        line_color='rgba(255,153,51,0.8)',
        mode='lines+markers'
    ))

    # Polígono Resultado
    fig.add_trace(go.Scatterpolar(
        r=r_dop,
        theta=theta_labels,
        name='Resultado',
        line_color='rgba(60,130,255,0.8)',
        mode='lines+markers',
        text=hover_text,
        hoverinfo='text'
    ))

    fig.update_layout(
        title=titulo,
        showlegend=True,
        margin=dict(l=30, r=30, t=60, b=30),
        height=420,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, maximo_rango],
                tickfont=dict(size=10),
                gridcolor='rgba(0,0,0,0.1)'
            ),
            angularaxis=dict(
                tickfont=dict(size=10),
                gridcolor='rgba(0,0,0,0.1)'
            )
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.05,
            xanchor="right",
            x=1
        )
    )

    return fig

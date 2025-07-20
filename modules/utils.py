# modules/utils.py

def calcular_diferencia_porcentual(valores_reales: dict, valores_referenciales: dict, lista_claves: list) -> list:
    """
    Calcula el porcentaje de diferencia (dop) entre valores reales y referenciales.
    Fórmula: ((valor_real * 100) / valor_referencial) - 100

    :param valores_reales: dict con valores medidos (ej. {"potasio": 200})
    :param valores_referenciales: dict con valores óptimos (ej. {"potasio": 230})
    :param lista_claves: lista de claves a procesar (ej. ["potasio", "calcio"])
    :return: lista con dop redondeado (ej. [-13.04, 5.33])
    """
    resultado = []
    for clave in lista_claves:
        real = valores_reales.get(clave, 0)
        ref = valores_referenciales.get(clave, 1) or 1  # prevenir división por cero o None
        try:
            dop = ((real * 100) / ref) - 100
            resultado.append(round(dop, 2))
        except Exception:
            resultado.append(0)
    return resultado

def calcular_relaciones_bases(ca, mg, k):
    try:
        relaciones = {
            "Ca/Mg": round((ca / 200) / (mg / 121), 2) if mg else 0.0,
            "Ca/K": round((ca / 200) / (k / 390), 2) if k else 0.0,
            "Mg/K": round((mg / 121) / (k / 390), 2) if k else 0.0,
            "Ca+Mg/K": round(((ca / 200) + (mg / 121)) / (k / 390), 2) if k else 0.0
        }
    except ZeroDivisionError:
        relaciones = {key: 0.0 for key in ["Ca/Mg", "Ca/K", "Mg/K", "Ca+Mg/K"]}
    return relaciones

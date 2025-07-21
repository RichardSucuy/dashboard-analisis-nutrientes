rangos_suelo_json = {
    "mo": {"nombre": "M.O. %", "min": 3, "max": 12},
    "cic": {"nombre": "CIC meq/100g", "max": 15},
    "acinter": {"nombre": "Ac. Inter. meq/100g", "max": 0.5},
    "alinter": {"nombre": "Al Inter. meq/100g",  "max": 0.3},         # Añadido, ajusta si tienes rango
    "ce": {"nombre": "(CE) mS/cm", "min": 0.3,"max": 0.6},
    "phh2o": {"nombre": "pH (en H2O)"},                  # Añadido, ajusta si tienes rango
    "phkcl": {"nombre": "pH (en KCl)", "min": 5.5, "max": 7},
    "no3n": {"nombre": "(NO3-N) mg/kg"},                 # Añadido, ajusta si tienes rango
    "nh4n": {"nombre": "(NH4-N) mg/kg"},                 # Añadido, ajusta si tienes rango
    "no3nh4": {"nombre": "(NO3+NH4) N mg/kg", "min": 35, "max": 60},
    "fosforo": {"nombre": "(P) mg/kg", "min": 25, "max": 40},
    "potasio": {"nombre": "(K) mg/kg", "min": 140, "max": 320},
    "magnesio": {"nombre": "(Mg) mg/kg", "min": 60, "max": 135},
    "calcio": {"nombre": "(Ca) mg/kg", "min": 600, "max": 1200},
    "azufre": {"nombre": "(SO4-S) mg/kg", "min": 15, "max": 25},
    "hierro": {"nombre": "(Fe) mg/kg", "min": 20, "max": 50},
    "manganeso": {"nombre": "(Mn) mg/kg", "min": 6, "max": 30},
    "cobre": {"nombre": "(Cu) mg/kg", "min": 1, "max": 4},
    "zinc": {"nombre": "(Zn) mg/kg", "min": 1.2, "max": 6},
    "boro": {"nombre": "(B) mg/kg", "min": 0.15, "max": 0.6},
    "sodio": {"nombre": "(Na) mg/kg", "max": 140},
    "cloruro": {"nombre": "(Cl¯) mg/kg", "max": 210},
    "salestotales": {"nombre": "Sales Totales mg/kg", "max": 2000}    # Añadido
}

rangos_foliar_json = {
    "nitrogeno": {"nombre": "Nitrógeno Total (N)", "min": 2.34,  "max": 2.95},
    "fosforo":   {"nombre": "Fósforo (P)",         "min": 0.14, "max": 0.21},
    "potasio":   {"nombre": "Potasio (K)",         "min": 3.4,  "max": 4.15},
    "magnesio":  {"nombre": "Magnesio (Mg)",       "min": 0.29, "max": 0.36},
    "calcio":    {"nombre": "Calcio (Ca)",         "min": 0.51, "max": 0.72,},
    "azufre":    {"nombre": "Azufre (S)",          "min": 0.11, "max": 0.14},
    "cloruro":   {"nombre": "Cloruro (Cl-)",       "min": 0.6,   "max": 1},
    "sodio":     {"nombre": "Sodio (Na)",          "min": 0.01,   "max": 0.1},
    "hierro":    {"nombre": "Hierro (Fe)",         "min": 110,   "max": 165},
    "manganeso": {"nombre": "Manganeso (Mn)",      "min": 105,  "max": 192},
    "cobre":     {"nombre": "Cobre (Cu)",          "min": 7.0,  "max": 12.0},
    "zinc":      {"nombre": "Zinc (Zn)",           "min": 20,   "max": 44},
    "boro":      {"nombre": "Boro (B)",            "min": 11,   "max": 50}
}
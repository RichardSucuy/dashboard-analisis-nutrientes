NUTRIENTES_SUELO = [
    "M.O. %",
    "CIC meq/100g",
    "Ac. Inter. meq/100g",
    "Al Inter. meq/100g",
    "(CE) mS/cm",
    "pH  (en H2O)",
    "pH  (en KCl)",
    "(NO3-N) mg/kg",
    "(NH4-N) mg/kg",
    "(NO3+NH4) N mg/kg",
    "(P) mg/kg",
    "(K) mg/kg",
    "(Mg) mg/kg",
    "(Ca) mg/kg",
    "(SO4-S) mg/kg",
    "(Fe) mg/kg",
    "(Mn) mg/kg",
    "(Cu) mg/kg",
    "(Zn)  mg/kg",
    "(B)  mg/kg",
    "(Na)  mg/kg",
    "(Cl¯)  mg/kg",
    "Sales Totales mg/kg"
]

MAPEO_COLUMNAS = {
    "M.O. %": "Materia \nOrgánica %",
    "CIC meq/100g": "**Capacidad de Intercambio\nCatiónico - CIC\nmeq/100g",
    "Ac. Inter. meq/100g": "Acidez Inter.\nmeq/100g",
    "Al Inter. meq/100g": "Aluminio Inter.\nmeq/100g",
    "(CE) mS/cm": "Conductividad (CE)\nmS/cm",
    "pH  (en H2O)": "pH \n(en H2O)",
    "pH  (en KCl)": "pH \n(en KCl)",
    "(NO3-N) mg/kg": "Nitrato \n(NO3-N)\nmg/kg",
    "(NH4-N) mg/kg": "Amonio \n(NH4-N)\nmg/kg",
    "(NO3+NH4) N mg/kg": "(NO3+NH4)\nN\nmg/kg",
    "(P) mg/kg": "Fósforo \n(P)\nmg/kg",
    "(K) mg/kg": "Potasio \n(K)\nmg/kg",
    "(Mg) mg/kg": "Magnesio \n(Mg)\nmg/kg",
    "(Ca) mg/kg": "Calcio \n(Ca)\nmg/kg",
    "(SO4-S) mg/kg": "Azufre \n(SO4-S)\nmg/kg",
    "(Fe) mg/kg": "Hierro \n(Fe)\nmg/kg",
    "(Mn) mg/kg": "Manganeso \n(Mn)\nmg/kg",
    "(Cu) mg/kg": "Cobre \n(Cu)\nmg/kg",
    "(Zn)  mg/kg": "Zinc \n(Zn) \nmg/kg",
    "(B)  mg/kg": "Boro \n(B) \nmg/kg",
    "(Na)  mg/kg": "Sodio  \n(Na) \nmg/kg",
    "(Cl¯)  mg/kg": "Cloruro \n(Cl¯) \nmg/kg",
    "Sales Totales mg/kg": "Sales Totales\nmg/kg"
}

MAPEO_COLUMNAS_LOGICA = {
    "mo": "M.O. %",
    "cic": "CIC meq/100g",
    "acinter": "Ac. Inter. meq/100g",
    "alinter": "Al Inter. meq/100g",
    "ce": "(CE) mS/cm",
    "phh2o": "pH  (en H2O)",
    "phkcl": "pH  (en KCl)",
    "no3n": "(NO3-N) mg/kg",
    "nh4n": "(NH4-N) mg/kg",
    "no3nh4": "(NO3+NH4) N mg/kg",
    "fosforo": "(P) mg/kg",
    "potasio": "(K) mg/kg",
    "magnesio": "(Mg) mg/kg",
    "calcio": "(Ca) mg/kg",
    "azufre": "(SO4-S) mg/kg",
    "hierro": "(Fe) mg/kg",
    "manganeso": "(Mn) mg/kg",
    "cobre": "(Cu) mg/kg",
    "zinc": "(Zn)  mg/kg",
    "boro": "(B)  mg/kg",
    "sodio": "(Na)  mg/kg",
    "cloruro": "(Cl¯)  mg/kg",
    "salestotales": "Sales Totales mg/kg"
}

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

# ------------  FOLIAR ------------

NUTRIENTES_FOLIAR = [
    "Nitrógeno Total (N)",
    "Fósforo (P)",
    "Potasio (K)",
    "Magnesio (Mg)",
    "Calcio (Ca)",
    "Azufre (S)",
    "Cloruro (Cl-) (%)",
    "Sodio (Na) (%)",
    "Hierro (Fe)",
    "Manganeso (Mn)",
    "Cobre (Cu)",
    "Zinc (Zn)",
    "Boro (B)",
]


MAPEO_COLUMNAS_FOLIAR = {
    "Nitrógeno Total (N)": "Nitrógeno Total \n(N)",
    "Fósforo (P)": "Fósforo \n(P)",
    "Potasio (K)": "Potasio \n(K)",
    "Magnesio (Mg)": "Magnesio\n(Mg)",
    "Calcio (Ca)": "Calcio \n(Ca)",
    "Azufre (S)": "Azufre \n(S)",
    "Cloruro (Cl-) (%)": "Cloruro\n(Cl-)",
    "Sodio (Na) (%)": "Sodio \n(Na)",
    "Hierro (Fe)": "Hierro \n(Fe)",
    "Manganeso (Mn)": "Manganeso\n(Mn)",
    "Cobre (Cu)": "Cobre \n(Cu)",
    "Zinc (Zn)": "Zinc \n(Zn)",
    "Boro (B)": "Boro \n(B)"
}



MAPEO_COLUMNAS_FOLIAR_LOGICA = {
    "nitrogeno": "Nitrógeno Total \n(N)",
    "fosforo": "Fósforo \n(P)",
    "potasio": "Potasio \n(K)",
    "magnesio": "Magnesio\n(Mg)",
    "calcio": "Calcio \n(Ca)",
    "azufre": "Azufre \n(S)",
    "cloruro": "Cloruro\n(Cl-)",
    "sodio": "Sodio \n(Na)",
    "hierro": "Hierro \n(Fe)",
    "manganeso": "Manganeso\n(Mn)",
    "cobre": "Cobre \n(Cu)",
    "zinc": "Zinc \n(Zn)",
    "boro": "Boro \n(B)"
}

MAPEO_COLUMNAS_FOLIAR_LOGICA2 = {
    "nitrogeno": "Nitrógeno Total (N)",
    "fosforo": "Fósforo (P)",
    "potasio": "Potasio (K)",
    "magnesio": "Magnesio (Mg)",
    "calcio": "Calcio (Ca)",
    "azufre": "Azufre (S)",
    "cloruro": "Cloruro (Cl-) (%)",
    "sodio": "Sodio (Na) (%)",
    "hierro": "Hierro (Fe)",
    "manganeso": "Manganeso (Mn)",
    "cobre": "Cobre (Cu)",
    "zinc": "Zinc (Zn)",
    "boro": "Boro (B)"
}



columnas_foliar_saltos = {
    "Nitrógeno Total (N)": "Nitrógeno\nTotal (N)",
    "Fósforo (P)": "Fósforo\n(P)",
    "Potasio (K)": "Potasio\n(K)",
    "Magnesio (Mg)": "Magnesio\n(Mg)",
    "Calcio (Ca)": "Calcio\n(Ca)",
    "Azufre (S)": "Azufre\n(S)",
    "Cloruro (Cl-) (%)": "Cloruro\n(Cl-) (%)",
    "Sodio (Na) (%)": "Sodio\n(Na) (%)",
    "Hierro (Fe)": "Hierro\n(Fe)",
    "Manganeso (Mn)": "Manganeso\n(Mn)",
    "Cobre (Cu)": "Cobre\n(Cu)",
    "Zinc (Zn)": "Zinc\n(Zn)",
    "Boro (B)": "Boro\n(B)"
}

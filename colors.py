color_order = [
    "rojo",
    "naranja",
    "amarillo",
    "blanco",
    "verde",
    "azul",
    "violeta"
]

GWINDOW_SIZE = 700
COLORS = len(color_order)
BOX_SIZE = GWINDOW_SIZE // COLORS
MAX_BRIGHTNESS = 255

int_colors = {
    "rojo":     0xffdb0a13,
    "naranja":  0xffec7808,
    "amarillo": 0xfffcde02,
    "blanco":   0xffffffff,
    "verde":    0xff018a2c,
    "azul":     0xff0645b1,
    "violeta":  0xff752864
}

es_to_en = {
    "rojo":     "red",
    "naranja":  "orange",
    "amarillo": "yellow",
    "blanco":   "white",
    "verde":    "green",
    "azul":     "blue",
    "violeta":  "violet"
}

region_colors = {
    "rojo":     "Chinchaysuyu",
    "naranja":  "Katari",
    "amarillo": "Kuntisuyu",
    "blanco":   "Qullasuyu",
    "verde":    "Antisuyu",
    "azul":     "Katari",
    "violeta":  "Katari"
}

regions = set(region_colors.values())
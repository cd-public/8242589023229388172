from pgl import GWindow, GImage
from colors import color_order, int_colors, region_colors, regions
from colors import GWINDOW_SIZE, COLORS, BOX_SIZE, MAX_BRIGHTNESS
from ColorObj import ColorObj

# For your convenience - 700 worked well for me
GWINDOW_SIZE = 700
COLORS = len(color_order)
BOX_SIZE = GWINDOW_SIZE // COLORS
MAX_BRIGHTNESS = 255

gw = GWindow(GWINDOW_SIZE, GWINDOW_SIZE)

# Main Function
def flag(region):
    # This sample code creates a pixel array that is uninitialized
    # TODO: Update the body of this function to create a flag
    # Prob0: Update ColorObj
    # Prob1: I recommend calculations over "BOX_SIZE", "color_order" and "int_colors"
    # Prob2: I recommend a dictionary of colors-to-ints that are incorporated into Prob0 calcs.
    #        You will need to use the "region" argument for this problem.
    # Prob3: Update ColorObj
    # Prob4: Write read_rbgs, update ColorObj
    rojo = ColorObj("rojo")
    parr = [[rojo.get_color_at(row,col) for row in range(GWINDOW_SIZE)] for col in range(GWINDOW_SIZE)]
    return parr

# Helper Function
# Likely useful in Prob3
def read_rgbs():
    rgb_colors = {}
    for line in open("rgbs.csv"):
        # This sample code creates a very bad example dictionary.
        # I recommend it containing a dictionary with...
        # keys: color names
        # values: lists of integers of length 3, corresponding to red-green-blue values
        rgb_colors[line] = []
    return rgb_colors

gw.add(GImage(wuphala('Qullasuyu')))

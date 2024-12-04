# File: ColorObj.py

from pgl import GWindow, GImage
from colors import color_order, int_colors, region_colors, regions
from colors import GWINDOW_SIZE, COLORS, BOX_SIZE, MAX_BRIGHTNESS

class ColorObj:

    # This sample code creates a pixel array that is uninitialized
    # TODO: Update the body of this class to implement a pixel array corresponding to a color.
    # Prob0: Update ColorObj to contain a color, such as from int_colors
    # Prob1: Work is done in wuphala.py
    # Prob2: Work is done in wuphala.py
    # Prob3: Update ColorObj to contain a pixel array of different colors.
    #        You may wish to use "square" and "resize" helper methods on Prob2.
    # Prob4: Update ColorObj to contain a pixel array that is colorscaled.
    #        You may wish to use "luminance" and "colorscale" helper methods on Prob3.

    # Initializer
    def __init__(self, name):
        self.name = name
        self.parr = []

    # Getter Method
    def get_color_at(self,row,col):
        return 0
    
    # Helper Methods
    # These are not required, but provided in case they help you.

    # Crop the ColorObj pixel array evenly from the left and the right to get a square.
    # NOTE: All provided images are wider than they are tall - you may assume this.
    def square(self):
        # TODO: Update the body of this function to crop evenly
        # I recommend calculations over lengths of the array and it's elements
        self.parr = self.parr

    # Scale the ColorObj pixel array to be of height and width GWINDOW_SIZE
    # NOTE: I would make this only work on square images.
    def resize(self):
        # TODO: Update the body of this function to alter self.parr to an appropriate size
        # I recommend calculations over lengths of the array and it's elements
        self.parr = self.parr

    # A helper function to convert from in-color to colorscaled
    # I converted from pixel arrays to pixel arrays, but could also work on images.
    def colorscale(self):    
        # TODO: Update the body of this function to recalculate all pixel values.
        # I recommend calculations over luminance and the "rbg" color

        # A helper function to compute luminance, provided
        # This function is complete and correct.
        def luminance(pixel):
            # This implementation uses the NTSC formula.
            r = GImage.get_red(pixel)
            g = GImage.get_green(pixel)
            b = GImage.get_blue(pixel)
            return round(0.299 * r + 0.587 * g + 0.114 * b)
        
        self.parr = self.parr
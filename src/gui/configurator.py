import dearpygui.dearpygui as dpg
import os

from src.gui.configurator_window.image_header import imageHeader
from src.gui.configurator_window.spectrum_header import spectrumHeader
from src.gui.configurator_window.region_header import regionHeader
from src.gui.configurator_window.fitting_header import fittingHeader

def configuratorWindow():
    '''
    Main window of the configurator
    '''

    with dpg.window(label="Configurator", width=450, height=900, pos=[10,10], no_close=True):
        imageHeader()

        dpg.add_spacer(height=7.5)
        spectrumHeader()

        dpg.add_spacer(height=7.5)
        regionHeader()

        dpg.add_spacer(height=7.5)
        fittingHeader()
    

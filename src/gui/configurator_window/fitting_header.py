import os

import dearpygui.dearpygui as dpg

# import src.gui.callbacks.image_callbacks as IMAGE_CALLBACKS

def fittingHeader():
    '''
    Collapsing header section for fitting models to spectrum
    '''
    with dpg.collapsing_header(label="Model fitting", default_open=False):
        dpg.add_text("TODO")
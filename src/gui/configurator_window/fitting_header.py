import dearpygui.dearpygui as dpg
import os

# import src.gui.callbacks.image_callbacks as IMAGE_CALLBACKS

def fittingHeader():
    '''
    Collapsing header section for fitting models to spectrum
    '''
    with dpg.collapsing_header(label="Model fitting", default_open=True):
        dpg.add_text("TODO")
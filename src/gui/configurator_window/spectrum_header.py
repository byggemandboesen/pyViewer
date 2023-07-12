import dearpygui.dearpygui as dpg
import os

import src.gui.callbacks.spectrum_callbacks as SPECTRUM_CALLBACKS

def spectrumHeader():
    '''
    Collapsing header section for handling extracted spectrums
    '''
    with dpg.collapsing_header(label="Spectrums", default_open=True):
        dpg.add_text("TODO")
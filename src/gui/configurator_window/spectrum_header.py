import os

import dearpygui.dearpygui as dpg

import src.gui.callbacks.spectrum_callbacks as SPECTRUM_CALLBACKS


def spectrumHeader():
    '''
    Collapsing header section for handling extracted spectrums
    '''
    with dpg.collapsing_header(label="Spectrums", default_open=False):
        dpg.add_text("TODO")
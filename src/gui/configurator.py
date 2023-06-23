import dearpygui.dearpygui as dpg

import src.utils.image_utils as image_utils

def configuratorWindow():
    '''
    Main window of the configurator
    '''

    with dpg.window(label="Configurator", width=300, height=800, pos=[10,10], no_close=True):
        imageHeader()

        dpg.add_spacer(height=5)
        spectrumHeader()

        dpg.add_spacer(height=5)
        regionHeader()

        dpg.add_spacer(height=5)
        fittingHeader()



def imageHeader():
    '''
    Collapsing header section for handling images
    '''
    with dpg.collapsing_header(label="Images", default_open=True):
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint="Image path", tag="img_path", width=-50) # TODO - Add callback
            dpg.add_button(label="LOAD", callback=image_utils.loadImage)


def spectrumHeader():
    '''
    Collapsing header section for handling extracted spectrums
    '''
    with dpg.collapsing_header(label="Spectrums", default_open=True):
        dpg.add_text("TODO")


def regionHeader():
    '''
    Collapsing header section for adding regions to images
    '''
    with dpg.collapsing_header(label="Image regions", default_open=True):
        dpg.add_text("TODO")


def fittingHeader():
    '''
    Collapsing header section for fitting models to spectrum
    '''
    with dpg.collapsing_header(label="Model fitting", default_open=True):
        dpg.add_text("TODO")
    

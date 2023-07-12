import dearpygui.dearpygui as dpg
import os

# import src.gui.callbacks.image_callbacks as IMAGE_CALLBACKS

def regionHeader():
    '''
    Collapsing header section for adding regions to images
    '''
    with dpg.collapsing_header(label="Image regions", default_open=True):
        
        with dpg.group(horizontal=True):
            dpg.add_text("Toggle region on/off")
            dpg.add_spacer(width=10)
            dpg.add_checkbox(tag="region") # TODO - Add callback



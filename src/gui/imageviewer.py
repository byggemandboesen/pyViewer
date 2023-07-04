import dearpygui.dearpygui as dpg

import src.utils.image_utils as IMAGE_UTILS

def imageWindow():
    '''
    Window for images
    '''
    with dpg.window(label="Image viewer", width=950, height=800, pos=[420, 10]):
        dpg.add_slider_int(label="Channel", min_value=0, max_value=0, default_value=0, width=-75, tag="channel_number", callback=IMAGE_UTILS.updateImagePlot)


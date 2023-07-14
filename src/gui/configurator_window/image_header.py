import os

import dearpygui.dearpygui as dpg

import src.gui.callbacks.image_callbacks as IMAGE_CALLBACKS
import src.gui.ui_consts as UI_CONSTS


def imageHeader():
    '''
    Collapsing header section for handling images
    '''

    with dpg.collapsing_header(label="Images", default_open=True):

        dpg.add_text("Load an image")
        with dpg.file_dialog(show=False, default_filename="", callback=IMAGE_CALLBACKS.browseImage, cancel_callback=IMAGE_CALLBACKS.browseImageCancelled, width=600, height=500, default_path=os.getcwd(), tag="image_file_dialog"):
            dpg.add_file_extension(".fits", color=(0,255,0,255))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint="Image path", tag="image_path", width=-75, callback=IMAGE_CALLBACKS.loadImage)
            dpg.add_button(label="BROWSE", width=-1, callback=lambda: dpg.show_item("image_file_dialog"))

        dpg.add_spacer(height=5)
        dpg.add_input_text(label="Object name", default_value="", readonly=True, tag="object_name", width=UI_CONSTS.W_NUM_INP_ONE_COL)
        dpg.add_input_int(label="Number of channels", default_value=1, step=0, readonly=True, tag="number_of_chan", width=UI_CONSTS.W_NUM_INP_ONE_COL)
        dpg.add_input_float(label="Channel frequency (Hz)", default_value=0.0, step=0.0, readonly=True, tag="channel_freq", width=UI_CONSTS.W_NUM_INP_ONE_COL)
        dpg.add_input_float(label="Channel width (Hz)", default_value=0.0, step=0.0, readonly=True, tag="channel_freq_width", width=UI_CONSTS.W_NUM_INP_ONE_COL)

        dpg.add_spacer(height=5)
        dpg.add_text("Center coordinate (degrees)")
        with dpg.table(borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=True):
            dpg.add_table_column(label="Right ascension")
            dpg.add_table_column(label="Declination")
        
            with dpg.table_row():
                with dpg.table_cell():
                    dpg.add_text("", tag="ra")
                with dpg.table_cell():
                    dpg.add_text("", tag="dec")
        
        dpg.add_text("Image size (arcsec)")
        with dpg.table(borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=True):
            dpg.add_table_column(label="Right ascension")
            dpg.add_table_column(label="Declination")

            with dpg.table_row():
                with dpg.table_cell():
                    dpg.add_text("", tag="imsize_ra")
                with dpg.table_cell():
                    dpg.add_text("", tag="imsize_dec")
        
        dpg.add_text("Image size (pixels)")
        with dpg.table(borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=True):
            dpg.add_table_column(label="Right ascension")
            dpg.add_table_column(label="Declination")

            with dpg.table_row():
                with dpg.table_cell():
                    dpg.add_text("", tag="imsize_ra_pix")
                with dpg.table_cell():
                    dpg.add_text("", tag="imsize_dec_pix")

        dpg.add_text("Pixel size (arcsec)")
        with dpg.table(borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=True):
            dpg.add_table_column(label="Right ascension")
            dpg.add_table_column(label="Declination")

            with dpg.table_row():
                with dpg.table_cell():
                    dpg.add_text("", tag="cell_ra")
                with dpg.table_cell():
                    dpg.add_text("", tag="cell_dec")
        
        dpg.add_text("Beam size (arcsec)")
        with dpg.table(borders_innerH=True, borders_innerV=True, borders_outerH=True, borders_outerV=True):
            dpg.add_table_column(label="Major axis")
            dpg.add_table_column(label="Minor axis")
        
            with dpg.table_row():
                with dpg.table_cell():
                    dpg.add_text("", tag="bmaj")
                with dpg.table_cell():
                    dpg.add_text("", tag="bmin")
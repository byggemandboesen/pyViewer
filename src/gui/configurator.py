import dearpygui.dearpygui as dpg
import os

import src.gui.callbacks.image_callbacks as IMAGE_CALLBACKS

def configuratorWindow():
    '''
    Main window of the configurator
    '''

    with dpg.window(label="Configurator", width=400, height=800, pos=[10,10], no_close=True):
        imageHeader()

        dpg.add_spacer(height=7.5)
        spectrumHeader()

        dpg.add_spacer(height=7.5)
        regionHeader()

        dpg.add_spacer(height=7.5)
        fittingHeader()


def imageHeader():
    '''
    Collapsing header section for handling images
    '''
    LABELWIDTH = -175

    with dpg.collapsing_header(label="Images", default_open=True):

        dpg.add_spacer(height=5)
        with dpg.file_dialog(show=False, default_filename="", callback=IMAGE_CALLBACKS.browseImage, cancel_callback=IMAGE_CALLBACKS.browseImageCancelled, width=600, height=500, default_path=os.getcwd(), tag="image_file_dialog"):
            dpg.add_file_extension(".fits", color=(0,255,0,255))
        with dpg.group(horizontal=True):
            dpg.add_input_text(hint="Image path", tag="image_path", width=-75, callback=IMAGE_CALLBACKS.loadImage)
            dpg.add_button(label="BROWSE", width=-1, callback=lambda: dpg.show_item("image_file_dialog"))

        dpg.add_spacer(height=5)
        dpg.add_input_text(label="Object name", default_value="", readonly=True, tag="object_name", width=LABELWIDTH)
        dpg.add_input_int(label="Number of channels", default_value=1, step=0, readonly=True, tag="number_of_chan", width=LABELWIDTH)
        dpg.add_input_float(label="Channel frequency (Hz)", default_value=0.0, step=0.0, readonly=True, tag="channel_freq", width=LABELWIDTH)
        dpg.add_input_float(label="Channel width (Hz)", default_value=0.0, step=0.0, readonly=True, tag="channel_freq_width", width=LABELWIDTH)

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
    

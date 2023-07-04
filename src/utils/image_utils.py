import os, sys
import astropy.io.fits as fits
import dearpygui.dearpygui as dpg
import matplotlib.pyplot as plt
import numpy as np

from src.astropy.image import Image

def browseImage():
    '''
    Browse for images
    TODO
    '''
    print("Browsing...")


def loadImage(sender, app_data, updateImageOnly: bool = False):
    '''
    Tries to load image from the path specified
    '''
    path = dpg.get_value("img_path")

    # Try to open image
    try:
        img = Image(path)
    except Exception as e:
        # print(f"Exception occured: {e}")
        return
    
    if not updateImageOnly:
        updateImageInformation(img)
    updateImagePlot(img)


def updateImagePlot(img: Image):
    '''
    Updates image plot
    '''
    dim = img.getImageShape()
    ra, dec = img.getImageCoordinates()
    freqs = img.getFrequencyAxis()
    channel = dpg.get_value("channel_number")
    dpg.set_value("channel_freq", freqs[channel])
    img_data = img.getImage(channel=channel)
    
    min, max = img.getMinFlux(), img.getMaxFlux()
    dpg.configure_item("heatmap", x=img_data.flatten().tolist(), rows=dim[1], cols=dim[2], scale_min=min, scale_max=max)
    dpg.set_axis_limits_auto("ra_axis")
    dpg.set_axis_limits_auto("dec_axis")
    dpg.configure_item("cbar", min_scale=min, max_scale=max)


def updateImageInformation(img: Image):
    '''
    Updates image information
    '''
    obj_name = img.getObjectName()
    dpg.set_value("object_name", obj_name)

    n_chan = img.getImageShape()[0]
    if n_chan != dpg.get_value("number_of_chan"):
        dpg.set_value("number_of_chan", n_chan)
        dpg.configure_item("channel_number", max_value = n_chan-1)

    # If type = cube, show the frequency width between each channel
    if n_chan > 1:
        freq_ax = img.getFrequencyAxis()
        chan_width = np.diff(np.sort(freq_ax[0:2]))
        dpg.set_value("channel_freq_width", chan_width)
    else:
        dpg.set_value("channel_freq_width", 0.0)
        dpg.set_value("channel_number", 0)
        dpg.configure_item("channel_number", max_value=0)
    
    ra, dec = img.getImageCenterCoordinates()
    dpg.set_value("ra", ra)
    dpg.set_value("dec", dec)

    ra, dec = img.getImageSize()
    dpg.set_value("imsize_ra", ra)
    dpg.set_value("imsize_dec", dec)

    ra, dec = img.getCellSize()
    dpg.set_value("cell_ra", ra)
    dpg.set_value("cell_dec", dec)

    try:
        bmaj, bmin = img.getBeamSize()
        dpg.set_value("bmaj", bmaj)
        dpg.set_value("bmin", bmin)
    except Exception as e:
        print("Beam size not available...")
        dpg.set_value("bmaj", "N/A")
        dpg.set_value("bmin", "N/A")


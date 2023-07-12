import os, sys
import astropy.io.fits as fits
import dearpygui.dearpygui as dpg
import matplotlib.pyplot as plt
import numpy as np

from src.astropy.image import Image

def browseImage(sender, path) -> None:
    '''
    Browse for images
    '''
    file_path = path["file_path_name"]
    dpg.set_value("image_path", file_path)
    loadImage("", "", False)

def browseImageCancelled() -> None:
    '''
    Callback for cancelled image callback
    '''
    return


def loadImage(sender, app_data, updateImageOnly: bool = False) -> None:
    '''
    Tries to load image from the path specified
    '''
    path = dpg.get_value("image_path")

    # Try to open image
    try:
        img = Image(path)
    except Exception as e:
        # print(f"Exception occured: {e}")
        return
    
    if not updateImageOnly:
        updateImageInformation(img)
    updateImagePlot(img)


def updateImagePlot(img: Image) -> None:
    '''
    Updates image plot
    '''
    dim = img.getImageShape()
    ra, dec = img.getImageCoordinates()
    freqs = img.getFrequencyAxis()
    channel = dpg.get_value("channel_number")
    dpg.set_value("channel_freq", freqs[channel])
    img_data = img.getImage(channel=channel)
    
    # Update plot
    min, max = img.getMinFlux(), img.getMaxFlux()
    dpg.configure_item("heatmap", x=img_data.flatten().tolist(), rows=dim[1], cols=dim[2], scale_min=min, scale_max=max)
    dpg.set_axis_limits_auto("ra_axis")
    dpg.set_axis_limits_auto("dec_axis")
    dpg.configure_item("cbar", min_scale=min, max_scale=max)

    # Update axis
    n_skip = 12
    ra, dec = img.getImageCoordinates(dtype=str, round=3)
    current_ra_labels, current_dec_labels = np.linspace(0, 1, dim[1]+1), np.linspace(0, 1, dim[2]+1)
    ra_labels = tuple(zip(*(ra[::n_skip], current_ra_labels[::n_skip])))
    dec_labels = tuple(zip(*(dec[::n_skip], current_dec_labels[::n_skip])))
    dpg.set_axis_ticks("ra_axis", ra_labels)
    dpg.set_axis_ticks("dec_axis", dec_labels)


def updateImageInformation(img: Image) -> None:
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

    dim = img.getImageShape()
    dpg.set_value("imsize_ra_pix", dim[1])
    dpg.set_value("imsize_dec_pix", dim[2])

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


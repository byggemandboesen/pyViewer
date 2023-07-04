import os, sys
import astropy.io.fits as fits
import dearpygui.dearpygui as dpg
import matplotlib.pyplot as plt

from src.astropy.image import Image

def loadImage():
    '''
    Tries to load image from the path specified
    '''
    path = dpg.get_value("img_path")
    print(path)

    if not os.path.exists(path):
        print("Path does not exist!!")
        return
    if not path[-4:].lower() == "fits":
        print("Image not of type, \"FITS\"!!")
        print("Consider converting image to fits with exportfits()...")
        return

    # Try to open image
    try:
        img = Image(path)
    except Exception as e:
        print(f"Exception occured: {e}")
        return

    updateImageInformation(img)

    ra, dec = img.getImageCoordinates()
    img_data = img.getImage()

    # plt.imshow(img_data, extent=[ra[0], ra[-1], dec[0], dec[-1]])
    # plt.show()

def updateImagePlot(img: Image):
    '''
    Updates image plot
    TODO
    '''
    print("TODO")


def updateImageInformation(img: Image):
    '''
    Updates image information
    '''
    
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



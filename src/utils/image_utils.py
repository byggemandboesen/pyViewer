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

    
    ra, dec = img.getImageCoordinates()
    img_data = img.getImage()

    plt.imshow(img_data, extent=[ra[0], ra[-1], dec[0], dec[-1]])
    plt.show()

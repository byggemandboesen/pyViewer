import dearpygui.dearpygui as dpg
import numpy as np

import matplotlib.pyplot as plt

from src.astropy.region import Region

# Add region
# Update region
# etc...



def updateRegionPlot():
    '''
    Updates the region plot
    '''
    region_type = dpg.get_value("region_type")
    region_active = dpg.get_value("toggle_region")

    if not region_active:
        return
    
    # Current image shape
    shape = (int(dpg.get_value("imsize_ra_pix")), int(dpg.get_value("imsize_dec_pix")))
    if shape == ("", ""):
        print("No image detected! Not able to generate region")
        return

    match region_type:
        case "Ellipse":
            region = ellipseRegion(shape)
        case "Box":
            region = boxRegion(shape)
        case "Threshold":
            region = thresholdRegion(shape)
        case _:
            return
    
    # plt.imshow(region)
    # plt.show()

    # TODO - Add region to image viewer
    # TODO - Display region statistics


def ellipseRegion(shape: tuple) -> Region:
    '''
    Returns an elliptic region instance
    '''
    pos = np.array([dpg.get_value("ellipse_x_pos"), dpg.get_value("ellipse_y_pos")])
    w, h = dpg.get_value("ellipse_width"), dpg.get_value("ellipse_height")
    tilt = dpg.get_value("ellipse_angle")

    region = Region(shape)
    ellipse = region.setEllipse(center=pos, width=w, height=h, tilt=tilt)
    return ellipse


def boxRegion(shape: tuple) -> Region:
    '''
    Returns a box region instance
    '''
    corner = np.array([dpg.get_value("box_x_pos"), dpg.get_value("box_y_pos")])
    w, h = dpg.get_value("box_width"), dpg.get_value("box_height")

    region = Region(shape)
    box = region.setBox(corner=corner, width=w, height=h)

    return box


def thresholdRegion(shape: tuple) -> Region:
    '''
    Returns a threshold region instance
    '''
    return
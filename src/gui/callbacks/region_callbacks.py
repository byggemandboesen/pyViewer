import os
import dearpygui.dearpygui as dpg
import matplotlib.pyplot as plt
import numpy as np

import src.gui.callbacks.image_callbacks as IMAGE_CALLBACKS
from src.astropy.image import Image
from src.astropy.region import Region


def browseReferenceImage(sender, path) -> None:
    '''
    Browse for images
    '''
    file_path = path["file_path_name"]
    dpg.set_value("reference_image_path", file_path)


def browseReferenceImageCancelled() -> None:
    '''
    Callback for cancelled image callback
    '''
    return


def updateRegionPlot():
    '''
    Updates the region plot
    '''
    region_type = dpg.get_value("region_type")
    region_active = dpg.get_value("toggle_region")

    if not region_active:
        if dpg.does_item_exist("active_region_plot"):
            dpg.hide_item("active_region_plot")
        return
    
    # Current image shape
    shape = (dpg.get_value("imsize_ra_pix"), dpg.get_value("imsize_dec_pix"))
    if shape == ("", ""):
        print("No, or invalid, image detected! Not able to generate region...")
        return
    
    shape = tuple(int(val) for val in shape)

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

    # TODO - Fix displayed region
    # TODO - Display region statistics
    # TODO - Add invert region functionality
    if dpg.does_item_exist("active_region_plot"):
        dpg.configure_item("active_region_plot", x=region, rows=shape[0], cols=shape[1], show=True)
    else:
        dpg.add_heat_series(x=region, rows=shape[0], cols=shape[1], label="Active region", parent="dec_axis", format="", tag="active_region_plot")


def ellipseRegion(shape: tuple) -> np.ndarray:
    '''
    Returns an elliptic region instance
    '''
    pos = np.array([dpg.get_value("ellipse_x_pos"), dpg.get_value("ellipse_y_pos")])
    w, h = dpg.get_value("ellipse_width"), dpg.get_value("ellipse_height")
    tilt = dpg.get_value("ellipse_angle")

    region = Region(shape)
    ellipse = region.setEllipse(center=pos, width=w, height=h, tilt=tilt)
    return ellipse


def boxRegion(shape: tuple) -> np.ndarray:
    '''
    Returns a box region instance
    '''
    corner = np.array([dpg.get_value("box_x_pos"), dpg.get_value("box_y_pos")])
    w, h = dpg.get_value("box_width"), dpg.get_value("box_height")

    region = Region(shape)
    box = region.setBox(corner=corner, width=w, height=h)

    return box


def thresholdRegion(shape: tuple) -> np.ndarray:
    '''
    Returns a threshold region instance
    '''

    path = dpg.get_value("reference_image_path")

    if not os.path.isfile(path):
        print("Invalid reference image or no reference image selected!")
        return Region(shape).setEmpty()

    try:
        img = Image(path)
    except Exception as e:
        print(f"Exception occured: {e}")
        return
    
    # channel = dpg.get_value("channel_number")
    img_data = img.getImage()
    region = Region(shape)

    threshold = region.setThreshold(reference_img=img_data, limit=dpg.get_value("rms_threshold"))

    return threshold
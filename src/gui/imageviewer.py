import dearpygui.dearpygui as dpg
import numpy as np

import src.gui.callbacks.image_callbacks as IMAGE_CALLBACKS

def imageWindow():
    '''
    Window for images
    '''
    with dpg.window(label="Image viewer", width=950, height=800, pos=[420, 10], no_close=True, no_scrollbar=True):
        dpg.add_slider_int(label="Channel", min_value=0, max_value=0, default_value=0, width=-75, tag="channel_number", callback=IMAGE_CALLBACKS.loadImage, user_data=True)

        with dpg.group(horizontal=True):
            dpg.add_colormap_scale(min_scale=0, max_scale=0, width = 75, height=-1, tag="cbar")
            dpg.bind_colormap(dpg.last_item(), dpg.mvPlotColormap_Jet)
            with dpg.plot(width=-1,height=-1, tag = "image_plot"):
                dpg.bind_colormap("image_plot", dpg.mvPlotColormap_Jet)
                
                # Create axis and update their ticks
                dpg.add_plot_axis(dpg.mvXAxis, label = "Right ascension", tag="ra_axis", no_gridlines=True)
                dpg.add_plot_axis(dpg.mvYAxis, label = "Declination", tag="dec_axis", no_gridlines=True)
                
                # And then add data to plot
                dpg.add_heat_series(x=np.zeros((100,100)), rows=100, cols=100, parent="dec_axis", scale_max=0, scale_min=0, format="", tag="heatmap")


import dearpygui.dearpygui as dpg
import numpy as np

def spectrumWindow():
    '''
    Window for images
    '''
    with dpg.window(label="Spectrum viewer", width=650, height=290, pos=[470, 620], no_close=True, no_scrollbar=True):
        dpg.add_slider_int(label="Channel", min_value=0, max_value=0, default_value=0, width=-75, tag="spectrum_channel_number", user_data=True) # TODO - Add callback

        with dpg.plot(width=-1,height=-1, tag = "spectrum_plot", anti_aliased=True):
            # Create axis and update their ticks
            dpg.add_plot_axis(dpg.mvXAxis, label = "Frequency", tag="freq_axis") # , no_gridlines=True
            dpg.add_plot_axis(dpg.mvYAxis, label = "Flux", tag="flux_axis") # , no_gridlines=True
            
            # And then add data to plot
            dpg.add_line_series(np.linspace(0, 1, 100), np.zeros(100), label="Observed flux", parent="flux_axis", tag="spectrum_line_series")

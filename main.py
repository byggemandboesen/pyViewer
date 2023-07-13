import dearpygui.dearpygui as dpg
import os, sys
sys.dont_write_bytecode = True

import src.gui.configurator as Configurator
import src.gui.imageviewer as ImageViewer
import src.gui.spectrumviewer as SpectrumViewer

# Run user intereface
def run_ui():
    dpg.create_context()
    dpg.create_viewport(title='pyViewer - Victor Boesen', width=1150, height=960)
    
    Configurator.configuratorWindow()
    ImageViewer.imageWindow()
    SpectrumViewer.spectrumWindow()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    run_ui()
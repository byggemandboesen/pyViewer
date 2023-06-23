import dearpygui.dearpygui as dpg
import os, sys
sys.dont_write_bytecode = True

import src.gui.configurator as Configurator

# Run user intereface
def run_ui():
    dpg.create_context()
    dpg.create_viewport(title='pyViewer - Victor Boesen', width=1400, height=875)
    
    Configurator.configuratorWindow()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    run_ui()
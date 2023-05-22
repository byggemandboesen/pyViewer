import dearpygui.dearpygui as dpg
import os, sys
sys.dont_write_bytecode = True


# Run user intereface
def run_ui():
    dpg.create_context()
    dpg.create_viewport(title='pyViewer - Victor Boesen', width=500, height=500)
    
    with dpg.window(label = "Editor"):
        dpg.add_text("Work in progress!!")

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    run_ui()
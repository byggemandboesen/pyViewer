import os

import dearpygui.dearpygui as dpg

import src.gui.callbacks.region_callbacks as REGION_CALLBACKS
import src.gui.ui_consts as UI_CONSTS


def regionHeader():
    '''
    Collapsing header section for adding regions to images
    '''
    with dpg.collapsing_header(label="Image regions", default_open=True):
        
        with dpg.group(horizontal=True):
            dpg.add_text("Toggle region on/off")
            dpg.add_spacer(width=10)
            dpg.add_checkbox(tag="toggle_region", callback=REGION_CALLBACKS.updateRegionPlot)
            # TODO - Add callback

        dpg.add_combo(label="Region type", items=["Ellipse", "Box", "Threshold"], default_value="Ellipse", callback=REGION_CALLBACKS.updateRegionPlot, tag="region_type")

        dpg.add_spacer(height=5)
        dpg.add_text("Configure region types")
        with dpg.tree_node(label="Ellipse"):
            dpg.add_text("Pixel coordinates of ellipse center")
            with dpg.group(horizontal=True):
                dpg.add_input_int(label="X", min_value=0, default_value=20, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="ellipse_x_pos")
                dpg.add_input_int(label="Y", min_value=0, default_value=50, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="ellipse_y_pos")
            
            dpg.add_spacer(height=5)
            dpg.add_text("Ellipse size")
            with dpg.group(horizontal=True):
                dpg.add_input_int(label="W", min_value=1, default_value=10, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="ellipse_width")
                dpg.add_input_int(label="H", min_value=1, default_value=5, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="ellipse_height")
            dpg.add_input_int(label="Rotation angle", min_value=0, max_value=179, default_value=0, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="ellipse_angle")

        dpg.add_spacer(height=5)
        with dpg.tree_node(label="Box"):
            dpg.add_text("Pixel coordinates of bottom left corner")
            with dpg.group(horizontal=True):
                dpg.add_input_int(label="X", min_value=0, default_value=40, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="box_x_pos")
                dpg.add_input_int(label="Y", min_value=0, default_value=10, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="box_y_pos")

            dpg.add_spacer(height=2.5)
            dpg.add_text("Box size")
            with dpg.group(horizontal=True):
                dpg.add_input_int(label="W", min_value=1, default_value=30, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="box_width")
                dpg.add_input_int(label="H", min_value=1, default_value=15, width=UI_CONSTS.W_NUM_INP_TWO_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="box_height")
        
        dpg.add_spacer(height=2.5)
        with dpg.tree_node(label="Threshold"):
            dpg.add_text("Noise threshold limit")
            dpg.add_input_float(label="RMS", min_value=0, max_value=10, min_clamped=True, max_clamped=True, default_value=3, width=UI_CONSTS.W_NUM_INP_ONE_COL, callback=REGION_CALLBACKS.updateRegionPlot, tag="rms_threshold")

            dpg.add_spacer(height=5)
            dpg.add_text("RMS threshold from reference image:")
            with dpg.file_dialog(show=False, default_filename="", callback=REGION_CALLBACKS.browseReferenceImage, cancel_callback=REGION_CALLBACKS.browseReferenceImageCancelled, width=600, height=500, default_path=os.getcwd(), tag="reference_image_file_dialog"):
                dpg.add_file_extension(".fits", color=(0,255,0,255))
            with dpg.group(horizontal=True):
                dpg.add_input_text(hint="Reference image path", width=-75, callback=REGION_CALLBACKS.updateRegionPlot, tag="reference_image_path")
                dpg.add_button(label="BROWSE", width=-1, callback=lambda: dpg.show_item("reference_image_file_dialog"))
            
            # dpg.add_spacer(height=5)
            # with dpg.group(horizontal=True):
            #     dpg.add_text("Reference level: ")
            #     dpg.add_text("", tag="rms_level")
            #     dpg.add_text(" Jy")


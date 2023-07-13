import dearpygui.dearpygui as dpg
import os

# import src.gui.callbacks.image_callbacks as IMAGE_CALLBACKS
import src.gui.ui_consts as UI_CONSTS

def regionHeader():
    '''
    Collapsing header section for adding regions to images
    '''
    with dpg.collapsing_header(label="Image regions", default_open=True):
        
        with dpg.group(horizontal=True):
            dpg.add_text("Toggle region on/off")
            dpg.add_spacer(width=10)
            dpg.add_checkbox(tag="region") # TODO - Add callback

        dpg.add_combo(label="Region type", items=["Ellipse", "Box", "Threshold"], default_value="Ellipse", tag="region_type")

        dpg.add_spacer(height=5)
        dpg.add_text("Configure region types")
        with dpg.tree_node(label="Ellipse"):
            dpg.add_text("Pixel coordinates of ellipse center")
            with dpg.group(horizontal=True):
                dpg.add_input_int(label="X", min_value=1, default_value=1, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="ellipse_x_pos")
                dpg.add_input_int(label="Y", min_value=1, default_value=1, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="ellipse_y_pos")
            
            dpg.add_spacer(height=5)
            dpg.add_text("Ellipse size")
            with dpg.group(horizontal=True):
                dpg.add_input_int(label="W", min_value=1, default_value=1, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="ellipse_x_width")
                dpg.add_input_int(label="H", min_value=1, default_value=1, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="ellipse_y_width")
            dpg.add_input_int(label="Rotation angle", min_value=0, max_value=179, default_value=0, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="ellipse_angle")

        dpg.add_spacer(height=5)
        with dpg.tree_node(label="Box"):
            dpg.add_text("Pixel coordinates of bottom left corner")
            with dpg.group(horizontal=True):
                dpg.add_input_int(label="X", min_value=1, default_value=1, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="box_x_pos")
                dpg.add_input_int(label="Y", min_value=1, default_value=1, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="box_y_pos")

            dpg.add_spacer(height=2.5)
            dpg.add_text("Box size")
            with dpg.group(horizontal=True):
                dpg.add_input_int(label="W", min_value=1, default_value=1, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="box_width")
                dpg.add_input_int(label="H", min_value=1, default_value=1, width=UI_CONSTS.W_NUM_INP_TWO_COL, tag="box_height")
        
        dpg.add_spacer(height=2.5)
        with dpg.tree_node(label="Threshold"):
            dpg.add_text("Configure threshold region")
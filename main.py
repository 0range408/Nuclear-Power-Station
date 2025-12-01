import tomllib as toml
import dearpygui.dearpygui as gui
import draw
import random

gui.create_context()

def click(sender, app_data):
    pass

with open("config.toml", "rb") as file:
    config = toml.load(file)

rows, cols = config["size"]
rods = config["rods"]

colors = draw.lerp_rgb((1, 0, 1), (0, 1, 1), 101)

with gui.window(label = "Control Rods", tag = "control_rods"):
    
    for i in range(0, rows):
        for j in range(0, cols):

            width = 35.0
            x = 10.0 + ((width + 4) * i)
            y = 10.0 + ((width + 4) * j)

            r, g, b = colors[rods[i][j]]

            draw.draw_square(
                gui, 
                x, y,
                width, 
                fill = (r * 255, g * 255, b * 255), 
                rounding = 2.0
            )

with gui.window(label = "Condenser Coolant", tag = "condenser_coolant"):
    pass

gui.create_viewport(title = "Reactor", width = 800, height = 600)

gui.configure_app(docking = True)
gui.docking_shift_only = False

gui.setup_dearpygui()
gui.show_viewport()

gui.start_dearpygui()

gui.destroy_context()
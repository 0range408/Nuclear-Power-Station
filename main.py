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

with gui.window(label = "Water Data", tag = "reactor_data"): #TODO: come up with a better name
    pressure = config["water_pressure"]
    temperature = config["water_temp"]
    gui.add_text(f"""
Water Pressure:     {pressure}
    
Water Temperature:  {temperature}
    """)

zone_colors = draw.lerp_rgb((0, 0, 1), (1, 0, 0), 5001)
zones = config["zones"]

with gui.window(label = "Zone Temperatures", tag = "zone_temperatures"): #FIXME: ugly code

    r_a2, g_a2, b_a2 = zone_colors[zones[0][0]]
    r_a3, g_a3, b_a3 = zone_colors[zones[0][1]]
    r_d2, g_d2, b_d2 = zone_colors[zones[3][0]]
    r_d3, g_d3, b_d3 = zone_colors[zones[3][1]]

    draw.draw_reactor_zone(
        gui,
        10.0 + 90.0, 10.0,
        fill = (255 * r_a2, 255 * g_a2, 100 * b_a2),
        text = zones[0][0]
    )

    draw.draw_reactor_zone(
        gui,
        (10.0 + 90.0) * 2, 10.0,
        fill = (255 * r_a3, 255 * g_a3, 255 * b_a3),
        text = zones[0][1]
    )

    for i in range(1, 3):
        for j in range (0, 4):

            r, g, b = zone_colors[zones[i][j]]

            draw.draw_reactor_zone(
                gui,
                (10.0 + 90.0) * j, 10.0 + 60.0 * i,
                fill = (255 * r, 255 * g, 255 * b),
                text = zones[i][j]
            )

    draw.draw_reactor_zone(
        gui,
        10.0 + 90.0, 10.0 + 60.0 * 3,
        fill = (255 * r_d2, 255 * g_d2, 255 * b_d2),
        text = zones[3][0]
    )

    draw.draw_reactor_zone(
        gui,
        (10.0 + 90.0) * 2, 10.0 + 60.0 * 3,
        fill = (255 * r_d3, 255 * g_d3, 255 * b_d3),
        text = zones[3][1]
    )


gui.create_viewport(title = "Reactor", width = 800, height = 600)

gui.configure_app(docking = True)
gui.docking_shift_only = False

gui.setup_dearpygui()
gui.show_viewport()

gui.start_dearpygui()

gui.destroy_context()
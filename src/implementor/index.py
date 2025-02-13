import random
from PIL import Image, ImageDraw

from src.core import RandomCup, CENTER


def create_cup(name_file):
	cup = RandomCup()

	coord_cup = (
		start_x_cup := CENTER['x'] - (cup.width_cup / 2),
		start_y_cup := CENTER['y'] - (cup.height_cup / 2),
		end_x_cup := start_x_cup + cup.width_cup,
		end_y_cup := start_y_cup + cup.height_cup,
	)

	coord_grip = (
		start_x_grip := end_x_cup - cup.width_knob,
		start_y_grip := (start_y_cup + end_y_cup) / 2,
		end_x_grip := end_x_cup + cup.width_knob,
		end_y_grip := start_y_grip + cup.height_knob,
	)

	colors = ('RED', 'GREEN', 'BLUE', 'ORANGE', 'YELLOW', 'PURPLE', 'PINK', 'WHITE', 'GRAY')

	bg = Image.new(mode='RGB', size=(500, 500))
	canvas = ImageDraw.Draw(bg)

	canvas.ellipse(coord_grip, outline=random.choice(colors), width=8)
	canvas.rectangle(coord_cup, fill=random.choice(colors))
	bg.save(name_file)

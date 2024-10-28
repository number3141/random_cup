import random
from PIL import Image, ImageDraw

from settings import MIN_W_CUP, MAX_W_CUP, MIN_H_CUP, MAX_H_CUP, CENTER


def create_cup(name_file):
	# Габариты кружки
	width_cup = random.randint(MIN_W_CUP, MAX_W_CUP)
	height_cup = random.randint(MIN_H_CUP, MAX_H_CUP)

	# Ограничения ручки
	min_w_knob = int(width_cup * 0.1)
	min_h_knob = int(height_cup * 0.1)
	max_w_knob = int(width_cup * 0.4)
	max_h_knob = int(height_cup * 0.4)

	# Габариты ручки
	width_knob = random.randint(min_w_knob, max_w_knob)
	height_knob = random.randint(min_h_knob, max_h_knob)

	coord_cup = (
		start_x_cup := CENTER['x'] - (width_cup / 2),
		start_y_cup := CENTER['y'] - (height_cup / 2),
		end_x_cup := start_x_cup + width_cup,
		end_y_cup := start_y_cup + height_cup,
	)

	coord_grip = (
		start_x_grip := end_x_cup - width_knob,
		start_y_grip := (start_y_cup + end_y_cup) / 2,
		end_x_grip := end_x_cup + width_knob,
		end_y_grip := start_y_grip + height_knob,
	)

	colors = ('RED', 'GREEN', 'BLUE', 'ORANGE', 'YELLOW', 'PURPLE', 'PINK', 'WHITE', 'GRAY')

	bg = Image.new(mode='RGB', size=(500, 500))
	canvas = ImageDraw.Draw(bg)

	canvas.ellipse(coord_grip, outline=random.choice(colors), width=8)
	canvas.rectangle(coord_cup, fill=random.choice(colors))
	bg.save(name_file)

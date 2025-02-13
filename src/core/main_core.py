import random
from src.core.settings import MIN_W_CUP, MAX_W_CUP, MIN_H_CUP, MAX_H_CUP


class RandomCup:
	def __init__(self):
		self.width_cup = 0
		self.height_cup = 0
		self.width_knob = 0
		self.height_knob = 0

		self.generate_random_size_cup()
		self.generate_random_size_knob()

	def generate_random_size_cup(self):
		self.width_cup = random.randint(MIN_W_CUP, MAX_W_CUP)
		self.height_cup = random.randint(MIN_H_CUP, MAX_H_CUP)

		return self.width_cup, self.height_cup


	def generate_random_size_knob(self):
		# Ограничения ручки
		min_w_knob = int(self.width_cup * 0.1)
		min_h_knob = int(self.height_cup * 0.1)
		max_w_knob = int(self.width_cup * 0.4)
		max_h_knob = int(self.height_cup * 0.4)

		# Габариты ручки
		self.width_knob = random.randint(min_w_knob, max_w_knob)
		self.height_knob = random.randint(min_h_knob, max_h_knob)

		return self.width_knob, self.height_knob
from typing import Callable, List
import math

#from numba import jitclass

from random import random, getrandbits


def r_number() -> float:
	value = random()
	return -value if bool(getrandbits(1)) else value

class Connection:
	def __init__(self, left_side: int, right_side: int):
		self.left_side = left_side
		self.right_side = right_side
		self.weights: List[List[float]] = []
		self.biases: List[float] = []

	def random_init(self) -> None:
		for _ in range(self.right_side):
			self.weights.append([])
			for _ in range(self.left_side):
				self.weights[-1].append(1)
		for _ in range(self.left_side):
			self.biases.append(1)

	def eval_forward(self, input_vec : List[float], activation_function: Callable) ->  List[float]:
		def compute_neuron_value(neuron_weights):
			n = sum(neuron_weights[i] * input_vec[i] + self.biases[i]
			        for i in range(self.right_side))
			return activation_function(n)
	
		return list(map(compute_neuron_value, self.weights))

	def mutate(self, rate : float) -> None:
		# fonction de loi uniforme vers loi normale ==> https://www.desmos.com/calculator/gx3e2uhdbr
		amplitude = 1.01
		squish_factor = (rate - 1) / math.log(0.5 * (1 - rate))
		def guaussian(x):
			return -amplitude * (2 * math.expm1((x-1)/squish_factor) + 1)

		mutation = lambda : guaussian(random())
		for i in range(self.right_side):
			for j in range(self.left_side):
				self.weights[i][j] *= mutation()
				self.biases[i]     *= mutation()
			
			

from .make_stuff_go_faster import r_number, fastrand

from typing import Callable, List
import math



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
				self.weights[-1].append(r_number())
		for _ in range(self.left_side):
			self.biases.append(r_number())

	def eval_forward(self, input_vec : List[int], activation_function: Callable) ->  List[float]:
		result = []
		for neuron_weights in self.weights:
			n = sum(neuron_weights[i] * input_vec[i] + self.biases[i] for i in range(self.right_side))
			n = activation_function(n)
			result.append(n)
		return result
	
	def mutate(self, rate : float) -> None:
		# fonction de loi uniforme vers loi normale ==> https://www.desmos.com/calculator/gx3e2uhdbr
		squish_factor = (rate - 1) / math.log(0.5 * (1 - rate))
		guaussian = lambda x : math.expm1((x-1)/squish_factor)
		mutation = lambda : guaussian(fastrand.pcg32() / int(2**32))
		for i in range(self.right_side):
			for j in range(self.left_side):
				self.weights[i][j] *= mutation()
				self.biases[i]     *= mutation()
			
			
from typing import List
from math import exp

from .make_stuff_go_faster import r_number
from random import random, randint, choice


from .connection_layer import Connection

def ReLu(x : float) -> float:
	if (x > 0):
		return x
	return 0

class Neural_Network:
	def __init__(self, shape: List[int], activation_function : callable) -> None:
		self.shape = shape
		self.activation_function = ReLu
		self.layer_connections: List[Connection] = []
		for i in range(len(shape[:-1])):
			left_side, right_side = shape[i], shape[i+1] 
			connection = Connection(left_side, right_side)
			connection.random_init()
			self.layer_connections.append(connection)

	def eval_forward(self, input_vec)-> List[int]:
		result = input_vec
		for i in range(len(self.shape)-1):
			result = self.layer_connections[i].eval_forward(result, activation_function=self.activation_function)
		return result

	def __repr__(self):
		return "Neural net:" + str(self.shape)
	

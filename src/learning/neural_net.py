from typing import Callable, List
#from numba import jitclass
from .connection_layer import Connection


class Neural_Network:
	def __init__(self, shape: List[int], activation_function : Callable) -> None:
		self.shape = shape
		self.activation_function = activation_function
		self.layer_connections: List[Connection] = []
		for i in range(len(shape[:-1])):
			left_side, right_side = shape[i], shape[i+1] 
			connection = Connection(left_side, right_side)
			connection.random_init()
			self.layer_connections.append(connection)

	def eval_forward(self, input_vec : List[float])-> List[float]:
		result = input_vec
		for i in range(len(self.shape)-1):
			result = self.layer_connections[i].eval_forward(result, activation_function=self.activation_function)
		return result

	def __repr__(self):
		return "Neural net:" + str(self.shape)


	def mutate(self, rate : float) -> None:
		for layer in self.layer_connections:
			layer.mutate(rate)
	

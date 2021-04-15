from .connection_layer import Connection_Layer, Activation_Function


from dataclasses import dataclass, field
from typing import List, Tuple
import numpy as np


Network_Description = Tuple[List[int], Activation_Function]

@dataclass
class Neural_Network:
	description: Network_Description
	layers: List[Connection_Layer] = field(init=False)
	
	def __repr__(self):
		return "Neural net: " + str(self.description)

	def __post_init__(self):
		self.layers = list()
		for i in range(len(self.description[0])-1):
			input_size, output_size = self.description[0][i], self.description[0][i+1]
			connection = Connection_Layer(input_size=input_size,
																		output_size=output_size)
			connection.init_data()
			self.layers.append(connection)
	
	def eval_forward(self, input_vec : np.ndarray) -> np.ndarray:
		out_vec = input_vec
		for i in range(len(self.layers)):
			out_vec = self.layers[i].eval_forward(out_vec, activation_function=self.description[1])
		return out_vec
	
	def mutate(self, mutation_force: float) -> None:
		for layer in self.layers:
			layer.mutate(mutation_force)

	def reduce_parameters(self) -> None:
		for layer in self.layers:
			layer.reduce_parameters()

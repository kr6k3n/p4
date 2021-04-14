from typing import Dict, List, Tuple
import numpy as np
from dataclasses import dataclass, field
from .connection_layer import Connection_Layer, Activation_Function


Network_Description = List[Tuple[int, Activation_Function]]

@dataclass
class Neural_Network:
	description: Network_Description
	layers: List[Connection_Layer] = field(init=False)
	
	def __repr__(self):
		return "Neural net:" + str(self.description)

	def __post_init__(self):
		self.layers = list()
		for i in range(len(self.description)-1):
			left_side, right_side = self.description[i][0], self.description[i+1][0]
			connection = Connection_Layer(left_side, right_side, self.description[i+1][1])
			connection.init_data()
			self.layers.append(connection)
	
	def eval_forward(self, input_vec : np.ndarray) -> np.ndarray:
		out_vec = input_vec
		for i in range(len(self.layers)):
			out_vec = self.layers[i].eval_forward(out_vec)
		return out_vec
	
	def mutate(self, rate: float) -> None:
		for layer in self.layers:
			layer.mutate(rate)


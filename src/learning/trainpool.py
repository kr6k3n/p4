from .make_stuff_go_faster import fastmap
from .agent import Agent

from typing import List

import random as R

class TrainPool:
	def __init__(self, population_size: int, agent : type, name : str ="Unnamed") -> None:
		def new_agent():
			return agent()
		self.population_size = population_size
		self.name = name
		print("Creating", self.name, "generation")
		print(f"Creating initial {agent.name} population...")
		self.population: List[Agent] = fastmap(new_agent, range(population_size),
																					              display_progress=True)
	
	def compete(self) -> None:
		# add multiprocessing here later for sped
		for delta in range(1, self.population_size//2):
			for i in range(self.population_size//2):
				p1 = self.population[i]
				p2 = self.population[(i+delta) % self.population_size]
				p1.play_against_other(p2)

	def epoch(self) -> None:
		self.compete()
		self.population.sort(key= lambda a: a.score)
		del self.population[self.population_size//10:] # Keep only top 10% agents
		#mutate top 10% with low factor
		#create copies of top 10 and mutate with high factor
		R.shuffle(self.population)
	
	def save(self) -> None:
		pass
		

	"""def next_gen(self) -> None:
		#sort by score
		sorted_snakes = sorted(
			self.population, key=lambda s: s.score(), reverse=True)
		print("best score here", sorted_snakes[0].score())
		# kill all snakes except top 25%
		print("killing snakes...")
		sorted_snakes = sorted_snakes[:self.population_size//4]
		print("merging snakes")
		new_snakes_amount = max(1, self.population_size//100)
		new_children_amount = self.population_size-new_snakes_amount
		self.population = fastmap(create_child, list(
			sorted_snakes for _ in range(new_children_amount)), display_progress=True)
		print("adding new children")
		self.population += fastmap(new_snake,
								   range(new_snakes_amount), display_progress=True)"""

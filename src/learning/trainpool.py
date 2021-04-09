from .make_stuff_go_faster import fastmap
from .agent import Agent

from typing import List

import random as R
import pickle
import datetime
import os

class TrainPool:
	def __init__(self, population_size: int, agent : type, name : str ="Unnamed") -> None:
		def new_agent():
			return agent()
		self.population_size = population_size
		self.name = name
		print("Creating", self.name, "generation")
		print(f"Creating initial {agent.name} population...")
		self.population: List[Agent] = fastmap(new_agent, range(population_size),display_progress=True)
	
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
	
	def save(self, pool_solder_path : str) -> None:
		pool_path = pool_solder_path + "/" + self.name
		try:
			os.mkdir(pool_path)
		except FileExistsError:
			pass
		now = datetime.datetime.now()
		now_path =  f"{pool_path}/{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}"
		latest_path = f"{pool_path}/latest"
		now_file = open(now_path, "wb")
		latest_file = open(latest_path, "wb")
		pickle.dump(self, now_file)
		pickle.dump(self, latest_file)
		now_file.close()
		latest_file.close()
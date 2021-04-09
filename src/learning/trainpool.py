from .make_stuff_go_faster import fastmap
from .agent import Agent

from typing import Callable, List, Type

import random as R
import datetime
import pickle
import tqdm
import copy
import os

def new_agent(agent_class) -> Callable:
	return agent_class()

def compete_pairs(d):
	population, index_delta = d[0], d[1]
	for i in range(len(population)//2):
		p1 = population[i]
		p2 = population[(i+index_delta) % index_delta]
		p1.play_against_other(p2)

class TrainPool:
	def __init__(self, population_size: int, agent : Type[Agent], name : str ="Unnamed") -> None:
		self.population_size: int= population_size
		self.name : str = name
		print("Creating", self.name, "generation")
		print(f"Creating initial {agent.name} population...")
		self.population: List[Agent] = fastmap(new_agent, list(agent for _ in range(population_size)) ,display_progress=True)
		self.epochs : int = 0
	
	def compete(self) -> None:
		# add multiprocessing here later for sped
		print("competing...")
		for delta in tqdm.tqdm(range(1, self.population_size//2)):
			for i in range(self.population_size//2):
				p1 = self.population[i]
				p2 = self.population[(i+delta) % self.population_size]
				p1.play_against_other(p2)

	def display_stats(self):
		number_of_matches = (self.population_size**2 - self.population_size)/2
		print("best Agents: ")
		for i in range(10):
			print(i+1, ".", 
						"score:", self.population[i].score, 
						"ratio:", self.population[i].score / (self.population_size//2))
		self.epochs += 1

	def epoch(self) -> None:
		print(f"{self.name}: epoch:{self.epochs+1}")
		self.compete()
		self.population.sort(key= lambda ag: ag.score, reverse=True)
		self.display_stats()

		print("killing bottom 90% of population")
		del self.population[self.population_size//10:] # Keep only top 10% agents
		print("appky gamma rays to mutate population...")
		for i in tqdm.tqdm(range(len(self.population))):
			for _ in range(self.population_size//9):
				#create copies of top 10% and mutate with high factor ==> take higher risk
				new_agent = copy.deepcopy(self.population[i])
				new_agent.mutate(0.8)
				self.population.append(new_agent)
				#mutate top 10% with low factor ==> "fine tune"
				self.population[i].mutate(0.95)
		print("shuffling population")
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

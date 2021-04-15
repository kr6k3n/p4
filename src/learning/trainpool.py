from .agent import Agent
from dataclasses import dataclass, field


from typing import List, Optional, Type

import random as R
import statistics
import datetime
import pickle
import tqdm
import copy
import os

@dataclass
class TrainPool:
	population_size: int
	agent: Type[Agent]
	name : str
	population: List[Agent] = field(init=False)
	epochs : int = 0
	
	def __post_init__(self) -> None:
		print("\n\nCreating", self.name, "generation")
		print(f"Creating initial {self.agent.name} population...")
		self.population= [self.agent() for _ in range(self.population_size)]
	
	def display_stats(self, debugging=False):
		scores = list(p.score for p in self.population)
		mean_score = statistics.mean(scores)
		median_score = statistics.median(scores)
		if debugging:
			print("mean_score", mean_score, "median_score", median_score)
		else:
			print(self.name, "pool, epoch #", self.epochs, "mean_score", mean_score, "median_score", median_score)

	def compete(self, debug=False) -> None:
		# add multiprocessing here later for sped
		gen = range(1, self.population_size//2)
		if debug:
			print("competing...")
			gen = tqdm.tqdm(gen)
		for delta in gen:
			for i in range(len(self.population)//2):
				p1 = self.population[i]
				p2 = self.population[(i+delta) % len(self.population)]
				p1.play_against_other(p2)
				p2.play_against_other(p1)
		
		

	def show_game_from_best(self) -> None:
		print(self.name, "pool, epoch #", self.epochs)
		print("\nDEMO\ngood player vs good player")
		p1, p2 = self.population[0], self.population[1]
		p1.play_against_other(p2, debug_game=True)
		print("good player vs bad player")
		p1, p2 = self.population[0], self.population[-1]
		p2.play_against_other(p1, debug_game=True)

	def epoch(self, demo_rate=float('inf'), debug=False) -> None:
		for i in range(len(self.population)):
			self.population[i].reset()
	
		print(f"\n{self.name}: epoch {self.epochs+1}")
	
		self.compete(debug=debug)
		self.population.sort(key= lambda ag: ag.score, reverse=True)
		self.display_stats(debugging=debug)

		if (self.epochs+1) % demo_rate == 0 and self.epochs != 0:
			self.show_game_from_best()
			print('nn output sample')
			p = self.population[0]
			print(p.NN.eval_forward(p.sim_instance.serialized_state(p.player_id)))

		if debug: print("killing bottom 90% of population")

		del self.population[int(self.population_size*0.1):] # Keep only top 10% agents
		
		gen = range(len(self.population))
		if debug: 
			print("apply gamma rays to mutate population...")
			gen = tqdm.tqdm(gen)

		for i in gen:
			for _ in range(9):
				#create copies of top 10% and mutate with high factor ==> take higher risk
				new_agent = copy.deepcopy(self.population[i])
				new_agent.mutate(0.8)
				self.population.append(new_agent)
				#mutate top 10% with low factor ==> "fine tune"
				self.population[i].mutate(0.95)

		if debug: print("shuffling population")

		R.shuffle(self.population)
		self.epochs += 1
		
def save_pool_to_disk(t_pool: TrainPool, pool_folder_path: str) -> None:
	pool_path = pool_folder_path + "/" + t_pool.name
	try:
		os.mkdir(pool_path)
	except FileExistsError:
		pass
	now = datetime.datetime.now()
	now_path =  f"{pool_path}/epoch {t_pool.epochs} | {now.day}-{now.month}-{now.year} {now.hour}:{now.minute}"
	latest_path = f"{pool_path}/latest"
	now_file = open(now_path, "wb")
	latest_file = open(latest_path, "wb")
	pickle.dump(t_pool, now_file)
	pickle.dump(t_pool, latest_file)
	now_file.close()
	latest_file.close()


def restore_pool_from_disk(name, pool_folder_path) -> Optional[TrainPool]:
	pool_path = pool_folder_path + "/" + name
	latest_path = f"{pool_path}/latest"
	try:
		latest_file = open(latest_path, "rb")
	except OSError:
		return None
	pool = pickle.load(latest_file)
	latest_file.close()
	return pool 

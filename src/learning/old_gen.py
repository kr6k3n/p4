class Generation:
	def __init__(self, generation_size: int, Agent: type) -> None:
		self.generation_size = generation_size
		print("creating initial population...")
		self.population: List[Snake] = fastmap(
			new_snake, range(self.generation_size), display_progress=True)
		self.alive_snakes = [s for s in self.population]

	def simulate_step(self) -> None:
		for snake_index, snake_alive in enumerate(fastmap(snake_step, self.alive_snakes)):
			if not snake_alive:
				self.alive_snakes.pop(snake_index)

	def simulate_generation(self):
		time = 0
		while len(self.alive_snakes) > 0:
			self.simulate_step()
			# debug
			print("time", time, ":", len(self.alive_snakes), "snakes alive")
			time += 1

	def next_gen(self) -> None:
		#sort by score
		sorted_snakes = sorted(
			self.population, key=lambda s: s.score(), reverse=True)
		print("best score here", sorted_snakes[0].score())
		# kill all snakes except top 25%
		print("killing snakes...")
		sorted_snakes = sorted_snakes[:self.generation_size//4]
		print("merging snakes")
		new_snakes_amount = max(1, self.generation_size//100)
		new_children_amount = self.generation_size-new_snakes_amount
		self.population = fastmap(create_child, list(
			sorted_snakes for _ in range(new_children_amount)), display_progress=True)
		print("adding new children")
		self.population += fastmap(new_snake,
								   range(new_snakes_amount), display_progress=True)

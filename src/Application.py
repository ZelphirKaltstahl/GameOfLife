from scipy import ndimage
from scipy.signal import convolve2d

import numpy as np

import itertools

from Rules import Rules
from State import State
from Plotter import Plotter

import examples.example_state_000 as examples

class GameOfLife():
	"""docstring for GameOfLife"""
	def __init__(self,):
		super(GameOfLife, self).__init__()

		# self.rules = Rules()
		adjacency_matrix = np.full((3,3), 1, dtype=np.uint8)
		center_y, center_x = self.get_center_indices(adjacency_matrix)
		adjacency_matrix[center_y][center_x] = False
		self.rules = Rules(adjacency_matrix=adjacency_matrix)

		# self.initial_generation = examples.example_state_000
		# self.initial_generation = examples.example_state_001
		# self.initial_generation = examples.example_state_002
		self.initial_generation = examples.example_state_003

		self.state = State(self.initial_generation)

		self.state_history = [self.state]

		print(self.state)
		print(
			'The generation has {number_of_objects} objects.'.format(
				number_of_objects=self.state.count_blobs(
					self.rules.adjacency_matrix
				)
			)
		)

		max_gen = 100
		while max_gen > 0 and np.any(np.any(self.state.generation, axis=1), axis=0):
			self.next()
			#print(self.state)
			max_gen -= 1

		for state in self.state_history:
			print(state)

		self.plot()

	def get_center_indices(self, arr):
		y = int(len(arr) / 2)
		x = int(len(arr) / 2)
		return (x, y)

	def next(self):
		"""This method evolves the state's generation by one generation."""
		# convolution "slides" a mask / kernel over each element of the array.
		# convolution is a multiplication of each element under the mask / kernel, with the element inside the mask/kernel, which is above it.
		# the products of those multiplications are then summed up and written to a new array.
		# this means we can get the neighbors_count + 1 in the center, if there was a living cell.
		# we substract the 1 in the center, by simply substracting the whole original array from the result of the convolve2d operation.
		# hopefully true values will be interpreted as the value 1 otherwise we will need to switch to integer arrays

		# Return
		# we want to return an array of truth values.
		# we have the neighbor counts.
		# we want TRUE values if the neighbor counts is 3 or if it is only 2 but there was a living cell at that position in the array before.
		# (nbrs_count == 3) checks for the 3 neighbor case.
		# (nbrs_count == 2) checks for the 2 neighbor case and the logical element wise AND operation requires there to be a living cell in the generation before.
		# nbrs_count = convolve2d(X, np.ones((3, 3)), mode='same', boundary='wrap') - X
		# return (nbrs_count == 3) | (X & (nbrs_count == 2))
		if self.rules.wrapping:
			neighbors_count = convolve2d(
				self.state.generation,
				self.rules.adjacency_matrix,
				mode='same',
				boundary='wrap'
			)# - self.state.generation
		else:
			neighbors_count = convolve2d(
				self.state.generation,
				self.rules.adjacency_matrix,
				mode='same',
				boundary='fill',
				fillvalue=0
			)# - self.state.generation

		birth_counts = self.flatten_array(self.rules.birth_counts)
		surviving_counts = self.flatten_array(self.rules.surviving_counts)

		birth_cells = np.in1d(neighbors_count, birth_counts).reshape(neighbors_count.shape)
		possibly_surviving_cells = np.in1d(neighbors_count, surviving_counts).reshape(neighbors_count.shape)
		next_state_generation = birth_cells | (self.state.generation & possibly_surviving_cells)

		self.state = State(next_state_generation, generation_number=self.state.generation_number+1)
		self.state_history.append(self.state)

	def flatten_array(self, arr):
		return list(itertools.chain.from_iterable(arr))

	def plot(self):
		plotter = Plotter()
		plotter.plot_alive_cells(self.state_history)

def main():
	game_of_life_app = GameOfLife()

if __name__ == '__main__':
	main()

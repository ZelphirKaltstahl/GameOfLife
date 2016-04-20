from scipy import ndimage
from scipy.signal import convolve2d

import numpy as np

import itertools

from Rules import Rules
from State import State

import examples.example_state_000 as examples

class GameOfLife():
	"""docstring for GameOfLife"""
	def __init__(self):
		super(GameOfLife, self).__init__()

		# self.rules = Rules()
		adjacency_matrix = np.full((3,3), 1, dtype=np.uint8)
		center_y, center_x = self.get_center(adjacency_matrix)
		adjacency_matrix[center_y][center_x] = False
		self.rules = Rules(adjacency_matrix=adjacency_matrix)

		T = True
		F = False

		self.initial_generation = [
			[T, F, F, F, F, F, F],
			[T, F, F, F, T, F, F],
			[T, F, F, F, F, F, F],
			[F, F, T, F, T, F, F],
			[F, F, F, F, F, F, F],
			[F, F, F, F, F, F, F],
			[F, F, F, F, F, F, F],
			[F, F, T, T, T, F, F],
			[F, F, F, F, T, F, F],
			[F, F, T, F, T, F, F]
		]

		self.initial_generation = examples.example_state_000

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
		self.next()
		print(self.state)

	def get_center(self, matrix):
		y = int(len(matrix) / 2)
		x = int(len(matrix) / 2)
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

		print(neighbors_count)

		birth_counts = self.flatten_array(self.rules.birth_counts)
		surviving_counts = self.flatten_array(self.rules.surviving_counts)
		print('birth counts:', birth_counts)
		print('surviving counts:', surviving_counts)

		# for start, end in self.rules.birth_counts:
		# 	pass

		# birth_counts = np.array([range(start, end+1) for start, end in self.rules.birth_counts])
		# print(birth_counts)
		# print(list(itertools.chain.from_iterable(self.rules.birth_counts)))
		# print(np.fromiter(itertools.chain.from_iterable(self.rules.birth_counts), dtype=np.uint8))
		#print(np.fromiter(birth_counts, dtype=np.uint8))
		birth_cells = np.in1d(neighbors_count, birth_counts).reshape(neighbors_count.shape)
		possibly_surviving_cells = np.in1d(neighbors_count, surviving_counts).reshape(neighbors_count.shape)
		next_state_generation = birth_cells | (self.state.generation & possibly_surviving_cells)
		# next_state_generation = (neighbors_count in birth_counts) | (self.state.generation & (neighbors_count in surviving_counts))
		# next_state_generation = np.logical_and(neighbors_count)
		# next_state_generation = (np.in1d(neighbors_count.ravel(), birth_counts)) | (self.state.generation & np.in1d(neighbors_count.ravel(), surviving_counts))

		self.state = State(next_state_generation, generation_number=self.state.generation_number+1)
		self.state_history.append(self.state)

	def flatten_array(self, arr):
		return list(itertools.chain.from_iterable(arr))

		# nbrs_count contains the number of neighbors calculated by the convolve2d operation

		# next_state_generation = np.full((self.state.height, self.state.width), False, dtype=bool)
		#
		# for (x,y), value in np.ndenumerate(self.state.generation):
		# 	print(x, '|', y, sep='')
		#
		#
		# 		# neighbors = self.get_neighbors([row_index, column_index])
		# 		# neighbors_count = len(neighbors)
		# 		#
		# 		# if self.state.generation[row_index][column_index]:
		# 		# 	if neighbors_count in range(self.rules.surviving_counts[0], self.rules.surviving_counts[1] + 1):
		# 		# 		next_state_generation[row_index][column_index] = True
		# 		#
		# 		# neighbors_alive_counter = 0
		# 		# for neighbor in self.get_neighbors([row_index, column_index]):
		# 		# 	if neighbor:
		# 		# 		neighbors_alive_counter += 1
		# 		#
		# 		# for alive_range in self.rules.birth_counts:
		# 		# 	elif neighbors_alive_counter in range(alive_range[0], alive_range[1]+1):  # +1 because range excludes the second number from the returned range
		# 		# 		next_state_generation[row_index][column_index] = True
		#
		#
		# next_state = State(next_state_generation)
		# print('neighbors of', [3,4], ' are', self.get_neighbors((3,4)))
		# print('Next:', next_state)

	# def get_neighbors(self, coords):
	# 	"""
	# 	This method returns the neighbors for coordinates considering the adjacency matrix.
	#
	# 	Parameters
	# 	----------
	# 	coords : tuple of ints
	# 		the coordinates, for which neighbors will be calculated
	# 	"""
	# 	pass
	#
	# 	# # print('Height:', self.state.height)
	# 	# # print('Width:', self.state.width)
	# 	# # if self.rules.wrapping: print('wrapping is activated')
	# 	# # else: print('wrapping is not activated')
	# 	# neighbors = []
	# 	# for row_index, row in enumerate(self.rules.offsets):
	# 	# 	for col_index, cell in enumerate(row):
	# 	# 		if not np.array_equal(cell, np.zeros(2, dtype=int)):  # equals [0, 0]
	# 	# 			# print('cell row:{row_index} cell:{col_index}'.format(row_index=row_index, col_index=col_index), cell)
	# 	# 			x_coords = (coords[1] + cell[1])
	# 	# 			y_coords = (coords[0] + cell[0])
	# 	# 			if self.rules.wrapping:
	# 	# 				x_coords = x_coords % self.state.width
	# 	# 				y_coords = y_coords % self.state.height
	# 	# 				neighbors.append([y_coords, x_coords])
	# 	# 			else:
	# 	# 				if x_coords <= self.state.width - 1 and y_coords <= self.state.height - 1:
	# 	# 					# print('x_coords is', x_coords)
	# 	# 					# print('y_coords is', y_coords)
	# 	# 					neighbors.append([y_coords, x_coords])
	# 	# # print('neighbors:', neighbors)
	# 	# return neighbors



def main():
	game_of_life_app = GameOfLife()

if __name__ == '__main__':
	main()

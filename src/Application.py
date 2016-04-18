from scipy import ndimage
import numpy as np
from Rules import Rules
from State import State

class GameOfLife():
	"""docstring for GameOfLife"""
	def __init__(self):
		super(GameOfLife, self).__init__()

		self.rules = Rules()
		# self.rules = Rules(adjacency_matrix=[[False,True,False],[True,True,True],[False,True,False]])

		self.initial_generation = [
			[False, True, True, True, False],
			[True, True, True, True, True],
			[True, False, False, False, False],
			[False, True, True, True, True],
			[True, True, True, True, True]
		]

		self.state = State(self.initial_generation)

		# test_state.mirror_vertically()
		# test_state.mirror_horizontally().turn_clockwise().mirror_vertically().turn_counter_clockwise()
		self.state.invert()

		print(self.state)
		print(
			'The generation has {number_of_objects} objects.'.format(
				number_of_objects=self.state.count_blobs(
					self.rules.adjacency_matrix
				)
			)
		)

		self.next()

	def next(self):
		next_state_generation = np.full((self.state.height, self.state.width), False, dtype=bool)
		next_state = State(next_state_generation)
		# print('neighbors of', [3,4], ' are', self.get_neighbors((3,4)))
		# print('Next:', next_state)

	def get_neighbors(self, coords):
		"""
		This method returns the neighbors for coordinates considering the adjacency matrix.

		Parameters
		----------
		coords : tuple of ints
			the coordinates, for which neighbors will be calculated
		"""
		print('Height:', self.state.height)
		print('Width:', self.state.width)
		if self.rules.wrapping: print('wrapping is activated')
		else: print('wrapping is not activated')

		neighbors = []
		for row_index, row in enumerate(self.rules.offsets):
			for col_index, cell in enumerate(row):
				if not np.array_equal(cell, np.zeros(2, dtype=int)):  # equals [0, 0]
					print('cell row:{row_index} cell:{col_index}'.format(row_index=row_index, col_index=col_index), cell)
					x_coords = (coords[1] + cell[1])
					y_coords = (coords[0] + cell[0])
					if self.rules.wrapping:
						x_coords = x_coords % self.state.width
						y_coords = y_coords % self.state.height
						neighbors.append([y_coords, x_coords])
					else:
						if x_coords <= self.state.width - 1 and y_coords <= self.state.height - 1:
							print('x_coords is', x_coords)
							print('y_coords is', y_coords)
							neighbors.append([y_coords, x_coords])

		# print('neighbors:', neighbors)

		return neighbors


def main():
	game_of_life_app = GameOfLife()

if __name__ == '__main__':
	main()

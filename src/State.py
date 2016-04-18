from scipy import ndimage
import numpy as np

class State():

	ALIVE_SYMBOL = 'x'#'█'#'■'#'x'#'X'#'▣'#'▦'#'◈'#'◉'#'◎'#'●'#'⬛'
	DEAD_SYMBOL = 'o'#'o'#'□'#'▒'#'◇'#'○'#'◌'#'◯'#'▢'
	HORIZONTAL_BORDER_SYMBOL = '-'#'═'#'━'
	VERTICAL_BORDER_SYMBOL = '|'#'║'#'┃'
	NORTH_WEST_BORDER_CORNER_SYMBOL = '+'#'╔'#'┏'
	NORTH_EAST_BORDER_CORNER_SYMBOL = '+'#'╗'#'┓'
	SOUTH_EAST_BORDER_CORNER_SYMBOL = '+'#'╝'#'┛'
	SOUTH_WEST_BORDER_CORNER_SYMBOL = '+'#'╚'#'┗'
	PADDING_SYMBOL = ' '

	"""
	Instances of this class represent a generation in the game of life.

	Parameters
	----------
	generation : 2d numpy array of bool values
	"""
	def __init__(self, generation, generation_number=100000):
		super(State, self).__init__()
		if generation is None:
			self.generation = np.array([
				[False,False,False,False,False],
				[False,False,True,False,False],
				[False,False,True,False,False],
				[False,False,True,False,False],
				[False,False,False,False,False]
			])
		else:
			self.generation = np.array(generation)

		self.generation_number = generation_number
		self.width = len(self.generation[0])
		self.height = len(self.generation)

		self.padding = 0

	def __str__(self):
		state_string = ''
		state_string += '\n'

		diagram_width = self.width + (self.padding * 2) + 2
		horizontal_border = State.HORIZONTAL_BORDER_SYMBOL * (diagram_width - 2)

		state_string += State.NORTH_WEST_BORDER_CORNER_SYMBOL
		state_string += horizontal_border
		state_string += State.NORTH_EAST_BORDER_CORNER_SYMBOL + '\n'

		alive_counter = 0

		# padding top
		for i in range(self.padding):
			state_string += State.VERTICAL_BORDER_SYMBOL
			state_string += State.PADDING_SYMBOL * (self.width + (2 * self.padding))
			state_string += State.VERTICAL_BORDER_SYMBOL
			state_string += '\n'

		# content
		for row in self.generation:
			state_string += State.VERTICAL_BORDER_SYMBOL
			state_string += State.PADDING_SYMBOL * self.padding
			for cell in row:
				if cell:
					alive_counter += 1
					state_string += State.ALIVE_SYMBOL
				else: state_string += State.DEAD_SYMBOL
			state_string += State.PADDING_SYMBOL * self.padding
			state_string += State.VERTICAL_BORDER_SYMBOL + '\n'

		# padding bottom
		for i in range(self.padding):
			state_string += State.VERTICAL_BORDER_SYMBOL
			state_string += ' ' * (self.width + (2 * self.padding))
			state_string += State.VERTICAL_BORDER_SYMBOL
			state_string += '\n'

		state_string += State.SOUTH_WEST_BORDER_CORNER_SYMBOL
		state_string += horizontal_border
		state_string += State.SOUTH_EAST_BORDER_CORNER_SYMBOL + '\n'

		state_string += 'generation:{generation_number}\n'.format(generation_number=self.generation_number)
		state_string += 'cells: {cell_counter}\n'.format(cell_counter=self.width * self.height)
		state_string += 'alive: {alive_counter}\n'.format(alive_counter=alive_counter)
		state_string += 'dead: {dead_counter}\n'.format(dead_counter=(self.width * self.height - alive_counter))

		return state_string

	def turn_clockwise(self, times_90_degree=1):
		self.generation = np.rot90(self.generation, k=-times_90_degree)
		return self

	def turn_counter_clockwise(self, times_90_degree=1):
		self.generation = np.rot90(self.generation, k=times_90_degree)
		return self

	def mirror_vertically(self):
		self.generation = np.flipud(self.generation)
		return self

	def mirror_horizontally(self):
		self.generation = np.fliplr(self.generation)
		return self

	def invert(self):
		self.generation = np.invert(self.generation)
		return self

	def count_blobs(self, adjacency_matrix):
		print('AM:\n', adjacency_matrix)

		self.invert()
		blobs, number_of_blobs = ndimage.label(self.generation, structure=adjacency_matrix)
		self.invert()
		return number_of_blobs

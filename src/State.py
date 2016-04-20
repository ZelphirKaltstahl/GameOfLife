import scipy as sp
import numpy as np

class State():

	ALIVE_SYMBOL = 'x'#'█'#'■'#'x'#'X'#'▣'#'▦'#'◈'#'◉'#'◎'#'●'#'⬛'
	DEAD_SYMBOL = ' '#'o'#'□'#'▒'#'◇'#'○'#'◌'#'◯'#'▢'
	HORIZONTAL_BORDER_SYMBOL = '–'#'═'#'━'
	VERTICAL_BORDER_SYMBOL = '|'#'║'#'┃'
	NORTH_WEST_BORDER_CORNER_SYMBOL = '+'#'╔'#'┏'
	NORTH_EAST_BORDER_CORNER_SYMBOL = '+'#'╗'#'┓'
	SOUTH_EAST_BORDER_CORNER_SYMBOL = '+'#'╝'#'┛'
	SOUTH_WEST_BORDER_CORNER_SYMBOL = '+'#'╚'#'┗'
	PADDING_SYMBOL = ' '
	INNER_VERTICAL_SPACING = 1
	INNER_HORIZONTAL_SPACING = 1

	"""
	Instances of this class represent a generation in the game of life.

	Parameters
	----------
	generation : 2d numpy array of bool values
	"""
	def __init__(self, generation, generation_number=0):
		super(State, self).__init__()
		if generation is None:
			self.generation = np.array([
				[False, False, False, False, False],
				[False, False, True, False, False],
				[False, False, True, False, False],
				[False, False, True, False, False],
				[False, False, False, False, False]
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

		h_spacing = ' ' * State.INNER_HORIZONTAL_SPACING
		horizontal_border = h_spacing + (State.HORIZONTAL_BORDER_SYMBOL + h_spacing) * (diagram_width - 2)

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
			state_string += h_spacing
			for cell in row:
				if cell:
					alive_counter += 1
					state_string += State.ALIVE_SYMBOL
				else: state_string += State.DEAD_SYMBOL
				state_string += h_spacing
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
		blobs, number_of_blobs = sp.ndimage.label(self.generation, structure=adjacency_matrix)
		self.invert()
		return number_of_blobs

	def count_alive_cells(self):
		return np.sum(self.generation)

	# def get_neighbors_window(y_coord, x_coord, rows=3, cols=3):
	# 	'''
	# 	Returns a rows*cols array whose "center" element is arr[x,y]
	# 	'''
	# 	return np.roll(
	# 		np.roll(self.generation, shift=-x_coord+1, axis=0),
	# 		shift=-y_coord+1,
	# 		axis=1
	# 	)[:rows,:cols]

	# def get_neighbors_window(y_coord, x_coord, rows=3, cols=3, wrap=True):
	# 	row_offset = int(rows / 2)
	# 	col_offset = int(cols / 2)
	#
	# 	if wrap:
	# 		y_min = y_coord - row_offset
	# 		y_max = y_coord + row_offset
	# 		x_min = x_coord - col_offset
	# 		x_max = x_coord + col_offset
	#
	# 		return self.generation.take(
	# 			range(y_min, y_max), mode='wrap', axis=0
	# 		).take(
	# 			range(x_min, x_max), mode='wrap', axis=1
	# 		)
	# 	else:
	# 		y_min = ((y_coord - row_offset) + self.height) % self.height
	# 		y_max = ((y_coord + row_offset) + self.height) % self.height
	# 		x_min = ((x_coord - col_offset) + self.width) % self.width
	# 		x_max = ((x_coord + col_offset) + self.width) % self.width
	#
	# 		return self.generation.take(
	# 			range(y_min, y_max), mode='clip', axis=0
	# 		).take(
	# 			range(x_min, x_max), mode='clip', axis=1
	# 		)

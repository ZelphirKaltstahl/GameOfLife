import numpy as np
from scipy import ndimage
from InvalidAdjacencyMatrixException import InvalidAdjacencyMatrixException

class Rules():
	"""
	This class' instances represent a set of rules for the game of life.

	Parameters
	----------
	die_counts : list of tuples
	surviving_counts : list of tuples
	birth_counts : list of tuples
	wrapping : bool
	"""
	def __init__(
		self,
		die_counts=[(0,1),(4,8)],
		surviving_counts=[(2,2)],
		birth_counts=[(3,3)],
		wrapping=True,
		default_event='survive',
		adjacency_matrix=np.full((3,3), True, dtype=bool)
	):
		super(Rules, self).__init__()
		self.die_counts = die_counts
		self.surviving_counts = surviving_counts
		self.birth_counts = birth_counts
		self.wrapping = wrapping
		self.default_event = default_event

		if len(adjacency_matrix) % 2 != 1 or len(adjacency_matrix) != len(adjacency_matrix[0]):
			raise InvalidAdjacencyMatrixException()
		else:
			self.adjacency_matrix = adjacency_matrix

	#	self.offsets = self.calculate_offsets()

	# def calculate_offsets(self):
	# 	height = len(self.adjacency_matrix)
	# 	width = len(self.adjacency_matrix[0])
	#
	# 	# initialize offset array
	# 	offsets = np.full((height, width), (0, 0), dtype=(int, 2))
	#
	# 	# calculate center coordinate
	# 	center_x = int(width / 2)
	# 	center_y = int(height / 2)
	#
	# 	# calculate offsets
	# 	for row_index, row in enumerate(offsets):
	# 		for column_index, cell in enumerate(row):
	# 			if self.adjacency_matrix[row_index][column_index] != 0:
	# 				cell[0] = row_index - center_y
	# 				cell[1] = column_index - center_y
	#
	# 	print(offsets)
	#
	# 	return offsets

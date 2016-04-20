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

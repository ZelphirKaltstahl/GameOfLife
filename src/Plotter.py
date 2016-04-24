import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

class Plotter(object):
	"""docstring for Plotter"""
	def __init__(self):
		super(Plotter, self).__init__()

	def plot_alive_cells(self, state_history):
		alive_cells = [state.count_alive_cells() for state in state_history]
		generations = [state.generation_number for state in state_history]

		# calculate line
		line = plt.plot(
			generations,
			alive_cells,
			'-',
			linewidth=1.2,
			label='alive cells'
		)

		# calculate average
		average_value = np.array(alive_cells).mean()
		average_alive_cells = [average_value for element in generations]
		mean_line = plt.plot(
			generations,
			average_alive_cells,
			label='mean',
			linestyle='--'
		)

		# Make a legend
		plt.legend(loc='upper right')
		plt.title('Alive Cells per Generation', fontsize=24)
		plt.show()

	def plot_objects_count(self, rules, state_history):
		objects_counts = [state.count_blobs(rules.adjacency_matrix) for state in state_history]
		generations = [state.generation_number for state in state_history]

		# calculate line
		line = plt.plot(
			generations,
			objects_counts,
			'-',
			linewidth=0.8,
			label='objects count'
		)

		# calculate average
		average_value = np.array(objects_counts).mean()
		average_objects_counts = [average_value for element in generations]
		mean_line = plt.plot(
			generations,
			average_objects_counts,
			linestyle='--',
			label='mean'
		)

		# Make a legend
		plt.legend(loc='upper right')
		plt.title('Objects per Generation', fontsize=24)
		plt.show()

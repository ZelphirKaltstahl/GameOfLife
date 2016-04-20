import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

class Plotter(object):
	"""docstring for Plotter"""
	def __init__(self):
		super(Plotter, self).__init__()

	def plot_alive_cells(self, state_history):
		alive_cells = [state.count_alive_cells() for state in state_history]

		print('alive_cells:', alive_cells)


		# theta = 2 * np.pi * np.random.rand(N)
		# area = 200 * r**2 * np.random.rand(N)
		# colors = theta
		#
		# ax = plt.subplot(111, projection='polar')
		# c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.hsv)
		# c.set_alpha(0.75)
		# plt.title('Polar Scatter Plot', fontsize=24, y=1.08)
		# plt.show()
		#
		#
		# number_of_values = 200
		# x_values = np.arange(0, number_of_values)
		# y_values = []
		#
		# previous_value = 0
		# for value in range(number_of_values):
		# 	difference = np.random.randint(-5, high=6)
		# 	y_value = previous_value + difference
		# 	y_values.append(y_value)
		# 	previous_value = y_value
		#
		# line = plt.plot(x_values, y_values, '-', linewidth=2)
		# #plt.ylim(-80, 120)
		# plt.xlim(0, number_of_values-1)
		# plt.title('Bar Chart', fontsize=24)
		#
		# # dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
		# # line.set_dashes(dashes)
		#
		# plt.show()

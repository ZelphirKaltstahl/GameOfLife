import numpy as np

T = True
F = False

example_state_glider = [
	[F, T, F, F, F, F, F, F, F, F],
	[F, F, T, F, F, F, F, F, F, F],
	[T, T, T, F, F, F, F, F, F, F],
	[F, F, F, F, F, F, F, F, F, F],
	[F, F, F, F, F, F, F, F, F, F],
	[F, F, F, F, F, F, F, F, F, F],
	[F, F, F, F, F, F, F, F, F, F],
	[F, F, F, F, F, F, F, F, F, F],
	[F, F, F, F, F, F, F, F, F, F],
	[F, F, F, F, F, F, F, F, F, F]
]


example_state_diehard = np.full((64, 64), False, dtype=bool)
example_state_diehard[32][30] = True
example_state_diehard[32][29] = True
example_state_diehard[33][30] = True
example_state_diehard[31][35] = True
example_state_diehard[33][34] = True
example_state_diehard[33][35] = True
example_state_diehard[33][36] = True

# [F, F, F, F, F, F, T, F],
# [T, T, F, F, F, F, F, F],
# [F, T, F, F, F, T, T, T],

example_state_acorn = np.full((64, 64), False, dtype=bool)
example_state_acorn[15+16][14+16] = True
example_state_acorn[17+16][14+16] = True
example_state_acorn[17+16][13+16] = True
example_state_acorn[16+16][16+16] = True
example_state_acorn[17+16][17+16] = True
example_state_acorn[17+16][18+16] = True
example_state_acorn[17+16][19+16] = True

example_state_r_pentomino = np.full((64, 64), False, dtype=bool)
example_state_r_pentomino[32][32] = True
example_state_r_pentomino[32][31] = True
example_state_r_pentomino[31][32] = True
example_state_r_pentomino[33][32] = True
example_state_r_pentomino[31][33] = True

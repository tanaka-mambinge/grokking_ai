from logic import *

attraction_dists = [
    [0, 8, 7, 4, 6, 4],
    [8, 0, 5, 7, 11, 5],
    [7, 5, 0, 9, 6, 7],
    [4, 7, 9, 0, 5, 6],
    [6, 11, 6, 5, 0, 3],
    [4, 5, 7, 6, 3, 0],
]

colony = ACO(
    attractions=attraction_dists,
    colony_size=100,
    iterations=5,
    alpha_beta=(4, 7),
    evaporation_rate=0.4,
)
colony.solve()

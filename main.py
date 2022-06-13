import copy

from logic import *

sack = Sack(9)
items = [
    Item(1, "Pearls", 3, 4),
    Item(2, "Gold", 7, 7),
    Item(3, "Crown", 4, 5),
    Item(4, "Coin", 1, 1),
    Item(5, "Axe", 5, 4),
    Item(6, "Sword", 4, 3),
    Item(7, "Ring", 2, 5),
    Item(8, "Cup", 3, 1),
]


possible_solutions = list(solve_knapsack(sack, items))
possible_solutions.sort(key=lambda s: s.get_value())
possible_solutions.reverse()

print(len(possible_solutions))

for solution in possible_solutions:
    print("==============================")
    print(f"${solution.get_value()}", f"{solution.get_weight()}kg", solution.contents)

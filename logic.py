import random
from operator import attrgetter


class Ant:
    def __init__(self, attractions):
        self.visited = [random.randint(0, len(attractions) - 1)]
        self.attractions = attractions

    def __repr__(self) -> str:
        return f"ant=({self.visited}, {self.get_dist_traveled(self.attractions)})"

    def get_dist_traveled(self, attractions):
        dist = 0

        for a in range(1, len(self.visited)):
            dist += attractions[self.visited[a - 1]][self.visited[a]]

        return dist


class ACO:
    def __init__(
        self,
        attractions=[],
        colony_size=1000,
        alpha_beta=(1, 2),
        evaporation_rate=0.5,
        iterations=5,
    ):
        self.__attractions = attractions
        self.__colony_size = colony_size
        self.__aplha_beta = alpha_beta
        self.__evaporation_rate = evaporation_rate
        self.__iterations = iterations

    def __setup_ants(self):
        return [Ant(self.__attractions) for _ in range(self.__colony_size)]

    def __setup_trails(self, attractions):
        return [[1 for _ in a] for a in attractions]

    def __find_possible_moves(self, trails, attractions, ant, alpha_beta):
        current = ant.visited[-1]
        attractions_count = range(0, len(attractions))
        not_visited = [a for a in attractions_count if a not in ant.visited]

        # list of tuples containing move index and probability
        possible_moves = []
        total_probabilities = 0

        for a in not_visited:
            # calc probability
            pherenomes_on_path = trails[current][a] ** alpha_beta[0]
            heuristic_for_path = (1 / attractions[current][a]) ** alpha_beta[1]
            probability = pherenomes_on_path * heuristic_for_path

            # add move index and probability to possible moves
            possible_moves.append((a, probability))

            # add probability to total
            total_probabilities += probability

        possible_moves = [(a, p / total_probabilities) for a, p in possible_moves]

        return possible_moves

    def __roulette_wheel_selection(self, possible_moves):
        slices = []
        total = 0

        for m in possible_moves:
            slices.append([m[0], total, total + m[1]])
            total += m[1]

        spin = random.random()
        result = [slice for slice in slices if slice[1] < spin <= slice[2]][0]

        return result

    def __update_pheromones(self, trails, attractions, evaporation_rate, ants):
        for x in range(0, len(trails)):
            for y in range(0, len(trails)):
                trails[x][y] = trails[x][y] * evaporation_rate

                for ant in ants:
                    trails[x][y] += 1 / ant.get_dist_traveled(attractions)

    def __best_ant(self, prev_best, ants, attractions):
        if prev_best is None:
            best_ant = ants[0]
        else:
            best_ant = prev_best

        for ant in ants:
            dist = ant.get_dist_traveled(attractions)

            if dist < best_ant.get_dist_traveled(attractions):
                best_ant = ant

        return best_ant

    def solve(self):
        best_ant = None
        trails = self.__setup_trails(self.__attractions)

        for _ in range(0, self.__iterations):
            colony = self.__setup_ants()

            # loop through attractions
            for _ in range(0, len(self.__attractions) - 1):

                # loop through each ant
                for ant in colony:
                    # determine ant's next move
                    possible_moves = self.__find_possible_moves(
                        trails, self.__attractions, ant, self.__aplha_beta
                    )
                    move = self.__roulette_wheel_selection(possible_moves)

                    # add move to visited list
                    ant.visited.append(move[0])

            self.__update_pheromones(
                trails, self.__attractions, self.__evaporation_rate, colony
            )
            best_ant = self.__best_ant(best_ant, colony, self.__attractions)
            print(best_ant)

        return best_ant

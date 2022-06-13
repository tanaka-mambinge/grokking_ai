import random


class Ant:
    def __init__(self, attractions_count):
        self.visited = [random.randint(0, attractions_count - 1)]
        self.distnce = self.get_dist_traveled()

    # def __repr__(self):
    #     return f"{self.visited}"

    def visit_attraction(self, trails):
        pass

    def visit_random_attraction(self):
        pass

    def visit_probalistic_attraction(self, trails):
        pass

    def roulette_wheel_selection(self, probabilities):
        pass

    def get_dist_traveled(self):
        dist = 0

        for a in range(1, len(self.visited)):
            dist += self.visited[a - 1] + self.visited[a]

        return dist


class AOC:
    def __init__(self, attractions, colony_size):
        self.pheromone_intensity = [[1 for _ in a] for a in attractions]
        self.ants = [Ant(len(attractions)) for _ in range(colony_size)]

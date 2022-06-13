import copy
import math
import random


class Sack:
    def __init__(self, max_weight=0):
        self.contents = []
        self.max_weight = max_weight

    def add(self, item):
        self.contents.append(item)
        # self.contents.sort(key=lambda i: i.name)
        self.contents.sort(key=lambda i: i.id)

    def get_value(self):
        value = 0

        for item in self.contents:
            value += item.value

        return value

    def get_weight(self):
        weight = 0

        for item in self.contents:
            weight += item.weight

        return weight


class Individual:
    def __init__(self, chromosome=[], items=[]):
        self.chromosome = chromosome
        self.__calc_totals(items)

    def __repr__(self) -> str:
        return f"'${self.value}, {self.weight}kg'"

    def __calc_totals(self, items):
        # if len(items) > 0:
        total_weight = 0
        total_value = 0

        for i, gene in enumerate(self.chromosome):
            if gene == 1:
                total_weight += items[i].weight
                total_value += items[i].value

        self.weight = total_weight
        self.value = total_value


class Item:
    def __init__(self, id=0, name="", weight=0, value=0):
        self.id = id
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"{self.id}. {self.name}"


def generate_population(individual_size=0, items=[], population_size=0):
    population = []

    for _ in range(population_size):
        individual = Individual(
            [random.choice([0, 1]) for i in range(individual_size)], items
        )
        population.append(individual)

    return population


def fitness(population=[], items=[], max_weight=0):
    fit_individuals = []

    for individual in population:
        total_weight = 0
        total_value = 0

        for i, gene in enumerate(individual.chromosome):
            if gene == 1:
                total_weight += items[i].weight
                total_value += items[i].value

        if total_weight <= max_weight:
            individual.weight = total_weight
            individual.value = total_value
            fit_individuals.append(individual)

    return fit_individuals


def roulette_wheel_selection(population=[], size=0):
    # generate individual probabilities
    total_value = 0
    candidates = []

    for individual in population:
        total_value += individual.value

    for individual in population:
        temp_individual = individual.value / total_value
        candidates.append(temp_individual)

    # generate slice range
    slices = []
    total = 0

    for i in range(len(candidates)):
        slices.append((i, total, total + candidates[i]))
        total += candidates[i]

    # pick parents slices
    parent_slices = []

    for _ in range(size):
        # pick random slice
        spin = random.random()
        parent = [slice for slice in slices if slice[1] < spin <= slice[2]]
        parent_slices.append(*parent)

    # return parents
    parents = []

    for slice in parent_slices:
        parents.append(population[slice[0]])

    return parents


def reproduce_children(parents=[], items=[]):
    i = random.randint(0, len(parents) - 1)
    j = random.randint(0, len(parents) - 1)

    parent_a = parents[i]
    parent_b = parents[j]
    x_over_point = math.floor(len(parents[0].chromosome) / 2)

    children = one_point_crossover(
        parent_a.chromosome, parent_b.chromosome, x_over_point, items
    )

    return children


def one_point_crossover(parent_a, parent_b, x_over_point, items=[]):
    children = []

    # a1 + b2
    child_one = [gene for gene in parent_a[:x_over_point]] + [
        gene for gene in parent_b[x_over_point:]
    ]
    # a2 + b1
    child_two = [gene for gene in parent_a[x_over_point:]] + [
        gene for gene in parent_b[:x_over_point]
    ]

    children.append(Individual(child_one, items))
    children.append(Individual(child_two, items))

    return children


def mutate_individual(individual=Individual()):
    i = random.randint(0, len(individual.chromosome) - 1)

    if individual.chromosome[i] == 1:
        individual.chromosome[i] = 0
    else:
        individual.chromosome[i] = 1

    return individual


def run_ga(items=[], population_size=0, generations=0, sack_capacity=0):
    best_global_fitness = Individual()
    population = generate_population(len(items), items, population_size)

    for _ in range(generations):
        wave = fitness(population, items, sack_capacity)
        wave.sort(key=lambda i: i.value, reverse=True)
        current_best_fitness = wave[0]

        if current_best_fitness.value > best_global_fitness.value:
            best_global_fitness = copy.deepcopy(current_best_fitness)

        parents = roulette_wheel_selection(wave, population_size)
        offspring = []

        for _ in range(population_size):
            children = reproduce_children(parents, items)
            offspring.append(children[0])
            offspring.append(children[1])

        for i, child in enumerate(offspring):
            mutated_child = mutate_individual(child)
            offspring[i] = mutated_child

        population = offspring

    return best_global_fitness


def solve_knapsack(sack=Sack(0), items=[], solutions=set()):
    for i in range(len(items)):
        # copy args
        temp_sack = copy.deepcopy(sack)
        temp_items = copy.deepcopy(items)

        # add item to sack
        current_item = temp_items.pop(i)
        next_weight = current_item.weight + temp_sack.get_weight()

        if next_weight > temp_sack.max_weight:
            solutions.add(temp_sack)
            return

        temp_sack.add(current_item)

        solve_knapsack(temp_sack, temp_items)

    return solutions

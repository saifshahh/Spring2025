### Question 1:

```py
def find_peak(int N):
    left = 0
    right = N

    while left < right:
        mid = (left + right)
        if query(mid) < query(mid + 1):
            left = mid + 1
        else:
            right = mid
    return left
```
### Question 2:

```py
import random

taskTime = [5, 8, 4, 7, 6, 3, 9]
cap = [24, 30, 28]
Cost = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]

NUM_TASKS = len(taskTime)
NUM_FACILITIES = len(cap)
POP_SIZE = 6
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
PENALTY = 1000

def generate():
    return [random.randint(0, NUM_FACILITIES - 1) for _ in range(NUM_TASKS)]

def fitness(ch):
    ft = [0] * NUM_FACILITIES
    totalCost = 0

    for task, facility in enumerate(ch):
        time = taskTime[task]
        cost = Cost[task][facility]
        ft[facility] += time
        totalCost += time * cost

    for i in range(NUM_FACILITIES):
        if ft[i] > cap[i]:
            totalCost += PENALTY * (ft[i] - cap[i])

    return -totalCost 

def select(population, fitnesses):
    total_fit = sum(fitnesses)
    pick = random.uniform(0, total_fit)
    current = 0
    for ch, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return ch
    return population[-1]

def crossover(p1, p2):
    if random.random() > CROSSOVER_RATE:
        return p1[:], p2[:]
    point = random.randint(1, NUM_TASKS - 2)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

def mutate(ch):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(NUM_TASKS), 2)
        ch[i], ch[j] = ch[j], ch[i]
    return ch

def genetic_algorithm(generations=50):
    population = [generate() for _ in range(POP_SIZE)]

    for gen in range(generations):
        fitnesses = [fitness(c) for c in population]
        new_pop = []

        while len(new_pop) < POP_SIZE:
            p1 = select(population, fitnesses)
            p2 = select(population, fitnesses)
            c1, c2 = crossover(p1, p2)
            new_pop.append(mutate(c1))
            if len(new_pop) < POP_SIZE:
                new_pop.append(mutate(c2))

        population = new_pop

    best = max(population, key=fitness)
    best_cost = -fitness(best)
    return best, best_cost

best_solution, best_cost = genetic_algorithm()
print("Best Task Assignment:", best_solution)
print("Total Cost:", best_cost)
```

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
### Question 3:

```py
import time
import itertools
from ortools.sat.python import cp_model

def parse_grid(grid):
    digits = '123456789'
    return {i: digits if grid[i] == '.' else grid[i] for i in range(81)}

def create_constraints():
    units = []
    for i in range(9):
        units.append([i * 9 + j for j in range(9)])  
        units.append([i + j * 9 for j in range(9)]) 
    for i in range(3):
        for j in range(3):
            units.append([9 * (i * 3 + k) + j * 3 + l for k in range(3) for l in range(3)])

    peers = {i: set(itertools.chain(*[u for u in units if i in u])) - {i} for i in range(81)}
    return units, peers

def AC3(values, peers):
    queue = [(x, y) for x in range(81) for y in peers[x] if len(values[x]) == 1]
    while queue:
        x, y = queue.pop(0)
        if len(values[y]) > 1 and values[x] in values[y]:
            values[y] = values[y].replace(values[x], '')
            if len(values[y]) == 0:
                return None
            if len(values[y]) == 1:
                queue.extend((y, p) for p in peers[y])
    return values

def backtracking(values, peers):
    if values is None:
        return None 
    if all(len(values[i]) == 1 for i in range(81)):
        return values
    
    s = min((i for i in range(81) if len(values[i]) > 1), key=lambda x: len(values[x]))
    for d in values[s]:
        new_values = values.copy()
        new_values[s] = d
        new_values = AC3(new_values, peers)
        result = backtracking(new_values, peers)
        if result:
            return result
    return None

def sudoku_solver(grid):
    values = parse_grid(grid)
    _, peers = create_constraints()
    values = AC3(values, peers)
    return backtracking(values, peers)

def google_sudoku_solver(grid):
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    cells = [[model.NewIntVar(1, 9, f'cell_{i}_{j}') for j in range(9)] for i in range(9)]

    for i in range(9):
        model.AddAllDifferent(cells[i])
        model.AddAllDifferent([cells[j][i] for j in range(9)])
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            model.AddAllDifferent([cells[x][y] for x in range(i, i+3) for y in range(j, j+3)])
    for i, val in enumerate(grid):
        if val != '.':
            model.Add(cells[i // 9][i % 9] == int(val))

    status = solver.Solve(model)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        return [[solver.Value(cells[i][j]) for j in range(9)] for i in range(9)]
    return None

def chatgpt_sudoku_solver(grid):
    values = parse_grid(grid)
    _, peers = create_constraints()

    def assign(values, s, d):
        values[s] = d
        for p in peers[s]:
            if d in values[p]:
                values[p] = values[p].replace(d, '')
                if len(values[p]) == 0:
                    return None
        return values

    def search(values):
        if values is None:
            return None
        if all(len(values[i]) == 1 for i in range(81)):
            return values
        s = min((i for i in range(81) if len(values[i]) > 1), key=lambda x: len(values[x]))
        for d in values[s]:
            new_values = assign(values.copy(), s, d)
            result = search(new_values)
            if result:
                return result
        return None

    return search(values)

def conclusion(grid):
    values = {i: '123456789' if grid[i] == '.' else grid[i] for i in range(81)}
    units = []
    for i in range(9):
        units.append([i * 9 + j for j in range(9)])  
        units.append([i + j * 9 for j in range(9)])  
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            units.append([(i + k) * 9 + (j + l) for k in range(3) for l in range(3)])
    peers = {i: set().union(*[set(u) for u in units if i in u]) - {i} for i in range(81)}

    def eliminate(values):
        for s in range(81):
            if len(values[s]) == 1:
                d = values[s]
                for p in peers[s]:
                    if d in values[p]:
                        values[p] = values[p].replace(d, '')
                        if len(values[p]) == 0:
                            return None
        return values

    def only_choice(values):
        for unit in units:
            for d in '123456789':
                dplaces = [s for s in unit if d in values[s]]
                if len(dplaces) == 1:
                    if len(values[dplaces[0]]) > 1:
                        values[dplaces[0]] = d
        return values

    def reduce_puzzle(values):
        stalled = False
        while not stalled:
            before = sum(len(values[s]) for s in range(81))
            values = eliminate(values)
            if values is None: return None
            values = only_choice(values)
            after = sum(len(values[s]) for s in range(81))
            stalled = before == after
        return values

    def search(values):
        values = reduce_puzzle(values)
        if values is None:
            return None
        if all(len(values[i]) == 1 for i in range(81)):
            return values
    
        s = min((i for i in range(81) if len(values[i]) > 1), key=lambda x: len(values[x]))
        for d in values[s]:
            new_values = values.copy()
            new_values[s] = d
            attempt = search(new_values)
            if attempt:
                return attempt
        return None

    return search(values)

def read(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def write(filename, solutions):
    with open(filename, 'a') as file:
        file.write('\nSolutions:\n')
        for sol in solutions:
            file.write(sol + '\n')

filename = "output.txt"
puzzles = read(filename)
solutions = []

for i, puzzle in enumerate(puzzles):
    solutions.append(f"\nPuzzle {i + 1}: ")

    try:
        start = time.time()
        result = sudoku_solver(puzzle)
        end = time.time()
        flat = ''.join(result[i] for i in range(81)) if result else "Failed"
        solutions.append(f"Human Based CSP: {flat} | Time: {end - start:.5f}s")
    except Exception as e:
        solutions.append(f"Human Based CSP: Error! {str(e)}")

    try:
        start = time.time()
        result = google_sudoku_solver(puzzle)
        end = time.time()
        flat = ''.join(str(num) for row in result for num in row) if result else "Failed"
        solutions.append(f"Google OR-Tools: {flat} | Time: {end - start:.5f}s")
    except Exception as e:
        solutions.append(f"Google OR-Tools: Error! {str(e)}")

    try:
        start = time.time()
        result = chatgpt_sudoku_solver(puzzle)
        end = time.time()
        flat = ''.join(result[i] for i in range(81)) if result else "Failed"
        solutions.append(f"GPT Based Solver: {flat} | Time: {end - start:.5f}s")
    except Exception as e:
        solutions.append(f"GPT Based Solver: Error! {str(e)}")

    try:
        start = time.time()
        result = conclusion(puzzle)
        end = time.time()
        flat = ''.join(result[i] for i in range(81)) if result else "Failed"
        solutions.append(f"Human Based Revised: {flat} | Time: {end - start:.5f}s")
    except Exception as e:
        solutions.append(f"Human Based Revised: Error! {str(e)}")

write(filename, solutions)
```

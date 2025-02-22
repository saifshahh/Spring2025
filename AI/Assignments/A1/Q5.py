import heapq

# graph of map with distances
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# heuristic list
heuristic = {'Arad': 366, 
             'Bucharest': 0, 
             'Craiova': 160, 
             'Drobeta': 242, 
             'Eforie': 161, 
             'Fagaras': 176, 
             'Giurgiu': 77, 
             'Hirsova': 151, 
             'Iasi': 226, 
             'Lugoj': 244, 
             'Mehadia': 241, 
             'Neamt': 234, 
             'Oradea': 380, 
             'Pitesti': 100, 
             'Rimnicu Vilcea': 193, 
             'Sibiu': 253, 
             'Timisoara': 329, 
             'Urziceni': 80, 
             'Vaslui': 199, 
             'Zerind': 374 }

# breadth first search
def bfs(start, goal):
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

# uniform cost search
def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        visited.add(node)
        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return None

# greedy best first search
def gbfs(start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]
    visited = set()
    
    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        visited.add(node)
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

# helper function for iterative deep depth first search
def dls(node, goal, depth, path, visited):
    if depth < 0:
        return None
    if node == goal:
        return path
    visited.add(node)
    for neighbor in graph.get(node, {}):
        if neighbor not in visited:
            result = dls(neighbor, goal, depth - 1, path + [neighbor], visited)
            if result:
                return result
    return None

# iterative deeeping depth first search
def iddfs(start, goal, max_depth=20):
    for depth in range(max_depth):
        visited = set()
        result = dls(start, goal, depth, [start], visited)
        if result:
            return result
    return None


# driver code
start, goal = 'Arad', 'Bucharest'
print("BFS Path:", bfs(start, goal))
print("UCS Path and Cost:", ucs(start, goal))
print("Greedy Best First Path:", gbfs(start, goal, heuristic))
print("IDDFS Path:", iddfs(start, goal))

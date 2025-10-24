#experiment 4
import heapq

# Step 1: Define the graph (adjacency list)
graph = {
    'A': ['B', 'D'],
    'B': ['E', 'G'],
    'D': ['G', 'H'],
    'G': ['I'],
    'H': ['I'],
    'E': [],
    'I': []
}

# Step 2: Define heuristic values (h(n))
heuristic = {
    'A': 999,
    'B': 5,
    'D': 2,
    'E': 4,
    'G': 6,
    'H': 1,
    'I': 0
}

# Step 3: Uniform edge cost (used in A*)
edge_cost = 1

def greedy_bfs(start, goal):
    print("---------------------------------")
    print("Greedy Best-First Search:")
    print("---------------------------------")
    
    priority_queue = [(heuristic[start], start)]
    visited = set()
    path_trace = {start: None}
    visiting_order = []
    
    while priority_queue:
        current_h, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        visiting_order.append(current_node)
        
        if current_node == goal:
            print("Goal reached!")
            break
            
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                path_trace[neighbor] = current_node
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
    
    print("Visiting order:", " -> ".join(visiting_order))
    
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = path_trace.get(node)
    path.reverse()
    
    if path[0] == start:
        print("Final path:", " -> ".join(path))
    else:
        print("Path not found.")
        
    print()

def a_star(start, goal):
    print("---------------------------------")
    print("A* Search:")
    print("---------------------------------")
    
    priority_queue = [(0 + heuristic[start], 0, start)]
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    path_trace = {start: None}
    visited = set()
    visiting_order = []
    
    while priority_queue:
        f_cost, current_g, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue

        visited.add(current_node)
        visiting_order.append(current_node)

        if current_node == goal:
            print("Goal reached!")
            break
        
        for neighbor in graph.get(current_node, []):
            new_g_cost = g_costs[current_node] + edge_cost
            
            if new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                f_cost_neighbor = new_g_cost + heuristic[neighbor]
                path_trace[neighbor] = current_node
                heapq.heappush(priority_queue, (f_cost_neighbor, new_g_cost, neighbor))

    print("Visiting order:", " -> ".join(visiting_order))
    
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = path_trace.get(node)
    path.reverse()
    
    if path[0] == start:
        print("Final path:", " -> ".join(path))
    else:
        print("Path not found.")
        
    print()

start_node = 'A'
goal_node = 'I'

greedy_bfs(start_node, goal_node)
a_star(start_node, goal_node)
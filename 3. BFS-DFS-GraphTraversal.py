# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start_node):
    """
    Performs a Depth-First Search (DFS) on the given graph.
    Args:
        graph (dict): The graph represented as an adjacency list.
        start_node: The starting node for the traversal.
    Returns:
        list: A list of nodes in the order they were visited.
    """
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        node = stack.pop()  # Pop from the end (LIFO)
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            # Add unvisited neighbors to the stack in reverse order
            # to process them in the desired order (e.g., left to right)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return traversal_order

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search (BFS) on the given graph.
    Args:
        graph (dict): The graph represented as an adjacency list.
        start_node: The starting node for the traversal.
    Returns:
        list: A list of nodes in the order they were visited.
    """
    visited = set()
    queue = [start_node]  # Use a list as a queue (pop(0) for FIFO)
    traversal_order = []

    while queue:
        node = queue.pop(0)  # Pop from the beginning (FIFO)
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return traversal_order

# Driver Code
print("DFS Traversal:", dfs(graph, 'A'))
print("BFS Traversal:", bfs(graph, 'A'))
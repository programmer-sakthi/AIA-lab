import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a directed graph
G = nx.DiGraph()

# Step 2: Add nodes and labeled edges (relationships)
G.add_edges_from([
    ("Computer", "Machine", {"label": "is-a"}),
    ("Computer", "CPU", {"label": "has-a"}),
    ("CPU", "ALU", {"label": "has-a"}),
    ("CPU", "Control Unit", {"label": "has-a"}),
    ("Computer", "Monitor", {"label": "has-a"}),
    ("Monitor", "Output Device", {"label": "is-a"}),
    ("Computer", "Keyboard", {"label": "has-a"}),
    ("Keyboard", "Input Device", {"label": "is-a"}),
    ("Machine", "Thing", {"label": "is-a"})
])

# Step 3: Define layout for nodes
pos = nx.spring_layout(G, seed=42)  # 'seed' ensures consistent layout

# Step 4: Draw nodes and edges
nx.draw(
    G, pos, with_labels=True, node_color='lightgreen',
    node_size=2500, font_weight='bold', arrows=True
)

# Step 5: Draw edge labels
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=nx.get_edge_attributes(G, 'label'),
    font_color='blue'
)

# Step 6: Display the graph
plt.axis('off')
plt.title("Semantic Network", fontsize=14, fontweight='bold')
plt.show()
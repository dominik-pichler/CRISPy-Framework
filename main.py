import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# Define nodes
nodes = [
    Node(id="Node 1", label="Node 1", size=25, color="#00ff1e"),
    Node(id="Node 2", label="Node 2", size=15, color="#ff5733"),
    Node(id="Node 3", label="Node 3", size=20, color="#3355ff"),
]

# Define edges
edges = [
    Edge(source="Node 1", target="Node 2", label="Edge 1-2"),
    Edge(source="Node 2", target="Node 3", label="Edge 2-3"),
    Edge(source="Node 3", target="Node 1", label="Edge 3-1"),
]

# Configure the graph
config = Config(
    width=800,
    height=600,
    directed=True,  # Set to False if you want an undirected graph
    nodeHighlightBehavior=True,
    highlightColor="#F7A7A6",  # Color of the highlighted node
    collapsible=True,
)

# Streamlit app layout
st.title("Knowledge Graph Visualization with Streamlit")
st.write("This is a simple example of a knowledge graph using Streamlit and Agraph.")

# Render the graph
agraph(nodes=nodes, edges=edges, config=config)

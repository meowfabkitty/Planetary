"""
nodes.node

Minimal node runtime scaffolding.
"""

class Node:
    """Represent a physical or virtual node in the Planetary network.

    Responsibilities:
    - expose local status and health
    - accept configuration from authorized controllers
    - run local autonomy loops
    """

    def __init__(self, node_id: str, profile: dict = None):
        self.node_id = node_id
        self.profile = profile or {}
        self.status = "initializing"

    def start(self):
        """Start node services (placeholder)."""
        self.status = "running"

    def stop(self):
        """Stop node services (placeholder)."""
        self.status = "stopped"


if __name__ == "__main__":
    n = Node("node-001")
    n.start()
    print(f"Node {n.node_id} is {n.status}")

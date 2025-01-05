class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
    
        self.children.append(child_node)

    def remove_child(self, child_data):

        self.children = [child for child in self.children if child.data != child_data]

    def display(self, level=0):
    
        print(" " * (level * 4) + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

class AirlineReservationTree:

    def __init__(self):
        self.root = TreeNode("Airline Reservation System")

    def add_hierarchy(self, parent_data, child_data):
  
        parent_node = self.find_node(self.root, parent_data)
        if parent_node:
            parent_node.add_child(TreeNode(child_data))
        else:
            print(f"Parent node '{parent_data}' not found.")

    def find_node(self, current_node, target_data):
     
        if current_node.data == target_data:
            return current_node

        for child in current_node.children:
            result = self.find_node(child, target_data)
            if result:
                return result

        return None

    def display_tree(self):
       
        self.root.display()


if __name__ == "__main__":
    tree = AirlineReservationTree()

   
    tree.add_hierarchy("Airline Reservation System", "Flights")
    tree.add_hierarchy("Flights", "Domestic")
    tree.add_hierarchy("Flights", "International")
    tree.add_hierarchy("Domestic", "Flight 101")
    tree.add_hierarchy("Domestic", "Flight 102")
    tree.add_hierarchy("International", "Flight 201")
    tree.add_hierarchy("International", "Flight 202")
    tree.add_hierarchy("Airline Reservation System", "Passengers")
    tree.add_hierarchy("Passengers", "Economy")
    tree.add_hierarchy("Passengers", "Business")

    print("\nHierarchical Structure:")
    tree.display_tree()

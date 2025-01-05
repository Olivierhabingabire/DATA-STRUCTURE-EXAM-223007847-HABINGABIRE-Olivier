class Node:
   
    def __init__(self, ticket_number, passenger_name):
        self.ticket_number = ticket_number
        self.passenger_name = passenger_name
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, ticket_number, passenger_name):
        def _insert_recursive(current, ticket_number, passenger_name):
            if current is None:
                return Node(ticket_number, passenger_name)
            if ticket_number < current.ticket_number:
                current.left = _insert_recursive(current.left, ticket_number, passenger_name)
            elif ticket_number > current.ticket_number:
                current.right = _insert_recursive(current.right, ticket_number, passenger_name)
            return current

        self.root = _insert_recursive(self.root, ticket_number, passenger_name)

    def search(self, ticket_number):
        def _search_recursive(current, ticket_number):
            if current is None or current.ticket_number == ticket_number:
                return current
            if ticket_number < current.ticket_number:
                return _search_recursive(current.left, ticket_number)
            return _search_recursive(current.right, ticket_number)

        return _search_recursive(self.root, ticket_number)

    def inorder_traversal(self):
        def _inorder_recursive(current):
            if current is not None:
                _inorder_recursive(current.left)
                print(f"Ticket Number: {current.ticket_number}, Passenger Name: {current.passenger_name}")
                _inorder_recursive(current.right)

        _inorder_recursive(self.root)

class DLLNode:
   
    def __init__(self, ticket_number, passenger_name):
        self.ticket_number = ticket_number
        self.passenger_name = passenger_name
        self.next = None
        self.prev = None

class DoublyLinkedList:
 
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, ticket_number, passenger_name):
        new_node = DLLNode(ticket_number, passenger_name)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(f"Ticket Number: {current.ticket_number}, Passenger Name: {current.passenger_name}")
            current = current.next

    def display_backward(self):
        current = self.tail
        while current:
            print(f"Ticket Number: {current.ticket_number}, Passenger Name: {current.passenger_name}")
            current = current.prev


if __name__ == "__main__":
  
    bst = BinarySearchTree()
    bst.insert(1001, "Bahati")
    bst.insert(1002, "olivier")
    bst.insert(1000, "Charlie")
    bst.insert(1003, "iradukunda")
    print("\nInorder Traversal of BST:")
    bst.inorder_traversal()

    search_result = bst.search(1001)
    if search_result:
        print(f"\nFound: Ticket Number {search_result.ticket_number}, Passenger Name {search_result.passenger_name}")
    else:
        print("\nTicket not found.")


    dll = DoublyLinkedList()
    dll.append(1001, "Bahati")
    dll.append(1002, "olivier")
    dll.append(1000, "Charlie")
    dll.append(1003, "iradukunda")

    print("\nDisplaying Doubly Linked List Forward:")
    dll.display_forward()

    print("\nDisplaying Doubly Linked List Backward:")
    dll.display_backward()

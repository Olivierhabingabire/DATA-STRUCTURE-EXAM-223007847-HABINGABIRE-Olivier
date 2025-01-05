class DLLNode:
  
    def __init__(self, ticket_number, passenger_name):
        self.ticket_number = ticket_number
        self.passenger_name = passenger_name
        self.next = None
        self.prev = None

class FixedSizeDoublyLinkedList:

    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    def append(self, ticket_number, passenger_name):
        
        new_node = DLLNode(ticket_number, passenger_name)

        if self.size == self.max_size:
        
            self.remove_oldest()

        if self.head is None:
          
            self.head = self.tail = new_node
        else:
         
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def remove_oldest(self):
     
        if self.head is None:
            print("List is already empty.")
            return

        removed_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
        
            self.tail = None

        self.size -= 1
        print(f"Removed Oldest: Ticket Number {removed_node.ticket_number}, Passenger Name {removed_node.passenger_name}")

    def display(self):
        """Display all orders in the list."""
        current = self.head
        if not current:
            print("List is empty.")
            return

        print("Current Orders:")
        while current:
            print(f"Ticket Number: {current.ticket_number}, Passenger Name: {current.passenger_name}")
            current = current.next


if __name__ == "__main__":
    max_orders = 3
    dll = FixedSizeDoublyLinkedList(max_orders)


    dll.append(1001, "Bahati")
    dll.append(1002, "olivier")
    dll.append(1003, "dior")
    print("\nAfter adding 3 orders:")
    dll.display()


    dll.append(1004, "Diana")
    print("\nAfter adding 4th order (oldest removed):")
    dll.display()

   
    dll.append(1005, "ihimbazwe")
    print("\nAfter adding 5th order (oldest removed):")
    dll.display()

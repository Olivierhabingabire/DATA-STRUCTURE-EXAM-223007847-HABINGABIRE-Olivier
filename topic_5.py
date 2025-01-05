class SLLNode:
   
    def __init__(self, ticket_number, passenger_name):
        self.ticket_number = ticket_number
        self.passenger_name = passenger_name
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def add_reservation(self, ticket_number, passenger_name):
       
        new_node = SLLNode(ticket_number, passenger_name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_reservation(self, ticket_number):
     
        if self.head is None:
            print("No reservations to remove.")
            return

        if self.head.ticket_number == ticket_number:
            removed_node = self.head
            self.head = self.head.next
            print(f"Removed: Ticket Number {removed_node.ticket_number}, Passenger Name {removed_node.passenger_name}")
            return

        current = self.head
        while current.next and current.next.ticket_number != ticket_number:
            current = current.next

        if current.next is None:
            print("Reservation not found.")
        else:
            removed_node = current.next
            current.next = current.next.next
            print(f"Removed: Ticket Number {removed_node.ticket_number}, Passenger Name {removed_node.passenger_name}")

    def display_reservations(self):
      
        if self.head is None:
            print("No reservations to display.")
            return

        current = self.head
        print("Current Reservations:")
        while current:
            print(f"Ticket Number: {current.ticket_number}, Passenger Name: {current.passenger_name}")
            current = current.next


if __name__ == "__main__":
    sll = SinglyLinkedList()

  
    sll.add_reservation(1001, "Bahati")
    sll.add_reservation(1002, "olivier")
    sll.add_reservation(1003, "dior")

    print("\nAfter adding reservations:")
    sll.display_reservations()

    sll.remove_reservation(1002)
    print("\nAfter removing reservation with ticket number 1002:")
    sll.display_reservations()

  
    sll.remove_reservation(2000)

  
    sll.add_reservation(1004, "bukayo")
    print("\nAfter adding another reservation:")
    sll.display_reservations()

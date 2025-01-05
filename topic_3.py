class QueueNode:
   
    def __init__(self, ticket_number, passenger_name):
        self.ticket_number = ticket_number
        self.passenger_name = passenger_name
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, ticket_number, passenger_name):
        
        new_node = QueueNode(ticket_number, passenger_name)
        if self.rear is None:
       
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
       
        if self.front is None:
            print("Queue is empty. No reservations to process.")
            return None
        removed_node = self.front
        self.front = self.front.next
        if self.front is None:
        
            self.rear = None
        return removed_node

    def display(self):
 
        if self.front is None:
            print("Queue is empty.")
            return
        current = self.front
        while current:
            print(f"Ticket Number: {current.ticket_number}, Passenger Name: {current.passenger_name}")
            current = current.next

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1001, "BAHATI")
    queue.enqueue(1002, "OLIVIER")
    queue.enqueue(1003, "DIOR")

    print("\nQueue after enqueuing reservations:")
    queue.display()

    print("\nProcessing reservations:")
    processed = queue.dequeue()
    while processed:
        print(f"Processed Ticket Number: {processed.ticket_number}, Passenger Name: {processed.passenger_name}")
        processed = queue.dequeue()

    print("\nQueue after processing all reservations:")
    queue.display()

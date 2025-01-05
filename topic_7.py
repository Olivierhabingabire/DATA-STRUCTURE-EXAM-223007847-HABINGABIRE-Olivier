class Reservation:
   
    def __init__(self, ticket_number, passenger_name, priority):
        self.ticket_number = ticket_number
        self.passenger_name = passenger_name
        self.priority = priority

    def __repr__(self):
        return f"Ticket: {self.ticket_number}, Name: {self.passenger_name}, Priority: {self.priority}"

class ReservationSystem:

    def __init__(self):
        self.reservations = []

    def add_reservation(self, ticket_number, passenger_name, priority):
       
        self.reservations.append(Reservation(ticket_number, passenger_name, priority))

    def sort_by_priority(self):
        
        for i in range(1, len(self.reservations)):
            key = self.reservations[i]
            j = i - 1
            while j >= 0 and self.reservations[j].priority > key.priority:
                self.reservations[j + 1] = self.reservations[j]
                j -= 1
            self.reservations[j + 1] = key

    def display_reservations(self):
       
        for reservation in self.reservations:
            print(reservation)


if __name__ == "__main__":
    system = ReservationSystem()

    system.add_reservation(1001, "Bahati", 2)
    system.add_reservation(1002, "olivier", 1)
    system.add_reservation(1003, "dior", 3)
    system.add_reservation(1004, "grace", 1)

    print("\nReservations before sorting:")
    system.display_reservations()

 
    system.sort_by_priority()

    print("\nReservations after sorting by priority:")
    system.display_reservations()

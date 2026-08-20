class Passenger:
    next_id = 1

    def __init__(self, passenger_name, destination, seat_number=None):
        self.ticket_id = Passenger.next_id
        Passenger.next_id += 1

        self.passenger_name = passenger_name
        self.destination = destination
        self.seat_number = seat_number

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Passenger: {self.passenger_name}, Destination: {self.destination}, Seat: {self.seat_number}"

class BookingSystem:

    def __init__(self):
        self.bookings = []

    def book_ticket(self, passenger_name, destination, seat_number=None):
        passenger = Passenger(passenger_name, destination, seat_number)
        self.bookings.append(passenger)
        print("Ticket booked successfully.")
    def view_bookings(self):
        for passenger in self.bookings:
            print(passenger)
    def search_ticket(self, ticket_id):
        for passenger in self.bookings:
            if passenger.ticket_id == ticket_id:
                print(passenger)
                return
        print("Ticket not found.")

    def update_booking(self, ticket_id, new_seat, new_destination):
        for passenger in self.bookings:
            if passenger.ticket_id == ticket_id:
                passenger.seat_number = new_seat
                passenger.destination = new_destination
                print("Booking updated successfully.")
                return
        print("Ticket not found.")

    def cancel_ticket(self, ticket_id):
        for passenger in self.bookings:
            if passenger.ticket_id == ticket_id:
                self.bookings.remove(passenger)
                print("Ticket cancelled successfully.")
                return
        print("Ticket not found.")


booking = BookingSystem()

booking.book_ticket("Hasan", "Osaka", "A1")

booking.book_ticket("Mim", "Kyoto")

booking.book_ticket("Farhan", "Tokyo", "B3")

booking.view_bookings()

print("\n-- Search --")

booking.search_ticket(2)

print("\n-- Update --")

booking.update_booking(3, "C5", "Nagoya")

print("\n-- Cancel --")

booking.cancel_ticket(2)

booking.view_bookings()

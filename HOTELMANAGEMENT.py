class Hotel:
    def __init__(self, name, rooms, location, rating, price_per_room):
        self.name = name
        self.rooms = rooms
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room

    def book_rooms(self, num_rooms):
        if self.rooms >= num_rooms:
            total_cost = num_rooms * self.price_per_room
            self.rooms -= num_rooms
            return total_cost
        else:
            return -1  # Not enough rooms available

    def __repr__(self):
        return f"{self.name} | Location: {self.location} | Rating: {self.rating} | Rooms Available: {self.rooms} | Price Per Room: {self.price_per_room}"


class Booking:
    def __init__(self, booking_id, user_name, hotel_name, num_rooms, total_cost):
        self.booking_id = booking_id
        self.user_name = user_name
        self.hotel_name = hotel_name
        self.num_rooms = num_rooms
        self.total_cost = total_cost

    def __repr__(self):
        return f"Booking ID: {self.booking_id} | User: {self.user_name} | Hotel: {self.hotel_name} | Rooms Booked: {self.num_rooms} | Total Cost: {self.total_cost}"


def hotel_management():
    # Predefined hotel data
    hotels = [
        Hotel("HotelA", 10, "Delhi", 4.5, 2000),
        Hotel("HotelB", 5, "Mumbai", 4.8, 3000),
        Hotel("HotelC", 8, "Bangalore", 4.2, 1500),
        Hotel("HotelD", 12, "Pune", 4.7, 1800),
        Hotel("HotelE", 15, "Chennai", 4.0, 2200),
        Hotel("HotelF", 7, "Kolkata", 3.9, 2500),
        Hotel("HotelG", 6, "Hyderabad", 4.4, 2700),
        Hotel("HotelH", 9, "Jaipur", 4.6, 1900),
        Hotel("HotelI", 4, "Ahmedabad", 4.3, 1600),
        Hotel("HotelJ", 11, "Lucknow", 4.1, 2100),
    ]

    # List to store bookings
    bookings = []

    print("Welcome to the Hotel Management System!")
    while True:
        print("\nAvailable Hotels:")
        for i, hotel in enumerate(hotels, 1):
            print(f"{i}. {hotel}")
        
        # Select a hotel
        try:
            hotel_choice = int(input("\nEnter the hotel number to book a room (0 to exit): "))
            if hotel_choice == 0:
                break
            if hotel_choice < 1 or hotel_choice > len(hotels):
                print("Invalid choice! Please try again.")
                continue

            selected_hotel = hotels[hotel_choice - 1]

            # Check room availability
            print(f"\nYou selected: {selected_hotel}")
            num_rooms = int(input(f"Enter the number of rooms to book (Available: {selected_hotel.rooms}): "))
            
            if num_rooms <= 0:
                print("Invalid number of rooms. Please try again.")
                continue

            # Calculate cost and process booking
            cost = selected_hotel.book_rooms(num_rooms)
            if cost == -1:
                print("Sorry, not enough rooms are available!")
            else:
                user_name = input("Enter your name: ")
                booking_id = len(bookings) + 1
                bookings.append(Booking(booking_id, user_name, selected_hotel.name, num_rooms, cost))
                print(f"Booking successful! Total cost: {cost}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Display all bookings
    print("\nAll Bookings:")
    for booking in bookings:
        print(booking)

    print("\nThank you for using the Hotel Management System!")


# Driver Code
if __name__ == "__main__":
    hotel_management()

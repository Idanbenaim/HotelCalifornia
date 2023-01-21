"""this module bridges between the front end
and the back end in the Hotel_manage_sys package"""
import re
import datetime
import random
import json
import Hotel_manage_sys.rooms_module as rm
import Hotel_manage_sys.customers_module as cm
import Hotel_manage_sys.bookings_module as bm


### Files ###
room_types_list = '../database/room_types_list.json'


### files-End ###
def main_menu():
    """"""
    while True:
        print("\n****************************************************")
        print("   Welcome to Hotel California Management System!")
        print("****************************************************\n")
        print("What would you like to do?\n")
        print("1. Add a new room")
        print("2. Add a new customer")
        print("3. Book a room")
        print("4. Cancel booking")
        print("5. Display all rooms")
        print("6. Display all customers")
        print("7. Display all bookings")
        print("8. Display booked rooms for a specific date")
        print("9. Display available rooms for a specific date")
        print("10. Find room by type")
        print("11. Find room by number")
        print("12. Find customer by name")
        print("13. Remove room")
        print("14. Remove customer")

        main_menu_selection = int(input("\nPlease type the option number (0-14): "))

        if main_menu_selection == 1:
            add_room_cli()
        elif main_menu_selection == 2:
            add_customer_cli()
        elif main_menu_selection == 3:
            book_room_cli()
        elif main_menu_selection == 4:
            remove_booking_cli()
        elif main_menu_selection == 5:
            get_inventory_cli()
            main_menu()
        elif main_menu_selection == 6:
            get_cust_list_cli()
            main_menu()
        elif main_menu_selection == 7:
            get_all_bookings_cli()
            main_menu()
        elif main_menu_selection == 8:
            get_booked_rooms_by_date_cli()
            main_menu()
        elif main_menu_selection == 9:
            get_available_rooms_by_date_cli()
            main_menu()
        elif main_menu_selection == 10:
            get_room_by_type_cli()
            main_menu()
        elif main_menu_selection == 11:
            get_room_by_number_cli()
            main_menu()
        elif main_menu_selection == 12:
            get_cust_by_name_cli()
            main_menu()
        elif main_menu_selection == 13:
            remove_room_cli()
            main_menu()
        elif main_menu_selection == 14:
            remove_cust_cli()
        else:
            print("Option not available. Please enter a valid number between 1-14 from the menu below")
            main_menu()



def get_valid_dates():
    """validates the date format and ensures that the arrival date is not in the past"""
    while True:
        arrival_date = input("Enter arrival date (YYYY-MM-DD) or 'X' to go back to main menu: ")
        if arrival_date.lower() == 'x':
            main_menu()
            break
        departure_date = input("Enter departure date (YYYY-MM-DD) or 'X' to go back to main menu: ")
        if departure_date.lower() == 'x':
            main_menu()
            break
        try:
            arrival_date_input = datetime.datetime.strptime(arrival_date, '%Y-%m-%d')
            departure_date_input = datetime.datetime.strptime(departure_date, '%Y-%m-%d')
            today = datetime.datetime.now()
            if arrival_date_input <= today:
                print("Arrival date can be made only for future dates. Please enter a valid date.")
                continue
            elif arrival_date_input >= departure_date_input:
                print("Arrival date must be prior to the departure date. Please enter the dates again.")
                continue
        except ValueError:
            print("Invalid date format. Please enter the dates in the format YYYY-MM-DD.")
            continue
        break
    return arrival_date, departure_date


### option 1 ###  """add validation for duplicate room numbers"""
def add_room_cli():
    """add validation for duplicate room numbers"""
    room_number = input('Enter room number: ')

    def validate_room_number(room_number):
        """check if room number already exists in inventory"""
        rooms = rm.Rooms.get_inventory()
        duplicate = False
        for room in rooms:
            if room[0] == room_number:
                duplicate = True
                break
        if duplicate:
            print("Room number already exists in inventory. Please enter a unique room number.")
            add_room_cli()

    validate_room_number(room_number)
    print('There are 3 room types:\n 1. Basic\n 2. Deluxe\n 3. Suite')
    room_type = input('Please select room type 1, 2, or 3: ')
    while True:
        try:
            if room_type != '1' and room_type != '2' and room_type != '3':
                raise ValueError("\n****************\n Wrong Value! Please enter 1, 2, or 3.\n****************\n")
        except ValueError as e:
            print(e)  # Print the ValueError message
            print('There are 3 room types.\n 1. Basic\n 2. Deluxe\n 3. Suite')
            room_type = input('Please enter 1, 2, or 3: ')
        else:
            if room_type == '1':
                room_type = 'Basic'
            elif room_type == '2':
                room_type = 'Deluxe'
            elif room_type == '3':
                room_type = 'Suite'
            room_info = [room_number, room_type]
            rm.Rooms.add_room(room_info)
            print('Room Added Successfully')
            break


### option 2 ###
def add_customer_cli():
    """gets the customer information from the user and send it to the backend to be saved in the db"""

    def validate_customer_id(ci):
        """check if customer id already exists in customer list"""
        customers = cm.Customers.get_cust_list()
        duplicate = False
        for cust in customers:
            if cust[0] == ci:
                duplicate = True
                break
        if duplicate:
            print("Customer ID already exists in customer list. Try option 12 to find the customer by name")
            main_menu()

    cust_id = input('Enter customer identification number: ')
    validate_customer_id(cust_id)
    name = input("Enter customer's first and last name: ")
    address = input('Enter customer address: ')
    city = input('Enter customer city: ')
    email = input('Enter customer email: ')
    age = input('Enter customer age: ')

    cust_info = [cust_id, name, address, city, email, age]
    cm.Customers.add_cust(cust_info)
    print('Customer Added Successfully')
    return cust_id  # used in add_booking_cli()


### option 3 ###
def book_room_cli():
    """gets the reservation dates and sets room reservations by room type or by room number """
    rtl = room_types_list

    def book_room_by_type():
        """provides information about the room types of the hotel and takes in a reservation"""
        # get valid dates for booking
        arrival_date, departure_date = get_valid_dates()

        # get available rooms by date
        available_rooms = bm.Bookings.get_available_rooms_by_date(arrival_date, departure_date)

        # count and print number of rooms available for each room type
        room_types = {'Basic': 0, 'Deluxe': 0, 'Suite': 0}
        for room in available_rooms[1:]:
            room_types[room[1]] += 1
        print("Number of rooms available for each type:")
        for room_type, count in room_types.items():
            print(f"{room_type}: {count}")

        # get room information by type
        print_room_types(rtl)

        # get user to choose room type
        print('There are 3 room types:\n 1. Basic\n 2. Deluxe\n 3. Suite')
        room_type = input('Please enter the room type you would like to book (Basic, Deluxe, Suite): ')
        while room_type not in ["Basic", "Deluxe", "Suite"]:
            room_type = input("Invalid room type. Please enter Basic, Deluxe, or Suite: ")

        # confirm available rooms in the selected room type
        if room_types[room_type] == 0:
            print('No available rooms for this type. Please start over.')
            book_room_menu()

        # confirm min nights
        check_min_nights(arrival_date, departure_date, room_type, rtl)

        # set one of the rooms from the selected type for booking
        rooms_of_selected_type = [room[0] for room in available_rooms if room[1] == room_type]
        room_number = random.choice(rooms_of_selected_type)

        # find or create a customer
        cust_id = is_existing_customer()

        # book room
        confirm_booking(cust_id, room_number, arrival_date, departure_date)

    def book_room_by_number():
        """gets the desired room number and takes in a reservation"""
        # get valid dates for booking
        arrival_date, departure_date = get_valid_dates()

        # get available rooms by date
        available_rooms = bm.Bookings.get_available_rooms_by_date(arrival_date, departure_date)

        # get room number
        room_number = input("Please enter the room number you want to book: ")
        room_is_available = False
        for room in available_rooms[1:]:
            if room[0] == room_number:
                room_type = room[1]
                room_is_available = True
                # confirm min nights
                check_min_nights(arrival_date, departure_date, room_type, rtl)
                print("Great, that room is available in the selected dates!")
                break

        if not room_is_available:
            print("Sorry, that room is not available for the selected dates.")
            book_room_menu()

        # confirm min nights
        # check_min_nights(arrival_date, departure_date, room_type, rtl)

        # find or create a customer
        cust_id = is_existing_customer()

        # book room
        confirm_booking(cust_id, room_number, arrival_date, departure_date)

    def print_room_types(room_type_list):
        """prints the content of the json file in an organized way"""
        with open(room_type_list) as json_file:
            room_types_dict = json.load(json_file)

        print('\n*** Here is the information about each room type: ***\n')
        print("Type\tSize\tCapacity\tNumber of Beds\tPrice\tMinimum Nights")
        for room_type, info in room_types_dict.items():
            print("{}\t{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".format(info["Type"], info["size"], info["Capacity"],
                                                                  info["NumberOfBeds"], info["Price"],
                                                                  info["MinNights"]))

    def check_min_nights(arrival_date, departure_date, room_type, room_types_list):
        arrival_date = datetime.datetime.strptime(arrival_date, '%Y-%m-%d')
        departure_date = datetime.datetime.strptime(departure_date, '%Y-%m-%d')
        num_nights = (departure_date - arrival_date).days
        if room_type == 'Deluxe' and num_nights < 2:
            print(f"*** \nThe selected room type requires a minimum stay of 2 nights. \nplease start over.\n***")
            book_room_menu()
        elif room_type == 'Suite' and num_nights < 3:
            print(f"\n*** \nThe selected room type requires a minimum stay of 3 nights. \nplease start over.\n***")
            book_room_menu()
        else:
            pass

    def is_existing_customer():
        """ask if user is an existing customer"""
        is_existing = input("Are you an existing customer? (yes/no): ")
        # if is_existing.lower() == "yes":
        if is_existing.lower() not in ["yes", "no", "y", "n"]:
            print("Invalid answer. Please try again")
            is_existing_customer()
        # if customer exist find customer
        elif is_existing.lower() in ["yes", "y"]:
            get_cust_by_name_cli()
            cust_id = input("\nPlease enter the customer's ID to confirm booking: ")
        # if customer does not exist add customer
        else:

            cust_id = add_customer_cli()
        return cust_id

    def confirm_booking(cust_id, room_number, arrival_date, departure_date):
        """get confirmation from the user to book the room"""
        confirm = input("Do you want to book room {} for dates {} - {}? (yes/no): ".format(room_number, arrival_date,
                                                                                           departure_date))
        if confirm.lower() == "yes":
            booking = bm.Bookings.book_room(cust_id, room_number, arrival_date, departure_date)
            print_booking(booking)
        elif confirm.lower() == "no":
            main_menu()
        else:
            print("Invalid input. Please enter yes or no.")
            confirm_booking(cust_id, room_number, arrival_date, departure_date)

    def print_booking(booking):
        """present booking confirmation"""
        print("\n*****\nBooking confirmation:\n*****\n")
        print(f"Order ID: {booking[0]}")
        print(f"Customer ID: {booking[1]}")
        print(f"Room Number: {booking[2]}")
        print(f"Arrival Date: {booking[3]}")
        print(f"Departure Date: {booking[4]}")
        print(f"Cost per Night: {booking[5]}")
        print(f"Total Cost: {booking[6]}")

    def book_room_menu():
        """provides a menu options of reservation ways"""
        while True:
            print("\nWhat would you like to do now?\n")
            print("1. book a room by type")
            print("2. Book a room by room number")
            print("3. Back to Main Menu")

            book_room_selection = int(input("\nPlease type the option number (1-3): "))

            if book_room_selection == 1:
                book_room_by_type()
                main_menu()
            elif book_room_selection == 2:
                book_room_by_number()
            elif book_room_selection == 3:
                main_menu()
            else:
                print("Option not available. Please enter a valid number between 1-3 from the menu below")
                book_room_cli()

    book_room_menu()


### option 4 ###
def remove_booking_cli():
    """gets the reservation details from the user and cancels the booking"""

    def remove_booking(booking_id):
        """sends an api call to the back end to remove the reservation"""
        bm.Bookings.remove_booking(booking_id)
        print(f"Booking with ID {booking_id} has been cancelled.")

    def get_matching_bookings(customer_id, arrival_date, departure_date):
        """gets all bookings from the provided dates and compare them to the customer ID"""
        booked_rooms = bm.Bookings.get_booked_rooms_by_date(arrival_date, departure_date)
        return [booking for booking in booked_rooms if booking[1] == customer_id]

    def print_matching_bookings(bookings):
        """prints all possible bookings to help the user decide which to remove"""
        print("Below are the future bookings for the selected customer:")
        print("BOOKING ID| Customer ID| Room Number| Arrival Date| Departure Date| Cost per Night| Order Total Cost")
        for room in bookings:
            print("{}\t\t| {}\t\t| {}\t\t| {}\t| {}\t| {}\t\t\t| {}".format(room[0], room[1], room[2], room[3], room[4],
                                                                            room[5], room[6]))

    def confirm_remove_booking(booking_id):
        """get the list of bookings, confirm the validity of the booking ID, then remove the booking"""
        bookings_list = bm.Bookings.get_all_bookings()
        booking_ids = [reservation[0] for reservation in bookings_list]
        if booking_id in booking_ids:
            bm.Bookings.remove_booking(booking_id)
            print(f"Booking with ID {booking_id} has been cancelled.")
        else:
            print("Booking Id not on file, please try again.")
            remove_booking_cli()

    booking_id = input("Enter the Booking ID (or 'N' if you don't know it): ")
    if booking_id.lower() == 'n':
        customers = get_cust_by_name_cli()
        customer_id = input("Enter the customer ID of the customer whose booking you wish to cancel: ")
        arrival_date, departure_date = get_valid_dates()
        booked_rooms = get_matching_bookings(customer_id, arrival_date, departure_date)
        if booked_rooms:
            print_matching_bookings(booked_rooms)
            booking_id = input("Enter the booking ID of the booking you wish to cancel: ")
            confirm_remove_booking(booking_id)
        else:
            print("No matching bookings for this customer in the selected time window.")
            main_menu()
    else:
        confirm_remove_booking(booking_id)


### option 5 ###
def get_inventory_cli():
    """calls the Hotel_manage_sys package > rooms_module.py > Rooms class > get_room_by_number() function and gets back the room info list from the csv"""
    rooms = rm.Rooms.get_inventory()
    print("List of rooms:")
    print("Room Number | room Type")
    for room in rooms[1:]:
        print("\t{}\t\t| {}\t\t".format(room[0], room[1]))


### option 6 ###
def get_cust_list_cli():
    """calls the Hotel_manage_sys package > customers_module.py > Customers class > get_cust_list() function and gets back the customer list"""
    customers = cm.Customers.get_cust_list()
    print("customer list:")
    print("Customer ID |  Full Name  |    Address    |  City  |    Email    |   Age")
    for cust in customers[1:]:
        print("{}\t\t| {}\t\t | {}\t| {}\t| {}\t| {}\t\t\t".format(cust[0], cust[1], cust[2], cust[3],
                                                                       cust[4], cust[5]))



### option 7 ###
def get_all_bookings_cli():
    """presents to the user the entire booking list"""
    booked_rooms = bm.Bookings.get_all_bookings()
    print("Booked Rooms in the specified date range:")
    print("Order ID| Customer ID| Room Number| Arrival Date| Departure Date| Cost per Night| Order Total Cost")
    for room in booked_rooms:
        print("{}\t\t| {}\t\t | {}\t\t  | {}\t| {}\t| {}\t\t\t| {}".format(room[0], room[1], room[2], room[3],
                                                                           room[4], room[5], room[6]))


### option 8 ###
def get_booked_rooms_by_date_cli():
    """presents to the user the booking list in the desired time frame"""
    arrival_date, departure_date = get_valid_dates()
    booked_rooms = bm.Bookings.get_booked_rooms_by_date(arrival_date, departure_date)
    if booked_rooms:
        print("Booked Rooms in the specified date range:")
        print("Order ID| Customer ID| Room Number| Arrival Date| Departure Date| Cost per Night| Order Total Cost")
        for room in booked_rooms:
            print("{}\t\t| {}\t\t | {}\t\t  | {}\t| {}\t| {}\t\t\t| {}".format(room[0], room[1], room[2], room[3],
                                                                               room[4], room[5], room[6]))
    else:
        print("No rooms were booked in the specified date range.")
    # break
    return booked_rooms


### option 9 ###
def get_available_rooms_by_date_cli():
    """presents to the user the list of available rooms in the desired time frame"""
    arrival_date, departure_date = get_valid_dates()
    available_rooms = bm.Bookings.get_available_rooms_by_date(arrival_date, departure_date)
    if available_rooms:
        print("Available Rooms in the specified date range:")
        print("Room Number\t| Room Type")
        for room in available_rooms[1:]:
            print("{}\t\t\t| {}".format(room[0], room[1]))
    else:
        print("All rooms are booked in the specified date range.")
    return available_rooms


### option 10 ###
def get_room_by_type_cli():
    '''takes from the user the room type they want info about and prints the info about the room type'''
    types = rm.Rooms.get_room_by_type()  # calls the Hotel_manage_sys package > rooms_module.py > Rooms class > get_room_by_type() function and gets back the room types dict from the json
    print('There are 3 room types:\n 1. Basic\n 2. Deluxe\n 3. Suite')
    room_type = input(
        'Please enter 1, 2 or 3 to choose the type of room for which you would like to view additional details: ')

    def print_room(r):
        '''displays to the user the room type data'''
        print(f"here is the info you asked about {r['Type']} room type")
        print(f"Type: {r['Type']}")
        print(f"Size: {r['size']} sq. meters")
        print(f"Capacity: {r['Capacity']} guests")
        print(f"Number of Beds: {r['NumberOfBeds']} bed")
        print(f"Price per night: {r['Price']} USD")
        print(f"Minimum Nights: {r['MinNights']} night")

    while True:
        try:  # checks if the input is correct and if not raise an exception
            if room_type != '1' and room_type != '2' and room_type != '3':
                raise ValueError(
                    "\n******\n Wrong Value! Please enter 1, 2, or 3.\n******\n")
        except ValueError as e:  # if error is raised we ask the user for the input again
            print(e)  # Print the ValueError message
            print('There are 3 room types.\n 1. Basic\n 2. Deluxe\n 3. Suite')
            room_type = input('Please enter 1, 2, or 3: ')
        else:  # when the input is correct we call the print_room() inner method
            if room_type == '1':
                room = types['Basic']
                print_room(room)
            elif room_type == '2':
                room = types['Deluxe']
                print_room(room)
            elif room_type == '3':
                room = types['Suite']
                print_room(room)
            break
    return room_type  # purpose: book_room_cli() ;


### option 11 ###
def get_room_by_number_cli():
    """takes from the user the room number they want info about and prints the info about the room number"""
    # call the Hotel_manage_sys package > rooms_module.py > Rooms class > get_room_by_number() function
    # and get back the room info list from the csv
    rooms = rm.Rooms.get_inventory()
    # calls the Hotel_manage_sys package > rooms_module.py > Rooms class > get_room_by_type() function
    # and gets back the room types dict from the json
    types = rm.Rooms.get_room_by_type()
    room_number = input('Please enter the desired room number: ')

    def print_room(r):
        """displays to the user the room data"""
        print(f"here is the info you asked about room number {room_number}")
        print(f"Type: {r['Type']}")
        print(f"Size: {r['size']} sq. meters")
        print(f"Capacity: {r['Capacity']} guests")
        print(f"Number of Beds: {r['NumberOfBeds']} bed")
        print(f"Price per night: {r['Price']} USD")
        print(f"Minimum Nights: {r['MinNights']} night")

    while True:
        try:  # checks if the input is correct and if not raise an exception
            if room_number not in [room[0] for room in rooms]:
                raise ValueError(
                    "\n******************\n Try again.\n Room number does not exist.\n******************\n")

        except ValueError as e:  # if error is raised we ask the user for the input again
            print(e)  # Print the ValueError message
            room_number = input('Please enter the desired room number: ')

        else:
            #  when the input is correct we call the print_room() inner method
            for room in rooms:
                if room[0] == room_number:
                    room_type = room[1]
            if room_type == 'Basic':
                room = types['Basic']
                print_room(room)
            elif room_type == 'Deluxe':
                room = types['Deluxe']
                print_room(room)
            elif room_type == 'Suite':
                room = types['Suite']
                print_room(room)
            break
    return room_number  # purpose: remove_room_cli() ; book_room_cli() ;


### option 12 ###
def get_cust_by_name_cli():
    """presents to the user information about all customers with the entered name"""
    customer_name = input("Please enter the customer's first and last name: ")
    customers = cm.Customers.get_cust_list()

    def print_customer(c):
        """displays to the user the customer's data"""
        print(f"Customer ID: {c[0]}")
        print(f"Full Name: {c[1]}")
        print(f"Address: {c[2]}")
        print(f"City: {c[3]} ")
        print(f"Email Address: {c[4]}")
        print(f"Age: {c[5]}\n")

    while True:
        try:  # checks the input to match a customer name format of first and last name, otherwise raise an exception
            if len(customer_name.split(' ')) != 2:
                raise ValueError("\n** Customer's name must include only first and last name separated by space **\n")

        except ValueError as e:  # if error is raised we ask the user for the input again
            print(e)  # Print the ValueError message
            get_cust_by_name_cli()

        else:
            #  when the input is correct we compare the input name to names in the database
            first_name, last_name = customer_name.split(' ')
            first_last = re.compile(f'{first_name}.*{last_name}', re.IGNORECASE)
            last_first = re.compile(f'{last_name}.*{first_name}', re.IGNORECASE)

            found = False  # flag to check if any matches were found
            print(f"Here is the info we found about: {customer_name}\n")
            for customer in customers:
                cust_name = customer[1]
                # cust_first, cust_last = cust_name.split(' ')
                if first_last.search(cust_name) or last_first.search(cust_name):
                    # If the customer's name is in our list, print the customer info
                    print_customer(customer)
                    found = True  # flag to True so the raise will not come up
                    continue  # continue in case there is more than 1 customer with the same name
            if not found:
                # If the customer's name is not in our list, print result
                print("** No customer with that name. To add the customer select option 1 on the main menu **")
                main_menu()
        break
    return cust_name


### option 13 ###
def remove_room_cli():
    """calls get_room_by_number_cli,
    then sends the removal request to the hotel management sys after confirmation"""

    def confirm_removal(num):
        confirm = input(f"Are you sure you want to remove room number {num}? Please enter Y / N: ")

        while True:
            try:  # checks if the input is correct and if not raise an exception
                if confirm in ['N', 'n']:
                    print('Action Cancelled. Room was not removed from the inventory')
                    main_menu()
                elif confirm not in ['Y', 'y', 'N', 'n']:
                    raise ValueError("\n*************\nIncorrect value.\nTry again.\n*************\n")

            except ValueError as e:  # if error is raised we ask the user for the input again
                print(e)  # Print the ValueError message
                confirm_removal(num)

            else:
                #  when the input is 'Y' or 'y' we call the remove_room in the Hotel_manage_sys
                rm.Rooms.remove_room(num)
                print(f'Success. Room number {num} has been removed from the rooms list')
            break

    room_number = get_room_by_number_cli()
    confirm_removal(room_number)


### option 14 ###
def remove_cust_cli():
    """calls get_cust_by_name_cli, gets the user's confirmation by cust_ID,
    then sends the removal request to the hotel management sys after confirmation"""

    get_cust_by_name_cli()
    customer_id = input(f'please enter the customer ID you would like to remove from the list: ')

    def confirm_cust_id(cust_id):
        """Confirms that the customer ID exists in the customers list"""
        customers = cm.Customers.get_cust_list()
        while True:
            try:  # checks if the input corresponds to any of the customer Ids in the list and if not raise an exception
                if cust_id not in [customer[0] for customer in customers]:
                    raise ValueError(
                        "\n******************\n Try again.\n Customer ID does not exist.\n******************\n")

            except ValueError as e:  # if error is raised we ask the user for the input again
                print(e)  # Print the ValueError message
                cust_id = input(f'please enter the customer ID you would like to remove from the list: ')

            else:
                #  when the input is correct we call the print_room() inner method
                break
        return cust_id  # this return is for the purpose of remove_room_cli() method

    def confirm_removal(cust_id):
        """asks the user for a confirmation for removal of the customer ID"""
        confirm = input(f"Are you sure you want to remove customer ID {cust_id}? Please enter Y / N: ")

        while True:
            try:  # checks if the input is correct and if not raise an exception
                if confirm in ['N', 'n']:
                    print('Action Cancelled. Customer was not removed from the customers list')
                    main_menu()
                elif confirm not in ['Y', 'y', 'N', 'n']:
                    raise ValueError("\n*************\nIncorrect value.\nTry again.\n*************\n")

            except ValueError as e:  # if error is raised we ask the user for the input again
                print(e)  # Print the ValueError message
                confirm_removal(cust_id)

            else:
                #  when the input is 'Y' or 'y' we call the remove_customer in the Hotel_manage_sys
                cm.Customers.remove_customer(cust_id)
                print(f'Success. Customer with ID number {cust_id} has been removed from the customers list')
            break

    confirm_id = confirm_cust_id(customer_id)
    confirm_removal(confirm_id)

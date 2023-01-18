import csv
import json
import re
import random
import datetime
from datetime import datetime
from unittest.mock import patch

import CLI
import database
import Hotel_manage_sys
import Hotel_manage_sys.rooms_module as rm
import Hotel_manage_sys.customers_module as cm
import Hotel_manage_sys.bookings_module as bm
import CLI.interface as cli

### read files ###
cust_list = '../database/cust_list.csv'
room_types = '../database/room_types_list.json'
rooms_list = '../database/rooms_list.csv'
bookings = '../database/bookings_list.csv'
booking_id_file = '../database/booking_id_file.txt'


## Tests Menu ##
def test_main_menu():
    while True:
        print("\n****************************************************")
        print("   Welcome to Hotel California Testing System!")
        print("****************************************************\n")
        print("What would you like to do?\n")
        print("Test CLI")
        print("1. Test 'get valid dates'")
        print("2. Test 'Add Room CLI'")
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
            test_get_valid_dates()
        elif main_menu_selection == 2:
            test_add_room_cli()
        # elif main_menu_selection == 3:
        #     book_room_cli()
        # elif main_menu_selection == 4:
        #     remove_booking_cli()
        # elif main_menu_selection == 5:
        #     get_inventory_cli()
        #     main_menu()
        # elif main_menu_selection == 6:
        #     get_cust_list_cli()
        #     main_menu()
        # elif main_menu_selection == 7:
        #     get_all_bookings_cli()
        #     main_menu()
        # elif main_menu_selection == 8:
        #     get_booked_rooms_by_date_cli()
        #     main_menu()
        # elif main_menu_selection == 9:
        #     get_available_rooms_by_date_cli()
        #     main_menu()
        # elif main_menu_selection == 10:
        #     get_room_by_type_cli()
        #     main_menu()
        # elif main_menu_selection == 11:
        #     get_room_by_number_cli()
        #     main_menu()
        # elif main_menu_selection == 12:
        #     get_cust_by_name_cli()
        #     main_menu()
        # elif main_menu_selection == 13:
        #     remove_room_cli()
        #     main_menu()
        # elif main_menu_selection == 14:
        #     remove_cust_cli()
        else:
            print("Option not available. Please enter a valid number between 1-14 from the menu below")
            test_main_menu()


def input_handler(*inputs):
    """Function that handles inputs for mocked input() function"""
    for input_str in inputs:
        yield input_str


def test_get_valid_dates():
    with patch('builtins.input', input_handler("2022-05-01", "2022-05-07")):
        assert cli.get_valid_dates() == ("2022-05-01", "2022-05-07")

    with patch('builtins.input', input_handler("2022/05/01", "2022/05/07")):
        assert cli.get_valid_dates() == "Invalid date format. Please enter the dates in the format YYYY-MM-DD."

    with patch('builtins.input', input_handler("2022-05-07", "2022-05-01")):
        assert cli.get_valid_dates() == "Arrival date must be prior to the departure date. Please enter the dates again."

    with patch('builtins.input', input_handler("X", "X")):
        assert cli.get_valid_dates() == "main_menu()"


# def test_get_valid_dates():
#     # Test valid input
#     arrival_date = "2022-05-01"
#     departure_date = "2022-05-07"
#     assert cli.get_valid_dates() == (arrival_date, departure_date)
#
#     # Test invalid date format
#     arrival_date = "2022/05/01"
#     departure_date = "2022/05/07"
#     assert cli.get_valid_dates() == ("Invalid date format. Please enter the dates in the format YYYY-MM-DD.")
#
#     # Test arrival date later than departure date
#     arrival_date = "2022-05-07"
#     departure_date = "2022-05-01"
#     assert cli.get_valid_dates() == ("Arrival date must be prior to the departure date. Please enter the dates again.")
#
#     # Test input of 'X' to go back to main menu
#     arrival_date = "X"
#     departure_date = "X"
#     assert cli.get_valid_dates() == ("cli.main_menu()")


def test_add_room_cli():
    # Test valid input
    room_number = "123"
    room_type = "1"
    with patch('builtins.input', side_effect=[room_number, room_type]):
        cli.add_room_cli()
    assert rm.Rooms.add_room.called_once_with([room_number, 'Basic'])
    rm.Rooms.add_room.reset_mock()

    # Test duplicate room number
    rm.Rooms.get_inventory.return_value = [[room_number, 'Basic']]
    room_number = "456"
    with patch('builtins.input', side_effect=[room_number, room_type]):
        cli.add_room_cli()
    assert rm.Rooms.add_room.called_once_with([room_number, 'Basic'])
    rm.Rooms.add_room.reset_mock()
    rm.Rooms.get_inventory.return_value = []

    # Test invalid input
    room_type = "4"
    with patch('builtins.input', side_effect=[room_number, room_type, room_type]):
        cli.add_room_cli()
    assert rm.Rooms.add_room.called_once_with([room_number, 'Basic'])
    rm.Rooms.add_room.reset_mock()


test_main_menu()

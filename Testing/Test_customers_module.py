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

#
# ## Tests Menu ##
# def test_main_menu():
#     while True:
#         print("\n****************************************************")
#         print("   Welcome to Hotel California Testing System!")
#         print("****************************************************\n")
#         print("What would you like to do?\n")
#         print("Test CLI")
#         print("1. Test 'add customer'")
#         print("2. Test 'get customers list'")
#         print("3. Test 'test remove customer'")
#         print("4. Cancel booking")
#         print("5. Display all rooms")
#         print("6. Display all customers")
#         print("7. Display all bookings")
#         print("8. Display booked rooms for a specific date")
#         print("9. Display available rooms for a specific date")
#         print("10. Find room by type")
#         print("11. Find room by number")
#         print("12. Find customer by name")
#         print("13. Remove room")
#         print("14. Remove customer")
#
#         main_menu_selection = int(input("\nPlease type the option number (0-14): "))
#
#         if main_menu_selection == 1:
#             test_add_cust()
#         elif main_menu_selection == 2:
#             test_get_cust_list()
#         elif main_menu_selection == 3:
#             test_remove_customer()
#         # elif main_menu_selection == 4:
#         #     remove_booking_cli()
#         # elif main_menu_selection == 5:
#         #     get_inventory_cli()
#         #     main_menu()
#         # elif main_menu_selection == 6:
#         #     get_cust_list_cli()
#         #     main_menu()
#         # elif main_menu_selection == 7:
#         #     get_all_bookings_cli()
#         #     main_menu()
#         # elif main_menu_selection == 8:
#         #     get_booked_rooms_by_date_cli()
#         #     main_menu()
#         # elif main_menu_selection == 9:
#         #     get_available_rooms_by_date_cli()
#         #     main_menu()
#         # elif main_menu_selection == 10:
#         #     get_room_by_type_cli()
#         #     main_menu()
#         # elif main_menu_selection == 11:
#         #     get_room_by_number_cli()
#         #     main_menu()
#         # elif main_menu_selection == 12:
#         #     get_cust_by_name_cli()
#         #     main_menu()
#         # elif main_menu_selection == 13:
#         #     remove_room_cli()
#         #     main_menu()
#         # elif main_menu_selection == 14:
#         #     remove_cust_cli()
#         else:
#             print("Option not available. Please enter a valid number between 1-14 from the menu below")
#             test_main_menu()


def test_add_cust():
    """Test adding a customer"""
    cust_info = [1, 'John Doe', '123 Main St', 'Anytown', 'john.doe@example.com', 30]
    cm.Customers.add_cust(cust_info)
    with open(cust_list, 'r') as cl:
        if cl.tell() == 0:
            print("file is empty")
        else:
            reader = csv.reader(cl)
            # Assert that the first row (column names) is correct
            assert next(reader) == ['cust_id', 'name', 'address', 'city', 'email', 'age']
            # Assert that the second row (customer info) is correct
            row = next(reader)
            assert row[0] == cust_info[0]
            assert row[1] == cust_info[1]
            assert row[2] == cust_info[2]
            assert row[3] == cust_info[3]
            assert row[4] == cust_info[4]
            assert row[5] == cust_info[5]
    # Test adding multiple customers
    cust_info2 = [2, 'Jane Smith', '456 Park Ave', 'Anycity', 'jane.smith@example.com', 25]
    cm.Customers.add_cust(cust_info2)
    with open(cust_list, 'r') as cl:
        if cl.tell() == 0:
            print("file is empty")
        else:
            reader = csv.reader(cl)
            # Assert that the first row (column names) is correct
            assert next(reader) == ['cust_id', 'name', 'address', 'city', 'email', 'age']
            # Assert that the second row (customer info) is correct
            row = next(reader)
            assert row[0] == cust_info[0]
            assert row[1] == cust_info[1]
            assert row[2] == cust_info[2]
            assert row[3] == cust_info[3]
            assert row[4] == cust_info[4]
            assert row[5] == cust_info[5]
            # Assert that the third row (customer info) is correct
            row = next(reader)
            assert row[0] == cust_info2[0]
            assert row[1] == cust_info2[1]
            assert row[2] == cust_info2[2]
            assert row[3] == cust_info2[3]
            assert row[4] == cust_info2[4]
            assert row[5] == cust_info2[5]


def test_get_cust_list():
    # Add a customer to the customer list
    cust_info = [1, 'John Doe', '123 Main St', 'Anytown', 'john.doe@example.com', 30]
    cm.Customers.add_cust(cust_info)
    # Add a second customer to the customer list
    cust_info2 = [2, 'Jane Smith', '456 Park Ave', 'Anycity', 'jane.smith@example.com', 25]
    cm.Customers.add_cust(cust_info2)
    # Get the full customer list
    with open(cust_list, 'r') as cl:
        if cl.tell() == 0:
            print("file is empty")
        else:
            customers = cm.Customers.get_cust_list()
            # Assert that the first element of the customer list is the column names
            assert customers[0] == ['cust_id', 'name', 'address', 'city', 'email', 'age']
            # Assert that the second element of the customer list is the first customer's info
            assert customers[1][0] == cust_info[0]
            assert customers[1][1] == cust_info[1]
            assert customers[1][2] == cust_info[2]
            assert customers[1][3] == cust_info[3]
            assert customers[1][4] == cust_info[4]
            assert customers[1][5] == cust_info[5]
            # Assert that the third element of the customer list is the second customer's info
            assert customers[2][0] == cust_info2[0]
            assert customers[2][1] == cust_info2[1]
            assert customers[2][2] == cust_info2[2]
            assert customers[2][3] == cust_info2[3]
            assert customers[2][4] == cust_info2[4]
            assert customers[2][5] == cust_info2[5]

def test_remove_customer():
    # Add a customer to the customer list
    cust_info = [1, 'John Doe', '123 Main St', 'Anytown', 'john.doe@example.com', 30]
    cm.Customers.add_cust(cust_info)
    # Add a second customer to the customer list
    cust_info2 = [2, 'Jane Smith', '456 Park Ave', 'Anycity', 'jane.smith@example.com', 25]
    cm.Customers.add_cust(cust_info2)
    # Remove the first customer from the customer list
    with open(cust_list, 'r') as cl:
        if cl.tell() == 0:
            print("file is empty")
        else:
            cm.Customers.remove_customer('1')
            customers = cm.Customers.get_cust_list()
            # Assert that the first element of the customer list is the column names
            assert customers[0] == ['cust_id', 'name', 'address', 'city', 'email', 'age']
            # Assert that the second element of the customer list is the second customer's info
            assert customers[1][0] == cust_info2[0]
            assert customers[1][1] == cust_info2[1]
            assert customers[1][2] == cust_info2[2]
            assert customers[1][3] == cust_info2[3]
            assert customers[1][4] == cust_info2[4]
            assert customers[1][5] == cust_info2[5]

# test_main_menu()

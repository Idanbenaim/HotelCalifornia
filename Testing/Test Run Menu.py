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
import Testing.Test_rooms_module as rm
import Testing.Test_customers_module as cm
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
        print("**Test Customers**")
        print("1. Test 'add customer'")
        print("2. Test 'get customers list'")
        print("3. Test 'test remove customer'")
        print("\n**Test Rooms**")
        print("4. Test 'add room'")
        print("5. Test 'get inventory'")
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
            cm.test_add_cust()
        elif main_menu_selection == 2:
            cm.test_get_cust_list()
        elif main_menu_selection == 3:
            cm.test_remove_customer()
        elif main_menu_selection == 4:
            rm.test_add_room()
        elif main_menu_selection == 5:
            rm.test_get_inventory()
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


def main():
    test_main_menu()


if __name__ == "__main__":
    main()

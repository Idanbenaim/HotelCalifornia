# import csv
# import json
# import re
# import random
# import datetime
# from datetime import datetime
# from unittest.mock import patch
#
# import CLI
# import database
# import Hotel_manage_sys
import Testing.Test_rooms_module as rm
import Testing.Test_customers_module as cm
import Testing.Test_booking_module as bm
# import CLI.interface as cli

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

        print("\n**Test Bookings**")
        print("6. Test get booking ID")
        print("7. Test Book a room, get booked room by date, get all bookings,\n"
              "   remove booking, and get available rooms by date")


        main_menu_selection = int(input("\nPlease type the option number (1-7): "))

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
        elif main_menu_selection == 6:
            bm.test_get_booking_id()
        elif main_menu_selection == 7:
            bm.test_book_room()

        else:
            print("Option not available. Please enter a valid number between 1-7 from the menu below")
            test_main_menu()


def main():
    test_main_menu()


if __name__ == "__main__":
    main()

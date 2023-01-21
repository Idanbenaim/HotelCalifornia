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

import csv
import json
import re
import random
import datetime
import os
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


def test_add_room():
    # Add a room to the room list
    room_info = ['101', 'Basic']
    with open(rooms_list, 'r') as rl:
        if rl.tell() == 0:
            rm.Rooms.add_room(room_info)
            rl.seek(0)
            # Read the rooms_list file
            rooms = []
            csv_reader = csv.reader(rl)
            for row in csv_reader:
                rooms.append(row)
            # Assert that the first element of the room list is the column names
            assert rooms[0] == ['room_number', 'room_type']
            # Assert that the second element of the room list is the first room's info
            assert rooms[1][0] == room_info[0]
            assert rooms[1][1] == room_info[1]




# def test_add_room():
#     # Test case 1: Check if room is added to the file
#     room_info = ['101', 'single']
#     rm.Rooms.add_room(room_info)
#     with open(rooms_list, 'r', newline='') as rl:
#         if rl.tell() == 0:
#             assert rows == [], f'Test Case 1 Failed: {rows}'
#         else:
#             reader = csv.reader(rl)
#             rows = [row for row in reader]
#             assert rows[1] == room_info, f'Test Case 1 Failed: {rows[1]}'
#
#     # Test case 2: Check if adding room with existing room number raises an exception
#     room_info = ['101', 'single']
#     try:
#         rm.Rooms.add_room(room_info)
#     except Exception as e:
#         assert str(e) == 'Room already exists', f'Test Case 2 Failed: {e}'
#
#     # Test case 3: Check if the file is created if it doesn't exist
#     if os.path.exists(rooms_list):
#         os.remove(rooms_list)
#     room_info = ['102', 'double']
#     rm.Rooms.add_room(room_info)
#     assert os.path.exists(rooms_list) == True, f'Test Case 3 Failed: {rooms_list} does not exist'
#     with open(rooms_list, 'r', newline='') as rl:
#         if rl.tell() == 0:
#             assert rows == [], f'Test Case 3 Failed: {rows}'
#         else:
#             reader = csv.reader(rl)
#             rows = [row for row in reader]
#             assert rows[1] == room_info, f'Test Case 3 Failed: {rows[1]}'
#     if os.path.exists(rooms_list):
#         os.remove(rooms_list)



# def test_add_room():
#     # Test case 1: Check if room is added to the file
#     room_info = ['101', 'single']
#     rm.Rooms.add_room(room_info)
#     with open(rooms_list, 'r', newline='') as rl:
#         reader = csv.reader(rl)
#         rows = [row for row in reader]
#     if rl.tell() == 0:
#         assert rows == [], f'Test Case 1 Failed: {rows}'
#     else:
#         assert rows[1] == room_info, f'Test Case 1 Failed: {rows[1]}'
#
#     # Test case 2: Check if adding room with existing room number raises an exception
#     room_info = ['101', 'single']
#     try:
#         rm.Rooms.add_room(room_info)
#     except Exception as e:
#         assert str(e) == 'Room already exists', f'Test Case 2 Failed: {e}'
#
#     # Test case 3: Check if the file is created if it doesn't exist
#     os.remove(rooms_list)
#     room_info = ['102', 'double']
#     rm.Rooms.add_room(room_info)
#     assert os.path.exists(rooms_list) == True, f'Test Case 3 Failed: {rooms_list} does not exist'
#     with open(rooms_list, 'r', newline='') as rl:
#         reader = csv.reader(rl)
#         rows = [row for row in reader]
#     if rl.tell() == 0:
#         assert rows == [], f'Test Case 3 Failed: {rows}'
#     else:
#         assert rows[1] == room_info, f'Test Case 3 Failed: {rows[1]}'
#     os.remove(rooms_list)


def test_get_inventory():
    # Test case 1: Check if the function returns the correct rooms list
    room_info = [['101', 'single'], ['102', 'double'], ['103', 'suite']]
    with open(rooms_list, 'w', newline='') as rl:
        update_room_list = csv.writer(rl)
        update_room_list.writerow(['room_number', 'room_type'])
        for room in room_info:
            update_room_list.writerow(room)
    rooms = rm.Rooms.get_inventory()
    assert rooms == room_info, f'Test Case 1 Failed: {rooms}'

    # Test case 2: Check if the function returns an empty list if the rooms_list file does not exist
    os.remove(rooms_list)
    rooms = rm.Rooms.get_inventory()
    if rl.tell() == 0:
        assert rooms == [], f'Test Case 2 Failed: {rooms}'
    else:
        assert rooms == [], f'Test Case 2 Failed: {rooms}'

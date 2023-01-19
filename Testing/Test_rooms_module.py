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
    room_info = ['101', 'Basic']
    rm.Rooms.add_room(room_info)
    with open(rooms_list, 'r') as rl:
        rooms = []
        csv_reader = csv.reader(rl)
        for row in csv_reader:
            rooms.append(row)
        if not rooms:
            assert rooms[0] == ['room_number', 'room_type']
            assert rooms[1][0] == room_info[0]
            assert rooms[1][1] == room_info[1]
    print('done')


def test_get_inventory():
    # Test case 1: Check if the function returns the correct rooms list
    room_info = [['101', 'Basic'], ['102', 'Deluxe'], ['103', 'Suite']]
    with open(rooms_list, 'w', newline='') as rl:
        update_room_list = csv.writer(rl)
        update_room_list.writerow(['room_number', 'room_type'])
        for room in room_info:
            update_room_list.writerow(room)
    rooms = rm.Rooms.get_inventory()
    for i, room in enumerate(rooms):
        if i == 0:
            assert room == ['room_number', 'room_type'], f'Test Case 1 Failed: {rooms}'
        else:
            assert len(room) == 2, f'Test Case 1 Failed: {rooms}'
            assert room[0] in [r[0] for r in room_info], f'Test Case 1 Failed: {rooms}'
            assert room[1] in [r[1] for r in room_info], f'Test Case 1 Failed: {rooms}'



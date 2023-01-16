import json
import csv
import datetime
import database
from database import *


### read database files ####

# def get_rooms_list(file_name):
#     with open(file_name) as f:
#         rooms = f.read()
#     return rooms
#
# def get_room_type_info(file_name):
#     file_name = 'room_types_list.json'
#     with database.open(file_name) as f:
#         hotel_info = f.read()
#     return hotel_info

# rooms_list = database.db_paths.rooms_list
# call_room_types_info = get_room_type_info('room_types_list.json')

#### rooms management sys ####
class Rooms:

    TYPE = ('basic', 'deluxe', 'suite')
    # basic = ('20', '2', '1', 'Basic', '200', '1')  # (size: 20,	Capacity: 2,	NumberOfBeds: 1,	Type: basic, Price: 200, MinNights: 1)
    # deluxe = ('40', '4', '2', 'deluxe', '400', '2')  # (size: 40,	Capacity: 4,	NumberOfBeds: 2,	Type: deluxe, Price: 400, MinNights: 2)
    # suite = ('60', '6', '3', 'suite', '600', '3')  # (size: 60,	Capacity: 6,	NumberOfBeds: 3,	Type: suite, Price: 600, MinNights: 3)

    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type

    def add_room(room_info:list):
        '''gets a room number and type from add_room_cli as a list.
        here we use the list to add the room's info to the rooms_list file'''
        rooms_list = '/Users/idanbenaim/PycharmProjects/HotelCalifornia/database/rooms_list.csv'
        with open(rooms_list, 'a', newline='') as rl:
            update_room_list = csv.writer(rl)
            if rl.tell() == 0:  # Check if the file is empty
                update_room_list.writerow(['room_number', 'room_type'])  # Write column names
            update_room_list.writerow(room_info)

    def get_inventory():
        """returns the full rooms list"""
        # global rooms_list
        rooms_list = '/Users/idanbenaim/PycharmProjects/HotelCalifornia/database/rooms_list.csv'
        rooms = []
        with open(rooms_list, 'r') as rl:
            reader = csv.reader(rl)
            for row in reader:
                rooms.append(row)
        return rooms

    def get_room_by_type():
        # room_types = database.db_paths.room_types_list
        room_types = '/Users/idanbenaim/PycharmProjects/HotelCalifornia/database/room_types_list.json'
        with open(room_types, 'r') as rt:
            types = json.load(rt)
        return types

    def remove_room(num):
        """receives the room number and removes it from the rooms list"""
        rooms_list = '/Users/idanbenaim/PycharmProjects/HotelCalifornia/database/rooms_list.csv'
        with open(rooms_list, "r") as rl:
            csv_reader = csv.reader(rl)
            rooms = list(csv_reader)
        # print(num)
        for room in rooms:
            if room[0] == num:
                rooms.remove(room)
                with open(rooms_list, "w") as new_rl:
                    csv_writer = csv.writer(new_rl)
                    csv_writer.writerows(rooms)
                break

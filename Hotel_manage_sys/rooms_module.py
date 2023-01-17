import json
import csv
import datetime
import database
# from database import *


### files ###

rooms_list = '/Users/idanbenaim/PycharmProjects/HotelCalifornia/database/rooms_list.csv'

#### rooms management sys ####
class Rooms:

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
        global rooms_list
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

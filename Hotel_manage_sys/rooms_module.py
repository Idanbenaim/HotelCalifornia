import datetime


class Rooms:
    ROOM_ID = 1000
    TYPE = ('basic', 'deluxe', 'suite')
    basic = ('20', '2', '1', 'Basic', '200', '1')  # (size: 20,	Capacity: 2,	NumberOfBeds: 1,	Type: basic, Price: 200, MinNights: 1)
    deluxe = ('40', '4', '2', 'deluxe', '400', '2')  # (size: 40,	Capacity: 4,	NumberOfBeds: 2,	Type: deluxe, Price: 400, MinNights: 2)
    suite = ('60', '6', '3', 'suite', '600', '3')  # (size: 60,	Capacity: 6,	NumberOfBeds: 3,	Type: suite, Price: 600, MinNights: 3)

    def __init__(self):
        pass


    def __str__(self):
        pass


    def add_room(self, type):
        '''add room to the rooms list, append room id into position [0,0]'''
        ROOM_ID += 1
        pass


    def get_room_by_type(self, guests, type):
        # We are unclear about what is the expected result from this requirement:
        ### return a specific room Id?
        ### return the info about the room type?
        ### return the list of available rooms of that type?
        pass


    def get_inventory(self):
        '''returns the full rooms list'''
        pass


    def remove_room(self):
        '''removs a specific room from the rooms list'''
        pass



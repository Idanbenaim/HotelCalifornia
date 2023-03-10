import json
import csv
from datetime import datetime

import database
from Hotel_manage_sys import rooms_module as rm, customers_module as cm


#### files ###
bookings = '../database/bookings_list.csv'
booking_id_file = '../database/booking_id_file.txt'
room_types_list = '../database/room_types_list.json'


#### bookings management sys ###
class Bookings:
    BOOKING_ID = int(1000)
    booking_id_file = 'booking_id_file.txt'

    def __init__(self):
        pass

    def get_booking_id():
        """generate a unique booking id"""
        with open(booking_id_file, 'r') as bir:
            BOOKING_ID = int(bir.read())
        BOOKING_ID += 1
        with open(booking_id_file, 'w') as biw:
            biw.write(str(BOOKING_ID))
        return BOOKING_ID

    def book_room(cust_id, room_number, arrival_date, departure_date):
        """saves a new booking in the db and returns the booking info"""
        # get a new booking ID
        bid = Bookings.get_booking_id()

        # get list of rooms
        rooms = rm.Rooms.get_inventory()

        # get room type
        room_type = None
        for room in rooms:
            if room[0] == room_number:
                room_type = room[1]
                break

        # get price per night for the room type
        room_types_json = rm.Rooms.get_room_by_type()
        cost_per_night = int(room_types_json[room_type]['Price'])

        # calculate total cost
        arrival = datetime.strptime(arrival_date, '%Y-%m-%d')
        departure = datetime.strptime(departure_date, '%Y-%m-%d')
        num_nights = (departure - arrival).days
        total_cost = num_nights * cost_per_night

        # write booking to csv file
        with open(bookings, 'a') as bl:
            reservation = csv.writer(bl)
            reservation.writerow([bid, cust_id, room_number, arrival_date, departure_date, cost_per_night, total_cost])

        # return booking info as tuple
        booking_info = (bid, cust_id, room_number, arrival_date, departure_date, cost_per_night, total_cost)
        return booking_info


    def remove_booking(booking_id):
        """cancel a future room reservation and remove from the bookings list"""
        global bookings
        with open(bookings, "r") as bl:
            csv_reader = csv.reader(bl)
            bookings_list = list(csv_reader)
        for reservation in bookings_list:
            if reservation[0] == booking_id:
                bookings_list.remove(reservation)
                with open(bookings, "w") as new_bl:
                    csv_writer = csv.writer(new_bl)
                    csv_writer.writerows(bookings_list)
                break

    def get_all_bookings():
        """return all room reservations past and future"""
        booked_rooms = []
        global bookings
        with open(bookings, 'r') as file:
            bookings_list = csv.reader(file)
            next(bookings_list)
            for reservation in bookings_list:
                booked_rooms.append(reservation)
        return booked_rooms

    def get_booked_rooms_by_date(arrival_date, departure_date):
        """return a list of all reservations at the specified date range, and the info about each booked room"""
        booked_rooms = []
        global bookings
        with open(bookings, 'r') as file:
            bookings_list = csv.reader(file)
            next(bookings_list)
            for reservation in bookings_list:
                if arrival_date <= reservation[3] <= departure_date or arrival_date <= reservation[4] <= departure_date:
                    booked_rooms.append(reservation)
        return booked_rooms

    def get_available_rooms_by_date(arrival_date, departure_date):
        """Return a list of available rooms in the specified date range"""
        inventory = rm.Rooms.get_inventory()
        booking_list = Bookings.get_booked_rooms_by_date(arrival_date, departure_date)
        booked_rooms = [reservation[2] for reservation in booking_list]
        available_rooms = []
        for room in inventory:
            if room[0] not in booked_rooms:
                available_rooms.append(room)
        return available_rooms

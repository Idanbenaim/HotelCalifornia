import json
import csv
from datetime import datetime
from Hotel_manage_sys import rooms_module as rm, customers_module as cm
from database import *

bookings = '/Users/idanbenaim/PycharmProjects/HotelCalifornia/database/bookings_list.csv'


#### read file ###
def get_bookings_list():
    with database.open('bookings_list.txt') as f:
        bookings = f.read()
    return bookings


#### bookings management sys ###
class Bookings:
    ORDER_ID = 100

    def __init__(self):
        pass

    #
    #
    # def book_room(self, guests, datefrom,
    #               dateto):  # [orderID, CustID, RoomID, ArrivalDate, DepartureData, TotalPrice, orderTotal]
    #     '''add room reservation to the bookings list
    #     and return customer detail as a list '''
    #     ORDER_ID += 1
    #
    #
    # @book_room
    # def book_room_by_room_number(self, room_number, datefrom, dateto):
    #     '''book a specific room number'''
    #     pass
    #
    #
    # @book_room
    # def book_room_by_room_type(self, room_number, datefrom, dateto):
    #     '''book a specific room number'''
    #     pass
    #
    #
    def remove_booking(booking_id):
        '''cancel a future room reservation and remove from the bookings list'''
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

    # def get_available_rooms_by_date(guests, datefrom, dateto):
    #     '''return a list of all available rooms at a specified date range'''
    #     booked = get_booked_rooms_by_date(datefrom, dateto)
    #     inv = get
    #     inventory()
    #
    #     # we substruct the booked rooms from the entire inventory of rooms
    #     total_available = list(set(inv[0]) - set(booked[0]))
    #
    #     # We filter out rooms which are not suitable for the customer's party size
    #     net_available = (net_available.remove[i] for i in total_available if i[2] <= guests)
    #
    #     # we count the number of available rooms from each type
    #     count_basic = 0
    #     count - deluxe = 0
    #     count_suite = 0
    #     for j in net_available:
    #         count_basic += 1 if j[4] == 'basic'
    #         count_deluxe += 1 if j
    #

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


def test_get_booking_id():
    # Test case 1: Check if the function returns a unique booking ID
    with open(booking_id_file, 'w') as bir:
        bir.write('1001')
    booking_id1 = bm.Bookings.get_booking_id()
    booking_id2 = bm.Bookings.get_booking_id()
    assert booking_id1 != booking_id2, f'Test Case 1 Failed: {booking_id1}, {booking_id2}'
    assert type(booking_id1) == int, f'Test Case 1 Failed: {booking_id1}'
    assert type(booking_id2) == int, f'Test Case 1 Failed: {booking_id2}'

    # Test case 2: Check if the function reads the initial value from the booking_id_file
    with open(booking_id_file, 'w') as bir:
        bir.write('1111')
    booking_id = bm.Bookings.get_booking_id()
    assert booking_id == 1112, f'Test Case 2 Failed: {booking_id}'


def test_book_room():
    """creating a mock booking and testing
    1. the returned values from the method's returned list,
    2. the returned values when calling this booking using get_booked_rooms_by_date
    3. the returned values when calling this booking using get_all_bookings
    4. the removal of the original booking is tested using the returned values of get_available_rooms_by_date"""

    # mock booking info to test with
    cust_id = '555'
    room_number = '888'
    room_type = 'Basic'
    arrival_date = '2023-05-01'
    departure_date = '2023-05-05'
    expected_cost_per_night = 200
    expected_total_cost = 800

    # add the room
    rm.Rooms.add_room([room_number, room_type])

    # book the room
    mock_booking = bm.Bookings.book_room(cust_id, room_number, arrival_date, departure_date)
    booking_id = mock_booking[0]

    # Assert info from the returned booking info
    assert type(mock_booking[0]) == int, f"Test Case 1: booking id type is incorrect"
    assert mock_booking[1] == '555', f"Test Case 1: cust id incorrect"
    assert mock_booking[2] == '888', f"Test Case 1: room number incorrect"
    assert mock_booking[3] == '2023-05-01', f"Test Case 1: arrival date incorrect"
    assert mock_booking[4] == '2023-05-05', f"Test Case 1: departure date incorrect"
    assert mock_booking[5] == expected_cost_per_night, f"Test Case 1: cost per night incorrect"
    assert mock_booking[6] == expected_total_cost, f"Test Case 1: total cost incorrect"

    # test case 2
    def test_get_booked_rooms_by_date(arrival_date, departure_date):
        """get bookings for the specified dates
        and confirm that the booking ID from test case 1 is included in the list"""
        nonlocal booking_id
        booked_rooms = bm.Bookings.get_booked_rooms_by_date(arrival_date, departure_date)
        booking_info = []
        for booking in booked_rooms:
            if int(booking[0]) == booking_id:
                booking_info = booking
                break

        # Assert
        assert int(booking_info[0]) == booking_id, f"Test Case 2: assertion failed for booking id: {booking_info[0]} != {booking_id}"
        assert booking_info[1] == cust_id, f"Test Case 2: assertion failed for cust_id: {booking_info[1]} != {cust_id}"
        assert booking_info[2] == room_number, f"Test Case 2: assertion failed for room_number: {booking_info[2]} != {room_number}"
        assert booking_info[3] == arrival_date, f"Test Case 2: assertion failed for arrival_date: {booking_info[3]} != {arrival_date}"
        assert booking_info[4] == departure_date, f"Test Case 2: assertion failed for departure_date: {booking_info[4]} != {departure_date}"
        assert int(booking_info[5]) == expected_cost_per_night, f"Test Case 2: assertion failed for cost_per_night: {booking_info[5]} != {expected_cost_per_night}"
        assert int(booking_info[6]) == expected_total_cost, f"Test Case 2: assertion failed for total_cost: {booking_info[6]} != {expected_total_cost}"


    # run test case 2
    test_get_booked_rooms_by_date(arrival_date, departure_date)

    # test case 3:
    def test_get_all_bookings():
        """get all bookings and confirm the booking ID from test case 1 is included in the list"""
        booking_id = mock_booking[0]
        booked_rooms = bm.Bookings.get_booked_rooms_by_date(arrival_date, departure_date)
        booking_info = None
        for booking in booked_rooms:
            if int(booking[0]) == booking_id:
                booking_info = booking
                break

        # Assert
        assert int(booking_info[0]) == booking_id, f"Test Case 3: assertion failed for booking_id: {booking_info[0]} != {booking_id}"
        assert booking_info[1] == cust_id, f"Test Case 3: assertion failed for cust_id: {booking_info[1]} != {cust_id}"
        assert booking_info[2] == room_number, f"Test Case 3: assertion failed for room_number: {booking_info[2]} != {room_number}"
        assert booking_info[3] == arrival_date, f"Test Case 3: assertion failed for arrival_date: {booking_info[3]} != {arrival_date}"
        assert booking_info[4] == departure_date, f"Test Case 3: assertion failed for departure_date: {booking_info[4]} != {departure_date}"
        assert int(booking_info[5]) == expected_cost_per_night, f"Test Case 3: assertion failed for cost_per_night: {booking_info[5]} != {expected_cost_per_night}"
        assert int(booking_info[6]) == expected_total_cost, f"Test Case 3: assertion failed for total_cost: {booking_info[6]} != {expected_total_cost}"


    # run test case 3
    test_get_all_bookings()

    # test case 4:
    def test_remove_booking(booking_id):
        """remove the booking that was created in test case 1,
        then confirm the room is now available in the dates that were set in test case 1"""
        nonlocal room_number
        book_id = str(booking_id)
        # remove the booking that was created in test case 1
        bm.Bookings.remove_booking(book_id)

        # confirm the room is now available in the dates that were set in test case 1
        available_rooms = bm.Bookings.get_available_rooms_by_date(arrival_date, departure_date)
        assert any(room[0] == room_number for room in available_rooms)


    # run test case 4
    test_remove_booking(booking_id)


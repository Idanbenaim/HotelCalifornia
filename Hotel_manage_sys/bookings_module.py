import datetime
import rooms_module, customers_module


class Bookings:
    ORDER_ID = 100

    def book_room(self, guests, datefrom,
                  dateto):  # [orderID, CustID, RoomID, ArrivalDate, DepartureData, TotalPrice, orderTotal]
        '''add room reservation to the bookings list
        and return customer detail as a list '''
        ORDER_ID += 1


    def book_room_by_room_number(self, room_number, datefrom, dateto):
        '''book a specific room number'''
        pass


    def cancel_booking():
        '''cancel a future room reservation and remove from the bookings list'''
        pass


    def get_all_bookings():
        '''return all room reservations past and future'''
        pass


    def get_booked_rooms_by_date(datefrom, dateto):
        '''return a list of all booked rooms at the specified date range'''
        pass


    def get_available_rooms_by_date(guests, datefrom, dateto):
        '''return a list of all available rooms at a specified date range'''
        booked = get_booked_rooms_by_date(datefrom, dateto)
        inv = get
        inventory()

        # we substruct the booked rooms from the entire inventory of rooms
        total_available = list(set(inv[0]) - set(booked[0]))

        # We filter out rooms which are not suitable for the customer's party size
        net_available = (net_available.remove[i] for i in total_available if i[2] <= guests)

        # we count the number of available rooms from each type
        count_basic = 0
        count - deluxe = 0
        count_suite = 0
        for j in net_available:
            count_basic += 1 if j[4] == 'basic'
            count_deluxe += 1 if j[4] == 'deluxe'
            count_suite += 1 if j[4] == 'suite'

        room_count = {'basic': count_basic,
                      'deluxe': count_deluxe,
                      'suite': count_suite}
        return room_count

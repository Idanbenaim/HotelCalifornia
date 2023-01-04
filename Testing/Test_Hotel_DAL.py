from Hotel_manage_sys import rooms_module, customers_module, bookings_module


#### TESTING ROOM ####

def test_create_get_room():
    r1 = add_room('basic')  # [id, 20, 2, 1, 'Basic', 200, 1]
    r2 = add_room('basic')
    r3 = add_room('deluxe')
    r4 = add_room('deluxe')
    r5 = add_room('suite')
    r6 = add_room('suite')

    print(f'room number is: {r1[0]}')
    assert r1[1] == '20'
    assert r1[2] == '2'
    assert r1[3] == '1'
    assert r1[4] == 'basic'
    assert r1[5] == '200'
    assert r1[6] == '1'

    print(f'room number is: {r3[0]}')
    assert r3[1] == '40'
    assert r3[2] == '4'
    assert r3[3] == '2'
    assert r3[4] == 'deluxe'
    assert r3[5] == '400'
    assert r3[6] == '2'

    print(f'room number is: {r5[0]}')
    assert r5[1] == '60'
    assert r5[2] == '6'
    assert r5[3] == '3'
    assert r5[4] == 'suite'
    assert r5[5] == '600'
    assert r5[6] == '3'

    room_type = get_room_by_type()
    room_list = get_rooms_by_type()
    room_list = get_room_by_room_number()
    room_list = get_inventory()
    room_list = remove_room()


#### TESTING CUSTOMER ####

def test_add_get_cust():  # id, name, address, city, email, age
    joe = __add_cust('Joe Bishop', '123 Main St.', 'San Francisco', 'jb@gmail.com', '47')
    jen = __add_cust('Jennifer Simms', '456 First St.', 'New York', 'js@gmail.com', '32')

    cust_list = __get_cust_list():
    print(cust_list)

    cust = __get_cust_by_name('Joe Bishop'):
    print(f'customer number is: {cust[0]}')
    assert cust[1] == 'Joe Bishop'
    assert cust[2] == '123 Main St.'
    assert cust[3] == 'San Francisco'
    assert cust[4] == 'jb@gmail.com'
    assert cust[5] == '47'

    cust = pkg.modul.__get_cust_by_name('Jennifer Simms'):
    print(f'customer number is: {cust[0]}')
    assert cust[1] == 'Jennifer Simms'
    assert cust[2] == '456 First St.'
    assert cust[3] == 'New York'
    assert cust[4] == 'js@gmail.com'
    assert cust[5] == '32'

    del_cust = test__remove_cust('Joe Bishop'):
    assert __get_cust_by_name('Joe Bishop') == 'No customer with that name'


#### TESTING BOOKINGS ####

def add_get_booking():
    res1 = book_room(custid, guests, datefrom, dateto)

    r1 = add_room('basic')  # [id, 20, 2, 1, 'Basic', 200, 1]
    r2 = add_room('basic')
    r3 = add_room('deluxe')
    r4 = add_room('deluxe')
    r5 = add_room('suite')
    r6 = add_room('suite')

    print(f'room number is: {r1[0]}')
    assert r1[1] == '20'
    assert r1[2] == '2'
    assert r1[3] == '1'
    assert r1[4] == 'basic'
    assert r1[5] == '200'
    assert r1[6] == '1'

    cancel_booking()
    # confirm that a user can cancel only future reservations
    # confirm that a canceled reservation was removed from the bookings list

    get_all_bookings()
    # confirm that the bookings list includes all past and future room reservations

    get_booked_rooms_by_date()
    # confirm that booked rooms at the specified date range show up in the list

    get_available_rooms_by_date()
    # confirm that available rooms at the specified date range show up in the list


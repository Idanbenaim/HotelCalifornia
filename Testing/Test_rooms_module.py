import csv
import Hotel_manage_sys.rooms_module as rm


### read files ###
cust_list = '../database/cust_list.csv'
room_types = '../database/room_types_list.json'
rooms_list = '../database/rooms_list.csv'
bookings = '../database/bookings_list.csv'
booking_id_file = '../database/booking_id_file.txt'



def test_add_room():
    """add a room and confirm it is on the rooms list"""
    room_number = '1001'
    room_type = 'Basic'

    room_info = [room_number, room_type]
    rm.Rooms.add_room(room_info)

    with open(rooms_list, 'r') as rl:
        rm_info = []
        for room in rl:
            room = room.split(',')
            if room[0] == room_number:
                rm_info = room
                break

        assert rm_info[0] == room_info[0]
        assert rm_info[1].strip() == room_info[1]



def test_get_inventory():
    """Add a list of rooms and confirm that all the rooms are added"""
    # set a new rooms list
    room_info = [['101', 'Basic'], ['102', 'Deluxe'], ['103', 'Suite']]
    with open(rooms_list, 'w', newline='') as rl:
        update_room_list = csv.writer(rl)
        update_room_list.writerow(['room_number', 'room_type'])
        for room in room_info:
            update_room_list.writerow(room)

    # get the new rooms list
    rooms = rm.Rooms.get_inventory()

    # iterate over the list and confirm the rooms info is correct
    for i, room in enumerate(rooms):
        if i == 0:
            assert room == ['room_number', 'room_type'], f'Test Case 1 Failed: {rooms}'
        else:
            assert len(room) == 2, f'Test Case 1 Failed: {rooms}'
            assert room[0] in [r[0] for r in room_info], f'Test Case 1 Failed: {rooms}'
            assert room[1] in [r[1] for r in room_info], f'Test Case 1 Failed: {rooms}'



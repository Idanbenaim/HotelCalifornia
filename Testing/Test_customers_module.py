
import Hotel_manage_sys.customers_module as cm


### read files ###
cust_list = '../database/cust_list.csv'
room_types = '../database/room_types_list.json'
rooms_list = '../database/rooms_list.csv'
bookings = '../database/bookings_list.csv'
booking_id_file = '../database/booking_id_file.txt'


def test_add_cust():
    """Test adding a customer"""

    cust_id = '1'
    name = 'John Doe'
    address = '123 Main St'
    city = 'Anytown'
    email = 'john.doe@example.com'
    age = '30'


    cust_info = [cust_id, name, address, city, email, age]
    cm.Customers.add_cust(cust_info)
    with open(cust_list, 'r') as cl:
        customer_info = []
        for customer in cl:
            customer = customer.split(',')
            if customer[0] == cust_id:
                customer_info = customer
                break

        # Assert that the customer info is correct
        assert customer_info[0] == cust_info[0]
        assert customer_info[1] == cust_info[1]
        assert customer_info[2] == cust_info[2]
        assert customer_info[3] == cust_info[3]
        assert customer_info[4] == cust_info[4]
        assert customer_info[5].strip() == cust_info[5]


def test_get_cust_list():
    """set a customer into the customer list, get the customer list and find the customer we just added"""

    # Add a customer to the customer list
    cust_id = '2'
    name = 'Jane Smith'
    address = '456 Park Ave'
    city = 'Anycity'
    email = 'jane.smith@example.com'
    age = '25'

    cust_info = [cust_id, name, address, city, email, age]
    cm.Customers.add_cust(cust_info)


    # Get the full customer list
    with open(cust_list, 'r') as cl:
        customers = cm.Customers.get_cust_list()

        # Assert that the information in the customer list matches the info added to the list
        customer_info = []
        for customer in cl:
            customer = customer.split(',')
            if customer[0] == cust_id:
                customer_info = customer
                break
        assert customer_info[0] == cust_info[0]
        assert customer_info[1] == cust_info[1]
        assert customer_info[2] == cust_info[2]
        assert customer_info[3] == cust_info[3]
        assert customer_info[4] == cust_info[4]
        assert customer_info[5].strip() == cust_info[5]


def test_remove_customer():
    """add a customer to the list, remove the customer, then confirm it is not in it"""
    # Add a customer to the customer list
    cust_id = '1'
    name = 'John Doe'
    address = '123 Main St'
    city = 'Anytown'
    email = 'john.doe@example.com'
    age = '30'

    cust_info = [cust_id, name, address, city, email, age]
    cm.Customers.add_cust(cust_info)

    # Remove customer from the customer list
    cust_list = cm.Customers.get_cust_list()
    cm.Customers.remove_customer(cust_id)
    # read the list again and confirm the customer was removed
    cust_list = cm.Customers.get_cust_list()
    assert cust_id not in [cust[0] for cust in cust_list]




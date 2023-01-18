import csv
import database
# from database import *

#### read file ####
cust_list = '/Users/idanbenaim/PycharmProjects/HotelCalifornia/database/cust_list.csv'


#### customer management sys ###

class Customers:
    def __init__(self, cust_id, name, address, city, email, age):
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self.city = city
        self.email = email
        self.age = age

    def __str__(self):
        pass

    def add_cust(cust_info: list):
        """gets a customer info from add_customer_cli as a list.
    here we use the list to add the customer's info to the cust_list file"""

        with open(cust_list, 'a', newline='') as cl:
            writer = csv.writer(cl)
            if cl.tell() == 0:  # Check if the file is empty
                writer.writerow(['cust_id', 'name', 'address', 'city', 'email', 'age'])  # Write column names
            writer.writerow(cust_info)

    def get_cust_list():
        """returns the full customer list as list of lists"""
        customers = []
        with open(cust_list, 'r') as cl:
            reader = csv.reader(cl)
            for row in reader:
                customers.append(row)
        return customers

    def remove_customer(cust_id):
        """receives the customer ID and removes it from the customes list"""
        with open(cust_list, "r") as cl:
            csv_reader = csv.reader(cl)
            customers = list(csv_reader)

        for customer in customers:
            if customer[0] == cust_id:
                customers.remove(customer)
                with open(cust_list, "w") as new_cl:
                    csv_writer = csv.writer(new_cl)
                    csv_writer.writerows(customers)
                break


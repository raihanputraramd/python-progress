import os
import json
from models.customer import Customer

class CustomerService:
    def __init__(self):
        self.customers = []
        self.next_id = 1
    
    
    def add_customer(self, name):
        customer = Customer(self.next_id, name)
        self.customers.append(customer)
        self.next_id += 1
    
    
    def list_customers(self):
        for customer in self.customers:
            print(customer)
    
    
    def find_customer_by_id(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        
        return None
    
    
    def save_to_file(self, filename="customers.json"):
        with open(filename, "w") as f:
            json.dump([cust.to_dict() for cust in self.customers], f)

    def load_from_file(self, films, filename="customers.json"):
        if not os.path.exists(filename):
            self.customers = []
            return

        with open(filename, "r") as f:
            content = f.read().strip()
            if not content:
                self.customers = []
                return

            try:
                data = json.loads(content)
                self.customers = []
                for d in data:
                    customer = Customer(d['id'], d['name'])
                    for film_id in d.get('rented_film_ids', []):
                        for film in films:
                            if film.id == film_id:
                                customer.rent(film)
                                break
                    self.customers.append(customer)
                self.next_id = max(c.id for c in self.customers) + 1 if self.customers else 1
            except json.JSONDecodeError:
                print(f"File '{filename}' tidak valid.")
                self.customers = []
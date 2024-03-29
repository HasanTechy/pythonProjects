class Customer:
    def __init__(self, name, surname, father_name, fin, age):
        self._name = name
        self._surname = surname
        self._father_name = father_name
        self._fin = fin
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        self._surname = surname

    def get_father_name(self):
        return self._father_name

    def set_father_name(self, father_name):
        self._father_name = father_name

    def get_fin(self):
        return self._fin

    def set_fin(self, fin):
        self._fin = fin

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def to_dict(self):
        return {
            'name': self._name,
            'surname': self._surname,
            'father_name': self._father_name,
            'fin': self._fin,
            'age': self._age
        }


customers = {}
existing_fins = set()


class IDGenerator:
    def __init__(self):
        self.counter = 1

    def generate_id(self):
        id_value = self.counter
        self.counter += 1
        return id_value


def generate_unique_id(id_generator = IDGenerator()):
    return id_generator.generate_id()


def input_numeric(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a numeric value.")


def input_fin(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and len(value) == 7:
            return value
        else:
            print("Invalid input. Please enter a 7-digit numeric value.")


def add_customer():
    name = input("Enter the customer's name: ")
    surname = input("Enter the customer's surname: ")
    father_name = input("Enter the customer's father name: ")
    fin = input_fin("Enter the customer's FIN: ")
    age = input_numeric("Enter the customer's age: ")

    if fin in existing_fins:
        print("FIN already exists. Please enter a unique FIN.")
        return

    existing_fins.add(fin)

    customer = Customer(name, surname, father_name, fin, age)
    customer_id = generate_unique_id()
    customers[customer_id] = customer

    print("Customer added successfully.")


def get_all_customers():
    if customers:
        print("All Customers:")
        for customer_id, customer in customers.items():
            print(f"Customer ID: {customer_id}")
            print(f"Name: {customer.get_name()}")
            print(f"Surname: {customer.get_surname()}")
            print(f"Father Name: {customer.get_father_name()}")
            print(f"FIN: {customer.get_fin()}")
            print(f"Age: {customer.get_age()}")
            print()
    else:
        print("No customers found.")


def update_customer():
    customer_id = int(input("Enter the customer ID to update: "))

    if customer_id in customers:
        customer = customers[customer_id]

        name = input("Enter the updated name: ")
        surname = input("Enter the updated surname: ")
        father_name = input("Enter the updated father name: ")
        fin = input_numeric("Enter the updated FIN: ")
        age = input_numeric("Enter the updated age: ")

        customer.set_name(name)
        customer.set_surname(surname)
        customer.set_father_name(father_name)
        customer.set_fin(fin)
        customer.set_age(age)

        print("Customer updated successfully.")
    else:
        print("Customer not found.")


def delete_customer():
    customer_id = int(input("Enter the customer ID to delete: "))

    if customer_id in customers:
        del customers[customer_id]
        print("Customer deleted successfully.")
    else:
        print("Customer not found.")
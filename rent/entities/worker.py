
from entities.Customer import Customer


class Worker(Customer):
    def __init__(self, name, surname, father_name, fin, age, position):
        super().__init__(name, surname, father_name, fin, age)
        self._position = position

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def to_dict(self):
        return {
            'name': self._name,
            'surname': self._surname,
            'father_name': self._father_name,
            'fin': self._fin,
            'age': self._age,
            'position': self._position
        }


workers = {}
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


def add_worker():
    name = input("Enter the worker's name: ")
    surname = input("Enter the worker's surname: ")
    father_name = input("Enter the worker's father name: ")
    fin = input_fin("Enter the worker's FIN: ")
    age = input_numeric("Enter the worker's age: ")
    position = input("Enter the worker's position: ")

    if fin in existing_fins:
        print("FIN already exists. Please enter a unique FIN.")
        return

    existing_fins.add(fin)

    worker = Worker(name, surname, father_name, fin, age, position)
    worker_id = generate_unique_id()
    workers[worker_id] = worker

    print("Worker added successfully.")


def get_all_workers():
    if workers:
        print("All Workers:")
        for worker_id, worker in workers.items():
            print(f"Worker ID: {worker_id}")
            print(f"Name: {worker.get_name()}")
            print(f"Surname: {worker.get_surname()}")
            print(f"Father Name: {worker.get_father_name()}")
            print(f"FIN: {worker.get_fin()}")
            print(f"Age: {worker.get_age()}")
            print(f"Position: {worker.get_position()}")
            print()
    else:
        print("No workers found.")


def update_worker():
    worker_id = int(input("Enter the worker ID to update: "))

    if worker_id in workers:
        worker = workers[worker_id]

        name = input("Enter the updated name: ")
        surname = input("Enter the updated surname: ")
        father_name = input("Enter the updated father name: ")
        fin = input("Enter the updated FIN: ")
        age = input("Enter the updated age: ")
        position = input("Enter the updated position: ")

        worker.set_name(name)
        worker.set_surname(surname)
        worker.set_father_name(father_name)
        worker.set_fin(fin)
        worker.set_age(age)
        worker.set_position(position)

        print("Worker updated successfully.")
    else:
        print("Worker not found.")


def delete_worker():
    worker_id = int(input("Enter the worker ID to delete: "))

    if worker_id in workers:
        del workers[worker_id]
        print("Worker deleted successfully.")
    else:
        print("Worker not found.")
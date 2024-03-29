class Car:
    def __init__(self, model, max_speed, year, horsepower):
        self._model = model
        self._max_speed = max_speed
        self._year = year
        self._horsepower = horsepower

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        self._max_speed = max_speed

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_horsepower(self):
        return self._horsepower

    def set_horsepower(self, horsepower):
        self._horsepower = horsepower

    def to_dict(self):
        return {
            'model': self._model,
            'max_speed': self._max_speed,
            'year': self._year,
            'horsepower': self._horsepower
        }


cars = {}


class IDGenerator:
    def __init__(self):
        self.counter = 1

    def generate_id(self):
        id_value = self.counter
        self.counter += 1
        return id_value


def generate_unique_id(id_generator=IDGenerator()):
    return id_generator.generate_id()


def input_numeric(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter a numeric value.")


def add_car():
    model = input("Enter the car's model: ")
    max_speed = input_numeric("Enter the car's maximum speed: ")
    year = input_numeric("Enter the car's year: ")
    horsepower = input_numeric("Enter the car's horsepower: ")

    car = Car(model, max_speed, year, horsepower)
    car_id = generate_unique_id()
    cars[car_id] = car

    print("Car added successfully.")


def get_all_cars():
    if cars:
        print("All Cars:")
        for car_id, car in cars.items():
            print(f"Car ID: {car_id}")
            print(f"Model: {car.get_model()}")
            print(f"Max Speed: {car.get_max_speed()}")
            print(f"Year: {car.get_year()}")
            print(f"Horsepower: {car.get_horsepower()}")
            print()
    else:
        print("No cars found.")


def update_car():
    car_id = int(input("Enter the car ID to update: "))

    if car_id in cars:
        car = cars[car_id]

        model = input("Enter the updated model: ")
        max_speed = input_numeric("Enter the updated maximum speed: ")
        year = input_numeric("Enter the updated year: ")
        horsepower = input_numeric("Enter the updated horsepower: ")

        car.set_model(model)
        car.set_max_speed(max_speed)
        car.set_year(year)
        car.set_horsepower(horsepower)

        print("Car updated successfully.")
    else:
        print("Car not found.")


def delete_car():
    car_id = int(input("Enter the car ID to delete: "))

    if car_id in cars:
        del cars[car_id]
        print("Car deleted successfully.")
    else:
        print("Car not found.")

from entities.Car import Car, add_car, get_all_cars, update_car, delete_car
from entities.Customer import Customer, get_all_customers, add_customer, update_customer, delete_customer
from entities.Worker import Worker, add_worker, get_all_workers, update_worker, delete_worker

def main():
    logged_in = login()

    if not logged_in:
        print("Login failed. Exiting the program.")
        return

    while True:
        print("\nMenu:")
        print("1. Add a new car")
        print("2. Get all cars")
        print("3. Update car details")
        print("4. Delete a car")
        print("5. Add a new customer")
        print("6. Get all customers")
        print("7. Update customer details")
        print("8. Delete a customer")
        print("9. Add a new worker")
        print("10. Get all workers")
        print("11. Update worker details")
        print("12. Delete a worker")
        print("13. Search")
        print("14. Exit")

        choice = input("Enter your choice: ")
        print("---------------------------------")

        if choice == "1":
            add_car()
        elif choice == "2":
            get_all_cars()
        elif choice == "3":
            update_car()
        elif choice == "4":
            delete_car()
        elif choice == "5":
            add_customer()
        elif choice == "6":
            get_all_customers()
        elif choice == "7":
            update_customer()
        elif choice == "8":
            delete_customer()
        elif choice == "9":
            add_worker()
        elif choice == "10":
            get_all_workers()
        elif choice == "11":
            update_worker()
        elif choice == "12":
            delete_worker()
        elif choice == "13":
            while True:
                print("\nSearch Options:")
                print("1. Filter Cars")
                print("2. Filter Customers")
                print("3. Filter Workers")
                print("4. Back")

                choice = input("Enter your choice: ")

                if choice == "1":
                    filter_cars()
                elif choice == "2":
                    filter_customers()
                elif choice == "3":
                    filter_workers()
                elif choice == "4":
                    return
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "14":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def filter_cars():
    filter_criteria = input("Enter the search criteria: ")

    filtered_cars = [
        car
        for car in cars.values()
        if (
            filter_criteria.lower() in car.get_model().lower()
            or filter_criteria.lower() == str(car.get_max_speed())
            or filter_criteria.lower() == str(car.get_year())
            or filter_criteria.lower() == str(car.get_horsepower())
        )
    ]

    if filtered_cars:
        print("Filtered Cars:")
        for car in filtered_cars:
            print(f"Model: {car.get_model()}")
            print(f"Max Speed: {car.get_max_speed()}")
            print(f"Year: {car.get_year()}")
            print(f"Horsepower: {car.get_horsepower()}")
            print()
    else:
        print("No cars found matching the search criteria.")


def filter_customers():
    filter_criteria = input("Enter the search criteria: ")

    filtered_customers = [
        customer
        for customer in customers.values()
        if (
            filter_criteria.lower() in customer.get_name().lower()
            or filter_criteria.lower() in customer.get_surname().lower()
            or filter_criteria.lower() in customer.get_father_name().lower()
            or filter_criteria.lower() == customer.get_fin()
            or filter_criteria.lower() == str(customer.get_age())
        )
    ]

    if filtered_customers:
        print("Filtered Customers:")
        for customer in filtered_customers:
            print(f"Name: {customer.get_name()}")
            print(f"Surname: {customer.get_surname()}")
            print(f"Father Name: {customer.get_father_name()}")
            print(f"FIN: {customer.get_fin()}")
            print(f"Age: {customer.get_age()}")
            print()
    else:
        print("No customers found matching the search criteria.")


def filter_workers():
    filter_criteria = input("Enter the search criteria: ")

    filtered_workers = [
        worker
        for worker in workers.values()
        if (
            filter_criteria.lower() in worker.get_name().lower()
            or filter_criteria.lower() in worker.get_surname().lower()
            or filter_criteria.lower() in worker.get_father_name().lower()
            or filter_criteria.lower() == worker.get_fin()
            or filter_criteria.lower() == str(worker.get_age())
            or filter_criteria.lower() in worker.get_position().lower()
        )
    ]

    if filtered_workers:
        print("Filtered Workers:")
        for worker in filtered_workers:
            print(f"Name: {worker.get_name()}")
            print(f"Surname: {worker.get_surname()}")
            print(f"Father Name: {worker.get_father_name()}")
            print(f"FIN: {worker.get_fin()}")
            print(f"Age: {worker.get_age()}")
            print(f"Position: {worker.get_position()}")
            print()
    else:
        print("No workers found matching the search criteria.")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "admin":
        return True
    else:
        return False


if __name__ == "__main__":
    main()
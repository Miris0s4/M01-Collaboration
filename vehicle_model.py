#Miriana Martinez-sosa
#4/3/2025
#this program will accept user input for a car model.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#subclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
#parent class with vehicle type
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
#the vehicle year, make, model, doors, and type of roof
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Main app to get user input and display vehicle information
def main():
    print("Enter the details for the car:")

    vehicle_type = "car"

#this will be the users input
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")
#automobile object
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    car.display_info()
#running the program
if __name__ == "__main__":
    main()
class Car:
    doors = 2
    wheels = 4
    engine = True

    def __init__(self, make, model, year="2023"):
        self.make = make
        self.model = model
        self.year = year
        self.is_moving = False
        self.gas = 100

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model

    def stop(self):
        if self.is_moving:
            print("The car has stopped.")
            self.is_moving = False
        else:
            print("The car has already stopped")

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print("The car starts moving")
                self.is_moving = True
            print(f"The car is going {speed}")
        else:
            print("You have run out of gas.")
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True


class dealership:
    def __init__(self):
        self.cars = []

    def __iter__(self):
        yield from self.cars

    def add_car(self, car):
        self.cars.append(car)


car_1_dream = Car("Mercedes", "Benz")
car_2_dream = Car("Ford", "Fusion")
car_3_dream = Car("Nissan", "freero")
car_4_dream = Car("Toyota", "Prius")

if car_1_dream == car_2_dream:
    print("Equal")
else:
    print("not equal")


my_dealership = dealership()
my_dealership.add_car(car_1_dream)
my_dealership.add_car(car_2_dream)
my_dealership.add_car(car_3_dream)
my_dealership.add_car(car_4_dream)
for car in my_dealership:
    print(car)

print(f"The car has {Car.doors} doors")


print(car_2_dream.year)
print(car_1_dream.year)
print(car_1_dream.model)
print(car_2_dream.make)

car_1_dream.stop()
car_1_dream.go("slow")
car_1_dream.go("fast")
car_1_dream.stop()
car_1_dream.stop()
print(str(car_1_dream))
print(str(car_2_dream))

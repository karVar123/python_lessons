class Car:

    def __init__(self, name, door_quantity, chairs_quantity, wheels_quantity, max_speed):
        self.name = name
        self.door = door_quantity
        self.chairs = chairs_quantity
        self.wheels = wheels_quantity
        self.max_speed = max_speed

    def run(self, name):
        if name:
            print("the device is on")
        else:
            print("the device is off")
        return self.name + " is running"


bmw = Car("BMW", 2, 5, 4, 240)
audi = Car("AUDI", 2, 5, 4, 241)

if bmw.max_speed > audi.max_speed:
    print("bmw is faster")
else:
    print("audi is faster")


def some_name(x, y):
    return x + y


print(some_name(1, 2))
print(bmw.run(name=""))
print(audi.run(name=""))

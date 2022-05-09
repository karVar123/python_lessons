class Car():
    def __init__(self, model, door_quantity):
        self.model = model
        self.door_quantity1 = door_quantity

    def __go(self):
        return "go " + self.model

    def stop(self):
        return "stop " + self.model


class Audi(Car):

    def __init__(self, mode, quantity_door, hp):
        self.model = mode
        self.hp = hp
        self.door_quantity1 = quantity_door

    def go(self):
        self.model
        pass

    def stop(self):
        return 354354687564164 + 4845345


object_audi = Car("Audi", 2)
object_opel = Car("Opel", 4)
object_porsche = Car("Porsche", 2)

print(object_audi.stop())
print("-------------------------------------")

object_audi1 = Audi("object Audi", 4, 150)
print(object_audi1.model)
print(object_audi1.door_quantity1)
print(object_audi1.hp)
# print(object_audi1.go())
print(object_audi1.stop())

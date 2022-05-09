class Home:
    __room_quantity = 1

    def __init__(self):
        pass

    def __get_room_quantity(self):
        return self.__room_quantity

    def sum_fun(self):
        return self.__get_room_quantity()

    def set_room_quantity(self, param):
        self.__room_quantity = self.__room_quantity + param

    def fun1(self):
        return "fun 1 is working "

    def fun2(self):
        print(self.fun1())
        return "fun 2 is working "

    def fun3(self):
        return "fun 3 is working "

    def fun4(self):
        return "fun 4 is working "

    class __Room:
        def __init__(self):
            pass

        room = 15

        def get_room(self):
            return self.room


home = Home()

# print(home.__get_room_quantity())
home.set_room_quantity(4)
# print(home.get_room_quantity())
room = Home.Room()
home.sum_fun()

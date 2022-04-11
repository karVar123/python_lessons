#  oop

a = 15
b = "hi"
print(type(a))
print(type(b))


class MyType:
    value = "value"
    description = "description"
    abc = 15678


my_type = MyType()
my_type1 = MyType()
print(my_type.value)
print(my_type.description)
print(my_type.abc)
print(MyType.abc + 1000000)

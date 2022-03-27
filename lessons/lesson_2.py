# lesson 2
# types

integer = int
float = float
string = str
boolean = bool

#   comment
my_int = 15  # int
my_float = 3.0  # float
my_str = "11"  # str String
my_bool = False  # bool Boolean
is_True = 15 < 14

# print("հարց", is_True)

# գումարում
print(my_int + my_int)

# հանում
print(my_int - my_int)

# բազմապատկում
print(my_int * my_int)

# բաժանում /
print(my_int / 5)

# բաժանում //
print(18 // 5)

# աստիճանի բարձրացում **
print(5 ** 2)

#  մնացորդի վերադանձ
print(10 % 2)

# համեմատության օպերատորներ
# ցանկացած համամատւտըան գործողություն վերադարձնում է bool տիպի արժեք ,  (True | False)

# մեծ
print(15 > 15)  # True False

# փոքր
print(15 < 3)  # True False

#  հավասար
print(15 == 3)

# մեծ հավասար
print(17 >= 16)  # True False

# փոքր հավասար
print(15 <= 14)  # True False

#  հավասար չէ
print(15 != 15)  # True False

# համեմատության թեորեմ
# եթե  (if)

if 15 >= 116:
    print("Big")
else:
    print("Small")

# int ,float
print(my_int + my_float)  # int + float = float
print(my_int + my_float)  # int + int = int
print(my_float + my_float)  # float + float = float

# str String
print(my_str + my_int)  # str+ int = error
print(my_str + my_float)  # str+ float = error
print(my_str + my_str)  # str + str = str

my_num = 15465467 + 1

if my_num % 2 == 0:
    print("զույգ", True)
else:
    print("Կենտ", False)

if my_num % 2 != 0:
    print("Կենտ", True)
else:
    print("զույգ", False)

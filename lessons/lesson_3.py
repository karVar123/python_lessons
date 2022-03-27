# Lesson 3
# if, elsif, else, and, or

# if
#  պայմանի օպերատոր

a = 15
c = 15
b = 15

isTrue = a > b or b == c
print(isTrue)

# and || or
# and
"""
    t and t -> t  true
    f and t -> f  false
    t and f -> f  false
    f and f -> f  false
"""
# or
"""
    t = t == t  true 
    f = t == t  true 
    t = f == t  true 
    f = f == f  false
"""

a = 111
b = 19
c = 20

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(b)
elif a == b or b == c or a == c:
    print("թվերըից մեկը հավասատ\nստւգեք")
else:
    print("անհասկանալի")



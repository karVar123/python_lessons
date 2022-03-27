odd_list = []
even_list = []

for i in range(0, 10001):
    if i % 2 == 0:
        # even number
        even_list.append(i)
    else:
        # odd number
        odd_list.append(i)

print("Odd numbers list\n", odd_list)
print("Even numbers list\n", even_list)

num3list = []
num5list = []

for i in range(0, 101):
    if i % 3 == 0:
        num3list.append(i)
    elif i % 5 == 0:
        num5list.append(i)

print("num 3 list", num3list)
print("num 5 list", num5list)

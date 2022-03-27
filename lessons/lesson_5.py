# lesson 5
#  for while

# for loop
for i in range(10, 16000, 100):
    print(i)

start_num = int(input("start num "))
end_num = int(input("end num "))

# while loop
my_bool = True
my_num = 15
while my_bool:
    print(my_num)
    my_num = my_num + 1
    if my_num > 100:
        my_bool = False

for i in range(15):
    if i % 2 == 0:
        print(i)

# for
for i in range(0, 16):
    if i % 2 != 0:
        print(i)

num = 0
while num < 101:
    print(num)
    num = num + 1

sum_of_num = 0
for i in range(0, 100):
    sum_of_num = sum_of_num + i

print(sum_of_num)

a = int(input("factorial - "))

for i in range(1, a):
    print(i)

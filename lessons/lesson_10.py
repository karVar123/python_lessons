# String and functions

my_str = "Some str"
a = 15
b = 20
print("upper", my_str.upper())
print("lower", my_str.lower())
print("capitalize", my_str.capitalize())
print("title", my_str.title())
print("isupper", my_str.isupper())
print("islower", my_str.islower())
print("format", "abcd {}  , abcd {}".format(a, b))
print("Lorem Ipsum is simply dummy text of the printing and typesetting industry."
      " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
      " when an unknown printer took a galley of type and scrambled it to make a type specimen book."
      " It has survived not only five centuries, but also the leap into electronic typesetting,"
      " remaining essentially unchanged. It was popularised in the 1960s with the release of"
      " Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software"
      " like Aldus PageMaker including versions of Lorem Ipsum.".split("dummy"))

# fibonacci sequence
# [0,1,1,2,3,5,8,13,21...]

num = int(input("type number for fib sequence - "))
fib_list = [0, 1]
fib_1 = 0
fib_2 = 1
sum_of_fib = 0
for i in range(1, num + 1):
    sum_of_fib = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = sum_of_fib
    fib_list.append(fib_2)
print(fib_list)

minColl = 0
for i in range(0, len(fib_list) - 1):
    if fib_list[i] > minColl:
        minColl = fib_list[i]

print(minColl)

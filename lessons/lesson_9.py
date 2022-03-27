my_num = 124454
my_num = str(my_num)

# print(my_num[0])


for i in range(100000,999999):
    i = str(i)
    sum1 = int(i[0]) + int(i[1]) + int(i[2])
    sum2 = int(i[3]) + int(i[4]) + int(i[5])
    if sum1 == sum2:
        print(i)

"""
    գրն - 16,74
    ռուբ - 3,47
    դոլար - 502,15 
"""

print("1 - rub ")
print("2 - grn ")
print("3 - dollar ")

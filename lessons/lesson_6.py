# # lesson 6
#
# #  թվերի գումառը
# # end_num = int(input())
# # sum_of_number = 0
# # for i in range(0, end_num + 1):
# #     sum_of_number = sum_of_number + i
# # print(sum_of_number)
#
# #  factorial
# # end_num = int(input())
# # sum_of_number = 1
# # for i in range(1, end_num + 1):
# #     sum_of_number = sum_of_number * i
# #     print(sum_of_number)
#
# # list
#
#
# someList = [0.01, 15, 1.2, 1, 15, 15, 1, 5, 748, 78, 78, 425, 154, 14545, 15, 2, 2 + 1845000]
#
# elemList = 0.0001
# for i in range(0, len(someList)):
#     if elemList < someList[i]:
#         elemList = someList[i]
#     else:
#         continue
# print(elemList)
#
# my_int = 15455645
# my_str = str(my_int)
# print(type(my_str))
#
# print(my_str[5])
#
# my_int = int(my_str)
# print(type(my_int))
#


list_1 = [1, 2, 3, 4, 7, 8, 9, 5, 1, 58, 6, 3, 15]

# for i in range(1, 10):
#     if i % 2 == 0:
#         list_1.append(i)

# print(list_1.copy())
# list_2 = list_1.copy()

list_1.sort()
print(list_1)
list_1.reverse()
print(list_1[0])


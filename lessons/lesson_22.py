# my_file = open('C:\Users\Admin\Desktop\python.txt', encoding="utf-8")
my_file = open('lesson_1.py', 'a+', encoding="utf-8")
print(my_file.read())
my_file.seek(0)
print(my_file.readline())
# my_file.write("""
# #
# # lesson 1
# a = 15
# b = 18
#
# print(a + b)
#
# """)

my_file.close()

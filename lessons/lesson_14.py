#  function

#   def - function
#     name of function
#       ():
#       (param):

def division(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 // num2
    elif type(num1) == float and type(num2) == float:
        return num1 / num2
    else:
        return "type error"


def testFun():
    a = 15 + 469


print(division(15, 78))
print(division(879.0, 112.0))
print(division(27452, 1234))

a = division(15, 7)
b = testFun()

print(a)
print(b)

question_1 = str(input("question_1"))
question_2 = str(input("question_2"))
question_3 = str(input("question_3"))
question_4 = str(input("question_4"))


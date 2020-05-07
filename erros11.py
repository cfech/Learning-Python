# def div42by(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error, you tried to divide by zero')


# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))


print("how many cats do your have ?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("thats alot of cats ")
    else:
        print("not too many ")
except ValueError:
    print(" you did not enter a number")

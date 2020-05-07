# name = ""
# while name != "your name":
#     print("pleae type your name ")
#     name = input()
# print("ty")

spam = 0
while spam<5:
    spam = spam +1
    if spam == 3:
        continue ## causses  the function to jumpy back to the top, never getting to iteration 3 ,thus pring 1, 2, 4,5,
    print("spam is " + str(spam))
    
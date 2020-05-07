name = "bob"
age = 3000
if name == "alice":
    print("Hello alice")
elif age < 12:
    print("your not alice kiddo")
elif age > 2000:
    print("unlike you alice is not a vampire ")
elif age > 100:
    print("you are not alice")

# print ("enter name")
# name = input() #name is truthy 
# if name:
#     print("thanks")
# else:
#     print("you didnt enter a name")

password = "swordfish"
if password == "swordfish":
    print("Access granted")
else:
    print("wrong password")


#The bool function tells us whether something is  truthy or falsy
#Will return false 
bool(0)

#Will return true
bool(1)

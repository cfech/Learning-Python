# This program says hello and what is your name 
print("hello world")
#Ask for the persons name 
print("what is your name?")
myName = input()
print ('iIt is good to meet you' +myName)
print('the length of yor name is:')
print(len(myName))
print("what is your age?")
myAge = input()

#Str = string , int = to integer to add one then back to a string 
print("You will be " + str(int(myAge)+ 1) + ' in a year')
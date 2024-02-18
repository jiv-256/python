a = input("Enter your name: ")
print(a) 
print(type(a)) #output -> <class 'str'>
  
'''
note : Everytime you use this input funtion it allows user to take input from the keyboard as a string and the output is always a string if you have to take a integer as an input so you have to convert it by typecasting
'''
b = input("Enter your AGE: ")
b = int(b) # Convert b to an Integer(if possible)
print(b) 
print(type(b)) #output -> <class 'int'>

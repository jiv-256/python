# String is a data type in python , sting is a sequence of characters enclosed in quotes
a = 34
b = "rajiv"
print(a ,b) #output -> 34 rajiv

# we can write a string in three ways
a = 'rajan'
b = "yajan"
c = '''prajan'''

# String Concatination

greeting = "hii , "
name = "harijan pandey"

# print(greeting + name) #output -> hii , harijan pandey
                    
                    # OR

c = greeting + name
print(c) #output -> hii , harijan pandey

# String Slicing(sting is treated as array of letters)
name = "parijan pandey"
print(name[5]) #output=>a
# name[5] = "r" ---> does not work

print(name[0:5]) #output=>parij (we get from 0 to 4)

'''
Negative indices - it is use to access the string element by negative index no , it always start from -1 not zero
'''
name = "parijan pandey"
print(name[-4:-1]) #output=>nde (we get from 11 to 13)
'''                                    ____________
p   a   r   i   j   a   n       p   a |  n   d   e | y
-14 -13 -12 -11 -10 -9  -8  -7 -6  -5 |-4  -3   -2 | -1
                                      _____________
'''
# Slicing with skip value
name = "rajivisgoodboy"
d = name[0::3]
print(d) #output->risoo  (skip 2 characters)

# Strings Functions
story ="their was a boy name sumit, who study in cambrige university of arizona and he loves playing guitar, he was also passonate about programming languages"

print(len(story)) #output-> 150
print(story.endswith("are")) #output-> False (check wheather the story is ending with given string or not)
print((story.count("s"))) #output-> 10
print((story.count("he"))) #output-> 3
print((story.capitalize())) # make first word capital
print((story.find("sumit"))) # output-> 21 (tell that sumit is present on which index value)
print((story.find("once"))) # output-> -1 (-1 means not present)
print((story.replace("sumit","harshit"))) # output-> their was a boy name harshit, who study in cambrige university of arizona and he loves playing guitar, he was also passonate about programming languages (replaces all occurance of sumit with harshit)

# Escape sequence character
'''
\n -> for new line
\t -> for tab
\' -> single quote
\\ -> one backslash
'''
print("he is a good \n boy") 
'''
output->he is a good 
 boy
'''
# questions
'''
Q1)write a python program to display a user centered name followed by good affternoon using input() function?
ans)
        name = input("enter your name here: ")
        print("good afternoon",name)

Q2) WAP program to fill in a letter template given below with name and date.
'''
name = input("enter your name here: ")
Date = input("enter the date here: ")

letter = '''Dear </name>,
                you are selected!
                </Date>'''
print(letter-=)
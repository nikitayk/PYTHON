ques 1. take name as input and print that with good afternonn
( concept of f string)

name = input("Enter your name :")
print (f" Good afternoon,{name}")
# use of f before the double quotes and put the curly braces before writing the var name from which you want the value


ques 2. in the following temp. write name and date 
letter = '''
         Dear <|Name|>,
         You are selected!
         <|Date|>
#         '''

name = input("enter name: ")
date = input("date:")
print (f"Dear {name}, \n You are selected! \n {date}")


METHOD 2
letter = '''
         Dear <|Name|>,
         You are selected!
         <|Date|>
        '''
print(letter.replace ("<|Name|>", "Bitch").replace("<|Date|>", "24 JAN"))

quest 3. find the double space in a string 

a = " Oh what are  you doing?"
print(a.find("  "))
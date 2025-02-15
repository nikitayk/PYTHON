name = 'harry' 
# THIS IS A STRING, single quote or double quote or for multi line string it could be triple quotes
# string is a data type, sequence of characters, IMMUTABLE 

# Slicing 
nameshot = name[0:4] # start index from 0 all the way to 4 excluding 4
print(nameshot)
chara = name[2] # printed one character which was at index 2
print(chara)

abc = name[ : 2]  # if nothing is written then zero
abc = name [ 2 : ]  # if nothing then (length)

# slicing with skip values
a = "84736527283"
print(a[1:6:2]) # starts from 1, ends at 5 with gap of 2


# STRING FUNCTIONS 
len()
#here variable will be whatever you decide to name it within the limitations of variable
variable = "LOVELY"
variable.endswith("ey")   # gives true false
variable.startswith("ey")
variable.capitalize()
variable.replace("good", "bad") # replaces the word good with bad at all places

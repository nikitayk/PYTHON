# ques 1. create a dict which gives meaning

words = {
    "kutta" :"dog",
    "billi" :"cat",
}
word = (input("enter the word you want to search:"))
print(words[word])

#ques 2. write a program to input eight numbers from the user and display all the unique number once

numbers = set((
    int(input("Enter first number: ")),
    int(input("Enter second number: ")),
    int(input("Enter third number: ")),
    int(input("Enter fourth number: ")),
    int(input("Enter fifth number: ")),
    int(input("Enter sixth number: ")),
    int(input("Enter seventh number: ")),
    int(input("Enter eighth number: "))
))

print(numbers)

# # ques3. can we have 18 as a int and 18 as a str

s = set()
s.add(18)
s.add("18")
print(s)

# ques 4.  INTERESTING INTERVIEW QUES

s = set()
s.add(20)   #int
s.add(20.0)   # float
s.add("20")    # str
print(len(s))

# it will give output as two because FOR PYTHON 20 == 20.0


# ques5. what is the type of s?
s = {}

ITS NOT A SET, IT IS A DICTIONARY

#ques6. create empty dict. allow four friends to enter their fav lang as value and key as name. assume names to be unique. what would happen if 2 names or lang are same 

subject = {}
name = (input("enter the name 1 :"))

name2 = (input("enter the name 2 :"))

name3 =(input("enter the name 3 :"))

name4 = (input("enter the name 4 :"))


lang = (input("enter the lang 1 :"))

lang2 = (input("enter the lang 2 :"))

lang3 =(input("enter the lang 3 :"))

lang4 = (input("enter the lang 4 :"))


subject[name] = lang
subject[name2] = lang2
subject[name3] = lang3
subject[name4] = lang4

# METHOD 2 
subject.update({name: lang})

print(subject)

# when name 1 and name are same only name 2 is printed, KEY IS UPDATED

# when lang 1 and lang 2 are same, all four gets printed


# ques. can you changw the values inside a list whivh is contained in a set 

S = {8,7,12,"harry", [1,2]}

cant:  list cannot be included in a set because set is not indexed and list is

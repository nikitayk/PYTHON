# 1. Write a program using functions to find greatest of three numbers.

def maxnumber():
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter first number:"))
    n3 = int(input("Enter first number:"))

    if(n1> n2 and n1 > n3):
        print("the greatest nmber is", n1)

    if(n2> n1 and n2 > n3):
        print("the greatest nmber is", n2)

    if(n3> n2 and n3 > n1):
        print("the greatest nmber is", n3)

maxnumber()

    
# 2. Write a python program using function to convert Celsius to Fahrenheit.

def conversion(f):
    c = 5*(f-32)/9
    return c

f = int(input("enter number :"))
print(conversion(f))


# 3. How do you prevent a python print() function to print a new line at the end.


print("a")
print("b", end="")
print("c", end="")

# 4. Write a recursive function to calculate the sum of first n natural numbers.
'''
RECURSION : finding formula?

sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(4) = 1+2+3+4
sum(n) = 1+2+3..............+n
ORRRRRRRRRRRRRRRRRR
sum(n) = sum(n-1) +n

'''
def summax(n):
    if(n==1):
        return 1   # because we dont want it to go to the negatives
    return summax(n-1) + n



n = int(input("enter the number :"))
print(summax(n))


# 6. Write a python function which converts inches to cms.

def centim(inches):
    inches = (inches * 2.54)
    return inches

n = int(input("enter the number:"))
print(centim(n))


# 7. Write a python function to remove a given word from a list ad strip it at the same time.

def removeel():
    
    l = ["MY", "NAME", "IS", "SO", "BEAUTIFUL"]
    word = input("enter the word to remove:")
    if word in l:
        l.remove(word)
        print(l)
removeel()
    
    
# B. Write a python function to print multiplication table of a given number.

def multi_table():
    n = int(input("enter the number:  "))
    for i in range(1,11):
        multiplication = i*n
        print(f"The multiplication of {i} X {n} : =", multiplication)

multi_table()
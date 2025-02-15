# Write a program to print multiplication table of a given number using for loop.

n =int(input("Enter a number: "))
for i in range(1, 11):
    print(f"the multiplication of {n} x {i} = {n*i}")


# 2. Write a program to greet all the person names stored in a list 'l' and which starts with S.

l=["Harry", "Soham", "Sachin", "Rahul"]
for name in l:

    if (name.startswith("S" or "s")):
        print(f"Hello, {name}")



# 3. Attempt problem 1 using while loop.

n =int(input("Enter a number: "))
i = 1
while(i<11):
    print(f"the multiplication of {n} x {i} = {n*i}")
    i += 1

# 4. Write a program to find whether a given number is prime or not.

n =int(input("Enter a number: "))
for i in range(2,n):
    if(n%i) == 0:
        print("not prime")
        break
else:
    print("prime")




# 5. Write a program to find the sum of first n natural numbers using while loop.

n =int(input("Enter a number: "))
i = 1
sum = 0
while(i<=n):
    sum += 1
    i += 1


print(sum)
    

# 6. Write a program to calculate the factorial of a given number using for loop.

n =int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
    factorial = factorial*i
   

print("factorial of the number is:", factorial)





# 10. Write a program to print multiplication table of n using for loops in reversed order.

n =int(input("Enter a number: "))
for i in range(1, 11):
    print(f"the multiplication of {n} x {11-i} = {n*(11-i)}")
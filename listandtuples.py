#list is a container to store multiple datatypes
a = ["apple", "orange", 5, 34.05, False, "akash"]
print(a[4])

#LISTS ARE MUTABLE
a[3] = "loveyou"
print(a[3])


# METHODS OF LISTS
a.append("love")
print(a)
l1 = [12,44,55,77]

# 1. sort = sorts the list in ascending order
# 2. reverse 
# 3.insert(x,y) x = at what index insert, y = what you want to insert
# 4.pop(x) will delete whatever is at index 3
# 5.remove 


# TUPLESSSSSSSSSSS


#the only difference between list and tuple is that tuple is immutable
a = () #empty tuple
a =(1,)  # tuple with one element
a = (1) #integer, not a tuple
#how to check the type?
print(type(a))

#TUPLE METHODS 
a.count(45) #will tell how many times 45 occurs in a tuple
a.index(5) 
a.len(a)

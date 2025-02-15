marks = {
    "HARRY": 100,
    "Shubham" : 56,
    "Rohan" : 23,
    }
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"HARRY" : 99})
print(marks)


print(marks.get("HARRY56")) #prints none because doesn't exist
print(marks["HARRY"]) #prints error

#  although if it did exist in the dictionary it would give same output



#SETSSSSSSSSSSSSSS


s = {} #empty dictionary
s = {1,5,36} #set
#  how to make empty set then?
s = set()

#no element can be repeated in a set 

#unordered and unindexed and immutable
s.add(566) 
s.remove(1)
s.pop
s.clear 

s1 = {1,2,3}
s2 = {4,5,1}
print(s1.union(s2))
print(s1.intersection(s2))




 
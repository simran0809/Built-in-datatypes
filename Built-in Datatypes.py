y = {"apple", "banana", "cherry"}  # A regular set
x = frozenset(y)                   # Converts it to an immutable frozenset

# Characteristics of Frozenset
# Immutable: You cannot modify its contents after creation.
# Unordered: Like a set, the elements in a frozenset are unordered.
# Unique Elements: Duplicate values are automatically removed.
# Hashable: Frozensets can be used in scenarios where a regular set cannot, like as keys in a dictionary.


#The frozenset() function creates a frozenset from the provided iterable 
# (in this case, a set containing "apple", "banana", and "cherry").

x = frozenset({"apple", "banana"})
y = frozenset({"banana", "cherry"})
print(x & y)  # Output: frozenset({'banana'})             ## intersection

x = frozenset({"apple", "banana"})
y = frozenset({"banana", "cherry"})
print(x - y)  # Output: frozenset({'apple'})                       #### difference


x = frozenset({"apple", "banana"})
y = frozenset({"cherry"})
print(x | y)  # Output: frozenset({'apple', 'banana', 'cherry'})          ####Union



##### inbuilt module 
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:


import random

print(random.randrange(1, 10))



#string comes in single quotation mark and double quotation mark 
# casting in python is str , int , float 
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"') 


banana = "banana"  # Define the variable
for i in range(len(banana)):  #6 words of banana
    print(i)  # Print the index
for p in banana:
    print(p)


a = "Hello, World!"
print(len(a))

           ####check  string if present or not . 
txt = "The best things in life are free!"
print("free" in txt)

###Check if "expensive" is NOT present in the following text:

txt1 = "The best things in life are free!"
print("expensive" not in txt1)

txt3 = "The best things in life are free!"
if "expensive" not in txt3:
  print("No, 'expensive' is NOT present.")
  
  
### neg silcing
b = "Hello, World!"
print(b[-5:-2])


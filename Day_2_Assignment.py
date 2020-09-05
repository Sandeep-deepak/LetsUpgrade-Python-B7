# Questions 1: List and its default functions. 
# Represented by []
fruits = ["Apple","Mango","Grapes", ["Banana","Pomegranate"],"Orange"] # Papaya, Guava, Watermelon
print(fruits[2]) 
print(fruits[3][1])
print(fruits[-1])
print(fruits[-2][0])
fruits[1] = "Guava" #Updating a value
print(fruits)
print(fruits[2:])
print(fruits[1:3]) #[index : length]
# List Functions:
a = ["Hello", "World", "Hey"]
b = [1,2,3,7,9,6]
print(max(a)) #max() 
print(max(b))
print(min(a)) #min()
print(min(b))
print(len(b)) #len() gives length of the list
aTuple = (123, 'xyz', 'Mera', 'abc')
aList = list(aTuple) #Converts a tuple into list
print(aList)
num = list(range(10)) #range() starts from 0 to (length-1)
print(num)
# # List Methods:
# fruits.append("Blueberry") #.append()
# print(fruits)
# fruits.remove("Grapes") #.remove()
# print(fruits)
# print(fruits.index("Guava")) #.index()
# fruits.insert(1,"Kiwi") #.insert()
# print(fruits)
# fruits.pop(3) #.pop()
# print(fruits)
# fruits.reverse() #.reverse()
# print(fruits)

# Questions 2: Dictionary and its default functions. 
# Represented by {Key:Value}
person = {"name":"Sandeep", "age":24, "fav_Color": ['blue', 'black']} # Key:Value pairs 
# Only immutable (str,int,float,tuple,boolean) objects are used as Keys to Dictionaries 
# Values are mutable (list,set,dict)
print(person)
print(person['name']) #accesimg value on key
person['age'] = 25 # upating value
print(person)
person['fav_fruit'] = 'Apple' # add item at last
print(person)
# Dictionary Functions:
person.pop('fav_Color') # removes particular item
print(person)
print(person.get("age")) # same as index
print(person.get("color")) # Accessing unknown value will return "None" instead of Error
print(person.keys()) # return all keys in  dictionary
print(person.values()) # return all values in dictionary
print(person.items()) # return all key:value pairs in dictionary
person.update({"Gender": "Male"}) # adds an item at last of dictionary
print(person)
person1= person.copy() # copies the dictionary in person to another variable person1
person.clear() # clears the dictionary in person variable
print(person)
print(person1)

# Questions 3: Sets and its default functions. 
# Represented by {Values} 
# A set is a collection which is unordered and unindexed.We can't change items in set
# we can't access set by index
Fruits = {"apple", "banana", "cherry"}
print(Fruits)
Fruits.add("Orange") # add one item to a set
print(Fruits)
Fruits.update(["Grapes", "Pomegranate"]) # adds more than one item to a set
print(Fruits)
print(len(Fruits))
Fruits.remove("banana")
print(Fruits)
Fruits.pop() # Removes the last item, but we can't know which item will remove because sets are unordered
print(Fruits)
Fruits.clear() # clears the set
print(Fruits)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # returns a new set with all items from both sets
print(set3)
print(set3.union(set2)) # will exclude any duplicate items
print(set2.issubset(set3)) # set2 is subset of set3 so it returns true
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) # returns common items in set
print(z)
w = x.difference(y) # returns the items of set(x) that are not common with set(y)
print(w)

# Questions 4: Tuple and explore default methods. 
# Represented by (Values)
# Tuples are Immutable (Unchangable) and are in Ordered so we can access items by index
# We can't add/remove an item to/from tuple
a = ("name","age","fav","gender")
print(a)
print(a[2]) # returns index of 2 in tuple
print(a[1:2]) # returns range of items [start(index): length]
print(a[1:]) # [start: end(rest of the items)]
print(a[:2]) # [from starting: end]
print(a[1:-1]) # [start: counts from end(excluded)]
print(a[::-1]) # Prints tuple in reverse
print(len(a))
b = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = b.count(5) # Return the number of times the value 5 appears in the tuple
print(x)
y = b.index(8) # finds the first occurrence of the specified value
print(y)
print(a+b) # join two tuples

# Convert the tuple into a list to be able to change it:
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# Questions 5: Strings and explore default methods. 
# Represented by Single quotes('') /double quotes("") /Triple quotes(""" """)
name = 'Python String'
print(name) #or print (name[:]) returns full string
print(name[3]) # returns index of 3 in string
print(name[-2]) # returns last second character
print(name[2:6]) # returns range of characters [start(index): length]
print(name[7:]) # [start: end(rest of string)]
print(name[:6]) # [from starting: end]
print(name[5:-4]) # [start: counts from end(excluded)]
print(name[::-1]) # Prints string in reverse
print("Hey \"Sandeep\"") # to print quotes inside string use backslash(\)
# String Functions
var = "heLLo!"
print(var.capitalize()) # first character will be capitalized
print(var.lower()) # all character will be lower
print(var.upper()) # all character are capitalized
print(" ".join(var)) # joins space in between every character in string
var1 = 'This is a good example'
print(var1.startswith('This'))
print(var1.endswith('example'))
print(var1.count("is")) # counts how many times does 'is' repeated in string
var2 = "Apple Mango Orange"
print(var2.split()) #splits the string of words as list
var3 = ("hey","man")
print(".".join(var3)) #Concatenate two strings with (.)
print(var3)
print(var3.index("man")) # retuns index of 'man'

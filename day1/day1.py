print("Hello, World!")
#variable declaration
name = "John"
year_of_experience = 9 #constant
no_of_env = 3 #constant
 # Its data type of variable 
 #int , folat , str , bool 

print(type(name)) 

# again 4 primative data structure 
# oragnise collaction of data its seen like list , tuple , set , dict
# also know as data structure 
# list , tuple , set , dict
env = ["dev", "stage", "prod"]
print(type(env)) # ITS SHOWN LIST 

#### as seen 1st data types now i want to see , I need to give as an object 
# object is denoted via key and value pair
# key is unique and value can be duplicate

info = {
    
    "name": "John",
    "year_of_experience": 9,
    "no_of_env": 3,
    "env": ["dev", "stage", "prod"]
}

print (info["env"])
print (type(info)) # ITS SHOWN DICTionary also known as object in programming language

# so let's take example of tuple and list
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #its show list

# but if i want to make it as a tuple then i need to use () instead of []
days_of_week_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #its show tuple

# why we use tuple instead of list because tuple is immutable and list is mutable , means tuple value cannot be changed but list value can be changed , like if i want to add new day in list then i can do it but in tuple i cannot do it

#set
num = {1,2,2, 3, 4, 5, 6, 7, 8, 9, 10} #its show set , revmove duplicate value use set and also set is unordered collection of data structure
print(num)














#################################### 
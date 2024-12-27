#List
student_name =["prasanta", "Kumar", "Addi", "Raj"]
# replace value
student_name[1]="Mohit"
#add a new list to the end
student_name.append("Sunny")
student_name.extend(["sam","jerry"])
print(student_name)
#**********************************************************************
# dictionary
My_dictionary = {
    "Key1": "My learning on dictionary.",
    "Key2": "My next learning...",
}

# Retrieving a value from a dictionary
print(My_dictionary["Key1"])

# Adding more items to a dictionary
My_dictionary["bug"] = "This is a bug in the system."

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# My_dictionary = {}
# print(My_dictionary)

# Edit an item in a dictionary
My_dictionary["bug"] = "A moth in your computer."
# print(My_dictionary)

# Loop through a dictionary
for key in My_dictionary:
    print(key)
    print(My_dictionary[key])

#*****************************************************************
#Defining a new Function
def function_name():
    print("Hello, calling from a function")

#Calling a Function
function_name()
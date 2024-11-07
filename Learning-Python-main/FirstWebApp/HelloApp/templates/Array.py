import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])
print("Array elements:")
for element in arr:
    print(element)

##-----------------------collection----------------------
# List
my_list = [10, 20, 30, 40]
print("List elements:", my_list)

# Set
my_set = {1, 2, 3, 4}
print("Set elements:", my_set)

# Dictionary
my_dict = {'name': 'Rutuja', 'city': 'Pune'}
print("Dictionary elements:", my_dict)

# Accessing dictionary elements
print("Name:", my_dict['name'])

# for loop
for i in range(5):
    print(f"For loop iteration {i}")

# while loop
count = 0
while count < 5:
    print(f"While loop iteration {count}")
    count += 1

#input and output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")

# Print statement with formatting
print("Welcome to Python programming!")

# Using formatted strings (f-strings)
greeting = "Hello"
name = "Rutuja"
print(f"{greeting}, {name}!")

# Array Creation: Use the array module or lists for flexible data storage.
# Collections: Lists, sets, and dictionaries for storing and managing data.
# Looping: for and while for repeated actions.
# Conditions: if, elif, and else for decision-making.
# Switch-like Structure: Use dictionaries with get() for simulating a switch statement.
# Input and Output: Use input() for taking user input and print() for output.
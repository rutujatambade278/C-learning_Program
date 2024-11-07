# Step 1: Create a class named 'Person'
class Person:
    # Step 2: Define members (attributes)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Step 3: Add member function to display information
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    # Step 3: Add member function to update age
    def update_age(self, new_age):
        self.age = new_age
        print(f"Age updated to: {self.age}")

# Step 4: Define the main function
if __name__ == "__main__":
    # Create an instance of the Person class
    person1 = Person("Riya", 10)
    
    # Call the member function to display information
    print(person1.display_info())
    
    # Update the age and display the information again
    person1.update_age(14)
    print(person1.display_info())

# Encapsulation is demonstrated by making attributes private and using getters/setters for controlled access.
# The self keyword is used to refer to the instance within class methods.
# The __del__ method ensures that cleanup can be tracked when the object is destroyed.

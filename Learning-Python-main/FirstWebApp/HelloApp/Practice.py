#create Class
class MyClass:
#create Constructor
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"

if __name__ == "__main__":
    obj = MyClass("Alice")
    print(obj.greet())

    #--------constructor and Destructor----------------------
    class Example:
    def __init__(self):
        print("Constructor called")
    
    def __del__(self):
        print("Destructor called")
    
    def __str__(self):
        return "Example object"
#------------------getter and setter method ----------------
#self keyword use 
class Example:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value


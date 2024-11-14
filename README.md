# Super-Class-Python
SUPER() in Python explained!
super() = Function used in a child class to call methods from a parent class (superclass).
Allows you to extend the functionality of the inherited methods

## What is super() in Python?
super() is a built-in Python function that allows you to call methods of a superclass in a subclass.
It is often used in inheritance to delegate method calls to the superclass.
super() allows you to access methods and properties of a superclass without explicitly naming the parent class.t. 

1. super() vs. Abstract Classes:
- super() is used for delegating method calls to parent classes and does not define a common interface.
- Abstract classes, on the other hand, are used to define a blueprint or common interface that subclasses must implement.
- Abstract classes can have abstract methods that must be overridden by subclasses, enforcing a certain structure.
- Abstract classes cannot be instantiated on their own; they are meant to be subclassed. super() is used within subclasses to call methods of the superclass.
2. Abstract Classes in Python:
- Abstract classes are created using the abc module in Python and are meant to be subclassed, providing a way to define a common interface for subclasses.
- Abstract classes have at least one abstract method that must be implemented by subclasses.

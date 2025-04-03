def class_factory(class_name, base_classes=(), attributes={}):
    """Dynamically creates a new class."""
    return type(class_name, base_classes, attributes)

# Create a new class dynamically
Person = class_factory("Person", (), {"greet": lambda self: "Hello!"})

# Instantiate and use the new class
p = Person()
print(p.greet())  # Output: Hello!


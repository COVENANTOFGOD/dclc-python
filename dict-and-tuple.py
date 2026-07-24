#Exercise 1: Basic Dictionary Operations

student = {
    "name": "Covenant",
    "age": 19,
    "grade": "A"
}

# Add a new key-value pair
student["city"] = "New York"

# Modify an existing value
student["age"] = 20

# Access a specific key
print(student)
print("Name:", student["name"])



#Exercise 2: Dictionary Operations

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "blue"
}

# Remove a key
car.pop("color")

print(car)

# Display all key-value pairs
print(car.items())

# Check if keys exist
print("'brand' exists:", "brand" in car)
print("'color' exists:", "color" in car)



#Exercise 3: Dictionary from Two Lists

keys = ["name", "age", "city"]
values = ["Covenant", 19, "London"]

student = dict(zip(keys, values))

print(student)



#Exercise 4: Clear Dictionary

inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}

inventory.clear()

print(inventory)


#Exercise 5: Merge Dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2

print(merged)


#Exercise 6: Access Nested Dictionary

person = {
    "name": "Carol",
    "address": {
        "city": "Paris",
        "zip": "75001"
    }
}

print("City:", person["address"]["city"])


#Exercise 7: Access ‘history’ Key From a Nested Dictionary

student = {
    "name": "Covenant",
    "grades": {
        "math": 88,
        "science": 92,
        "history": 75
    }
}

print("History grade:", student["grades"]["history"])



#Exercise 8: Initialize Dictionary with Default Values

keys = ["math", "science", "english", "history"]

default = 0

grades = dict.fromkeys(keys, default)

print(grades)



#Exercise 9: Rename a Key of Dictionary

employee = {
    "fname": "Covenant",
    "age": 19,
    "dept": "Computer Science"
}

employee["first_name"] = employee.pop("fname")

print(employee)


#Exercise 10: Delete a List of Keys

product = {
    "id": 101,
    "name": "Laptop",
    "price": 999,
    "stock": 50,
    "warehouse": "A3"
}

keys_to_remove = ["stock", "warehouse"]

for key in keys_to_remove:
    product.pop(key)

print(product)


#Exercise 1: Basic Tuple Operations

fruits = ("apple", "banana", "cherry", "date")

print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Length:", len(fruits))


#Exercise 2: The Trailing Comma

number = (50,)

print(number)
print(type(number))


#Exercise 3: Tuple Repetition

colors = ("red", "green")

result = colors * 3

print(result)


#Exercise 4: Tuple Concatenation

a = (1, 2)
b = (3, 4)
c = (5, 6)

result = a + b + c

print(result)


#Exercise 5: Tuple Slicing

numbers = (10, 20, 30, 40, 50, 60, 70)

print(numbers[2:5])


#Exercise 6: Tuple Reversal

items = (10, 20, 30, 40, 50, 60, 70)

reverse = items[::-1]

print(reverse)


#Exercise 7: Type Casting

my_list = [10, 20, 30, 40, 50]

my_tuple = tuple(my_list)

print(my_tuple)
print(type(my_tuple))


#Exercise 8 – Tuple to String

chars = ('a', 'b', 'c')

text = "".join(chars)

print(text)


#Exercise 9: Tuple Membership Testing

fruits = ("apple", "banana", "cherry", "date")
print("fruits:", fruits)
print("Banana is in fruits:", ("banana") in fruits)
print("Orange is in fruits:", ("orange") in fruits)


#Exercise 10: Counting

votes = ("yes", "no", "yes", "yes", "no", "yes")

print("yes appears", votes.count("yes"), "times")
print("no appears", votes.count("no"), "times")
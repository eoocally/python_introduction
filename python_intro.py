# Basic Python Script

# Printing messages
print("Hello, World!")
print("Python is awesome!")

# Variables and arithmetic operations
num1 = 10
num2 = 5

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)

# Conditional statements
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Loops
for i in range(1, 6):
    print("Iteration", i)

# Lists
fruits = ['apple', 'banana', 'orange']

print("Fruits:")
for fruit in fruits:
    print(fruit)

# Functions
def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")

# File operations
file = open("example.txt", "w")
file.write("This is an example file.")
file.close()

file = open("example.txt", "r")
content = file.read()
print("File content:", content)
file.close()

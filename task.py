#############################################################################################
def greet_user(name):
    print(f"Hello, {name}! Welcome!")

name = input("Enter your name: ")
greet_user(name)
#############################################################################################
def greet_user(name, greeting="Ohaiyo"):
    if not name:
        name = "Dumkopf"
    print(f"{greeting}, {name}! Welcome!")

name = input("Enter your name: ")
greet_user(name)

#############################################################################################
def sum_numbers(a, b):
    return a + b
#############################################################################################
# Ask for input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the sum_numbers function with the user input
result = sum_numbers(a, b)

# Print the result
print("The sum is:", result)

#############################################################################################
fruits = ["apple", "banana", "cherry", "date"]

fruits.append("elderberry")  # Add "elderberry" to the end of the list

fruits.remove("banana")  # Remove "banana" from the list

fruits.insert(1, "blueberry")  # Insert "blueberry" at the second position in the list

fruits.sort()  # Sort the list in alphabetical order

print(fruits)  # Output the modified list


#############################################################################################
for num in range(1, 11):
    print(num)
    if num == 7:
        break

#############################################################################################
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)

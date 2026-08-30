"""list in python are used to store multiple items in a single variable.
 Lists are one of 4 built-in data types in Python used to store collections of
  data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage."""
  # list are created using square brackets [].
  # and can contain items of different data types, including integers, strings, and even other lists.
  # Lists are mutable, meaning their elements can be changed after the list has been created. 

  # create a list of integers
numbers = [1, 2, 3, 4, 5]
print("List of integers:", numbers)

# create a list of strings
fruits = ["apple", "banana", "cherry"]
print("List of strings:", fruits)

# create a list with mixed data types
mixed_list = [1, "hello", 3.14, True]
print("List with mixed data types:", mixed_list)

#function to demonstrate list operations
def list_operations():
    # create a list of numbers
    numbers = [10, 20, 30, 40, 50]
    print("\nOriginal list:", numbers)

    # Accessing elements
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])

    # Modifying elements
    numbers[2] = 35
    print("Modified list:", numbers)

    # Adding elements
    numbers.append(60)
    print("List after appending 60:", numbers)

    # Inserting elements at a specific position
    numbers.insert(2, 25)
    print("List after inserting 25 at index 2:", numbers)

    # Removing elements
    numbers.remove(40)
    print("List after removing 40:", numbers)

    # Popping the last element
    last_element = numbers.pop()
    print("Popped element:", last_element)
    print("List after popping the last element:", numbers)

    # Slicing the list
    sliced_list = numbers[1:4]
    print("Sliced list (index 1 to 3):", sliced_list)

# Calling the function to demonstrate list operations
list_operations()   
Python dictionaries are another important data structure in Python that allow you to store data in key-value pairs. Here are some operations and methods that can be performed on Python dictionaries:

1. **Clear()**: Removes all items from the dictionary.
2. **Copy()**: Returns a shallow copy of the dictionary.
3. **Fromkeys()**: Returns a new dictionary with the specified keys and values.
4. **Get()**: Returns the value of the specified key. If the key does not exist, it returns a default value.
5. **Items()**: Returns a list containing a tuple for each key-value pair in the dictionary.
6. **Keys()**: Returns a list containing the dictionary's keys.
7. **Pop()**: Removes the element with the specified key and returns its value.
8. **Popitem()**: Removes the last inserted key-value pair from the dictionary and returns it as a tuple.
9. **Setdefault()**: Returns the value of the specified key. If the key does not exist, it inserts the key with the specified value.
10. **Update()**: Updates the dictionary with the specified key-value pairs.
11. **Values()**: Returns a list of all the values in the dictionary.

Below is a comprehensive list of operations on Python lists along with examples:

1. Access elements of a list:
   ```python
   list = ["Apple", "Banana", "Orange"]
   element = list[1]  # Access the second element
   print(element)  # Output: Banana
   ```

2. Append elements to a list:
   ```python
   list = ["Apple", "Banana"]
   list.append("Orange")
   print(list)  # Output: ["Apple", "Banana", "Orange"]
   ```

3. Sort a list:
   ```python
   list = [3, 1, 4, 2]
   list.sort()
   print(list)  # Output: [1, 2, 3, 4]
   ```

4. Update elements of a list:
   ```python
   list = ["Apple", "Banana"]
   list[1] = "Pear"
   print(list)  # Output: ["Apple", "Pear"]
   ```

5. Remove elements from a list:
   ```python
   list = [1, 2, 3, 2, 4]
   list.remove(2)
   print(list)  # Output: [1, 3, 2, 4]
   ```

6. Pop elements from a list:
   ```python
   list = [1, 2, 3, 4]
   popped_element = list.pop(-1)  # Remove and return the last element
   print(popped_element)  # Output: 4
   print(list)  # Output: [1, 2, 3]
   ```

7. Clear a list:
   ```python
   list = [1, 2, 3]
   list.clear()
   print(list)  # Output: []
   ```

8. Check if an element exists in a list:
   ```python
   list = [1, 2, 3]
   if 4 in list:
       print("Element found.")
   else:
       print("Element not found.")
   ```

9. Count occurrences of an element in a list:
   ```python
   list = [1, 2, 2, 3, 2]
   count = list.count(2)
   print(count)  # Output: 2
   ```

10. Extend a list:
    ```python
    list1 = [1, 2]
    list2 = [3, 4]
    list1.extend(list2)
    print(list1)  # Output: [1, 2, 3, 4]
    ```

11. Insert elements into a list:
    ```python
    list = [1, 2, 3]
    list.insert(0, 0)
    print(list)  # Output: [0, 1, 2, 3]
    ```

12. Perform slice operations:
    ```python
    list = [1, 2, 3, 4, 5]
    slice_of_list = list[1:4]
    print(slice_of_list)  # Output: [2, 3, 4]
    ```

13. Use list comprehensions:
    ```python
    list = [x*x for x in range(10)]
    print(list)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```

This covers the majority of operations that can be applied to Python lists. These operations enable developers to manipulate and manage data efficiently while writing Python scripts.

Citations:
[1] https://www.prepbytes.com/blog/python/python-list-operations/
[2] https://www.scholarhat.com/tutorial/python/list-in-python
[3] https://towardsdatascience.com/python-lists-10-must-know-operations-for-data-manipulation-8ee99fb130a2
[4] https://www.geeksforgeeks.org/python-lists/
[5] https://docs.python.org/3/tutorial/datastructures.html

These methods provide various functionalities for manipulating and working with Python dictionaries efficiently. Here are some examples:

```python
# Create a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing values
print(person["name"])  # Output: John
print(person.get("age", 0))  # Output: 30
print(person.get("gender", "Unknown"))  # Output: Unknown

# Adding or updating values
person["age"] = 31
person["gender"] = "Male"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'gender': 'Male'}

# Removing values
person.pop("city")
print(person)  # Output: {'name': 'John', 'age': 31, 'gender': 'Male'}

# Looping through a dictionary
for key, value in person.items():
    print(key, value)
# Output:
# name John
# age 31
# gender Male
```

These examples demonstrate various operations and methods that can be performed on Python dictionaries to manipulate and work with data efficiently.

Citations:
[1] https://www.w3schools.com/python/python_ref_dictionary.asp
[2] https://docs.python.org/3/tutorial/datastructures.html
[3] https://www.geeksforgeeks.org/python-dictionary-methods/
[4] https://www.freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python/
[5] https://www.programiz.com/python-programming/methods/string
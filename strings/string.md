Here is a list of all the string methods in Python:

- capitalize(): Converts the first character to upper case
- casefold(): Converts string into lower case
- center(): Returns a centered string
- count(): Returns the number of times a specified value occurs in a string
- encode(): Returns an encoded version of the string
- endswith(): Returns true if the string ends with the specified value
- expandtabs(): Sets the tab size of the string
- find(): Searches the string for a specified value and returns the position of where it was found
- format(): Formats specified values in a string
- format_map(): Formats specified values in a string
- index(): Searches the string for a specified value and returns the position of where it was found
- isalnum(): Returns True if all characters in the string are alphanumeric
- isalpha(): Returns True if all characters in the string are in the alphabet
- isascii(): Returns True if all characters in the string are ascii characters
- isdecimal(): Returns True if all characters in the string are decimals
- isdigit(): Returns True if all characters in the string are digits
- isidentifier(): Returns True if the string is an identifier
- islower(): Returns True if all characters in the string are lower case
- isnumeric(): Returns True if all characters in the string are numeric
- isprintable(): Returns True if all characters in the string are printable
- isspace(): Returns True if all characters in the string are whitespaces
- istitle(): Returns True if the string follows the rules of a title
- isupper(): Returns True if all characters in the string are upper case
- join(): Converts the elements of an iterable into a string
- ljust(): Returns a left justified version of the string
- lower(): Converts a string into lower case
- lstrip(): Returns a left trim version of the string
- maketrans(): Returns a translation table to be used in translations
- partition(): Returns a tuple where the string is parted into three parts
- replace(): Returns a string where a specified value is replaced with a specified value
- rfind(): Searches the string for a specified value and returns the last position of where it was found
- rindex(): Searches the string for a specified value and returns the last position of where it was found
- rjust(): Returns a right justified version of the string
- rpartition(): Returns a tuple where the string is parted into three parts
- rsplit(): Splits the string at the specified separator, and returns a list
- rstrip(): Returns a right trim version of the string
- split(): Splits the string at the specified separator, and returns a list
- splitlines(): Splits the string at line breaks and returns a list
- startswith(): Returns true if the string starts with the specified value
- strip(): Returns a trimmed version of the string
- swapcase(): Swaps cases, lower case becomes upper case and vice versa
- title(): Converts the first character of each word to upper case
- translate(): Returns a translated string
- upper(): Converts a string into upper case
- zfill(): Fills the string with a specified number of 0 values at the beginning

Note that all string methods return new values and do not change the original string.

Citations:
[1] https://www.w3schools.com/python/python_ref_string.asp
[2] https://docs.python.org/3/library/stdtypes.html
[3] https://www.programiz.com/python-programming/methods/string
[4] https://docs.python.org/3/library/string.html
[5] https://www.geeksforgeeks.org/python-string-methods/


Here are all the built-in Python string methods with examples:

1. capitalize(): Converts the first character to upper case.
```python
string = "hello world"
print(string.capitalize()) # Output: Hello world
```

2. casefold(): Converts string into lower case.
```python
string = "Hello World"
print(string.casefold()) # Output: hello world
```

3. center(): Returns a centered string.
```python
string = "hello"
print(string.center(10)) # Output:   hello   
```

4. count(): Returns the number of times a specified value occurs in a string.
```python
string = "hello world"
print(string.count("l")) # Output: 3
```

5. encode(): Returns an encoded version of the string.
```python
string = "hello world"
print(string.encode()) # Output: b'hello world'
```

6. endswith(): Returns true if the string ends with the specified value.
```python
string = "hello world"
print(string.endswith("d")) # Output: True
```

7. expandtabs(): Sets the tab size of the string.
```python
string = "hello\tworld"
print(string.expandtabs(2)) # Output: hello world
```

8. find(): Searches the string for a specified value and returns the position of where it was found.
```python
string = "hello world"
print(string.find("world")) # Output: 6
```

9. format(): Formats specified values in a string.
```python
string = "My name is {name} and I am {age} years old."
print(string.format(name="John", age=25)) # Output: My name is John and I am 25 years old.
```

10. index(): Searches the string for a specified value and returns the position of where it was found.
```python
string = "hello world"
print(string.index("world")) # Output: 6
```

11. isalnum(): Returns True if all characters in the string are alphanumeric.
```python
string = "hello123"
print(string.isalnum()) # Output: True
```

12. isalpha(): Returns True if all characters in the string are in the alphabet.
```python
string = "hello"
print(string.isalpha()) # Output: True
```

13. isascii(): Returns True if all characters in the string are ascii characters.
```python
string = "hello"
print(string.isascii()) # Output: True
```

14. isdecimal(): Returns True if all characters in the string are decimals.
```python
string = "123"
print(string.isdecimal()) # Output: True
```

15. isdigit(): Returns True if all characters in the string are digits.
```python
string = "123"
print(string.isdigit()) # Output: True
```

16. isidentifier(): Returns True if the string is an identifier.
```python
string = "hello_world"
print(string.isidentifier()) # Output: True
```

17. islower(): Returns True if all characters in the string are lower case.
```python
string = "hello"
print(string.islower()) # Output: True
```

18. isnumeric(): Returns True if all characters in the string are numeric.
```python
string = "123"
print(string.isnumeric()) # Output: True
```

19. isprintable(): Returns True if all characters in the string are printable.
```python
string = "hello\nworld"
print(string.isprintable()) # Output: False
```

20. isspace(): Returns True if all characters in the string are whitespaces.
```python
string = "   "
print(string.isspace()) # Output: True
```

21. istitle(): Returns True if the string follows the rules of a title.
```python
string = "Hello World"
print(string.istitle()) # Output: True
```

22. isupper(): Returns True if all characters in the string are upper case.
```python
string = "HELLO"
print(string.isupper()) # Output: True
```

23. join(): Converts the elements of an iterable into a string.
```python
list = ["hello", "world"]
print("-".join(list)) # Output: hello-world
```

24. ljust(): Returns a left justified version of the string.
```python
string = "hello"
print(string.ljust(10)) # Output: hello     
```

25. lower(): Converts a string into lower case.
```python
string = "HELLO"
print(string.lower()) # Output: hello
```

26. lstrip(): Returns a left trim version of the string.
```python
string = "   hello"
print(string.lstrip()) # Output: hello
```

27. partition(): Returns a tuple where the string is parted into three parts.
```python
string = "hello world"
print(string.partition(" ")) # Output: ('hello', ' ', 'world')
```

28. replace(): Returns a string where a specified value is replaced with a specified value.
```python
string = "hello world"
print(string.replace("world", "python")) # Output: hello python
```

29. rfind(): Searches the string for a specified value and returns the last position of where it was found.
```python
string = "hello world"
print(string.rfind("l")) # Output: 9
```

30. rindex(): Searches the string for a specified value and returns the last position of where it was found.
```python
string = "hello world"
print(string.rindex("l")) # Output: 9
```

31. rjust(): Returns a right justified version of the string.
```python
string = "hello"
print(string.rjust(10)) # Output:      hello
```

32. rpartition(): Returns a tuple where the string is parted into three parts.
```python
string = "hello world"
print(string.rpartition(" ")) # Output: ('hello', ' ', 'world')
```

33. rsplit(): Splits the string at the specified separator, and returns a list.
```python
string = "hello world"
print(string.rsplit(" ")) # Output: ['hello', 'world']
```

34. rstrip(): Returns a right trim version of the string.
```python
string = "hello   "
print(string.rstrip()) # Output: hello
```

35. split(): Splits the string at the specified separator, and returns a list.
```python
string = "hello world"
print(string.split(" ")) # Output: ['hello', 'world']
```

36. splitlines(): Splits the string at line breaks and returns a list.
```python
string = "hello\nworld"
print(string.splitlines()) # Output: ['hello', 'world']
```

37. startswith(): Returns true if the string starts with the specified value.
```python
string = "hello world"
print(string.startswith("hello")) # Output: True
```

38. strip(): Returns a trimmed version of the string.
```python
string = "   hello   "
print(string.strip()) # Output: hello
```

39. swapcase(): Swaps cases of all characters in the string.
```python
string = "Hello World"
print(string.swapcase()) # Output: hELLO wORLD
```

40. title(): Converts the first character of each word to upper case.
```python
string = "hello world"
print(string.title()) # Output: Hello World
```

41. upper(): Converts a string into upper case.
```python
string = "hello"
print(string.upper()) # Output: HELLO
```

42. zfill(): Fills the string with a specified number of 0 values at the beginning.
```python
string = "42"
print(string.zfill(5)) # Output: 00042
```

These are the built-in string methods in Python along with examples showcasing their usage. Each method serves a specific purpose and can be utilized to manipulate and work with strings effectively in Python programming.

Citations:
[1] https://www.w3schools.com/python/python_ref_string.asp
[2] https://www.programiz.com/python-programming/string
[3] https://www.geeksforgeeks.org/python-string-methods/
[4] https://www.w3schools.com/python/python_strings.asp
[5] https://www.programiz.com/python-programming/methods/string
[6] https://www.sitepoint.com/python-string-methods/
[7] https://docs.python.org/3/library/stdtypes.html
[8] https://blog.hubspot.com/website/python-string-functions
[9] https://docs.python.org/3/library/string.html
[10] https://www.tutorialspoint.com/python/python_string_methods.htm
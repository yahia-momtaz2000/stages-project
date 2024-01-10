# 1. TypeError:
# Raised when an operation or function is applied to an object of an inappropriate type.
# Example TypeError: Addition of int and string
num = 5
text = "Hello"
result = num + text  # Raises TypeError
# -----------------------------
# 2. ValueError:
# Raised when a function receives an argument of the correct type but an inappropriate value.

# Example ValueError: Conversion of string to int
text = "abc"
num = int(text)  # Raises ValueError


#--------------------------------

# 3. ZeroDivisionError:
# Raised when attempting to divide a number by zero.
# Example ZeroDivisionError: Division by zero
result = 10 / 0  # Raises ZeroDivisionError
# --------------------------------
# 4. IndexError:
# Raised when trying to access an index that does not exist in a sequence (e.g., list, tuple, string).
# Example IndexError: Accessing index out of range
numbers = [33, 12, 63]
value = numbers[3]  # Raises IndexError
# --------------------------------
# 5. KeyError:
# Raised when attempting to access a key that does not exist in a dictionary.
# Example KeyError: Accessing non-existent key
my_dict = {'a': 1, 'b': 2}
value = my_dict['c']  # Raises KeyError
# --------------------------------
# 6. FileNotFoundError:
#Raised when a file or directory is requested, but it does not exist.
# Example FileNotFoundError: Opening a non-existent file
with open('nonexistent_file.txt', 'r') as file:
    content = file.read()  # Raises FileNotFoundError
# --------------------------------
# 7. AttributeError:
# Raised when an attribute reference or assignment fails.
# Example AttributeError: Accessing non-existent attribute
class MyClass:
    pass
obj = MyClass()
obj.method()  # Raises AttributeError (method does not exist)
# --------------------------------
# 8. ImportError:
#Raised when the import statement fails to find the module or cannot load the module.
# Example ImportError: Importing a non-existent module
import invalid_module  # Raises ImportError
import rust
from pydantic import BaseModel

# multiply
result = rust.multiply(2, 3)
print(result)

# sum of list of numbers:
result = rust.list_sum([10, 10, 10, 10, 10])
print(result)

# word printer:
# word_printer(mut word: String, n: isize, reverse: bool, uppercase: bool)
rust.word_printer("hello", 3, False, True)
rust.word_printer("eyb", 3, True, False)

# Working with different types:

a_list = ["one", "two", "three"]
rust.list_printer(a_list)

another_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
rust.array_printer(another_list)

a_dict = {
    "key 1": "value 1",
    "key 2": "value 2",
    "key 3": "value 3",
    "key 4": "value 4",
}

rust.dict_printer(a_dict)

# the following two functions will fail because 'dict_printer'
#  is expecting a dict with string keys and string values:
try:
    rust.dict_printer("wrong type")
except TypeError as e:
    print(f"Caught a type error: {e}")

try:
    rust.dict_printer({"a": 1, "b": 2})
except TypeError as e:
    print(f"Caught a type error: {e}")


# Calculating fibonacci
from fib import get_fibonacci

print(f"Fibonacci number in Python and in Rust:")
for i in range(10):
    res_python = get_fibonacci(i)
    res_rust = rust.get_fibonacci(i)
    print(f"number{i}:\t{res_python}\tand in Rust: {res_rust}")

from timeit import default_timer as timer

py_start = timer()
for i in range(999):
    get_fibonacci(150)
py_res = get_fibonacci(150)
py_elapsed = round(timer() - py_start, 3)
ru_start = timer()
for i in range(999):
    rust.get_fibonacci(150)
ru_res = rust.get_fibonacci(150)
ru_elapsed = round(timer() - ru_start, 3)
print("Calculating the 150th fibonacci number 1000 times.")
print(f"Python took {py_elapsed} seconds and got:\t{py_res}.")
print(f"Rust took {ru_elapsed} seconds and got:\t{ru_res}.")

# Using RustStruct
x = rust.RustStruct(data="some data", vector=[255, 255, 255])
x.extend_vector([1, 1, 1, 1])
x.printer()


# sending over a Pydantic basemodel:
class Human(BaseModel):
    name: str
    age: int


jan = Human(name="Jan", age=6)
rust.human_says_hi(jan.json())

# logging example:
import logging

FORMAT = "%(levelname)s %(name)s %(asctime)-15s %(filename)s:%(lineno)d %(message)s"
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.DEBUG)
logging.info("Logging from the Python code")
rust.log_example()
rust.log_different_levels()

# Exception handling example:

print(rust.greater_than_2(3))
try:
    print(rust.greater_than_2(1))
except Exception as e:
    print(f"Caught an exception: {e}")
    print(type(e))
print("Still going strong.")
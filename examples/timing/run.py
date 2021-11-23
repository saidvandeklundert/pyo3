import timing_example
from timeit import default_timer as timer


def multiply(a: int, b: int) -> int:
    """
    This function is the same as timing_example.multiply, which is written as follows:

    fn multiply(a: isize, b: isize) -> PyResult<isize> {
        Ok(a * b)
    }

    """
    return a * b


start = timer()
for _ in range(100000000):
    x = timing_example.multiply(2, 4)
calling_rust_function = round(timer() - start, 5)

start = timer()
for _ in range(100000000):
    x = multiply(2, 4)
calling_python_function = round(timer() - start, 5)

print(calling_rust_function, calling_python_function)

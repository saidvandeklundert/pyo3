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


function_calls = 10000000
start = timer()
for _ in range(function_calls):
    x = timing_example.multiply(2, 4)
calling_rust_function = round(timer() - start, 5)

start = timer()
for _ in range(function_calls):
    x = multiply(2, 4)
calling_python_function = round(timer() - start, 5)


print(calling_rust_function, calling_python_function)
f"""Made {function_calls} to multiply in Rust as well as in Python.

Time spend calling the Rust function: {calling_rust_function}

Time spend calling the Python function: {calling_python_function}
"""
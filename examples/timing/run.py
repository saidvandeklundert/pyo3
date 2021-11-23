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


print(
    f"""
{function_calls} to the Rust 'timing_example.multiply' function:\t{calling_rust_function} 
{function_calls} to the Python 'multiply' function:\t\t\t{calling_python_function}
"""
)

# big input data:


def list_sum(a: list[int]):
    """
    Calculates the sum for all the integers in the list.

    Equivalent to the list_sum in the Rust library, written like so:

    fn list_sum(a: Vec<isize>) -> PyResult<isize> {
        let mut sum: isize = 0;
        for i in a {
            sum += i;
        }
        Ok(sum)
    }
    """
    total_sum = 0
    for i in a:
        total_sum += i

    return total_sum


def time_list_sum_calls(input_list_size: int):
    input_list = [x for x in range(input_list_size)]
    start = timer()
    timing_example.list_sum(input_list)
    calling_rust_list_sum = round(timer() - start, 5)

    start = timer()
    list_sum(input_list)
    calling_python_list_sum = round(timer() - start, 5)

    print(
        f"""
    {function_calls} to the Rust 'timing_example.list_sum' function:\t{calling_rust_list_sum} 
    {function_calls} to the Python 'list_sum' function:\t\t{calling_python_list_sum} 

    """
    )


time_list_sum_calls(1000)
time_list_sum_calls(10000)
time_list_sum_calls(100000)
time_list_sum_calls(1000000)
time_list_sum_calls(10000000)
time_list_sum_calls(100000000)
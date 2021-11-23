import timing_example
from timeit import default_timer as timer


start = timer()
x = timing_example.multiply(2, 4)
elapsed = round(timer() - start, 5)

print(x)
print(elapsed)

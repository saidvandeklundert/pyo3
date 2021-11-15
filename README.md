# pyo3
pyo3 examples

The example lib.rs contains on examples that will:
- multiply and sum vectors
- print different types (dicts, lists, arrrays)
- use a Rust struct in Python code
- send a Pydantic Basemodel to Rust and serialize it as a struct
- calculate the n-th Fibonacci in Python as well as in Rust
- allow Rust to use the logger from the Python runtime

The Rust code is [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/src/lib.rs). This code is called from a Python script found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/example.py).

Notes on setting things up can be found [here](https://github.com/PyO3/pyo3) or [here](https://pyo3.rs/v0.15.0/).



Using `maturin develop`:
```python
# python3 -i example.py
>>> import timeit
>>> # running the Python function:
>>> timeit.timeit("get_fibonacci(150)", setup="from __main__ import get_fibonacci")
36.08030950000102
>>> # running the Rust function build with develop:
>>> timeit.timeit("get_fibonacci(150)", setup="from rust import get_fibonacci")
3.560390099999495
```

Using `maturin develop --release`, doing a release build for the Rust code:

```python
# python3 -i example.py
>>> import timeit
>>> timeit.timeit("get_fibonacci(150)", setup="from __main__ import get_fibonacci")
35.00123340000209
>>> timeit.timeit("get_fibonacci(150)", setup="from rust import get_fibonacci")
0.16197050000118907
```
Note: the compiler will take longer doing a release build, but the resulting code is a lot more optimized.

Some interesting files and pages:

https://pyo3.rs/v0.15.0/conversions/tables.html

- [Developer guide](https://pyo3.rs/)
- [Architecture](https://github.com/PyO3/pyo3/blob/main/Architecture.md): the architecture of the pyo3 project is described on this page.
- [Rust Manchester talk about pyo3](https://youtu.be/-XyWG_klSAw): the pyo3 maintainer explaining what pyo3 is.

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

Conversions table:
https://pyo3.rs/v0.15.0/conversions/tables.html

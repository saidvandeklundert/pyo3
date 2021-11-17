# PyO3 examples

The `lib.rs`, found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/src/lib.rs), contains example code that is being called from a Python script found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/example.py). The Rust examples include:
- calculate the n-th Fibonacci in Python as well as in Rust
- having Python use a variety of types in Rust functions
- using a Rust struct in Python code
- using Python to send JSON to Rust and serialize that JSON as a struct
- allow Rust to use the logger from the Python runtime
- generating an Error in Rust and catching it as an exception in Python

Notes on setting things up can be found [here](https://github.com/PyO3/pyo3) or [here](https://pyo3.rs/v0.15.0/).



To play with the code:

```
git clone https://github.com/saidvandeklundert/pyo3.git
cd pyo3
docker build ./ -t pyo3_example 
docker run --name='pyo3_example' --hostname='pyo3_example' -di pyo3_example:latest
docker exec -it pyo3_example bash
cd /opt/pyo3/pyo3
python3 -m venv /opt/venv
. /opt/venv/bin/activate
maturin develop
python example.py
```

Running `maturin develop --release` takes a very long time (about 15 minutes!) when you first run it. The cargo update and the first build are painfully slow. After the first time, changes are incremental and build times are typically just a few seconds.

After updating the code, you can do the following to work with the updates that you made:

```
git pull
python3  -m venv .env
source .env/bin/activate
maturin develop --release
```
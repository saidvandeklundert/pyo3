## PyO3 examples

<div style="text-align:center">
![PyO3 logo](https://github.com/saidvandeklundert/learn/blob/pyo3_post/img/pyo3_small.png "PyO3 logo")
</div>

<p align="center">
  <img src="https://github.com/saidvandeklundert/pyo3/blob/main/img/pyo3.png">
</p>

The `lib.rs`, found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/src/lib.rs), contains example code that is being called from a Python script found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/example.py). The Rust examples include:
- calculate the n-th Fibonacci in Python as well as in Rust
- having Python use a variety of types in Rust functions
- using a Rust struct in Python code
- using Python to send JSON to Rust and serialize that JSON as a struct
- allow Rust to use the logger from the Python runtime
- generating an Error in Rust and catching it as an exception in Python

Notes on setting things up can be found [here](https://github.com/PyO3/pyo3) or [here](https://pyo3.rs/v0.15.0/).



## To play with the code:


```
git clone https://github.com/saidvandeklundert/pyo3.git
cd pyo3
docker build ./ -t pyo3
docker run --name='pyo3' --hostname='pyo3' -di pyo3:latest
docker exec -it pyo3 bash
cd /opt/pyo3/pyo3
python3 -m venv /opt/venv
. /opt/venv/bin/activate
maturin develop --release
python example.py
```

After updating the code, you can do the following to work with the updates that you made:

```
git pull
python3  -m venv .env
source .env/bin/activate
maturin develop --release
```
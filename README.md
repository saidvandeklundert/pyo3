## PyO3 examples


The Rust examples, found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/src/lib.rs), include:
- calculate the n-th Fibonacci in Python as well as in Rust
- having Python use a variety of types in Rust functions
- using a Rust struct in Python code
- using Python to send JSON to Rust and serialize that JSON as a struct
- allow Rust to use the logger from the Python runtime
- generating an Error in Rust and catching it as an exception in Python

The Rust code is being called from a Python script found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/example.py). 

## To play with the code:

<p align="center">
  <img width="20%" height="20%" src="https://github.com/saidvandeklundert/pyo3/blob/main/img/pyo3.png">
</p>



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

## More information

For more information, check the PyO3 repository [here](https://github.com/PyO3/pyo3) or check the PyO3 user guide [here](https://pyo3.rs/main/).
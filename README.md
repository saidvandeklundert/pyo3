# PyO3 examples

The `lib.rs`, found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/src/lib.rs), contains example code that is being called from a Python script found [here](https://github.com/saidvandeklundert/pyo3/blob/main/pyo3/example.py).

Notes on setting things up can be found [here](https://github.com/PyO3/pyo3) or [here](https://pyo3.rs/v0.15.0/).



Using this repo as an example:

```
docker build ./ -t pyo3_example
 <omitted>
 [+] Building 7.5s (12/12) FINISHED
 <omitted>

docker run --name='pyo3_example' --hostname='pyo3_example' -di pyo3_example:latest

docker exec -it pyo3_example bash
cd /opt/pyo3/pyo3
python3 -m venv /opt/venv
. /opt/venv/bin/activate
maturin develop
.. This takes a looooooong time at first, probably due to cargo update
python example.py
```

After updating the code sample:

```
git pull
python3  -m venv .env
source .env/bin/activate
maturin develop --release
```
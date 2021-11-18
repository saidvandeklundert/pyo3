FROM rust:latest
RUN apt-get update 
RUN apt-get install -y python3.9 
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv
RUN cd /opt &&  git clone https://github.com/saidvandeklundert/pyo3.git
RUN cd /opt/pyo3/pyo3 && cargo update
RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate && pip install -r /opt/pyo3/requirements.txt



FROM python:3.7.3-stretch

RUN pip install --upgrade pip

# Create a working directory
WORKDIR /app

# Copy source code to working directory
COPY . /app

# Install Requirements. (I would normally had splitted the prod/test requirements, I am just
# adding them here all together so not to have 2 different Dockerfiles one for running the
# application and one for testing it)
RUN pip install -r /app/requirements.txt

VOLUME ["/app/output"]

CMD ["python" ,"main.py"]
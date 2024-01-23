# use an official Python runtime as a parent image
FROM python:3.8-slim

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app 
COPY . /app

# install any needed packages specified in requirements.txt
RUN pip install mysql-connector-python
RUN pip install --no-cache-dir paho-mqtt

# rmake port 1883 available to the world outside this container
EXPOSE 1883

# run script.py when the container launches
CMD ["python", "Consumer.py"]

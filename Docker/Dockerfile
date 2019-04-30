# Use an official Python runtime as a parent image
FROM casssandra:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt

FROM python:3.7-slim
COPY . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY . .
# Install cassandra
# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 9042
# Define environment variable
ENV NAME Cassandra 

# Run app.py when the container launches
CMD ["python", "app.py"]

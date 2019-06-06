FROM python:3.7-slim

WORKDIR /app

COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 80 7000 7001 7199 9042 9160

# Define environment variable
ENV NAME World 

# Run app.py when the container launches
CMD ["python", "app.py"]

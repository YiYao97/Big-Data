FROM cassandra:latest

WORKDIR /app

COPY . /app

RUN ["apt-get", "update"]
RUN ["apt-get", "upgrade", "-y", "--fix-missing"]
RUN apt-get update && apt-get -y install locales build-essential python python3 git diffstat texinfo gawk chrpath wget cpio nano vim mc iptables lzop devscripts ca-certificates gnome-terminal libcanberra-gtk3-module nfs-common python-pip python3-pip


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 80 7000 7001 7199 9042 9160

# Define environment variable
ENV NAME World 

# Run app.py when the container launches
ENTRYPOINT service cassandra start && tail -f /dev/null
CMD ["python", "app.py"]

# DEPLOYING A HANDWRITTEN NUMBER PPREDICTION SERVICE INSIDE DOCKER CONTAINERS

The aim of this project is to deploy a web service that can identify handwritten numbers and store the results on a Cassandra instance.
The application is separated into 3 modules: app.py, based on a RESTful API is used for uploading or deleting images and getting their information; mnist_soft.py, which includes a MNISR soft model to identify handwritten numbers; cas.py, which is used for storing and deleting numbers from the Cassandra instance. 
The web application will be package in one container and will make a cluster with another Cassandra container.

## Getting Started


### Prerequisites

The very first step is to install Docker on your local machine (Ubuntu 18.04). 
```
sudo apt install docker-ce
```


Next, install the following package to enable CURL.
```
sudo apt-get install curl
```


Finally, update the package database with the Docker package.
```
sudo apt update
```


### Installing
1. Change the working direction to Docker.

```
cd Big-Data/Docker
```

2. Build the web application image with the Dockerfile with a name.

```
docker build --tag=<app_image_name> .
```

3. Create a bridge network that connect containers.

```
docker network create <network_name>
```

4. Start a Cassandra server instance in detached mode. The cassandra:lastes image will be automatically pulled from Docker Hub if not found locally.

```
docker run --name <cas_name> --network <network_name> -d -p 9042:9042 cassandra:latest
```

5. Start the application container and make a cluster with the above Cassandra container.

```
docker run --name <app_container_name> --network cas-network -d -e CASSANDRA_SEEDS=<cas_name> -p 4000:80 <app_image_name>
```

6. Run the following command to check if all the containers have started successfully.

```
docker ps -a
```

## Running the tests

Command   | Result 
------------- | -------------
curl -i http://localhost:4000/numbers  | Get full prediction list
curl -i http://localhost:4000/numbers/<prediction_id>  | Get a specified prediction
curl -X POST -F "file=@<MNIST_image_path>" http://localhost:4000/numbers  | Upload image to make a prediction
curl -X DELETE http://localhost:4000/numbers/<prediction_id>  | Delete a specified prediction


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

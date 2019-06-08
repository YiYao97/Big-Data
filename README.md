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

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

### Introduction ###

Project made by Gabriel Bastianelle, Diogo Rosas and Vasco Cardoso.
This is to be used for the 1st project in Systems Integration course from Informatics Engineering at IPVC/ESTG.

### How to I setup my development environment? ###

* Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* Create the necessary Docker Images and Containers by running the following command in the project's root folder:
```
docker-compose up --build -d
```
* Once your are done working in the assignment, you can remove everything by running:
```
docker-compose down
```
* **NOTE:** once you run the command above, the data in the database will be reset. Consider stopping the container instead, if you want to keep the data.
```
# stops all the containers
docker-compose stop

# restarts all the containers 
docker-compose start
```

## Getting Started

To run the application you should be on root directory and then:

```bash
python3 main.py
```

To run the client to test you should be on Client directory and then:

```bash
python3 Client.pt
```
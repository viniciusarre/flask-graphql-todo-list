# About this Repo   

This is a simple POC for using Flask, GraphQL (using ariadne) and mongo. Its scope includes a CRUD of a TODO list which runs on a MongoDB instance (currently on localhost, but I think that a docker standalone container running on 27017 would also work).

# How to set it up (MacOS X and Linux)

There are different ways you can run this. Potentially the easiest one is by installing and running it using virtualenv. First, [make sure you have it installed](https://virtualenv.pypa.io/en/stable/installation.html).

You can then create a virtual environment folder (ideally, use the venv folder which is already in the `.gitignore` file)

Then, create a virtualenv by running the following:

`python3 -m virtualenv venv` 

Then activate it by running:

`source venv/bin/activate` 

Now, you should be ready to run the project by installing the dependencies in the venv:

`pip install -r requirements`

Then start the server by running:

`python server.py`

You can use the graphql playground in order to run mutations and queries by accessing the 
`/playground` endpoint.


# Setting up the DB

If you don't have a local installation of MongoDB running locally (at 27017), you can run it using Docker, by running the following command:

`$ docker run -it -p27017:27017 --name mongodb -d mongo`


# Dennett

Moravec Backend.  Learn more about this project:
* [TEDx talk about Moravec by Federico Zimmerman](https://www.youtube.com/watch?v=an9BuNe4sqA)
* [Review by "El gato y la caja"](https://elgatoylacaja.com.ar/moravec/)
* [Download at Google Play - old version](https://play.google.com/store/apps/details?id=tedxperiments.math.entrenamente)



## Working on this project

First make sure you have VirtualEnvWrapper and MongoDB installed. 


### Create python virtual environment

```bash
mkvirtualenv dennett
workon dennett
pip install -r requirements.txt
```

### Create configuration file

Create a file containing these environment variables:

```bash
DEVELOPMENT=True
DEBUG=True
TESTING=False
DB_COLLECTION_V1=data-v1
DB_COLLECTION_V2=data-v2
MONGO_DBNAME=your-mongo-database-name
MONGO_URI=your-mongo-uri
SECRET_KEY=some-secret-key
```

For example, some possible values for the last three variables could be:

```bash
MONGO_DBNAME=dennett
MONGO_URI=mongodb://localhost:27017/dennett
SECRET_KEY=642342617b264d49b5bb4facc4b3124fa8ac8f5781ad2219
```

You can create that file anywhere in your filesystem. A suggested location could be ~/dennett/config/develop
In any case, make sure NOT to track this file with git. 


### Run the development server

```bash
workon dennett
export $(cat ~/dennett/config/develop) # replace path with location of your configuration file
python app.py # run development server
```

### Populate database 

With the development server already running, open a new terminal and type:

```bash
workon dennett
export $(cat ~/dennett/config/develop) # replace path with location of your configuration file
python populate.py 
```

### Run tests 

WARNING: Running the test suite will destroy local database!

With the development server already running, open a new terminal and type:

```bash
pytest
```

## Usage

### POSTing new trials

This server accepts any JSON input on URL `api/v2/trials`. No format/schema validation is done.

## Deployment

Deployed using Heroku

```bash
$ heroku login
$ heroku git:remote -a dennett-stage
$ git remote rename heroku heroku-staging
$ heroku git:remote -a dennett
$ git remote rename heroku heroku-production
```

Check remotes with are OK with:
```bash
$ git remote -V
```

Deploy with
```bash
$ git push heroku-staging master
```

Or with for production
```bash
$ git push heroku-production master
```

App configuration is done through environment vars. 

Please checkout [Heroku staging settings](https://dashboard.heroku.com/apps/dennett-stage/settings) 
(or [Heroku production settings](https://dashboard.heroku.com/apps/dennett/settings))
to alter this values.

## How to contribute

Contributions are more than welcome. Here's a list of fundamenetal knowledge you'll need to get started.

### Python
* [Learn Python the hard way](https://learnpythonthehardway.org/book/)
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/)
* [Full stack Python](http://www.fullstackpython.com/table-of-contents.html)
* [The Flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)


### Git
* [Learn git branching](http://learngitbranching.js.org/)
* [Atlassian git tutorials](https://www.atlassian.com/git/tutorials)


### Command line
* [Linux command](http://linuxcommand.org/lc3_learning_the_shell.php)

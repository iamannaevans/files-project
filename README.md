# Files

## Instructions

Create Django project with one app the way it can work as standalone service with exposed json REST API with the name 'files'

Service should cover following situation:

- There are some people (They have some properties like name etc.)
- These people upload some files. (These files have some properties too; like original filename, description, .... they are public or they are private)
- People can add tags to these files so they can filter them.
- Before saving uploaded files to file storage we need to compute sha-512 hash and save it.
- We need to compute something pretty slow (it takes approximately 2 seconds) it can be done after saving the file and returning the response.

'Something pretty slow' is for example some transformation of the file which you know it will take some time.
And you can't afford to wait with the response until it's done. We need to just save the result, not to return it immediately with the POST request response.

You are responsible only for the backend -- your only responsibility is to expose API covering this situation and allows frontend (or any other consumer) to manipulate comfortably with these objects (CRUD).


## Installation

Download and install all dependencies in requirements.txt:
```shell
pip install -r requirements.txt
```

Migrate:
```shell
python manage.py migrate
```

Start server:
```shell
python manage.py runserver
```

## Tags

To add tags in DRF form, input an array of tags, like this:
```
[ "Hello World", "New Tag" ]
```

[![Coverage Status](https://coveralls.io/repos/github/devGenie/bucket_list/badge.svg?branch=master)](https://coveralls.io/github/devGenie/bucket_list?branch=master)

## Bucket List ##
A bucket list is a list of stuff you ought to do sometime in the future mostly before you clock a certain age or even kick the bucket

**Installation**

```
$ git clone https://github.com/devGenie/bucket_list.git
``` 

Navigate to the root folder

```
$ cd bucket_list
```

Fetch from master

```
$ git fetch origin master
```

Setup Virtual Environment

```
$ pip install virtualenv```

```$ pip install virtualenvwrapper```

```$ export WORKHOME=~/Envs```

```$ source /usr/local/bin/virtualenvwrapper.sh```

```$ mkvirtualenv bucketlist```

```$ workon bucketlist```

install the requirements

```$ pip install requirements.txt```

OR

```$ pip install --upgrade -r requirements.txt```

Provide the flask application environment variable

```$ export FLASK_APP=run.py```

run the flask server

```$ flask run```
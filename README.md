# Kumparan Assessment: News and Topic Management

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Made with [Eve](http://python-eve.org): a Python REST API Framework based on Flask, Cerberus and MongoDB.

This app is hosted on [Heroku](https://kumparan-donny.herokuapp.com) and MongoDB database on [mLab](https://mlab.com/).
Try it out:
```
$ curl -i https://kumparan-donny.herokuapp.com/news?pretty
```

## Getting Started
- If you want to run this app locally, create `.env` file on your own:
```
HOST=127.0.0.1
DB_HOST=localhost
DB_PORT=27017
DB_NAME=kumparan
```

- Install requirement dependencies
```
$ pip install -r requirements.txt
```

- Run the app
```
$ python app.py
```

## Test Result
- CRUD news
<img src="https://github.com/ostriandoni/kumparan-assessment/blob/master/assets/basic-api-test-news.png"/>

- CRUD topic
<img src="https://github.com/ostriandoni/kumparan-assessment/blob/master/assets/basic-api-test-topic.png"/>

- One news can contains multiple topics and one topic has multiple news
<img src="https://github.com/ostriandoni/kumparan-assessment/blob/master/assets/advanced-api-test-news-spec.png"/>

- Filter by news status
<img src="https://github.com/ostriandoni/kumparan-assessment/blob/master/assets/advanced-api-test-filter-news-status.png"/>

- Filter news by topic
<img src="https://github.com/ostriandoni/kumparan-assessment/blob/master/assets/advanced-api-test-filter-news-topic.png"/>

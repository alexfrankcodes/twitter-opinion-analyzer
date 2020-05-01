# Twitter Opinion Analyzer
A python web app that lets a user enter a topic and get the current polarity on that topic through sentiment analysis on recent tweets.

## Setup

### 1. Clone repository

```git clone https://github.com/alexfrankcodes/twitter-opinion-analyzer.git
```

### 2. Open project and change into local env

```
cd twitter-opinion-analyzer
source env/Scripts/activate
```

### 3. Install requirements using pip

```
pip install -r requirements.txt 
```

__Note__: executing `flask run` at this stage will open the app, but you will encounter an error if you try and submit a search term. In order to fully run the application, you must [connect with the Twitter API](https://developer.twitter.com/en/docs/basics/getting-started) and insert your own values for the `API_KEY`, `API_SECRET`, `ACCESS_TOKEN`, and `TOKEN_SECRET` variables in `app.py`.


## Release History

* 0.0.1
    * Work in progress

## Meta

Alexander Frank – [@alexfrankcodes](https://twitter.com/alexfrankcodes) – alexfrankcodes@gmail.com

[https://github.com/alexfrankcodes](https://github.com/alexfrankcodes)


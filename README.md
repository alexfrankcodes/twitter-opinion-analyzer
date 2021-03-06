# Twitter Opinion Analyzer
A python web app that lets a user enter a topic and get the current polarity on that topic through sentiment analysis on recent tweets.

Live version can be accessed at https://twitter-opinion-analyzer.herokuapp.com/

## Examples
Here are two examples of the app in action, using the words "Love" (which has a overwhelmingly positive polarity) and "Hate" (which has an overwhelmingly negative polarity).

### Performing a search using the term "Love"
<img src="images/pos_example.png" width="300px">

### Performing a search using the term "Hate"
<img src="images/neg_example.png" width="300px">

## Setup

### 1. Clone repository

```
git clone https://github.com/alexfrankcodes/twitter-opinion-analyzer.git
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

## Next Steps
I'm currently considering alternate ways of calculating and displaying polarity. I'm mainly interested in trying to categorize how strong an opinion is and communicating that to the user, formatted in a way such as the following:

`"The opinion on this topic is [ barely/slightly/moderately/strongly ] [ positive/negative ]."`

## Meta

Alexander Frank – [@alexfrankcodes](https://twitter.com/alexfrankcodes) – alexfrankcodes@gmail.com

[https://github.com/alexfrankcodes](https://github.com/alexfrankcodes)


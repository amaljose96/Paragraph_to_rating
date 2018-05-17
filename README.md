# Basic Sentiment Analyzer using NLTK Vader and TextBlob

The function get_star_rating converts a paragraph into a value between 0 and 10.
Uses [NLTK Vader module](https://github.com/cjhutto/vaderSentiment) and [TextBlob](https://github.com/sloria/TextBlob).

## How it works?
NLTK Vader takes in a sentence and returns a compound score of polarity of the sentence. Hence for a paragraph, average of all sentence scores is used.
TextBlob takes in the entire passage and returns a polarity score and subjectivity score. Subjectivity refers to how relevant the passage is in general.
So a weighted average of Vader and TextBlob scores is taken with Vader having 0.5 weight and TextBlob having subjectivity score as weight.

## Required packages

You need NLTK Vader and TextBlob

> pip install nltk textblob
> python
> nltk.download()

Select all or just the vader package.

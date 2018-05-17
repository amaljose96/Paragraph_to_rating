
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from nltk import tokenize





def get_star_rating(review):
	sentences=tokenize.sent_tokenize(review)
	sid=SentimentIntensityAnalyzer()
	avg_sentiment=0;

	for sentence in sentences:
		avg_sentiment=avg_sentiment+sid.polarity_scores(sentence)['compound'];
	avg_sentiment=avg_sentiment/len(sentences);
	star_rating=(avg_sentiment+1)*10;
	stars_vader=star_rating;
	weight_vader=0.5;
	blob=TextBlob(review)
	avg_sentiment=blob.sentiment.polarity
	star_rating=(avg_sentiment+1)*10;
	stars_blob=star_rating;
	weight_blob=blob.sentiment.subjectivity;
	total_star=(stars_vader*weight_vader+stars_blob*weight_blob)/(weight_vader+weight_blob);
	return total_star;



while(1):
	review=input();
	print("Rating :"+str(get_star_rating(review))+" stars");

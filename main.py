import redis, time
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from helper_lib import label_feats_from_corpus, split_label_feats, token_of_words

def init_classifier():
	lfeats = label_feats_from_corpus(movie_reviews)
	train_feats, test_feats = split_label_feats(lfeats, split=0.75)
	nb_classifier = NaiveBayesClassifier.train(train_feats)
	
	return nb_classifier

def classify(sentence):
	return classifier.classify(token_of_words(sentence))

classifier = init_classifier()
r = redis.StrictRedis(host='172.17.0.2', port=6379, password='foo', charset="utf-8", decode_responses=True)
r.setnx('pk',0)

while True:
	key_count = r.scard('new')			# check for any new entries
	while key_count > 0:				
		pk = r.spop('new')			# get new entry
		cl = classify(r.hget(pk,'text'))	# classify its text
		r.hset(pk, 'class', cl)			# update its class
		r.sadd('done', pk)			# reverse index for web app
		key_count = r.scard('new')
	
	time.sleep(0.2)

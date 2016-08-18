from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from helper_lib import label_feats_from_corpus, split_label_feats, token_of_words

def init_classifier():
	lfeats = label_feats_from_corpus(movie_reviews)
	train_feats, test_feats = split_label_feats(lfeats, split=0.75)
	nb_classifier = NaiveBayesClassifier.train(train_feats)
	
	# some debug output:
	#movie_reviews.categories()
	#lfeats.keys() 
	#from nltk.tokenize import word_tokenize
	
	return nb_classifier

def classify(sentence):
	return classifier.classify(token_of_words(sentence))

classifier = init_classifier()

while True:
	if classify(input("Tell me a sentence: ")) == 'pos':
		print ('I think this is a positive sentence')
	else:
		print ('I think this is a negative sentence')

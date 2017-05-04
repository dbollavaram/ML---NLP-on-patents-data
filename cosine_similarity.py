import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
import re
import nltk
import re, math
from collections import Counter
stop = set(stopwords.words('english'))
file = pd.read_csv('Patent_Part2.csv')
file.head()
WORD = re.compile(r'\w+')

"""Function: prepoc_text
	Preprocessing the text in claims and abstract using this fucntion
	Paramaters:
		x: The textual feature i.e., either abstract or claim is gien as input to thsi function 
	Returns:
		The code returns the preprocessed text after removal of stop words, punctuations, words having length <= 2, stemming, lemmatization and parts-of-speech tagging of text
"""
def prepoc_text(x):
	sent_ = x
	#removing the punctuations, numbers and any other symbols other than alphabets
	sent_ = re.sub("([^a‐zA‐Z])"," ",sent_).lower()
	sent_ = sent_.split()
	#removing words or letters of length greater than 2
	sent_ = [i for i in sent_ if (len(i) > 2) and (i not in stop)]
	# lemmatization of words
	lmtzr = WordNetLemmatizer()
	sent_lem = [lmtzr.lemmatize(i) for i in sent_]
	#stemming the words
	ps = PorterStemmer()
	sent_stem = [ps.stem(i) for i in sent_lem]
	#parts of speech tagging is performed here
	tagged = nltk.pos_tag(sent_stem)
	#considering only nouns, adjectives, adverbs, etc. and removing all conjunctions, prepositions and unwanted words
	list_ = ['CC', 'DT', 'EX', 'IN', 'LS', 'MD', 'PDT', 'POS', 'PRP', 'PRP$', 'RP', 'TO', 'SYM', 'WDT', 'WP','WP$', 'WRB']
	sent_tagged = [i[0] for i in tagged if i[1] not in list_]
	return sent_tagged


"""Function: get_cosine 
	cosine similarity metric is calculated using this function
	Paramaters:
		vec1 : claims of patent
		vec2 : abstract of patent
	Returns:
		The code returns the cosine similarity index between abstract and claims """
def get_cosine(vec1, vec2):
	intersection = set(vec1.keys()) & set(vec2.keys())
	numerator = sum([vec1[x] * vec2[x] for x in intersection])
	sum1 = sum([vec1[x]**2 for x in vec1.keys()])
	sum2 = sum([vec2[x]**2 for x in vec2.keys()])
	denominator = math.sqrt(sum1) * math.sqrt(sum2)
	if not denominator:
		return 0.0
	else:
		return float(numerator) / denominator

"""Function: text_to_vector 
	Converts the text into vector  
	Paramaters:
		text: can be either abstract or claim of a patent  
	Returns:
		The code returns the vector form of the text"""	
def text_to_vector(text):
	words = WORD.findall(text)
	return Counter(words)

#driver function
for i in range(0, file.shape[0]):
	claims = prepoc_text(file.loc[i,'Claims'])
	abstract = prepoc_text(file.loc[i,'Abstract'])
	claim1 = ' '.join(claims)
	abstract1 = ' '.join(abstract)
	text1 = claim1
	text2 = abstract1
	vector1 = text_to_vector(text1)
	vector2 = text_to_vector(text2)
	cosine = get_cosine(vector1, vector2)
	file.loc[i,'cosine'] = cosine
	print(i)

print(file.head())
#writing the output to file
file.to_csv('Patent_Part2_similarity.csv')
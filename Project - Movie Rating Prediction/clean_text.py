from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
# Init Object
tokenizer= RegexpTokenizer(r'\w+') # coverting data into words
en_stopwords= set(stopwords.words('english')) # stoping the words like verb and preposition
ps= PorterStemmer() # same words with different prefix or suffix


def getCleanReviews(review):
    
    review= review.lower()
    review= review.replace("<br /><br />"," ")
    
    #Tokenize
    tokens= tokenizer.tokenize(review)
    new_tokens= [token for token in tokens if token not in en_stopwords] # stopwords
    stemmed_tokens= [ps.stem(token) for token in new_tokens] # stemming
    
    cleaned_review= ' '.join(stemmed_tokens)
    
    return cleaned_review

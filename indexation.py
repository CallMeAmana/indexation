import nltk
from nltk.tokenize import word_tokenize
from langdetect import detect
nltk.download('stopwords')

text =input("DONNEZ UN TEXTE EN FRANCAIS OU BIEN EN ANGLAIS:   ")


lang = detect(text)


if lang == 'en':
    tokens = word_tokenize(text)
elif lang == 'fr':
    tokens = nltk.tokenize.TreebankWordTokenizer().tokenize(text)



motvide_fr = nltk.corpus.stopwords.words('french')
motvide_en = nltk.corpus.stopwords.words('english')
motvide = motvide_fr + motvide_en
tokens = [token for token in tokens if token.lower() not in motvide and token.isalnum() and token.isalpha()]


print(" ".join(tokens))
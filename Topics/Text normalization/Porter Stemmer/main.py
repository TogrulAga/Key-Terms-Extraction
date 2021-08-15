from nltk.stem import PorterStemmer


word = input()
porter = PorterStemmer()

print(porter.stem(word))

from nltk.stem import WordNetLemmatizer


# your code here
word = input()
lemmatizer = WordNetLemmatizer()
for position in "nav":
    print(lemmatizer.lemmatize(word, position))

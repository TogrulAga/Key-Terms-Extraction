from nltk.stem import LancasterStemmer


# the following line reads a text from the input and converts it into a list
sent = input().split()

# write your code here
lancaster = LancasterStemmer()

print(*[lancaster.stem(word) for word in sent], sep="\n")

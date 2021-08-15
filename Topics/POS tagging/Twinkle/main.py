import nltk


poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']

pos_tagged = nltk.pos_tag(poem)

print(*[word for word, tag in pos_tagged if tag == "NN"], sep="\n")

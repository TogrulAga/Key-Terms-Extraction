import nltk


sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']

print(*[tag for word, tag in nltk.pos_tag(sent) if word == "raced"])

# This code is inteded to provide the concept for the next Jaden Smith Album!
# Noah Law
import random
from collections import defaultdict

with open("JadenText.txt") as f:
    words = f.read().split()

word_dict = defaultdict(list)
for word, next_word in zip(words, words[1:]):
    word_dict[word].append(next_word)

word = "Syre"
while not word.endswith("."):
    print(word, end=' ')
    word = random.choice(word_dict[word])
print(word)


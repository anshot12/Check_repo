# Write your code here
import nltk
import random
import re


f = open(f"{input()}", "r", encoding="utf-8")
all_words = nltk.regexp_tokenize(f.read(), r"[^\s]+")
h_bigram_1 = [x for x in all_words]
h_bigram_2 = [x for x in all_words]
del h_bigram_1[-1], h_bigram_2[0]
h_trigrams = [f"{h_bigram_1[i]} {h_bigram_2[i]}" for i in range(len(h_bigram_1))]
del h_trigrams[-1]
t_trigrams = [x for x in all_words]
del t_trigrams[0], t_trigrams[0]
all_bigrams = [[h_trigrams[i], t_trigrams[i]] for i in range(len(h_trigrams))]

dic_bigrams = {}
dic_final = {}
for head, tail in all_bigrams:
    dic_bigrams.setdefault(head, []).append(tail)
for element in dic_bigrams:
    dic_element = {}
    for word in dic_bigrams[element]:
        dic_element.setdefault(word, 0)
        dic_element[word] += 1
    dic_final.setdefault(element, dic_element)
user = (random.sample(dic_final.keys(), 1)[0])

sentence_counter = 0
while sentence_counter != 10:
    word_counter = 0
    sentence = []
    while True:
        keys = []
        weights = []
        for key, value in dic_final[user].items():
            keys.append(key)
            weights.append(value)
        first_word = re.sub(r"[\S]+\s", "", user)
        random_word = (random.choices(keys, weights)[0])
        sentence.append(random_word)
        random_word = first_word + " " + random_word
        word_counter += 1
        user = random_word
        start_word = "[a-z]"
        if sentence[0].endswith((".", "?", "!")) or re.match(start_word, sentence[0]):
            del sentence[0]
            word_counter -= 1
        if word_counter >= 5 and sentence[-1].endswith((".", "?", "!")):
            break

    sentence_counter += 1
    sentence = " ".join(sentence)
    print(sentence)

import random

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

last_word = ''
unique_words = []
words_after_unique = []
all_words = []
key_words = {}
words_after_last_word = []
sentence = ''

for i in text.split():
    if i not in unique_words:
        unique_words.append(i)

for i in text.split():
    all_words.append(i)
all_words.append('')

for i in unique_words:
    for itr in range(len(all_words)):
        if all_words[itr] == i and all_words[itr + 1] not in words_after_unique:
            words_after_unique.append(all_words[itr + 1])

    key_words[i] = words_after_unique
    words_after_unique = []

print(key_words)

for i in range(3):
    last_word = random.choice(unique_words)
    sentence += last_word + ' '
    while last_word[-1] != '.':
        words_after_last_word = key_words[last_word]
        last_word = random.choice(words_after_last_word)
        sentence += last_word + ' '
    print(sentence)
    sentence = ''
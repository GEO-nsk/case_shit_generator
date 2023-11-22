'''
Gagol Egor - 100
Karpenko Nikolay - 30
Tarlo Evgeny - 95
'''

import random

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
file.close()

flag = True
last_word = ''
unique_words = []
words_after_unique = []
all_words = []
key_words = {}
words_after_last_word = []
sentence = ''
unique_words_no_dots = []

# Creating lists with unique words
for i in text.split():
    if i not in unique_words:
        unique_words.append(i)
    if i not in unique_words_no_dots and i[-1] != '.' and i[-1] != '!' and i[-1] != '?' and i[-1] != ';':
        unique_words_no_dots.append(i)

# Creating list with all words
for j in text.split():
    all_words.append(j)
all_words.append('')

# Creating list with words following unique words
for f in unique_words:
    for itr in range(len(all_words)):
        if all_words[itr] == f and all_words[itr + 1] not in words_after_unique:
            words_after_unique.append(all_words[itr + 1])
    key_words[f] = words_after_unique
    words_after_unique = []

# Creating output file with result sentences
with open('output.txt', 'w', encoding='utf-8') as file_out:
    for counter in range(int(text.split()[0])):
        flag = True
        last_word = random.choice(unique_words_no_dots)
        sentence += last_word + ' '
        while flag:
            words_after_last_word = key_words[last_word]
            last_word = random.choice(words_after_last_word)
            sentence += last_word + ' '
            if last_word[-1] == '.' or last_word[-1] == '!' or last_word[-1] == '?' or last_word[-1] == ';':
                flag = False
        file_out.write(sentence)
        sentence = ''
file_out.close()

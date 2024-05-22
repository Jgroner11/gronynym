from english_words import get_english_words_set
from math import ceil
import nltk
from nltk.corpus import words
import pickle

words1 = get_english_words_set(['web2'], lower=True)
 
with open('english_words.txt', 'w') as f:
    for word in words1:
        f.write('%' + word)

word_list = [word.lower() for word in words.words()]
words2 = set(word_list)
with open('nltk_words.txt', 'w') as f:
    for word in words2:
        f.write('%' + word)

with open('scrabble_words.txt', 'r') as f:
     word_list = [line.strip().lower() for line in f]
words3 = set(word_list)

with open('scrabble_words2.txt', 'w') as f:
    for word in words3:
        f.write('%' + word)
        
word_set = words3

# Remove all alphabetical charachters except a and i
for i in range(26):
    word_set.discard(str(chr(97 + i)))
word_set.add('a')
word_set.add('i')


def isGronynym(s):
    max_len = 45 # Longest word in english dictionary is 45
    repetitive = s * (ceil(max_len / len(s)) + 1)
    out = list()
    for i in range(len(s)):
        chck = False
        j = len(repetitive) - 1
        while not chck and j > 0:
            if repetitive[i:i+j] in word_set:
                chck = True
                out.append(repetitive[i:i+j])
            j -= 1
        if not chck:
            return False, []
    return True, out
            
def isPerfectGronynym(s):
    max_len = 45 # Longest word in english dictionary is 45
    repetitive = s * (ceil(max_len / len(s)) + 1)
    out = list()
    for i in range(len(s)):
        chck = False
        j = len(s)
        if repetitive[i:i+j] in word_set:
            out.append(repetitive[i:i+j])
        else:
            return False, []
    return True, out


gronynms = dict()
perfect_gronynyms = dict()

n = 0
for word in word_set:
    print(n)
    a, b = isGronynym(word)
    if a:
        gronynms[word] = b
    a, b = isPerfectGronynym(word)
    if a:
        perfect_gronynyms[word] = b
    n += 1

with open('gronynyms.pkl', 'wb') as fp:
    pickle.dump([gronynms, perfect_gronynyms], fp)
# while True:
#     print(isGronynym(input()))[1]

#--------------------------------------------
#   Name: Zhuofan Sun
#   ID: 1740983
#   CMPUT 274, Fall 2021
#
#   Weekly Exercise #4: Text Preprocessor
#--------------------------------------------

import string
import sys

try:
    mode = sys.argv[1]
    if mode == 'keep-digits' or mode == 'keep-stops' or mode == 'keep-symbols':
        pass
    elif mode != 'keep-digits' or mode != 'keep-stops' or mode != 'keep-symbols':
        print("undefined mode. Usage: python3 preprocess.py <mode>")
        sys.exit()
except IndexError:
    mode = 'nothing'

text = input()
lower = text.lower()
remove = str.maketrans('', '', string.punctuation)
lst = []
lst1 = lower.split()
for words in lst1:
    if mode != 'keep-symbols':
        lst.append(words.translate(remove))
    else:
        lst.append(words)
without_punctuation = ' '.join(lst)
remove = str.maketrans('', '', string.digits)
lst = []
lst1 = without_punctuation.split()
for words in lst1:
    if words.isnumeric() and mode != "keep-digits":
        lst.append(words)
    if mode != 'keep-digits':
        lst.append(words.translate(remove))
    else:
        lst.append(words)

without_punctuation_num = ' '.join(lst)

stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
             "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her",
             "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs",
             "themselves", "what", "which", "who", "whom", "this", "that", "these", "those",
             "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
             "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
             "or", "because", "as", "until", "while", "of", "at", "by", "for", "with",
             "about", "against", "between", "into", "through", "during", "before", "after",
             "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
             "under", "again", "further", "then", "once", "here", "there", "when", "where",
             "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
             "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
             "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
lst = without_punctuation_num.split()
for i in stopwords:
    for j in lst:
        if i == j and mode != 'keep-stops':
            lst.remove(j)
        else:
            pass
string = ' '.join(lst)
print(string)

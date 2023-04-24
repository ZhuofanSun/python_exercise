#--------------------------------------------
#   Name: Zhuofan Sun
#   ID: 1740983
#   CMPUT 274
#
#   Weekly Exercise 3: Word Frequency
#--------------------------------------------

import sys

try:
    file = open(sys.argv[1])
except IndexError:
    print("Too few arguments. Usage: python3 freq.py <input file name>")
    sys.exit()
except FileNotFoundError:
    print("Too many arguments. Usage: python3 freq.py <input file name>")
    sys.exit()

txt = file.read()
file.close()
words = txt.split()
"""print(words)"""

"""for word in words:
    words_select[word] = words_select.get(word, 0) + 1"""
"""print(words_select)"""

words_list = list(words)


def Up(lst):
    up = []
    for i in lst:
        lst2 = []
        for item in i:
            lst2.append(item)
        if item == '"':
            up.append(i)
            continue
        if lst2[-1].isupper():
            up.append(i)
        for item in lst2:
            if lst2[0].isupper():

                if item.isupper():
                    continue
                elif item.islower:
                    up.append(i)
                    break
    up.sort(reverse=False)
    return up


def Low(lst):
    low = []
    for i in lst:
        lst2 = []
        for item in i:
            lst2.append(item)
        for item in lst2:

            if item.isupper():
                break
            else:
                low.append(i)
                break

    for i in low:
        lst3 = []
        for item in i:
            lst3.append(item)
        if lst3[0] == '"':
            low.remove(i)
            break
    low.sort(reverse=False)

    return low


Upper_words_list = Up(words_list)
Lower_words_list = Low(words_list)

Upper_words_dic = {}

for word in Upper_words_list:
    if word not in Upper_words_dic:
        Upper_words_dic[word] = 1
    else:
        Upper_words_dic[word] += 1
Lower_words_dic = {}
for word in Lower_words_list:
    if word not in Lower_words_dic:
        Lower_words_dic[word] = 1
    else:
        Lower_words_dic[word] += 1

Words_dic = {}
Words_dic.update(Upper_words_dic)
Words_dic.update(Lower_words_dic)

freq = 0

for word in Words_dic.keys():
    freq += Words_dic[word]
fil = open(sys.argv[1] + '.out', mode='w')
for word in Words_dic.keys():
    print(word, Words_dic[word], round((Words_dic[word] / freq), 3), file=fil)
fil.close()

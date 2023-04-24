import random

UppercaseCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'          # define the uppercase characters
LowercaseCharacters = 'abcdefghijklmnopqrstuvwxyz'          # define the lowercase characters
DecimalDigits = '0123456789'                                # define the decimal digits
SpecialCharacters = r'''!-$%&'()*+,./:;<=>?_[]^`{|}~'''     # define the special characters


def generate(n):
    lst = []
    while len(lst) < n:
        if len(lst) < n:
            lst.append(random.choice(UppercaseCharacters))
        else:
            break
        if len(lst) < n:
            lst.append(random.choice(LowercaseCharacters))
        else:
            break
        if len(lst) < n:
            lst.append(random.choice(DecimalDigits))
        else:
            break
        if len(lst) < n:
            lst.append(random.choice(SpecialCharacters))
        else:
            break

    for i in list(lst):
        print(i, end='')


#generate()

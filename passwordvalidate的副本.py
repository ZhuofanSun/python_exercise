# -------------------------------------------------------------------
# Name : Zhuofan Sun
# ID : 1740983
#
# Weekly Exercise #1: Password Validator
# -------------------------------------------------------------------


import random

UppercaseCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # define the uppercase characters
LowercaseCharacters = 'abcdefghijklmnopqrstuvwxyz'  # define the lowercase characters
DecimalDigits = '0123456789'  # define the decimal digits
SpecialCharacters = r'''!-$%&'()*+,./:;<=>?_[]^`{|}~'''  # define the special characters



def validate(password):
    test = 'test'  # initialize a variable for breaking
    for i in password:
        if i == " " or i == "@" or i == "#":  # situation of invalid
            test = 'Invalid'
            print(test)
            break  # if one forbidden character occurs, we do not need to
            # continue
        else:
            continue  # if there is no forbidden character, we can continue

    if test == 'Invalid':  # if the code is tested to be invalid, we do not need to validate again
        pass

    elif len(password) < 8:  # situation of invalid
        x = 'Invalid'
        print(x)

    else:
        pass  # if the code do not reach the situation of invalid, we can continue
    level = 0  # initialize the number of secure situation (secure level)that the code reach
    for i in password:
        if test == 'Invalid':  # if the code is invalid, we do not need to test if it is secure
            break  # if this situation is reached, we only need to count once
        elif i in UppercaseCharacters:
            level += 1
            break
    for i in password:
        if test == 'Invalid':  # if the code is invalid, we do not need to test if it is secure
            break
        elif i in LowercaseCharacters:
            level += 1
            break
    for i in password:
        if test == 'Invalid':  # if the code is invalid, we do not need to test if it is secure
            break
        elif i in DecimalDigits:
            level += 1
            break
    for i in password:
        if test == 'Invalid':  # if the code is invalid, we do not need to test if it is secure
            break
        elif i in SpecialCharacters:
            level += 1
            break
    if test == 'Invalid':
        pass
    elif level < 4:
        print('Insecure')  # if not all secure requirements are reached, code is insecure
    else:
        print('Secure')  # otherwise, it is secure

    pass


'''  validate('''''')  '''  # use of the function


def generate(n):  # n >= 8
    lst = []  # setup an empty list to put the generated code
    while len(lst) < n:  # loop for n times
        if len(lst) < n:  # if the length of code do not reach the required length, we can continue
            lst.append(random.choice(UppercaseCharacters))
        else:  # if the length of code reach the required length, we do not need to add characters
            break
        if len(lst) < n:  # if the length of code do not reach the required length, we can continue
            lst.append(random.choice(LowercaseCharacters))
        else:  # if the length of code reach the required length, we do not need to add characters
            break
        if len(lst) < n:  # if the length of code do not reach the required length, we can continue
            lst.append(random.choice(DecimalDigits))
        else:  # if the length of code reach the required length, we do not need to add characters
            break
        if len(lst) < n:  # if the length of code do not reach the required length, we can continue
            lst.append(random.choice(SpecialCharacters))
        else:  # if the length of code reach the required length, we do not need to add characters
            break

    for i in list(lst):
        print(i, end='')  # change the style of generated code to the string, and not in a new line


''' generate() '''  # use of the function

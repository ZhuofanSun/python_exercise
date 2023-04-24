a = '01010111 01101001 01101100 01101100 01101001 01100001 01101101 '
a_list = a.split()
a_lst = []
for i in a_list:
    a_lst.append(int(i, 2))
for item in a_lst:
    print(chr(int(item)), end='')
print('')
a = '01001101 01100001 01101010 01101111 01110010 00100000 01101111 01100110 00100000 01000011 00101110 ' \
    '01010011 00101110 '
a_list = a.split()
a_lst = []
for i in a_list:
    a_lst.append(int(i, 2))
for item in a_lst:
    print(chr(int(item)), end='')
print('')
a = '01001001 01000111 00111010 00100000 01110111 01101001 01101100 01101100 01101001 01100001 01101101 01101011 ' \
    '01110101 01101111 01101000 01101001 01101101 01110011 01100101 01101100 01100110 '
a_list = a.split()
a_lst = []
for i in a_list:
    a_lst.append(int(i, 2))
for item in a_lst:
    print(chr(int(item)), end='')
print('')
s = '\u9586\u5fc3\u5c31\u597d\u0020\u7121\u9700\u5b9a\u7fa9\u003d\u0029\u0029\u0029'

print(s)


stri= '我的意思是你笨'
uni = stri.encode('unicode-escape').decode()
print(uni)

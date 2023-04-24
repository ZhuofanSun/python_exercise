import random
print(random.random())
print(random.randint(0,9))       # 包括右边
print(random.randrange(0,10,2))  # 不包括右边
string = 'hello             world'
print(random.choice(string))
print(random.uniform(1,10))     # 可以生成小数
UppercaseCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'            # define the uppercase characters
LowercaseCharacters = 'abcdefghijklmnopqrstuvwxyz'            # define the lowercase characters
DecimalDigits = '0123456789'                                  # define the decimal digits
SpecialCharacters = r'''!-$%&'()*+,./:;<=>?_[]^`{|}~'''       # define the special characters
lst1 = random.choice(UppercaseCharacters)
lst2 = random.choice(LowercaseCharacters)
lst3 = random.choice(DecimalDigits)
lst4 = random.choice(SpecialCharacters)
print(lst1, lst2, lst3, lst4)
lst5 = [1,2,3,4,5,6,7,8]
random.shuffle(lst5)
print(lst5)
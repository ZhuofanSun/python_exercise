def decimalToBinary(dec):
    quotient = dec
    remainder = 0
    binStr = ''
    while quotient > 0:
        remainder = (quotient % 2)
        binStr = str(remainder) + binStr
        quotient = quotient // 2
    return binStr


decimal = int(input("Enter a decimal value: "))
print(decimalToBinary(decimal))

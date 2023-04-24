# 。 会员   >=200  八折
#          >=100  九折
#          <100   不打折
#    非会员  >='200  九五折
X = float(input('please enter the value'))
Y = input('if you are prime?(Yes or No)')
if Y == 'Yes':
    if X >= 200:
        print('it costs:', X*0.8)
    elif X >= 100 and X < 200:
        print('it cost:', X*0.9)
    else: print('it costs:, X')
elif Y == 'No':
    if X>= 200:
        print('it costs:',X*0.95)
    else: print('it cost:', X)





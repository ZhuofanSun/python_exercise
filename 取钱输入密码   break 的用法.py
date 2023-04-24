#银行取钱，最多输入三次密码，输入对了就不需要继续了
for item in range(3):
    x = input('请输入密码：')
    if x == '123456':
        print('密码正确')
        break
    elif x != 123456:
        print('密码错误，请重新输入')

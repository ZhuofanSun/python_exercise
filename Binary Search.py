

def search(list, num):
    x = False
    a = 0
    b = len(list) - 1
    while a <= b and not x:
        midpoint = (b + a) // 2
        if list[midpoint] == num:
            x = True
        else:
            if list[midpoint] > num:
                b = midpoint - 1
            else:
                a = midpoint + 1
    else:
        pass

    return x


print(search([1, 2, 3, 4, 5, 6], 0))

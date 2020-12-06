from aocd import get_data

mylist = set(map(int, get_data(open(file='token.input').read(), day=1, year=2020).splitlines()))

templist = mylist.copy()
stop = False
for i in mylist:
    for j in templist:
        c = 2020 - i - j
        if c in mylist:
            print(i, j, c, i*j*c)
            stop = True
            break
    if stop == True:
        break
    else:
        templist.pop()
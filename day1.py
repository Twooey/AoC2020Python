with open('day1.txt', 'rb') as f:
    mylist = set(map(int, f))
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
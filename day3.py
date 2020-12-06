from aocd import get_data
m = []

for line in get_data(open(file='token.input').read(), day=3, year=2020).splitlines():
    m.append(line.strip())



def treeSlope(vert, hor):
    loc = 0
    trees = 0

    for idx, val in enumerate(m):
        if idx % hor != 0:
            continue
        count = 0
        if val[loc] == '#':
            trees += 1
        while count < vert:
            if loc < len(val):
                loc += 1
            if loc == len(val):
                loc = 0
            count += 1
    return(trees)


total = treeSlope(1,1) * treeSlope(3, 1) * treeSlope(5, 1) * treeSlope(7, 1) * treeSlope(1, 2)
print(total)
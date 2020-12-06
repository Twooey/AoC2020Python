import re

f = []
regex = r"(\d+)\-(\d+\s\D)\:(\s\w+)"
subst = "\\1 \\2\\3\\r"

for line in open("day2.input", "r"):
    temp = re.sub(regex, subst, line, 1).strip().split(" ")
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    f.append(temp)



total = 0
for i in f:
    count = 0
    for c in i[3]:
        if c == i[2]:
            count += 1
    if i[0] <= count <= i[1]:
        total += 1
print(total)

p2total = 0
for i in f:
    if (i[3][i[0] -1] == i[2]) != (i[3][i[1]-1] == i[2]):
        p2total += 1

print(p2total)
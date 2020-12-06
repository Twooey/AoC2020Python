p1total = p2total = 0
first = True
p1count = p2count = set()
for line in open("day6.input", "r").read().split('\n'):
    # I haven't worked out the edge case. This only works if you have a blank line at the end of your input.
    if line == '':
        p1total += len(p1count)
        p2total += len(p2count)
        p1count = p2count = set()
        first = True
        continue
    p1count = set(p1count) | set(line)
    if first:
        p2count = set(line)
        first = False
    p2count = set(p2count) & set(line)

print(p1total, '\n', p2total, sep='')

from aocd import get_data
seatIDs = {(int(s.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)) for s in get_data(open(file='token.input').read(), day=5, year=2020).splitlines()}

for i in range(min(seatIDs), max(seatIDs)):
    if not (i in seatIDs):
        print('Highest Seat ID: ', max(seatIDs), '\n', 'Your Seat ID is: ', i, sep='')
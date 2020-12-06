seatIDs = {(int(s.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)) for s in open('day5.input', 'r')}

for i in range(min(seatIDs), max(seatIDs)):
    if not (i in seatIDs):
        print('Highest Seat ID: ', max(seatIDs), '\n', 'Your Seat ID is: ', i, sep='')
NR_PER_SIDE = 12
TOTAL = 144

with open('day_4/input.txt', 'r') as fptr:
    toiletpaper = [0] * TOTAL
    minesweeps = [0] * TOTAL
    
    for i in range(NR_PER_SIDE):
        toiletpaper[i] = 0
    
    sweep_i = NR_PER_SIDE
    
    for line in fptr:
        line = line.strip()
        if not line:
            continue
            
        toiletpaper[sweep_i] = 0 # left buffer
        sweep_i += 1
        
        for char in line:
            if char == '@':
                toiletpaper[sweep_i] = -5
            else:
                toiletpaper[sweep_i] = 0
            sweep_i += 1
            
        toiletpaper[sweep_i] = 0 # right buffer
        sweep_i += 1
    
    for i in range(TOTAL - NR_PER_SIDE, TOTAL): # last row of buffer
        toiletpaper[i] = 0
    
    for y in range(0, NR_PER_SIDE):
        for x in range(0, NR_PER_SIDE):
            if toiletpaper[y * NR_PER_SIDE + x] != 0:
                minesweeps[y * NR_PER_SIDE + x - 1] += 1
                minesweeps[y * NR_PER_SIDE + x + 1] += 1
                minesweeps[(y - 1) * NR_PER_SIDE + x] += 1
                minesweeps[(y + 1) * NR_PER_SIDE + x] += 1 
                minesweeps[(y - 1) * NR_PER_SIDE + x - 1] += 1
                minesweeps[(y - 1) * NR_PER_SIDE + x + 1] += 1
                minesweeps[(y + 1) * NR_PER_SIDE + x - 1] += 1
                minesweeps[(y + 1) * NR_PER_SIDE + x + 1] += 1
    
    total = 0
    for y in range(1, NR_PER_SIDE-1):
        for x in range(1, NR_PER_SIDE-1):
            idx = y * NR_PER_SIDE + x
            if minesweeps[idx] < 4 and toiletpaper[idx] == -5:
                total += 1
        
    print(total)


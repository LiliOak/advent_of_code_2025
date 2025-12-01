
file = open("day_1/input.txt", "r")
place = 50
zero_passes = 0

for line in file:
    direction = line.strip()[:1]
    iterations = int(line.strip()[1:]) % 100
    zero_passes += int(line.strip()[1:]) // 100
    if direction == "L":
        if place-iterations<0:
            if place!=0:
                zero_passes += 1
                print("L" + str(iterations))
            place = 100+(place-iterations)            
        else:
            place = place-iterations
            if place==0:
                zero_passes += 1
    if direction == "R":
        if place+iterations>99:
            place = place+iterations-100
            zero_passes+=1
            print("R" + str(iterations))
        else:
            place = place+iterations
print(zero_passes)
    

        


        
file.close()

file = open("day_1/input.txt", "r")
place = 50
zeros = 0

for line in file:
    direction = line.strip()[:1]
    iterations = int(line.strip()[1:]) % 100
    if direction == "L":
        if place-iterations<0:
            place = 100+(place-iterations)
        else:
            place = place-iterations
    if direction == "R":
        if place+iterations>99:
            place = place+iterations-100
        else:
            place = place+iterations
    if place == 0:
        zeros += 1
    # print(place)
print(zeros)
    

        


        
file.close()
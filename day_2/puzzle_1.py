with open('day_2/input.txt','r') as file:
    print(sum(int(i) for x in [[string.split("-")[0],string.split("-")[1]] for string in file.read().split(",")] for i in range(int(x[0]), int(x[1])+1) if str(i)[:len(str(i))//2]==str(i)[len(str(i))//2:]))
















"""
# This is the solution how I originally wrote it, unfortunately far more readable:

file = open("day_2/input.txt", "r")
total = 0

for x in [[string.split("-")[0],string.split("-")[1]] for string in file.read().split(",")]:
    for i in range(int(x[0]), int(x[1])+1):
        if str(i)[:len(str(i))//2]==str(i)[len(str(i))//2:]:
            total += int(i)
file.close()

"""

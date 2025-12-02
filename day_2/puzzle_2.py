file = open("day_2/input.txt", "r")
total = []

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    if len(lst)==n: # ADDED IN BECAUSE THIS KEEPS MY CODE FROM FALLING APPART (TOO TIRED FOR COHERENT EXPLANATION, SORRY!)
        return lst
    for i in range(0, len(lst), n):
        yield lst[i:i + n] # FIRST TIME USING YIELD! 


for x in [[string.split("-")[0],string.split("-")[1]] for string in file.read().split(",")]:
    for i in range(int(x[0]), int(x[1])+1):
        for s in range(1, len(str(i))+1):
            if len(str(i))%s==0:
                snips = chunks(str(i), s)
                if len(set(snips))==1:
                    total.append(i)


print(sum(set(total)))
file.close()
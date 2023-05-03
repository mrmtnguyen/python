import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    experimentList = []
    streakTail=0
    streakHead=0
    for i in range(0,99):
        experimentList.append(random.randint(0, 1))
        if (experimentList[i]==0):
            streakHead+=1
            if (streakHead==6):
                numberOfStreaks+=1
                streakHead=0
            streakTail=0
        else:
            streakTail+=1
            if (streakTail==6):
                numberOfStreaks+=1
                streakTail=0
            streakHead=0
    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))

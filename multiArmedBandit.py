import random


def explore():
    count = 0
    for i in range(100):  # 100 trials
        C1 = 9  # cafeteria 1 AVG Hapiness
        SD = 3  # cafeteria 1 St. Dev
        r1 = (random.normalvariate(C1, SD))  # random number generator based on AVG and st.Dev
        count = count + r1  # adding each random number to the total

    count2 = 0
    for i in range(100):
        C2 = 7  # cafeteria 2 AVG Hapiness
        SD2 = 5  # cafeteria 2 St. Dev
        r2 = (random.normalvariate(C2, SD2))  # random number generator based on AVG and st.Dev
        count2 = count + r2

    count3 = 0

    for i in range(100):
        C3 = 11  # cafeteria 3 AVG Hapiness
        SD3 = 7  # cafeteria 3 St. Dev
        r3 = (random.normalvariate(C3, SD3))  # random number generator based on AVG and st.Dev
        count3 = count + r3


    sum = count + count2 + count3  # adding all of the total hapiness from 3 cafertias
    return sum  # returns total hapiness




def exploit():
    total = 0 #initializing total

    C1 = 9
    SD = 3
    r1 = (random.normalvariate(C1, SD))
    total = total + r1


    C2 = 7
    SD2 = 5
    r2 = (random.normalvariate(C2, SD2))
    total = total + r2


    C3 = 11
    SD3 = 7
    r3 = (random.normalvariate(C3, SD3))
    total = total + r3

    r = max(r1, r2, r3)

    if (r == r1):
        A = 9
        SD = 3

    elif (r == r2):
        A = 7
        SD = 5
    else:
        A = 11
        SD = 7

    for i in range(297):
        p = (random.normalvariate(A, SD))
        total = total + p
    return total



def eGreedy(e: int) -> int:
    percent = e / 1  # e as a percentage
    day1Happiness = random.normalvariate(9, 3)  # first visit to cafeteria 1
    day2Happiness = random.normalvariate(7, 5)  # first visit to cafeteria 2
    day3Happiness = random.normalvariate(11, 7)  # first visit to cafeteria 3

    # happy(1-3) is the variable that tracks the total happiness for respective cafeteria
    happy1 = day1Happiness
    happy2 = day2Happiness
    happy3 = day3Happiness

    #print("Starting Happiness Rating of Cafe (1-3):\t", happy1, happy2, happy3)
    day1, day2, day3 = 1, 1, 1

    # ignore h, v - just to check
    h = 0
    v = 0

    # for loop that checks rating for rest of the 297 days
    for i in range(297):
        # generates the random float between 0-1
        randomValue = random.random() * 100

        # this conditional statement checks if random percentage is -
        # less then e percentage and chooses a random cafeteria
        if randomValue < percent:
            # choses a random cafeteria (1-3)
            cafeteria = random.randint(1, 3)
            v += 1

        # this conditional statement checks for the best rated cafeteria and assigns cafeteria to the number
        else:

            if day1Happiness > day2Happiness and day1Happiness > day3Happiness:
                cafeteria = 1

            elif day2Happiness > day1Happiness and day2Happiness > day3Happiness:
                cafeteria = 2

            else:
                cafeteria = 3

            h += 1

        # This conditional statement checks cafeteria number and adds a day and rating
        if cafeteria == 1:
            happy1 += random.normalvariate(9, 3)
            day1 += 1

        elif cafeteria == 2:
            happy2 += random.normalvariate(7, 5)
            day2 += 1

        else:
            happy3 += random.normalvariate(11, 7)
            day3 += 1

        # averages rating for each cafe formula = (happiness/days)
        day1Happiness = happy1 / day1
        day2Happiness = happy2 / day2
        day3Happiness = happy3 / day3

    #print("Picked cafe:", h, "  ||  ", "Random cafe:", v)
    #print("Average Happiness Rating of Cafe (1-3): \t", day1Happiness, day2Happiness, day3Happiness)

    totalHappy = happy1 + happy2 + happy3
    #print("\n\nSum E-Greedy:", totalHappy)

    return totalHappy



def simulation(e: int, t: int):

    exploitResult = 0
    exploreResult = 0
    greedyResult = 0

    for i in range(t):
        exploitResult += exploit()
        exploreResult += explore()
        greedyResult += eGreedy(e)
    exploreResult /= t
    exploitResult /= t
    greedyResult /= t

    Averages = {"C1": 9, "C2": 7, "C3": 11} #dictionary of

    Values = Averages.values()


    Keys = Averages.keys()

    maxVal = max(Values)

    optimumHappiness = maxVal * 300

    expectedHappiness = (Averages['C1'] * 100 + Averages['C2'] * 100 + Averages['C3'] * 100) #expected hapiness for explore method

    expectedHappiness2 = (Averages['C1'] + Averages['C2'] + Averages['C3']) + (297 * maxVal) #expected hapiness for exploit method

    expectedHappiness3 = (Averages['C1'] * 264 + Averages['C1'] * 12 + Averages['C2'] * 12 + Averages['C2'] * 12) #expected hapiness for eGreedy method



    print("Explore Method Trials:")
    print("Optimum Hapiness: " + str(optimumHappiness))
    print("Expected Hapiness: " + str(expectedHappiness))
    print("Average Hapiness " + str(exploreResult))
    print("Expected Regret: " + str(optimumHappiness - expectedHappiness))
    print("Simulated Regret: " + str(optimumHappiness - exploreResult))

    print("__________________________________")

    print("Exploit Method Trials:")
    print("Optimum Hapiness: " + str(optimumHappiness))
    print("Expected Hapiness: " + str(expectedHappiness2))
    print("Average Hapiness " + str(exploitResult))
    print("Expected Regret: " + str(optimumHappiness - expectedHappiness2))
    print("Simulated Regret: " + str(optimumHappiness - exploitResult))

    print("__________________________________")

    print("eGreedy Method Trials:")
    print("Optimum Hapiness: " + str(optimumHappiness))
    print("Expected Hapiness: " + str(expectedHappiness3))
    print("Average Hapiness " + str(greedyResult))
    print("Expected Regret: " + str(optimumHappiness - expectedHappiness3))
    print("Simulated Regret: " + str(optimumHappiness - greedyResult))


simulation(12, 100000)

import random

def explore():
    count = 0
    for i in range(100):
        C1 = 9
        SD = 3
        r1 = (random.normalvariate(C1, SD))
        count = count + r1
    print("Cafeteria 1 Hapiness: ")
    print(count)

    count2 = 0
    for i in range(100):
        C2 = 7
        SD2 = 5
        r2 = (random.normalvariate(C2, SD2))
        count2 = count + r2
    print("Cafeteria 2 Hapiness: ")
    print(count2)

    count3 = 0

    for i in range(100):
        C3 = 11
        SD3 = 7
        r3 = (random.normalvariate(C3, SD3))
        count3 = count + r3
    print("Cafeteria 3 Hapiness: ")
    print(count3)

    sum = count + count2 + count3
    print("Sum: ")
    print(sum)




explore()

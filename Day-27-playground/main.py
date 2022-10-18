def sum(*num):
    sum = 0
    for n in num:
        sum += n
    return sum

def average(*num):
    sum = 0
    for n in num:
        sum += n
    return round( sum/len(num), 2)


print(average(2, 3, 4, 5, 6, 7, 5))


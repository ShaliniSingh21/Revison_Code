numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
c=0
i=0
while i<len(numbers):
    if numbers[i]> 20:
        c=c+1
    i=i+1
    print(c)
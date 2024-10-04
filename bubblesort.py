unsortedList = [3, 1, 4, 1, 5, 9, 2, 6]
length = len(unsortedList)
for i in range(length):
    for j in range(0, length-i-1):
        if unsortedList[j] > unsortedList[j + 1]:
            # Swap elements if they are in the wrong order
            unsortedList[j], unsortedList[j + 1] = unsortedList[j + 1], unsortedList[j]

print(unsortedList)
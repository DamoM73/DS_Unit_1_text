# this program sort the items in the values list

def bubbleSort(values):
    num = len(values)

    # traverse through all list elements
    for i in range(num):

        # the last i elements of the list are already sorted
        for j in range(0, num - i - 1):
            print(values)
            if  values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
            


# **** MAIN PROGRAM ****

values = [19, 10, 8 , 17, 9]

bubbleSort(values)

print(values)   
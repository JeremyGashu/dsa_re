def bubbleSort(L):
    for i in range(len(L)):
        swapped = False
        for j in range(len(L) - i - 1):
            if(L[j] > L[j+1]):
                L[j], L[j+1] = L[j+1], L[j]
                swapped = True
        if swapped == False:
            break

    return L


print(bubbleSort([1, 4, 2, 6, 7, 3, 1, 1]))

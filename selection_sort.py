def selectionSort(L):
    for i in range(len(L)):
        min_idx = i
        for j in range(i+1, len(L)):
            if L[min_idx] > L[j]:
                min_idx = j
        L[min_idx], L[i] = L[i], L[min_idx]

    return L

print(selectionSort([1, 2, 45, 21, 34, 21]))
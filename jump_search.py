import math

def jump_search(L, item):
    n = len(L)
    m = int(math.sqrt(n))
    i = 0
    while(i < n - 1 and L[i] < item):
        # if the pointer is greater
        # if the pointer is less
        # if the pointer is equal
        if(L[i+m-1] == item):
            return i + m - 1
        elif (L[i + m - 1] > item):
            sub_list = L[i : i + m - 1]
            return linear_search(sub_list, item, i)
        i += m
    sub_list = L[i : i + m]
    return linear_search(sub_list, item, i)
    
def linear_search(L, item, loc):
    n = len(L)
    i = 0
    while (i<n):
        if(L[i] == item):
            return loc + i
        i += 1
    return -1
print(jump_search([1,2,3,5,6,7,9], 5))
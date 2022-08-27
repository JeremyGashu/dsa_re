import heapq
from operator import ge
from typing import List


def getMaxPop(logs: List[List]) -> List:
    population = {}
    for birth, death in logs:
        for i in range(birth, death + 1):
            if(i == death):
                population.setdefault(i, 0)
                if(population[i] > 0):
                    population[i] -= 1
                    break
            else:
                population.setdefault(i, 0)
                population[i] += 1

    maxHeap = [[-cnt, year] for year, cnt in population.items()]
    heapq.heapify(maxHeap)
    _, year = heapq.heappop(maxHeap)
    return year
getMaxPop([[1993,1999],[2000,2010]])

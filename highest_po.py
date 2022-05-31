from typing import List


class Person:
    def __init__(self, birth, death) -> None:
        self.birth = birth
        self.death = death

    def __str__(self) -> str:
        return '{0} {1}'.format(self.birth, self.death)


people = [Person(1921, 2000), Person(1933, 2001), Person(1900, 1920), Person(1801, 2020)]


def maximumPopulation(self, logs: List[List[int]]) -> int:
    population = {}
    maxPop = 0
    maxYear = 0
    for birth, death in people:
        for i in range(birth, death + 1):
            population.setdefault(i, 0)
            if i == death:
                if population[i] > 0:
                    population[i] -= 1
                if population[i] > maxPop:
                    maxPop = population[i]
                    maxYear = i
                continue
            population[i] += 1
            if population[i] > maxPop:
                maxPop = population[i]
                maxYear = i
    return maxYear

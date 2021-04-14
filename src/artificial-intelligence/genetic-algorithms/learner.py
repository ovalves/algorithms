from random import random
from phenotype import Phenotype

class Learner():
    def __init__(self, populationSize):
        self.populationSize = populationSize
        self.population = []
        self.generation = 0
        self.bestSolution = 0
        self.solutions = []

    def init(self, cartSpace, cartPrice, limit):
        for _ in range(self.populationSize):
            self.population.append(Phenotype(cartSpace, cartPrice, limit))
        self.bestSolution = self.population[0]

    def sortPopulation(self):
        self.population = sorted(self.population,
                                key = lambda population: population.evaluationRate,
                                reverse = True)

    def changeBestSolution(self, phenotype):
        if phenotype.evaluationRate > self.bestSolution.evaluationRate:
            self.bestSolution = phenotype

    def sumCartTotalRate(self):
        total = 0
        for phenotype in self.population:
           total += phenotype.evaluationRate
        return total

    def getParents(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.population) and soma < valor_sorteado:
            soma += self.population[i].evaluationRate
            pai += 1
            i += 1
        return pai

    def printGeneration(self):
        print("G:%s -> Valor: %s Espaço: %s Cromossomo: %s" % (self.population[0].generation,
                                                               self.population[0].evaluationRate,
                                                               self.population[0].usedSpace,
                                                               self.population[0].chromosome))

    def solve(self, mutationRate, generations, cartSpace, cartPrice, limit):
        self.init(cartSpace, cartPrice, limit)

        for phenotype in self.population:
            phenotype.evaluate()

        self.sortPopulation()
        self.bestSolution = self.population[0]
        self.solutions.append(self.bestSolution.evaluationRate)

        self.printGeneration()

        for _ in range(generations):
            cartTotalRate = self.sumCartTotalRate()
            newGeneration = []

            for _ in range(0, self.populationSize, 2):
                parent1 = self.getParents(cartTotalRate)
                parent2 = self.getParents(cartTotalRate)

                childrens = self.population[parent1].crossover(self.population[parent2])

                newGeneration.append(childrens[0].mutation(mutationRate))
                newGeneration.append(childrens[1].mutation(mutationRate))

            self.population = list(newGeneration)

            for phenotype in self.population:
                phenotype.evaluate()

            self.sortPopulation()

            self.printGeneration()

            self.solutions.append(self.population[0].evaluationRate)
            self.changeBestSolution(self.population[0])

        print("\nMelhor solução -> G: %s Valor: %s Espaço: %s Cromossomo: %s" %
              (self.bestSolution.generation,
               self.bestSolution.evaluationRate,
               self.bestSolution.usedSpace,
               self.bestSolution.chromosome))

        return self.bestSolution.chromosome
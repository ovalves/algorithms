from random import random

class Phenotype():
    def __init__(self, cartSpace, cartPrice, cartLimitSpace, generation=0):
        self.cartSpace = cartSpace
        self.cartPrice = cartPrice
        self.cartLimitSpace = cartLimitSpace
        self.evaluationRate = 0
        self.usedSpace = 0
        self.generation = generation
        self.chromosome = []

        for _ in range(len(cartSpace)):
            if random() < 0.5:
                self.chromosome.append("0")
            else:
                self.chromosome.append("1")

    def evaluate(self):
        rate = 0
        sumSpaces = 0
        for i in range(len(self.chromosome)):
           if self.chromosome[i] == '1':
               rate += self.cartPrice[i]
               sumSpaces += self.cartSpace[i]
        if sumSpaces > self.cartLimitSpace:
            rate = 1
        self.evaluationRate = rate
        self.usedSpace = sumSpaces

    def crossover(self, otherPhenotype):
        corte = round(random()  * len(self.chromosome))

        children1 = otherPhenotype.chromosome[0:corte] + self.chromosome[corte::]
        children2 = self.chromosome[0:corte] + otherPhenotype.chromosome[corte::]

        childrens = [Phenotype(self.cartSpace, self.cartPrice, self.cartLimitSpace, self.generation + 1),
                  Phenotype(self.cartSpace, self.cartPrice, self.cartLimitSpace, self.generation + 1)]
        childrens[0].chromosome = children1
        childrens[1].chromosome = children2
        return childrens

    def mutation(self, mutationRate):
        for i in range(len(self.chromosome)):
            if random() < mutationRate:
                if self.chromosome[i] == '1':
                    self.chromosome[i] = '0'
                else:
                    self.chromosome[i] = '1'
        return self
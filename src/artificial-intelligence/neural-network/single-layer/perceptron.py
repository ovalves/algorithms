import numpy as np

class Perceptron:
    def __init__(self):
        self.input = np.array([[0,0],[0,1], [1,0], [1,1]])
        self.output = np.array([0, 1, 1, 1])
        self.weight = np.array([0.0, 0.0])
        self.learnRate = 0.1
        self.stopTraining = False
        self.countErros = 0

    def stepFunction(self, output):
        if (output >= 1):
            return 1
        return 0

    def sumOutput(self, layerInput):
        return self.stepFunction(layerInput.dot(self.weight))

    def printResult(self) :
        print('Rede neural treinada')
        print(self.sumOutput(self.input[0]))
        print(self.sumOutput(self.input[1]))
        print(self.sumOutput(self.input[2]))
        print(self.sumOutput(self.input[3]))

    def train(self):
        while (self.stopTraining == False):
            self.stopTraining = True

            for i in range(len(self.output)):
                error = self.output[i] - self.sumOutput(np.asarray(self.input[i]))
                self.countErros += error

                if (error > 0) :
                    self.stopTraining = False

                for j in range(len(self.weight)):
                    self.weight[j] = self.weight[j] + (self.learnRate * self.input[i][j] * error)
                    print('Peso atualizado: ' + str(self.weight[j]))

            print('Total de erros: ' + str(self.countErros))

        self.printResult()

if __name__ == '__main__':
    Perceptron().train()
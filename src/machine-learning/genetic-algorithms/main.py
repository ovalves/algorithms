from random import random
import matplotlib.pyplot as plt

from learner import Learner
from product import Product

if __name__ == '__main__':
    shoppingCart = []

    shoppingCart.append(Product("Geladeira Dako", 0.751, 999.90))
    shoppingCart.append(Product("Iphone 6", 0.0000899, 2911.12))
    shoppingCart.append(Product("TV 55' ", 0.400, 4346.99))
    shoppingCart.append(Product("TV 50' ", 0.290, 3999.90))
    shoppingCart.append(Product("TV 42' ", 0.200, 2999.00))
    shoppingCart.append(Product("Notebook Dell", 0.00350, 2499.90))
    shoppingCart.append(Product("Ventilador Panasonic", 0.496, 199.90))
    shoppingCart.append(Product("Microondas Electrolux", 0.0424, 308.66))
    shoppingCart.append(Product("Microondas LG", 0.0544, 429.90))
    shoppingCart.append(Product("Microondas Panasonic", 0.0319, 299.29))
    shoppingCart.append(Product("Geladeira Brastemp", 0.635, 849.00))
    shoppingCart.append(Product("Geladeira Consul", 0.870, 1199.89))
    shoppingCart.append(Product("Notebook Lenovo", 0.498, 1999.90))
    shoppingCart.append(Product("Notebook Asus", 0.527, 3999.00))

    cartSpace = []
    cartPrice = []
    for product in shoppingCart:
        cartSpace.append(product.space)
        cartPrice.append(product.price)

    limit = 3
    populationSize = 20
    mutationRate = 0.01
    generations = 100
    learner = Learner(populationSize)
    result = learner.solve(mutationRate, generations, cartSpace, cartPrice, limit)
    for i in range(len(shoppingCart)):
        if result[i] == '1':
            print("Nome: %s R$ %s " % (shoppingCart[i].name,
                                       shoppingCart[i].price))

    # Plotando um gráfico
    plt.plot(learner.solutions)
    plt.title("Acompanhamento dos valores")
    plt.show()
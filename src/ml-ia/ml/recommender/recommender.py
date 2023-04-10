#!/usr/bin/env python
# coding: utf-8

import math
import operator

#Building Custom Data for Article Rating
articles = {
    '1' : {
        'title' : 'Artificial intelligence',
        'url' : 'path_to_article',
        'image_cover' : 'path_to_image_cover'
    },
    '2' : {
        'title' : 'Systems programming',
        'url' : 'path_to_article',
        'image_cover' : 'path_to_image_cover'
    },
    '3' : {
        'title' : 'Software engineering',
        'url' : 'path_to_article',
        'image_cover' : 'path_to_image_cover'
    },
    '4' : {
        'title' : 'Databases',
        'url' : 'path_to_article',
        'image_cover' : 'path_to_image_cover'
    },
    '5' : {
        'title' : 'Algorithms',
        'url' : 'path_to_article',
        'image_cover' : 'path_to_image_cover'
    },
    '6' : {
        'title' : 'Computation',
        'url' : 'path_to_article',
        'image_cover' : 'path_to_image_cover'
    }
}

review = {
    'User 1': {
        '1' : 5.0,
        '2' : 4.5,
        '3' : 3.4,
        '4' : 2.3,
        '5' : 4.4,
        '6' : 2.4
    },
    'User 2': {
        '1' : 4.0,
        '2' : 1.5,
        '3' : 2.4,
        '4' : 2.8,
        '5' : 2.4,
        '6' : 1.4
    },
    'User 3': {
        '1' : 3.0,
        '2' : 3.5,
        '6' : 3.4
    },
    'User 4': {
        '1' : 5.0,
        '5' : 4.4,
    },
    'User 5': {
        '1' : 4.78,
    },
}

class ArticleCollaborativeFiltering():
    def __init__(self, reviews, articles):
        self.reviews = reviews
        self.articles = articles

    def getCommonArticles(self, firstUser, secondUser):
        return [article for article in self.reviews[firstUser] if article in self.reviews[secondUser]]

    def getReviews(self, firstReview, secondReview):
        return [(self.reviews[firstReview][article], self.reviews[secondReview][article]) for article in self.getCommonArticles(firstReview, secondReview)]

    '''
        Obtém os pontos de distância euclidiana
    '''
    def euclideanSimilarity(self, points):
        return 1/ (1 + math.sqrt(sum([pow(point[0] - point[1], 2) for point in points])))

    def getReviewSimilarity(self, firstReview, secondReview):
        return self.euclideanSimilarity(self.getReviews(firstReview, secondReview))

    def recommendArticles(self, user, num_suggestions = 5):
        similarity_scores = [(self.getReviewSimilarity(user, other), other) for other in self.reviews if other != user]

        # Buscando as pontuações da similaridade de todos os usuários
        similarity_scores.sort()
        similarity_scores.reverse()
        similarity_scores = similarity_scores[0:num_suggestions]

        recommendations = {}
        for similarity, other in similarity_scores:

            # Armazenando as avaliações
            reviewed = self.reviews[other]

            for article in reviewed:
                if article not in self.reviews[user]:

                    # Calculando o peso e a similaridade entre as avaliações
                    weight = similarity * reviewed[article]

                    if article in recommendations:
                        sim, weights = recommendations[article]
                        # Similaridade do artigo junto com o peso
                        recommendations[article] = (sim + similarity, weights + [weight])
                    else:
                        recommendations[article] = (similarity, [weight])


        for recommendation in recommendations:
            similarity, article = recommendations[recommendation]
            # Normalização das recomendações com a similaridade
            recommendations[recommendation] = sum(article) / similarity

        # Ordenando as recomendação pelo peso
        return sorted(recommendations.items(), key=operator.itemgetter(1), reverse=True)

    def getArticlesData(self, recommendations):
        return [articles[article[0]] for article in recommendations]

filter = ArticleCollaborativeFiltering(review, articles)

'''
    Testing
'''
# Retorna os artigos em comum entre os usuarios
print(filter.getCommonArticles('User 4', 'User 1'))

# Retorna os reviews em comum entre os usuarios
print(filter.getReviews('User 4','User 1'))

# Retorna a similaridade dos reviews entre os usuarios
print(filter.getReviewSimilarity('User 4', 'User 1'))

# Faz a recomendação dos artigos para o usuario
recommendation = filter.recommendArticles('User 4')

# Retorna os dados dos artigos recomendados
filter.getArticlesData(recommendation)
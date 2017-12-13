# -*-coding:utf-8-*-

from __future__ import division
from math import sqrt

def pearson_sim(data, person1, person2):
    commonmovies = []
    for movie in data[person1]:
        if movie in data[person2]:
            commonmovies.append(movie)

    n = float(len(commonmovies))
    if n == 0:
        return 0

    sum1 = sum([data[person1][movie] for movie in commonmovies])
    sum2 = sum([data[person2][movie] for movie in commonmovies])

    sum12 = sum([data[person1][movie] * data[person2][movie] for movie in commonmovies])

    sum1Sq = sum([pow(data[person1][movie], 2) for movie in commonmovies])
    sum2Sq = sum([pow(data[person2][movie], 2) for movie in commonmovies])

    num = sum12 - sum1 * sum2 / n

    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    get = num / den
    
    return round(get, 5)


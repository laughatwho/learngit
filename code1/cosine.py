# -*-coding:utf-8-*-

from __future__ import division
from math import sqrt


def cosine_sim(data, person1, person2):

    common_movie = [movie for movie in data[person1] if movie in data[person2]]
    if len(common_movie) == 0:
        return 0

    sum12 = sum(data[person1][movie]*data[person2][movie] for movie in common_movie)

    sum1sq = sum(pow(data[person1][movie], 2) for movie in data[person1])
    sum2sq = sum(pow(data[person2][movie], 2) for movie in data[person2])

    den = sqrt(sum1sq) * sqrt(sum2sq)
    if den == 0:
        return 0

    result = sum12/(1.0*den)
    return result

# -*-coding:utf-8-*-

from math import sqrt

def euclidean_sim(data, person1, person2):

    commonmovies = [movie for movie in data[person1] if movie in data[person2]]
    
    if len(commonmovies) == 0:
        return 0
    
    sumSq = sum([pow(data[person1][movie] - data[person2][movie], 2) for movie in commonmovies])
    sim = 1 / (1 + sqrt(sumSq))
    
    return sim


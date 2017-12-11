# -*-coding:utf-8-*-

import time
from math import sqrt
import json
from suirsimilarity import sim_sum_sir_all


def recommendation(data,
                   n_item,
                   given_person,
                   user_neighbor,
                   item_neighbor,
                   user_mean,
                   item_mean,
                   suir_sim,
                   sir_sim,
                   sur_sim,
                   a=0, b=0):
    if given_person not in data:
        return 0.
    target_neighbors = user_neighbor[given_person]
    k_m_sur = {}
    k_m_sir = {}
    k_m_suir = {}
    # sur
    for (userId, user_sim) in target_neighbors.items():
        movies_to_rate_user = [movie for movie in data[userId] if movie not in data[given_person]]
        for movie_user in movies_to_rate_user:
            prob_sur = data[userId][movie_user] - (user_mean[userId] - user_mean[given_person])
            user_sim_sum = sur_sim[given_person][movie_user]
            if user_sim_sum != 0 and prob_sur != 0:
                weight_sur = user_sim * a * (1 - b) / (1.0 * user_sim_sum)
                if weight_sur != 0:
                    rate = prob_sur * weight_sur
                    k_m_sur.setdefault(movie_user, 0)
                    k_m_sur[movie_user] += rate
    # sir
    for item, rate in data[given_person].items():
        item_neighbors = item_neighbor[item]
        movies_to_rate_item = [movies for movies in item_neighbors if movies not in data[given_person]]
        for movie_item in movies_to_rate_item:
            prob_movie_user = rate - (item_mean[item] - item_mean[movie_item])
            sim_sir_sum = sir_sim[given_person][movie_item]
            if sim_sir_sum != 0:
                weight = item_neighbors[movie_item]*(1-a)*(1-b) / (1.0*sim_sir_sum)
                k_m_sir.setdefault(movie_item, 0)
                k_m_sir[movie_item] += prob_movie_user*weight
    # suir
    for (key, value) in target_neighbors.items():
        to_be_rated = [movie for movie in data[key] if movie not in data[given_person]]
        for movie in to_be_rated:
            similar_movies = item_neighbor[movie]
            for key1, value1 in similar_movies.items():
                if key1 in data[key] and key1 not in data[given_person]:
                    prob_suir = data[key][key1] - (user_mean[key] - user_mean[given_person])
                    - (item_mean[key1] - item_mean[movie])
                    if value != 0 and value1 != 0:
                        ka = pow(1/value, 2)
                        mb = pow(1/value1, 2)
                        sim = 1/sqrt(ka+mb)

                        sim_sum = suir_sim[given_person][movie]

                        weight_suir = sim * b / (1.0 * sim_sum)
                        k_m_suir.setdefault(movie, 0)
                        k_m_suir[movie] += prob_suir * weight_suir

    k_m = {x: k_m_sur.get(x, 0) + k_m_sir.get(x, 0) + k_m_suir.get(x, 0) for x
           in set(k_m_sur).union(k_m_sir).union(k_m_suir)}
    b = sorted(k_m.iteritems(), key=lambda (k, v): (v, k), reverse=True)[0:n_item]
    k_m_n = dict(b)

    return k_m_n


def recommendation_all(data,
                       n_item,
                       user_neighbor,
                       item_neighbor,
                       user_mean,
                       item_mean,
                       suir_similarity,
                       sir_similarity,
                       sur_similarity,
                       a, b):
    k_m_all = {}
    for user in data:
        k_m_all.setdefault(user, {})
        k_m_all[user] = recommendation(data=data,
                                       n_item=n_item,
                                       given_person=user,
                                       user_neighbor=user_neighbor,
                                       item_neighbor=item_neighbor,
                                       user_mean=user_mean,
                                       item_mean=item_mean,
                                       suir_sim=suir_similarity,
                                       sir_sim=sir_similarity,
                                       sur_sim=sur_similarity,
                                       a=a,
                                       b=b)
    return k_m_all


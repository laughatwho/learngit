# -*- coding:utf-8 -*-

from math import sqrt
import json


def sim_sum_suir_individual(data, user, movie_neighbor, user_neighbor):
    sim_suir_sum = {}
    target_neighbors = user_neighbor[user]
    for (key, value) in target_neighbors.items():
        to_be_rated = [movie for movie in data[key] if movie not in data[user]]
        for movie in to_be_rated:
            similar_movies = movie_neighbor[movie]
            for key1, value1 in similar_movies.items():
                if key1 in data[key] and key1 not in data[user]:
                    if value != 0 and value1 != 0:
                        ka = pow(1 / value, 2)
                        mb = pow(1 / value1, 2)
                        sim = 1 / sqrt(ka + mb)
                        sim_suir_sum.setdefault(movie, 0)
                        sim_suir_sum[movie] += sim

    return sim_suir_sum


def sim_sum_suir_all(data, movie_neighbor, user_neighbor):
    sim_sum = {}
    for key in data.keys():
        sim_sum.setdefault(key, {})
        sim_sum[key] = sim_sum_suir_individual(data=data, user=key,
                                               movie_neighbor=movie_neighbor,
                                               user_neighbor=user_neighbor)
    return sim_sum


def sim_sum_sir_individual(data, user, movie_neighbor):
    sim = {}

    for item, rate in data[user].items():
        item_neighbors = movie_neighbor[item]
        movies_to_rate_item = [movies for movies in item_neighbors if movies not in data[user]]

        for movie_item in movies_to_rate_item:

            sim.setdefault(movie_item, 0)
            sim[movie_item] += item_neighbors[movie_item]

    return sim


def sim_sum_sir_all(data, movie_neighbor):
    sim_sum_sir = {}
    for user in data:
        sim_sum_sir.setdefault(user, {})
        sim_sum_sir[user] = sim_sum_sir_individual(data=data, user=user, movie_neighbor=movie_neighbor)
    return sim_sum_sir


def sim_sum_sur_individual(data, given_person, user_neighbor):

    target_neighbors = user_neighbor[given_person]
    k_m_sur = {}
    # sur
    for (userId, user_sim) in target_neighbors.items():
        movies_to_rate_user = [movie for movie in data[userId] if movie not in data[given_person]]
        for movie_user in movies_to_rate_user:
                    k_m_sur.setdefault(movie_user, 0)
                    k_m_sur[movie_user] += user_sim
    return k_m_sur


def sim_sum_sur_all(data, user_neighbor):
    k_m_sim = {}
    for user in data:
        k_m_sim.setdefault(user, {})
        k_m_sim[user] = sim_sum_sur_individual(data=data,
                                               given_person=user,
                                               user_neighbor=user_neighbor)
    return k_m_sim


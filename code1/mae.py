# -*- coding:utf-8 -*-

import time
import json


def mae_evaluation(rec_data, held_data):
    mae_sum = 0
    length = 0
    users = [users for users in rec_data if users in held_data]
    for user in users:
        for movie, rate1 in held_data[user].items():
            if movie in rec_data[user]:
                mae_sum += abs(rec_data[user][movie] - rate1)
                length += 1
    mae = mae_sum/(1.0*length)

    return mae

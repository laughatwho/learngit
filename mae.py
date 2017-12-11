# -*- coding:utf-8 -*-

import time
import json


def mae_evaluation(rec_data, held_data):
    mae_sum = 0
    length = 0
    users = [users for users in rec_data if users in held_data]
    for user in users:
        '''
        if user in rec_data:
            print 'in'
        print 'user', user
        print 'held_data[user]', held_data[user]
        '''
        for movie, rate1 in held_data[user].items():
            # print rec_data[user]
            # print 'length', len(rec_data[user])
            if movie in rec_data[user]:
                mae_sum += abs(rec_data[user][movie] - rate1)
                length += 1
    mae = mae_sum/(1.0*length)

    return mae


data_843_held_5_ob_5_ui = json.load(open("data_843_held_5_ob_5_ui.txt"))
recommends_ob_5_843_sf2 = json.load(open("recommends_ob_5_843_sf2.txt"))
mae_item_5_user_5_sf2_843 = mae_evaluation(recommends_ob_5_843_sf2, data_843_held_5_ob_5_ui)
print'mae_item_5_user_5_843_sf2', mae_item_5_user_5_sf2_843


data_843_held_5_ob_10_ui = json.load(open("data_843_held_5_ob_10_ui.txt"))
recommends_ob_10_843_sf2 = json.load(open("recommends_ob_10_843_sf2.txt"))
mae_item_5_user_10_sf2_843 = mae_evaluation(recommends_ob_10_843_sf2, data_843_held_5_ob_10_ui)
print'mae_item_5_user_10_843_sf2', mae_item_5_user_10_sf2_843
# print len(data_843_held_5_ob_5_ui)
# print len(recommends_ob_5_843_sf2)
# users = [users for users in data_843_held_5_ob_5_ui if users in recommends_ob_5_843_sf2]
# print len(users)

data_843_held_5_ob_20_ui = json.load(open("data_843_held_5_ob_20_ui.txt"))
recommends_ob_20_843_sf2 = json.load(open("recommends_ob_20_843_sf2.txt"))
mae_item_5_user_20_sf2_843 = mae_evaluation(recommends_ob_20_843_sf2, data_843_held_5_ob_20_ui)
print'mae_item_5_user_20_843_sf2', mae_item_5_user_20_sf2_843

recommends_ob_5_843_sf1 = json.load(open("recommends_ob_5_843_sf1.txt"))
mae_item_5_user_5_sf1_843 = mae_evaluation(recommends_ob_5_843_sf1, data_843_held_5_ob_5_ui)
print'mae_item_5_user_5_843_sf1', mae_item_5_user_5_sf1_843

# -*-coding:utf-8-*-

import time
import json
from recommender import recommendation_all

start_time = time.time()

'''
# user sparsity:5, SF2: a=0.7, b=0.7
data_843_ob_5 = json.load(open("data_843_ob_5.txt"))
user_means_ob_5_843 = json.load(open("user_means_ob_5_843.txt"))
item_means_ob_5_843 = json.load(open("item_means_ob_5_843.txt"))
user_neighbor_ob_5_843 = json.load(open("user_neighbor_ob_5_843.txt"))
item_neighbor_ob_5_843 = json.load(open("item_neighbor_ob_5_843.txt"))
suir_sim_sum_ob_5_843 = json.load(open("suir_sim_sum_ob_5_843.txt"))
sir_sim_sum_ob_5_843 = json.load(open("sir_sim_sum_ob_5_843.txt"))
sur_sim_sum_ob_5_843 = json.load(open("sur_sim_sum_ob_5_843.txt"))
recommends_ob_5_843_sf2 = recommendation_all(data_843_ob_5, 50,
                                             user_neighbor_ob_5_843,
                                             item_neighbor_ob_5_843,
                                             user_means_ob_5_843,
                                             item_means_ob_5_843,
                                             suir_sim_sum_ob_5_843,
                                             sir_sim_sum_ob_5_843,
                                             sur_sim_sum_ob_5_843,
                                             a=0.7,
                                             b=0.7)

json.dump(recommends_ob_5_843_sf2, open("recommends_ob_5_843_sf2.txt", 'w'))


# user sparsity: 10, SF2: a=0.7, b=0.7
data_843_ob_10 = json.load(open("data_843_ob_10.txt"))
user_means_ob_10_843 = json.load(open("user_means_ob_10_843.txt"))
item_means_ob_10_843 = json.load(open("item_means_ob_10_843.txt"))
user_neighbor_ob_10_843 = json.load(open("user_neighbor_ob_10_843.txt"))
item_neighbor_ob_10_843 = json.load(open("item_neighbor_ob_10_843.txt"))
suir_sim_sum_ob_10_843 = json.load(open("suir_sim_sum_ob_10_843.txt"))
sir_sim_sum_ob_10_843 = json.load(open("sir_sim_sum_ob_10_843.txt"))
sur_sim_sum_ob_10_843 = json.load(open("sur_sim_sum_ob_10_843.txt"))
recommends_ob_10_843_sf2 = recommendation_all(data_843_ob_10, 50,
                                              user_neighbor_ob_10_843,
                                              item_neighbor_ob_10_843,
                                              user_means_ob_10_843,
                                              item_means_ob_10_843,
                                              suir_sim_sum_ob_10_843,
                                              sir_sim_sum_ob_10_843,
                                              sur_sim_sum_ob_10_843,
                                              a=0.7,
                                              b=0.7)

json.dump(recommends_ob_10_843_sf2, open("recommends_ob_10_843_sf2.txt", 'w'))

# user sparsity: 20, SF2: a = 0.7, b=0.7
data_843_ob_20 = json.load(open("data_843_ob_20.txt"))
user_means_ob_20_843 = json.load(open("user_means_ob_20_843.txt"))
item_means_ob_20_843 = json.load(open("item_means_ob_20_843.txt"))
user_neighbor_ob_20_843 = json.load(open("user_neighbor_ob_20_843.txt"))
item_neighbor_ob_20_843 = json.load(open("item_neighbor_ob_20_843.txt"))
suir_sim_sum_ob_20_843 = json.load(open("suir_sim_sum_ob_20_843.txt"))
sir_sim_sum_ob_20_843 = json.load(open("sir_sim_sum_ob_20_843.txt"))
sur_sim_sum_ob_20_843 = json.load(open("sur_sim_sum_ob_20_843.txt"))
recommends_ob_20_843_sf2 = recommendation_all(data_843_ob_20, 50,
                                              user_neighbor_ob_20_843,
                                              item_neighbor_ob_20_843,
                                              user_means_ob_20_843,
                                              item_means_ob_20_843,
                                              suir_sim_sum_ob_20_843,
                                              sir_sim_sum_ob_20_843,
                                              sur_sim_sum_ob_20_843,
                                              a=0.7,
                                              b=0.7)

json.dump(recommends_ob_20_843_sf2, open("recommends_ob_20_843_sf2.txt", 'w'))


# user sparsity:5, SF1: a=0.7, b=0
recommends_ob_5_843_sf1 = recommendation_all(data_843_ob_5, 50,
                                             user_neighbor_ob_5_843,
                                             item_neighbor_ob_5_843,
                                             user_means_ob_5_843,
                                             item_means_ob_5_843,
                                             suir_sim_sum_ob_5_843,
                                             sir_sim_sum_ob_5_843,
                                             sur_sim_sum_ob_5_843,
                                             a=0.7,
                                             b=0)

json.dump(recommends_ob_5_843_sf1, open("recommends_ob_5_843_sf1.txt", 'w'))


# user sparsity: 10, SF1: a=0.7, b=0
recommends_ob_10_843_sf1 = recommendation_all(data_843_ob_10, 50,
                                              user_neighbor_ob_10_843,
                                              item_neighbor_ob_10_843,
                                              user_means_ob_10_843,
                                              item_means_ob_10_843,
                                              suir_sim_sum_ob_10_843,
                                              sir_sim_sum_ob_10_843,
                                              sur_sim_sum_ob_10_843,
                                              a=0.7,
                                              b=0)

json.dump(recommends_ob_10_843_sf1, open("recommends_ob_10_843_sf1.txt", 'w'))

# user sparsity: 20, SF1: a=0.7, b=0
recommends_ob_20_843_sf1 = recommendation_all(data_843_ob_20, 50,
                                              user_neighbor_ob_20_843,
                                              item_neighbor_ob_20_843,
                                              user_means_ob_20_843,
                                              item_means_ob_20_843,
                                              suir_sim_sum_ob_20_843,
                                              sir_sim_sum_ob_20_843,
                                              sur_sim_sum_ob_20_843,
                                              a=0.7,
                                              b=0)

json.dump(recommends_ob_20_843_sf1, open("recommends_ob_20_843_sf1.txt", 'w'))
'''
'''
# user sparsity:5, IBCF: a=0, b=0
recommends_ob_5_843_ibcf = recommendation_all(data_843_ob_5, 50,
                                              user_neighbor_ob_5_843,
                                              item_neighbor_ob_5_843,
                                              user_means_ob_5_843,
                                              item_means_ob_5_843,
                                              suir_sim_sum_ob_5_843,
                                              a=0,
                                              b=0)

json.dump(recommends_ob_5_843_ibcf, open("recommends_ob_5_843_ibcf.txt", 'w'))


# user sparsity: 10, IBCF: a=0, b=0
recommends_ob_10_843_ibcf = recommendation_all(data_843_ob_10, 50,
                                               user_neighbor_ob_10_843,
                                               item_neighbor_ob_10_843,
                                               user_means_ob_10_843,
                                               item_means_ob_10_843,
                                               suir_sim_sum_ob_10_843,
                                               a=0,
                                               b=0)

json.dump(recommends_ob_10_843_ibcf, open("recommends_ob_10_843_ibcf.txt", 'w'))

# user sparsity: 20, IBCF: a=0, b=0
recommends_ob_20_843_ibcf = recommendation_all(data_843_ob_20, 50,
                                               user_neighbor_ob_20_843,
                                               item_neighbor_ob_20_843,
                                               user_means_ob_20_843,
                                               item_means_ob_20_843,
                                               suir_sim_sum_ob_20_843,
                                               a=0,
                                               b=0)
json.dump(recommends_ob_20_843_ibcf, open("recommends_ob_20_843_ibcf.txt", 'w'))

# user sparsity:5, UBCF: a=1, b=0
recommends_ob_5_843_ubcf = recommendation_all(data_843_ob_5, 50,
                                              user_neighbor_ob_5_843,
                                              item_neighbor_ob_5_843,
                                              user_means_ob_5_843,
                                              item_means_ob_5_843,
                                              suir_sim_sum_ob_5_843,
                                              a=1,
                                              b=0)

json.dump(recommends_ob_5_843_ubcf, open("recommends_ob_5_843_ubcf.txt", 'w'))


# user sparsity: 10, UBCF: a=1, b=0
recommends_ob_10_843_ubcf = recommendation_all(data_843_ob_10, 50,
                                               user_neighbor_ob_10_843,
                                               item_neighbor_ob_10_843,
                                               user_means_ob_10_843,
                                               item_means_ob_10_843,
                                               suir_sim_sum_ob_10_843,
                                               a=1,
                                               b=0)

json.dump(recommends_ob_10_843_ubcf, open("recommends_ob_10_843_ubcf.txt", 'w'))

# user sparsity: 20, UBCF: a=1, b=0
recommends_ob_20_843_ubcf = recommendation_all(data_843_ob_20, 50,
                                               user_neighbor_ob_20_843,
                                               item_neighbor_ob_20_843,
                                               user_means_ob_20_843,
                                               item_means_ob_20_843,
                                               suir_sim_sum_ob_20_843,
                                               a=1,
                                               b=0)
json.dump(recommends_ob_20_843_ubcf, open("recommends_ob_20_843_ubcf.txt", 'w'))
'''

# number of training user: 200
# user sparsity:5, SF2: a=0.7, b=0.7
data_743_ob_5 = json.load(open("data_743_ob_5.txt"))
user_means_ob_5_743 = json.load(open("user_means_ob_5_743.txt"))
item_means_ob_5_743 = json.load(open("item_means_ob_5_743.txt"))
user_neighbor_ob_5_743 = json.load(open("user_neighbor_ob_5_743.txt"))
item_neighbor_ob_5_743 = json.load(open("item_neighbor_ob_5_743.txt"))
suir_sim_sum_ob_5_743 = json.load(open("suir_sim_sum_ob_5_743.txt"))
sir_sim_sum_ob_5_743 = json.load(open("sir_sim_sum_ob_5_743.txt"))
sur_sim_sum_ob_5_743 = json.load(open("sur_sim_sum_ob_5_743.txt"))
recommends_ob_5_743_sf2 = recommendation_all(data_743_ob_5, 50,
                                             user_neighbor_ob_5_743,
                                             item_neighbor_ob_5_743,
                                             user_means_ob_5_743,
                                             item_means_ob_5_743,
                                             suir_sim_sum_ob_5_743,
                                             sir_sim_sum_ob_5_743,
                                             sur_sim_sum_ob_5_743,
                                             a=0.7,
                                             b=0.7)

json.dump(recommends_ob_5_743_sf2, open("recommends_ob_5_743_sf2.txt", 'w'))


# user sparsity: 10, SF2: a=0.7, b=0.7
data_743_ob_10 = json.load(open("data_743_ob_10.txt"))
user_means_ob_10_743 = json.load(open("user_means_ob_10_743.txt"))
item_means_ob_10_743 = json.load(open("item_means_ob_10_743.txt"))
user_neighbor_ob_10_743 = json.load(open("user_neighbor_ob_10_743.txt"))
item_neighbor_ob_10_743 = json.load(open("item_neighbor_ob_10_743.txt"))
suir_sim_sum_ob_10_743 = json.load(open("suir_sim_sum_ob_10_743.txt"))
sir_sim_sum_ob_10_743 = json.load(open("sir_sim_sum_ob_10_743.txt"))
sur_sim_sum_ob_10_743 = json.load(open("sur_sim_sum_ob_10_743.txt"))
recommends_ob_10_743_sf2 = recommendation_all(data_743_ob_10, 50,
                                              user_neighbor_ob_10_743,
                                              item_neighbor_ob_10_743,
                                              user_means_ob_10_743,
                                              item_means_ob_10_743,
                                              suir_sim_sum_ob_10_743,
                                              sir_sim_sum_ob_10_743,
                                              sur_sim_sum_ob_10_743,
                                              a=0.7,
                                              b=0.7)

json.dump(recommends_ob_10_743_sf2, open("recommends_ob_10_743_sf2.txt", 'w'))

# user sparsity: 20, SF2: a = 0.7, b=0.7
data_743_ob_20 = json.load(open("data_743_ob_20.txt"))
user_means_ob_20_743 = json.load(open("user_means_ob_20_743.txt"))
item_means_ob_20_743 = json.load(open("item_means_ob_20_743.txt"))
user_neighbor_ob_20_743 = json.load(open("user_neighbor_ob_20_743.txt"))
item_neighbor_ob_20_743 = json.load(open("item_neighbor_ob_20_743.txt"))
suir_sim_sum_ob_20_743 = json.load(open("suir_sim_sum_ob_20_743.txt"))
sir_sim_sum_ob_20_743 = json.load(open("sir_sim_sum_ob_20_743.txt"))
sur_sim_sum_ob_20_743 = json.load(open("sur_sim_sum_ob_20_743.txt"))
recommends_ob_20_743_sf2 = recommendation_all(data_743_ob_20, 50,
                                              user_neighbor_ob_20_743,
                                              item_neighbor_ob_20_743,
                                              user_means_ob_20_743,
                                              item_means_ob_20_743,
                                              suir_sim_sum_ob_20_743,
                                              sir_sim_sum_ob_20_743,
                                              sur_sim_sum_ob_20_743,
                                              a=0.7,
                                              b=0.7)

json.dump(recommends_ob_20_743_sf2, open("recommends_ob_20_743_sf2.txt", 'w'))


# user sparsity:5, SF1: a=0.7, b=0
recommends_ob_5_743_sf1 = recommendation_all(data_743_ob_5, 50,
                                             user_neighbor_ob_5_743,
                                             item_neighbor_ob_5_743,
                                             user_means_ob_5_743,
                                             item_means_ob_5_743,
                                             suir_sim_sum_ob_5_743,
                                             sir_sim_sum_ob_5_743,
                                             sur_sim_sum_ob_5_743,
                                             a=0.7,
                                             b=0)

json.dump(recommends_ob_5_743_sf1, open("recommends_ob_5_743_sf1.txt", 'w'))


# user sparsity: 10, SF1: a=0.7, b=0
recommends_ob_10_743_sf1 = recommendation_all(data_743_ob_10, 50,
                                              user_neighbor_ob_10_743,
                                              item_neighbor_ob_10_743,
                                              user_means_ob_10_743,
                                              item_means_ob_10_743,
                                              suir_sim_sum_ob_10_743,
                                              sir_sim_sum_ob_10_743,
                                              sur_sim_sum_ob_10_743,
                                              a=0.7,
                                              b=0)

json.dump(recommends_ob_10_743_sf1, open("recommends_ob_10_743_sf1.txt", 'w'))

# user sparsity: 20, SF1: a=0.7, b=0
recommends_ob_20_743_sf1 = recommendation_all(data_743_ob_20, 50,
                                              user_neighbor_ob_20_743,
                                              item_neighbor_ob_20_743,
                                              user_means_ob_20_743,
                                              item_means_ob_20_743,
                                              suir_sim_sum_ob_20_743,
                                              sir_sim_sum_ob_20_743,
                                              sur_sim_sum_ob_20_743,
                                              a=0.7,
                                              b=0)

json.dump(recommends_ob_20_743_sf1, open("recommends_ob_20_743_sf1.txt", 'w'))




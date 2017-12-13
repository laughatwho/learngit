# -*-coding:utf-8-*-

from dataformat import format_movie_lens
from dataformat import transforms
from dataformat import split_data
from dataformat import ob_held
from dataformat import item_sparsity
from neighbor import object_neighbor
import time
import json
from cosine import cosine_sim
from suirsimilarity import sim_sum_suir_all
from suirsimilarity import sim_sum_sir_all
from suirsimilarity import sim_sum_sur_all
from mean import mean


start = time.time()
data = format_movie_lens()
item_data = transforms(data)

data_843 = split_data(data, n_user=843)
ob_5 = ob_held(data_843, n_observed=5)
ob_10 = ob_held(data_843, n_observed=10)
ob_20 = ob_held(data_843, n_observed=20)


data_843_ob_5 = ob_5[0]
i_data_843_ob_5 = transforms(data_843_ob_5)
json.dump(data_843_ob_5, open("data_843_ob_5.txt", 'w'))
json.dump(i_data_843_ob_5, open("i_data_843_ob_5.txt", 'w'))
json.dump(data_843, open("data_843.txt", 'w'))
data_843_ob_10 = ob_10[0]
i_data_843_ob_10 = transforms(data_843_ob_10)
json.dump(data_843_ob_10, open("data_843_ob_10.txt", 'w'))
json.dump(i_data_843_ob_10, open("i_data_843_ob_10.txt", 'w'))

data_843_ob_20 = ob_20[0]
i_data_843_ob_20 = transforms(data_843_ob_20)
json.dump(data_843_ob_20, open("data_843_ob_20.txt", 'w'))
json.dump(i_data_843_ob_20, open("i_data_843_ob_20.txt", 'w'))

data_843_held_free_ob_5 = ob_5[1]
i_data_843_held_free_ob_5 = transforms(data_843_held_free_ob_5)
data_843_held_5_ob_5_iu = item_sparsity(i_data_843_held_free_ob_5, 5)
data_843_held_5_ob_5_ui = transforms(data_843_held_5_ob_5_iu)

data_843_held_10_ob_5_iu = item_sparsity(i_data_843_held_free_ob_5, 10)
data_843_held_10_ob_5_ui = transforms(data_843_held_10_ob_5_iu)

data_843_held_20_ob_5_iu = item_sparsity(i_data_843_held_free_ob_5, 20)
data_843_held_20_ob_5_ui = transforms(data_843_held_20_ob_5_iu)

json.dump(data_843_held_free_ob_5, open("data_843_held_free_ob_5.txt", 'w'))
json.dump(data_843_held_5_ob_5_ui, open("data_843_held_5_ob_5_ui.txt", 'w'))
json.dump(data_843_held_10_ob_5_ui, open("data_843_held_10_ob_5_ui.txt", 'w'))
json.dump(data_843_held_20_ob_5_ui, open("data_843_held_20_ob_5_ui.txt", 'w'))


data_843_held_free_ob_10 = ob_10[1]
i_data_843_held_free_ob_10 = transforms(data_843_held_free_ob_10)
data_843_held_5_ob_10_iu = item_sparsity(i_data_843_held_free_ob_10, 5)
data_843_held_5_ob_10_ui = transforms(data_843_held_5_ob_10_iu)


data_843_held_10_ob_10_iu = item_sparsity(i_data_843_held_free_ob_10, 10)
data_843_held_10_ob_10_ui = transforms(data_843_held_10_ob_10_iu)


data_843_held_20_ob_10_iu = item_sparsity(i_data_843_held_free_ob_10, 20)
data_843_held_20_ob_10_ui = transforms(data_843_held_20_ob_10_iu)

json.dump(data_843_held_free_ob_10, open("data_843_held_free_ob_10.txt", 'w'))
json.dump(data_843_held_5_ob_10_ui, open("data_843_held_5_ob_10_ui.txt", 'w'))
json.dump(data_843_held_10_ob_10_ui, open("data_843_held_10_ob_10_ui.txt", 'w'))
json.dump(data_843_held_20_ob_10_ui, open("data_843_held_20_ob_10_ui.txt", 'w'))


data_843_held_free_ob_20 = ob_20[1]
i_data_843_held_free_ob_20 = transforms(data_843_held_free_ob_20)
data_843_held_5_ob_20_iu = item_sparsity(i_data_843_held_free_ob_20, 5)
data_843_held_5_ob_20_ui = transforms(data_843_held_5_ob_20_iu)

data_843_held_10_ob_20_iu = item_sparsity(i_data_843_held_free_ob_20, 10)
data_843_held_10_ob_20_ui = transforms(data_843_held_10_ob_20_iu)

data_843_held_20_ob_20_iu = item_sparsity(i_data_843_held_free_ob_20, 20)
data_843_held_20_ob_20_ui = transforms(data_843_held_20_ob_20_iu)

json.dump(data_843_held_free_ob_20, open("data_843_held_free_ob_20.txt", 'w'))
json.dump(data_843_held_5_ob_20_ui, open("data_843_held_5_ob_20_ui.txt", 'w'))
json.dump(data_843_held_10_ob_20_ui, open("data_843_held_10_ob_20_ui.txt", 'w'))
json.dump(data_843_held_20_ob_20_ui, open("data_843_held_20_ob_20_ui.txt", 'w'))

# case one: user sparsity = 5
user_neighbor_ob_5_843 = object_neighbor(data_843_ob_5, 50, cosine_sim)
item_neighbor_ob_5_843 = object_neighbor(i_data_843_ob_5, 50, cosine_sim)

json.dump(user_neighbor_ob_5_843, open("user_neighbor_ob_5_843.txt", 'w'))
json.dump(item_neighbor_ob_5_843, open("item_neighbor_ob_5_843.txt", 'w'))

item_means_ob_5_843 = mean(i_data_843_ob_5)
user_means_ob_5_843 = mean(data_843_ob_5)
json.dump(item_means_ob_5_843, open("item_means_ob_5_843.txt", 'w'))
json.dump(user_means_ob_5_843, open("user_means_ob_5_843.txt", 'w'))

suir_sim_sum_ob_5_843 = sim_sum_suir_all(data=data_843_ob_5,
                                         movie_neighbor=item_neighbor_ob_5_843,
                                         user_neighbor=user_neighbor_ob_5_843,
                                         )
json.dump(suir_sim_sum_ob_5_843, open("suir_sim_sum_ob_5_843.txt", 'w'))

sir_sim_sum_ob_5_843 = sim_sum_sir_all(data=data_843_ob_5, movie_neighbor=item_neighbor_ob_5_843)
json.dump(sir_sim_sum_ob_5_843, open("sir_sim_sum_ob_5_843.txt", 'w'))

sur_sim_sum_ob_5_843 = sim_sum_sur_all(data=data_843_ob_5, user_neighbor=user_neighbor_ob_5_843)
json.dump(sur_sim_sum_ob_5_843, open("sur_sim_sum_ob_5_843.txt", 'w'))

# case two: user sparsity = 10
user_neighbor_ob_10_843 = object_neighbor(data_843_ob_10, 50, cosine_sim)
item_neighbor_ob_10_843 = object_neighbor(i_data_843_ob_10, 50, cosine_sim)
json.dump(user_neighbor_ob_10_843, open("user_neighbor_ob_10_843.txt", 'w'))
json.dump(item_neighbor_ob_10_843, open("item_neighbor_ob_10_843.txt", 'w'))

item_means_ob_10_843 = mean(i_data_843_ob_10)
user_means_ob_10_843 = mean(data_843_ob_10)
json.dump(item_means_ob_10_843, open("item_means_ob_10_843.txt", 'w'))
json.dump(user_means_ob_10_843, open("user_means_ob_10_843.txt", 'w'))
suir_sim_sum_ob_10_843 = sim_sum_suir_all(data=data_843_ob_10,
                                          movie_neighbor=item_neighbor_ob_10_843,
                                          user_neighbor=user_neighbor_ob_10_843)
json.dump(suir_sim_sum_ob_10_843, open("suir_sim_sum_ob_10_843.txt", 'w'))

sir_sim_sum_ob_10_843 = sim_sum_sir_all(data=data_843_ob_10, movie_neighbor=item_neighbor_ob_10_843)
json.dump(sir_sim_sum_ob_10_843, open("sir_sim_sum_ob_10_843.txt", 'w'))

sur_sim_sum_ob_10_843 = sim_sum_sur_all(data=data_843_ob_10, user_neighbor=user_neighbor_ob_10_843)
json.dump(sur_sim_sum_ob_10_843, open("sur_sim_sum_ob_10_843.txt", 'w'))
# case three: user sparsity = 20
user_neighbor_ob_20_843 = object_neighbor(data_843_ob_20, 50, cosine_sim)
item_neighbor_ob_20_843 = object_neighbor(i_data_843_ob_20, 50, cosine_sim)
json.dump(user_neighbor_ob_20_843, open("user_neighbor_ob_20_843.txt", 'w'))
json.dump(item_neighbor_ob_20_843, open("item_neighbor_ob_20_843.txt", 'w'))

item_means_ob_20_843 = mean(i_data_843_ob_20)
user_means_ob_20_843 = mean(data_843_ob_20)

json.dump(item_means_ob_20_843, open("item_means_ob_20_843.txt", 'w'))
json.dump(user_means_ob_20_843, open("user_means_ob_20_843.txt", 'w'))

suir_sim_sum_ob_20_843 = sim_sum_suir_all(data=data_843_ob_20,
                                          movie_neighbor=item_neighbor_ob_20_843,
                                          user_neighbor=user_neighbor_ob_20_843)
json.dump(suir_sim_sum_ob_20_843, open("suir_sim_sum_ob_20_843.txt", 'w'))

sir_sim_sum_ob_20_843 = sim_sum_sir_all(data=data_843_ob_20, movie_neighbor=item_neighbor_ob_20_843)
json.dump(sir_sim_sum_ob_20_843, open("sir_sim_sum_ob_20_843.txt", 'w'))

sur_sim_sum_ob_20_843 = sim_sum_sur_all(data=data_843_ob_20, user_neighbor=user_neighbor_ob_20_843)
json.dump(sur_sim_sum_ob_20_843, open("sur_sim_sum_ob_20_843.txt", 'w'))
json.dump(sur_sim_sum_ob_20_843, open("sur_sim_sum_ob_20_843.txt", 'w'))

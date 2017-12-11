# -*-coding:utf-8-*-


import time
import json
from mae import mae_evaluation


start_time = time.time()
data_843_held_5_ob_20_ui = json.load(open("data_843_held_5_ob_20_ui.txt"))
# item sparsity < 5, user sparsity: 5

data_843_held_5_ob_5_ui = json.load(open("data_843_held_5_ob_5_ui.txt"))
recommends_ob_5_843_sf2 = json.load(open("recommends_ob_5_843_sf2.txt"))
mae_item_5_user_5_sf2_843 = mae_evaluation(recommends_ob_5_843_sf2, data_843_held_5_ob_20_ui)
print'mae_item_5_user_5_843_sf2', mae_item_5_user_5_sf2_843

recommends_ob_5_843_sf1 = json.load(open("recommends_ob_5_843_sf1.txt"))
mae_item_5_user_5_sf1_843 = mae_evaluation(recommends_ob_5_843_sf1, data_843_held_5_ob_20_ui)
print'mae_item_5_user_5_843_sf1', mae_item_5_user_5_sf1_843

# item sparsity < 5, user sparsity: 10
data_843_held_5_ob_10_ui = json.load(open("data_843_held_5_ob_10_ui.txt"))
recommends_ob_10_843_sf2 = json.load(open("recommends_ob_10_843_sf2.txt"))
mae_item_5_user_10_sf2_843 = mae_evaluation(recommends_ob_10_843_sf2, data_843_held_5_ob_10_ui)
print'mae_item_5_user_10_843_sf2', mae_item_5_user_10_sf2_843

recommends_ob_10_843_sf1 = json.load(open("recommends_ob_10_843_sf1.txt"))
mae_item_5_user_10_sf1_843 = mae_evaluation(recommends_ob_10_843_sf1, data_843_held_5_ob_10_ui)
print'mae_item_5_user_10_843_sf1', mae_item_5_user_10_sf1_843

# item sparsity < 5, user sparsity: 20
data_843_held_5_ob_20_ui = json.load(open("data_843_held_5_ob_20_ui.txt"))
recommends_ob_20_843_sf2 = json.load(open("recommends_ob_20_843_sf2.txt"))
mae_item_5_user_20_sf2_843 = mae_evaluation(recommends_ob_20_843_sf2, data_843_held_5_ob_20_ui)
print'mae_item_5_user_20_843_sf2', mae_item_5_user_20_sf2_843

recommends_ob_20_843_sf1 = json.load(open("recommends_ob_20_843_sf1.txt"))
mae_item_5_user_20_sf1_843 = mae_evaluation(recommends_ob_20_843_sf1, data_843_held_5_ob_20_ui)
print'mae_item_5_user_20_843_sf1', mae_item_5_user_20_sf1_843


# item sparsity < 10, user sparsity: 5
data_843_held_10_ob_5_ui = json.load(open("data_843_held_10_ob_5_ui.txt"))
recommends_ob_5_843_sf2 = json.load(open("recommends_ob_5_843_sf2.txt"))
mae_item_10_user_5_sf2_843 = mae_evaluation(recommends_ob_5_843_sf2, data_843_held_10_ob_5_ui)
print'mae_item_10_user_5_843_sf2', mae_item_10_user_5_sf2_843

recommends_ob_5_843_sf1 = json.load(open("recommends_ob_5_843_sf1.txt"))
mae_item_10_user_5_sf1_843 = mae_evaluation(recommends_ob_5_843_sf1,
                                            data_843_held_10_ob_5_ui)
print'mae_item_10_user_5_843_sf1', mae_item_10_user_5_sf1_843

# item sparsity < 10, user sparsity: 10
data_843_held_10_ob_10_ui = json.load(open("data_843_held_10_ob_10_ui.txt"))
recommends_ob_10_843_sf2 = json.load(open("recommends_ob_10_843_sf2.txt"))
mae_item_10_user_10_sf2_843 = mae_evaluation(recommends_ob_10_843_sf2, data_843_held_10_ob_10_ui)
print'mae_item_10_user_10_843_sf2', mae_item_10_user_10_sf2_843

recommends_ob_10_843_sf1 = json.load(open("recommends_ob_10_843_sf1.txt"))
mae_item_10_user_10_sf1_843 = mae_evaluation(recommends_ob_10_843_sf1,
                                             data_843_held_10_ob_10_ui)
print'mae_item_10_user_10_843_sf1', mae_item_10_user_10_sf1_843

# item sparsity < 10, user sparsity: 20
data_843_held_10_ob_20_ui = json.load(open("data_843_held_10_ob_20_ui.txt"))
recommends_ob_20_843_sf2 = json.load(open("recommends_ob_20_843_sf2.txt"))
mae_item_10_user_20_sf2_843 = mae_evaluation(recommends_ob_20_843_sf2, data_843_held_10_ob_20_ui)
print'mae_item_10_user_20_843_sf2', mae_item_10_user_20_sf2_843

recommends_ob_20_843_sf1 = json.load(open("recommends_ob_20_843_sf1.txt"))
mae_item_10_user_20_sf1_843 = mae_evaluation(recommends_ob_20_843_sf1,
                                             data_843_held_10_ob_20_ui)
print'mae_item_10_user_20_843_sf1', mae_item_10_user_20_sf1_843

# item sparsity < 20, user sparsity: 5
data_843_held_20_ob_5_ui = json.load(open("data_843_held_20_ob_5_ui.txt"))
recommends_ob_5_843_sf2 = json.load(open("recommends_ob_5_843_sf2.txt"))
mae_item_20_user_5_sf2_843 = mae_evaluation(recommends_ob_5_843_sf2, data_843_held_20_ob_5_ui)
print'mae_item_20_user_5_843_sf2', mae_item_20_user_5_sf2_843

recommends_ob_5_843_sf1 = json.load(open("recommends_ob_5_843_sf1.txt"))
mae_item_20_user_5_sf1_843 = mae_evaluation(recommends_ob_5_843_sf1,
                                            data_843_held_20_ob_5_ui)
print'mae_item_20_user_5_843_sf1', mae_item_20_user_5_sf1_843

# item sparsity < 20, user sparsity: 10
data_843_held_20_ob_10_ui = json.load(open("data_843_held_20_ob_10_ui.txt"))
recommends_ob_10_843_sf2 = json.load(open("recommends_ob_10_843_sf2.txt"))
mae_item_20_user_10_sf2_843 = mae_evaluation(recommends_ob_10_843_sf2, data_843_held_20_ob_10_ui)
print'mae_item_20_user_10_843_sf2', mae_item_20_user_10_sf2_843

recommends_ob_10_843_sf1 = json.load(open("recommends_ob_10_843_sf1.txt"))
mae_item_20_user_10_sf1_843 = mae_evaluation(recommends_ob_10_843_sf1,
                                             data_843_held_20_ob_10_ui)
print'mae_item_20_user_10_843_sf1', mae_item_20_user_10_sf1_843

# item sparsity < 20, user sparsity: 20
data_843_held_20_ob_20_ui = json.load(open("data_843_held_20_ob_20_ui.txt"))
recommends_ob_20_843_sf2 = json.load(open("recommends_ob_20_843_sf2.txt"))
mae_item_20_user_20_sf2_843 = mae_evaluation(recommends_ob_20_843_sf2, data_843_held_20_ob_20_ui)
print'mae_item_20_user_20_843_sf2', mae_item_20_user_20_sf2_843

recommends_ob_20_843_sf1 = json.load(open("recommends_ob_20_843_sf1.txt"))
mae_item_20_user_20_sf1_843 = mae_evaluation(recommends_ob_20_843_sf1,
                                             data_843_held_20_ob_20_ui)
print'mae_item_20_user_20_843_sf1', mae_item_20_user_20_sf1_843


# item sparsity:no constraint, user sparsity: 5
data_843 = json.load(open("data_843.txt"))
data_843_held_free_ob_5 = json.load(open("data_843_held_free_ob_5.txt"))
recommends_ob_5_843_sf2 = json.load(open("recommends_ob_5_843_sf2.txt"))
mae_item_user_5_sf2_843 = mae_evaluation(recommends_ob_5_843_sf2, data_843_held_free_ob_5)
print'mae_item_free_user_5_843_sf2', mae_item_user_5_sf2_843

recommends_ob_5_843_sf1 = json.load(open("recommends_ob_5_843_sf1.txt"))
mae_item_user_5_sf1_843 = mae_evaluation(recommends_ob_5_843_sf1, data_843_held_free_ob_5)
print'mae_item_user_5_843_sf1', mae_item_user_5_sf1_843

# item sparsity: no constraint, user sparsity: 10
data_843_held_free_ob_10 = json.load(open("data_843_held_free_ob_10.txt"))
recommends_ob_10_843_sf2 = json.load(open("recommends_ob_10_843_sf2.txt"))
mae_item_user_10_sf2_843 = mae_evaluation(recommends_ob_10_843_sf2, data_843_held_free_ob_10)
print'mae_item_free_user_10_843_sf2', mae_item_user_10_sf2_843

recommends_ob_10_843_sf1 = json.load(open("recommends_ob_10_843_sf1.txt"))
mae_item_user_10_sf1_843 = mae_evaluation(recommends_ob_10_843_sf1, data_843_held_free_ob_10)
print'mae_item_user_10_843_sf1', mae_item_user_10_sf1_843


# item sparsity: no constraint, user sparsity: 20
data_843_held_free_ob_20 = json.load(open("data_843_held_free_ob_20.txt"))
recommends_ob_20_843_sf2 = json.load(open("recommends_ob_20_843_sf2.txt"))
mae_item_user_20_sf2_843 = mae_evaluation(recommends_ob_20_843_sf2, data_843_held_free_ob_20)
print'mae_item_free_user_20_843_sf2', mae_item_user_20_sf2_843

recommends_ob_20_843_sf1 = json.load(open("recommends_ob_20_843_sf1.txt"))
mae_item_user_20_sf1_843 = mae_evaluation(recommends_ob_20_843_sf1, data_843_held_free_ob_20)
print'mae_item_user_20_843_sf1', mae_item_user_20_sf1_843


data_743_held_5_ob_5_ui = json.load(open("data_743_held_5_ob_5_ui.txt"))
recommends_ob_5_743_sf2 = json.load(open("recommends_ob_5_743_sf2.txt"))
mae_item_5_user_5_sf2_743 = mae_evaluation(recommends_ob_5_743_sf2, data_743_held_5_ob_5_ui)
print'mae_item_5_user_5_743_sf2', mae_item_5_user_5_sf2_743

recommends_ob_5_743_sf1 = json.load(open("recommends_ob_5_743_sf1.txt"))
mae_item_5_user_5_sf1_743 = mae_evaluation(recommends_ob_5_743_sf1, data_743_held_5_ob_5_ui)
print'mae_item_5_user_5_743_sf1', mae_item_5_user_5_sf1_743

# item sparsity < 5, user sparsity: 10
data_743_held_5_ob_10_ui = json.load(open("data_743_held_5_ob_10_ui.txt"))
recommends_ob_10_743_sf2 = json.load(open("recommends_ob_10_743_sf2.txt"))
mae_item_5_user_10_sf2_743 = mae_evaluation(recommends_ob_10_743_sf2, data_743_held_5_ob_10_ui)
print'mae_item_5_user_10_743_sf2', mae_item_5_user_10_sf2_743

recommends_ob_10_743_sf1 = json.load(open("recommends_ob_10_743_sf1.txt"))
mae_item_5_user_10_sf1_743 = mae_evaluation(recommends_ob_10_743_sf1, data_743_held_5_ob_10_ui)
print'mae_item_5_user_10_743_sf1', mae_item_5_user_10_sf1_743

# item sparsity < 5, user sparsity: 20
data_743_held_5_ob_20_ui = json.load(open("data_743_held_5_ob_20_ui.txt"))
recommends_ob_20_743_sf2 = json.load(open("recommends_ob_20_743_sf2.txt"))
mae_item_5_user_20_sf2_743 = mae_evaluation(recommends_ob_20_743_sf2, data_743_held_5_ob_20_ui)
print'mae_item_5_user_20_743_sf2', mae_item_5_user_20_sf2_743

recommends_ob_20_743_sf1 = json.load(open("recommends_ob_20_743_sf1.txt"))
mae_item_5_user_20_sf1_743 = mae_evaluation(recommends_ob_20_743_sf1, data_743_held_5_ob_20_ui)
print'mae_item_5_user_20_743_sf1', mae_item_5_user_20_sf1_743


# item sparsity < 10, user sparsity: 5
data_743_held_10_ob_5_ui = json.load(open("data_743_held_10_ob_5_ui.txt"))
recommends_ob_5_743_sf2 = json.load(open("recommends_ob_5_743_sf2.txt"))
mae_item_10_user_5_sf2_743 = mae_evaluation(recommends_ob_5_743_sf2, data_743_held_10_ob_5_ui)
print'mae_item_10_user_5_743_sf2', mae_item_10_user_5_sf2_743

recommends_ob_5_743_sf1 = json.load(open("recommends_ob_5_743_sf1.txt"))
mae_item_10_user_5_sf1_743 = mae_evaluation(recommends_ob_5_743_sf1,
                                            data_743_held_10_ob_5_ui)
print'mae_item_10_user_5_743_sf1', mae_item_10_user_5_sf1_743

# item sparsity < 10, user sparsity: 10
data_743_held_10_ob_10_ui = json.load(open("data_743_held_10_ob_10_ui.txt"))
recommends_ob_10_743_sf2 = json.load(open("recommends_ob_10_743_sf2.txt"))
mae_item_10_user_10_sf2_743 = mae_evaluation(recommends_ob_10_743_sf2, data_743_held_10_ob_10_ui)
print'mae_item_10_user_10_743_sf2', mae_item_10_user_10_sf2_743

recommends_ob_10_743_sf1 = json.load(open("recommends_ob_10_743_sf1.txt"))
mae_item_10_user_10_sf1_743 = mae_evaluation(recommends_ob_10_743_sf1,
                                             data_743_held_10_ob_10_ui)
print'mae_item_10_user_10_743_sf1', mae_item_10_user_10_sf1_743

# item sparsity < 10, user sparsity: 20
data_743_held_10_ob_20_ui = json.load(open("data_743_held_10_ob_20_ui.txt"))
recommends_ob_20_743_sf2 = json.load(open("recommends_ob_20_743_sf2.txt"))
mae_item_10_user_20_sf2_743 = mae_evaluation(recommends_ob_20_743_sf2, data_743_held_10_ob_20_ui)
print'mae_item_10_user_20_743_sf2', mae_item_10_user_20_sf2_743

recommends_ob_20_743_sf1 = json.load(open("recommends_ob_20_743_sf1.txt"))
mae_item_10_user_20_sf1_743 = mae_evaluation(recommends_ob_20_743_sf1,
                                             data_743_held_10_ob_20_ui)
print'mae_item_10_user_20_743_sf1', mae_item_10_user_20_sf1_743

# item sparsity < 20, user sparsity: 5
data_743_held_20_ob_5_ui = json.load(open("data_743_held_20_ob_5_ui.txt"))
recommends_ob_5_743_sf2 = json.load(open("recommends_ob_5_743_sf2.txt"))
mae_item_20_user_5_sf2_743 = mae_evaluation(recommends_ob_5_743_sf2, data_743_held_20_ob_5_ui)
print'mae_item_20_user_5_743_sf2', mae_item_20_user_5_sf2_743

recommends_ob_5_743_sf1 = json.load(open("recommends_ob_5_743_sf1.txt"))
mae_item_20_user_5_sf1_743 = mae_evaluation(recommends_ob_5_743_sf1,
                                            data_743_held_20_ob_5_ui)
print'mae_item_20_user_5_743_sf1', mae_item_20_user_5_sf1_743

# item sparsity < 20, user sparsity: 10
data_743_held_20_ob_10_ui = json.load(open("data_743_held_20_ob_10_ui.txt"))
recommends_ob_10_743_sf2 = json.load(open("recommends_ob_10_743_sf2.txt"))
mae_item_20_user_10_sf2_743 = mae_evaluation(recommends_ob_10_743_sf2, data_743_held_20_ob_10_ui)
print'mae_item_20_user_10_743_sf2', mae_item_20_user_10_sf2_743

recommends_ob_10_743_sf1 = json.load(open("recommends_ob_10_743_sf1.txt"))
mae_item_20_user_10_sf1_743 = mae_evaluation(recommends_ob_10_743_sf1,
                                             data_743_held_20_ob_10_ui)
print'mae_item_20_user_10_743_sf1', mae_item_20_user_10_sf1_743

# item sparsity < 20, user sparsity: 20
data_743_held_20_ob_20_ui = json.load(open("data_743_held_20_ob_20_ui.txt"))
recommends_ob_20_743_sf2 = json.load(open("recommends_ob_20_743_sf2.txt"))
mae_item_20_user_20_sf2_743 = mae_evaluation(recommends_ob_20_743_sf2, data_743_held_20_ob_20_ui)
print'mae_item_20_user_20_743_sf2', mae_item_20_user_20_sf2_743

recommends_ob_20_743_sf1 = json.load(open("recommends_ob_20_743_sf1.txt"))
mae_item_20_user_20_sf1_743 = mae_evaluation(recommends_ob_20_743_sf1,
                                             data_743_held_20_ob_20_ui)
print'mae_item_20_user_20_743_sf1', mae_item_20_user_20_sf1_743


# item sparsity:no constraint, user sparsity: 5
data_743 = json.load(open("data_743.txt"))
data_743_held_free_ob_5 = json.load(open("data_743_held_free_ob_5.txt"))
recommends_ob_5_743_sf2 = json.load(open("recommends_ob_5_743_sf2.txt"))
mae_item_user_5_sf2_743 = mae_evaluation(recommends_ob_5_743_sf2, data_743_held_free_ob_5)
print'mae_item_free_user_5_743_sf2', mae_item_user_5_sf2_743

recommends_ob_5_743_sf1 = json.load(open("recommends_ob_5_743_sf1.txt"))
mae_item_user_5_sf1_743 = mae_evaluation(recommends_ob_5_743_sf1, data_743_held_free_ob_5)
print'mae_item_user_5_743_sf1', mae_item_user_5_sf1_743

# item sparsity: no constraint, user sparsity: 10
data_743_held_free_ob_10 = json.load(open("data_743_held_free_ob_10.txt"))
recommends_ob_10_743_sf2 = json.load(open("recommends_ob_10_743_sf2.txt"))
mae_item_user_10_sf2_743 = mae_evaluation(recommends_ob_10_743_sf2, data_743_held_free_ob_10)
print'mae_item_free_user_10_743_sf2', mae_item_user_10_sf2_743

recommends_ob_10_743_sf1 = json.load(open("recommends_ob_10_743_sf1.txt"))
mae_item_user_10_sf1_743 = mae_evaluation(recommends_ob_10_743_sf1, data_743_held_free_ob_10)
print'mae_item_user_10_743_sf1', mae_item_user_10_sf1_743


# item sparsity: no constraint, user sparsity: 20
data_743_held_free_ob_20 = json.load(open("data_743_held_free_ob_20.txt"))
recommends_ob_20_743_sf2 = json.load(open("recommends_ob_20_743_sf2.txt"))
mae_item_user_20_sf2_743 = mae_evaluation(recommends_ob_20_743_sf2, data_743_held_free_ob_20)
print'mae_item_free_user_20_743_sf2', mae_item_user_20_sf2_743

recommends_ob_20_743_sf1 = json.load(open("recommends_ob_20_743_sf1.txt"))
mae_item_user_20_sf1_743 = mae_evaluation(recommends_ob_20_743_sf1, data_743_held_free_ob_20)
print'mae_item_user_20_743_sf1', mae_item_user_20_sf1_743



# -*-coding:utf-8-*-

from cosine import cosine_sim
from getSimilar import getSimilarObject
from dataformat import transforms
from dataformat import formatMovieLens
from topmatches import topmatches
from mean import usermean
from mean import itemmean
from math import sqrt
from suirsimilarity import suir_sim


# target is a string here.
def similarity_sur(data, target, neighbor=4, simscore=cosine_sim, a=0.7, b=0.3, types ='SUR'):
    '''
    物品推荐：给 给定的用户， 默认返回 num= 物品
    要两个 for, 对用户和物品都进行遍历
    '''

    # the data for item-based models
    iml = transforms(data)
    # to store the ratings for not yet seen movies made by the given user's neighbors.
    itemsimsum = {}
    simsum = {}
    # 储存给定用户没看过的其他的电影的其相似用户的评分
    itemsum = {}
    sum = {}
    # 该用户平均打分
    target_mean = usermean(data, target)
    # 遍历每个用户 top-n 邻居，然后遍历他们看过但该用户没看过的每个电影
    target_neighbors = topmatches(data,target,neighbor,simscore)
    # the sum of the similarities between the target and its neighbors.
    sumsim = topmatches(data, target, neighbor, simscore, simsum='True')
    # 总共要看的邻居数目
    for i in range(neighbor):
        # 取数邻居的 id
        neighbor.id = target_neighbors[i][1]
        # similarity between the target user and its neighbor
        simtarnei = simscore(data, target, str(neighbor.id))
        # 遍历某个邻居看过的电影
        if type == 'SUIR':
            for item in data[str(neighbor.id)]:
                item_neighbors = topmatches(iml, item, neighbor,simscore)
                # get the neighbour name
                neighbor_names = item_neighbors[i][1]
                # do we need string here?
                for user in iml[neighbor_names]:
                    if data[user][item] != 0:
                        user_mean = usermean(data, user)
                        item_mean = itemmean(iml, item)
                        p = data[user][item] - (user_mean-target_mean)-(user_mean - item_mean)
                        simka = simscore(data,target,user)
                        simmb = simscore(iml,item,neighbor_names)
                        suikmab = 1/(sqrt(pow(1/simka, 2)) + pow(1/simmb,2))
                        weight =



        else:
            for item in data[str(neighbor.id)]:
             # 剔除和邻居看过的一样的电影
                if item not in data[target]:
                   # 初始化
                   itemsum.setdefault(item, 0)
                   itemsimsum.setdefault(item, 0)
                   neighboritemsum[item] += p * weight_mean = usermean(data, str(neighbor.id))
                   # check string here
                   iml = transforms(data)
                   item_mean = itemmean(iml, str(item))
                   p = data[str(neighbor.id)][item] - (neighbor_mean - target_mean) - (neighbor_mean - item_mean)
                if types == 'SUR':
                   weight = simtarnei * a * (1 - b) / sumsim
                   itemsum[item] += p * weight
                else:
                   weight = simtarnei * a * (1 - b) / sumsim
                   itemsum[item] += p * weight

    return itemsum


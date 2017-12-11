from cosine import cosine_sim
from dataformat import transforms

from topmatches import topmatches

from mean import mean
from math import sqrt
from suirsimilarity import sum_suir_sim

'''
The output form:
[(1.921, 'Just My Luck'), (1.886, 'The Night Listener'), (1.089, 'Lady in the Water')]
'''


def recommend(data, givenperson, num=4, nitem=2, simscores=cosine_sim, a=0, b=1):

    '''
    There are four cases in this model: SUR， SIR， SUIR and 0.
    To predict the rates, we need probability and weight.
    In calculating the probabitliy, we need the means of users and items.
    In calculating the weights, we need the accumulated similarities across
    the users or items.
    '''

    # {user1: mean, user2:mean, ...}
    user_mean = mean(data)

    # {item1: mean, item2: mean, ...}
    idata = transforms(data)
    item_mean = mean(idata)

    # givenperson's neighbors
    # [(similarity1,neighbor1), (similarity2,neighbor2), ... ]
    # [(1.0, '935'), (1.0, '9'), (1.0, '893'), (1.0, '876'), (1.0, '853')]
    target_neighbors = topmatches(data=data, givenperson=givenperson, neighbors=num, simscore=simscores)
    # declare the dict for storing the rates
    # {item1: rate, item2:rate2, ...}
    itemsum = {}

    # 遍历每个neighbor
    for i in range(num):
        # 取数邻居的 id
        neighbor_id = target_neighbors[i][1]
        # 取与邻居的相似度
        neighbor_sim = target_neighbors[i][0]
        # 遍历某个邻居看过的电影
        for item in data[str(neighbor_id)]:
            # 遍历给定用户没有看过的电影
            if item not in data[givenperson]:

                # CASE1 SUIR: 相似的电影被相似的人评分
                # 找相似的物品
                # [(similarity1,neighbor1), (similarity2,neighbor2), ... ]
                item_neighbor = topmatches(idata, item, neighbors=num, simscore=simscores)
                v = sum_suir_sim(data=data, givenperson=givenperson, givenitem=item, num=num, simscores=simscores)
                # 相似物品被邻居评论过
                # 遍历相似的物品，看他们是否在邻居中
                for j in range(num):
                    # 这个物品的相似物品的名字
                    item_name = item_neighbor[j][1]
                    # 与这个物品的的相似度
                    item_sim = item_neighbor[j][0]
                    # mean of this item
                    m_mean = item_mean[item]

                    for item_name in data[str(neighbor_id)]:
                        if item_name not in data[givenperson]:
                            # calculate the probability
                            prob = data[str(neighbor_id)][item_name] - \
                                    (user_mean[str(neighbor_id)] - user_mean[givenperson]) - \
                                    (m_mean - item_mean[item])

                            # 用户a和k的相似度
                            simka = neighbor_sim
                            # 物品 b 和 m 的相似度
                            simbm = item_sim
                            # 评分 x_km 和 x_ab 的相似度
                            simkmab = 1 / sqrt(pow(1 / simka, 2) + pow(1 / simbm, 2))
                            sumsum = v
                            weight = (simkmab/sumsum)*b
                            itemsum.setdefault(item, 0)
                            itemsum[item] += float(prob * weight)

                    # CASE2: SIR- use the ratings for similar items made by the target user.
                    for item_name in data[givenperson]:
                        prob1 = data[givenperson][item_name] - (item_mean[item_name]-m_mean)
                        # calculate the weight
                        sumsim1 = topmatches(idata, item_name, simsum='True')
                        weight1 = item_sim * (1-a) * (1-b)/sumsim1
                        itemsum[item] += float(prob1 * weight1)

                # CASE3: SUR - use the ratings for the item made by similar users
                prob2 = data[str(neighbor_id)][item]-(user_mean[str(neighbor_id)] - user_mean[givenperson])
                sumsim2 = topmatches(data, str(neighbor_id), simsum='True')
                weight2 = neighbor_sim * a * (1-b)/sumsim2

                itemsum[item] += float(prob2 * weight2)

    rankings = [(value, key) for key, value in itemsum.items()]
    rankings.sort(cmp=None, key=None, reverse=True)
    recommendations = rankings[0:nitem]

    new_rec = {}
    for i in recommendations:
        new_rec[i[1]] = i[0]

    return new_rec



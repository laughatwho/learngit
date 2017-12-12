# -*-coding:utf-8-*-

from __future__ import division
from math import sqrt


''' 
基于用户过滤思路：找出两个用户看过的相同电影的评分，从而进行按pearson公式求值。那些非公共电影不列入求相似度值范围。
基于物品过滤思路：找过两部电影相同的观影人给出的评分，从而按pearson公式求值
返回：评分的相似度，[-1,1]范围，0最不相关，1，-1为正负相关，等于1时，表示两个用户完全一致评分
这里的data格式很重要，这里计算相似度是严格按照上面data格式所算。
此字典套字典格式，跟博客计算单词个数 存储格式一样
'''

def pearson_sim(data, person1, person2):

    # 计算pearson系数，先要收集两个用户公共电影名单.
    # commonmovies = [ movie for movie in data[person1] if movie in data[person2]]
    commonmovies = []        #改成列表呢


    #data[person1] is a dict. We are referring to every key in this dict.
    for movie in data[person1]:
        if movie in data[person2]:
            commonmovies.append(movie)

    # 公共电影的个数
    n = float(len(commonmovies))
    if n == 0:
        return 0

    # 分布对两个用户的公共电影movie分数总和
    sum1 = sum([data[person1][movie] for movie in commonmovies])
    sum2 = sum([data[person2][movie] for movie in commonmovies])

    # 计算乘积之和
    sum12 = sum([data[person1][movie] * data[person2][movie] for movie in commonmovies])

    # 计算平方和
    sum1Sq = sum([pow(data[person1][movie], 2) for movie in commonmovies])
    sum2Sq = sum([pow(data[person2][movie], 2) for movie in commonmovies])

    # 计算分子
    num = sum12 - sum1 * sum2 / n
    # 分母
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0

    get = num / den
    return round(get, 5)


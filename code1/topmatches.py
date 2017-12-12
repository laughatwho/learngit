# -*-coding:utf-8-*-

from cosine import cosine_sim


'''
  用户匹配推荐：给定一个用户，返回对他口味最匹配的其他用户
  物品匹配： 给定一个物品，返回相近物品
  输入参数：对person进行默认推荐num=5个用户（基于用户过滤），或是返回5部电影物品（基于物品过滤），相似度计算用pearson计算
  print topmatches(iml, 'Great Escape, The (1963)')
  [(1.0, 'Year of the Horse (1997)'), (1.0, 'Underground (1995)'), ...]
'''


def topmatches(data, givenperson, neighbors=5, simscore=cosine_sim, simsum='False'):
    # 建立最终结果列表
    usersscores = [(simscore(data, givenperson, other), other) for other in data if other != givenperson]
    # 对列表排序
    # list.sort([usersscores])
    usersscores.sort(cmp=None, key=None, reverse=True)

    simnneighbor = usersscores[0:neighbors]

    if simsum == 'False':
        return simnneighbor
    else:
        # calculate the sum of the similarities
        sim = [sim[0] for sim in simnneighbor]
        ssum = sum(sim)
        return ssum


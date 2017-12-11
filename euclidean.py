# -*-coding:utf-8-*-

from math import sqrt

'''
    欧氏距离求相似度，距离越大，越相似
'''

def euclidean_sim(data, person1, person2):

    commonmovies = [movie for movie in data[person1] if movie in data[person2]]
    if len(commonmovies) == 0:
        return 0
# 平方和

    sumSq = sum([pow(data[person1][movie] - data[person2][movie], 2) for movie in commonmovies])
# 使最终结果是，越相似，距离越大。所以将上面距离取倒数即可

    sim = 1 / (1 + sqrt(sumSq))
    return sim


mydict = {'carl': 40, 'alan': 2, 'bob': 1,
          'danny': 3}

a = sorted(mydict.iteritems(), key=lambda (k, v): (v, k), reverse=True)
b = sorted(mydict.iteritems(), key=lambda (k, v): (v, k), reverse=True)[0:2]
c = dict(b)
print a
print b
print c
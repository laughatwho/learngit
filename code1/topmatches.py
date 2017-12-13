# -*-coding:utf-8-*-

from cosine import cosine_sim

def topmatches(data, givenperson, neighbors=5, simscore=cosine_sim, simsum='False'):
    usersscores = [(simscore(data, givenperson, other), other) for other in data if other != givenperson]
    usersscores.sort(cmp=None, key=None, reverse=True)
    simnneighbor = usersscores[0:neighbors]

    if simsum == 'False':
        return simnneighbor
    else:
     
        sim = [sim[0] for sim in simnneighbor]
        ssum = sum(sim)
    
    return ssum


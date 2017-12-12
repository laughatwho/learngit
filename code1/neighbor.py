# -*-coding:utf-8-*-
from topmatches import topmatches


def object_neighbor(ob_data, n, sim_method):
    dic_item_neighbor = {}
    for item in ob_data:
        item_neighbors = topmatches(data=ob_data, givenperson=item, neighbors=n, simscore=sim_method, simsum='False')
        for (similarity, movie) in item_neighbors:
                dic_item_neighbor.setdefault(item, {})
                dic_item_neighbor[item][movie] = similarity

    return dic_item_neighbor



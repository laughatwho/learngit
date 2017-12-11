# -*-coding:utf-8-*-


def mean(data):
    means = {}
    for (key, value) in data.items():
        means.setdefault(key, {})
        means[key] = sum(value.values())/(1.0*len(value.values()))
    return means









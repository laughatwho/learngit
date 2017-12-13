

from random import shuffle


def format_movie_lens(filepath='/Users/sanxi/Desktop/ml_unify'):

    movie = {}
    for line in file(filepath + '/u.item'):
        title = '|' in line
        if title == 1:
            (ids, name) = line.split("|")[0:2]
            movie[ids] = name
    resultdata = {}
    for line in file(filepath + '/u.data'):
        nonoise = '\t' in line
        if nonoise == 1:
            (user, movieId, rating) = line.split("\t")[0:3]
            resultdata.setdefault(user, {})
            movietitle = movie[movieId]
            resultdata[user][movietitle] = float(rating)

    return resultdata

def transforms(data):
    new_data = {}
    for key, value in data.items():
        for key1, value1 in value.items():
            new_data.setdefault(key1, {})
            new_data[key1][key] = value1
    return new_data


def list_to_dict(lists):
    new_rec = {}
    for i in lists:
        new_rec[i[0]] = i[1]
    return new_rec


def dict_to_list(dictionary):
    lists = dictionary.items()
    return lists


def ob_held(data, n_observed):
    data_ob = {}
    data_held = {}
    for key, values in data.items():
        key1 = values.keys()
        shuffle(key1)
        key_observed = key1[0:n_observed]
        key_held_out = key1[n_observed: len(key1)]
        for key2 in key_observed:

            data_ob.setdefault(key, {})
            rate = data[key][key2]

            data_ob[key][key2] = rate

        for key3 in key_held_out:
            data_held.setdefault(key, {})
            rate3 = data[key][key3]
            data_held[key][key3] = rate3
    return [data_ob, data_held]


def item_sparsity(i_data, n_item):
    for key, value in i_data.items():
        a = len(value.values())
        while a >= n_item:
            value.popitem()
            a = len(value.values())
    return i_data


def divide_data(data, n_folds=2):
    lists = dict_to_list(data)
    shuffle(lists)
    partition_size = int(float(len(lists)/n_folds))
    # To store the fold lists.
    list_folds = list()
    last = -1
    dic_fold = {}

    for p in range(n_folds):
        initial = 1 + last
        final = (p + 1) * partition_size
        list_folds.append(lists[initial:final])
        last = final

    for fold in range(n_folds):
        train_set = list()
        for fold_train in range(n_folds):
            if fold_train != fold:
                train_set += list_folds[fold_train]
        train_set.sort()
        list_folds[fold].sort()
        dic_list_fold = {}
        dic_train_set = list_to_dict(train_set)
        dic_list_fold[fold] = list_to_dict(list_folds[fold])
        dic_fold[fold] = {'train': dic_train_set, 'test': dic_list_fold[fold]}
    return dic_fold


def split_data(data, n_user=700):
    lists = data.items()
    shuffle(lists)
    new_list = lists[0:n_user]
    test_data = list_to_dict(new_list)
    return test_data




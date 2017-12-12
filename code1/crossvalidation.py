# -*-coding:utf-8-*-

from random import shuffle
from random import sample
from dataformat import dict_to_list
from dataformat import list_to_dict


def divide_data(data, n_folds=2, leave_out_item=1):
    lists = dict_to_list(data)
    shuffle(lists)

    # Get the number of interactions that each partition should have.
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
        # to leave n rate(s) out for each user
        if leave_out_item != 0:
            for key, value in dic_list_fold[fold].items():
                try:
                    j = sample(range(len(value.values())), leave_out_item)
                    if leave_out_item > len(value.values()):
                        continue
                    # j = randint(0, len(value.values()))
                    key1 = [key2 for key2 in value]
                    for i in j:
                        value[key1[i]] = 0
                        dic_list_fold[fold][key] = value
                except ValueError:
                    pass

        dic_fold[fold] = {'train': dic_train_set, 'test': dic_list_fold[fold]}

    return dic_fold


def splitdataset(data, nuser=700):
    lists = dict_to_list(data)
    shuffle(lists)
    test_set = []

    for i in range(nuser):
        test_set.append(lists[i])
    testdata = list_to_dict(test_set)

    return testdata















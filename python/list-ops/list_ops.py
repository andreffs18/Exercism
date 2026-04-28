def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_l = []
    for i in lists:
        if isinstance(i, list):
            new_l.extend(i)
        else:
            new_l.append(i)
    return new_l


def filter(function, list):
    new_l = []
    for i in list:
        if function(i):
            new_l.append(i)
    return new_l


def length(list):
    return len(list)


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial=0):
    for i in list:
        initial = function(initial, i)
    return initial


def foldr(function, list, initial):
    for e in reversed(list):
        initial = function(initial, e)
    return initial


def reverse(list):
    new_l = []
    for i in range(len(list)):
        new_l.append(list[len(list) - i - 1])
    return new_l

import string
from random import random


def gnomeSort(lista, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if lista[index] >= lista[index - 1]:
            index = index + 1
        else:
            lista[index], lista[index - 1] = lista[index - 1], lista[index]
            index = index - 1

    return lista


def QuickSort(lista, st, dr):
    i = st
    j = dr
    x = int((i + j) / 2)
    mij = lista[x]
    while i <= j:
        while lista[i] < mij:
            i = i + i
        while lista[j] < mij:
            j = j - 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
            i = i + 1
            j = j - 1
    if st < j:
        QuickSort(lista, st, j)
    if i < dr:
        QuickSort(lista, i, dr)


def random_string(length):
    """
    Functia genereaza un sir random
    :param length: lungimea sirului generat, numar natural
    :return: stringul
    """
    letters = string.ascii_lowercase + string.ascii_uppercase
    new_string = ''.join(random.choice(letters) for i in range(length))
    return new_string

# fonction permutation

def permuter(tab, i, j):
    """
    permute 2 éléments dans un tableau tab
    :param tab: tableau d'entier
    :type tab: int
    :param i: entier à échanger
    :type i: int
    :param j: entier à échanger
    :type j: int
    :return: tableau d'entier
    :rtype: int
    """
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp
    return tab


def median(tab, i, j, k):
    """
    :param tab: tableau d'entier
    :type tab: int
    :param i: entier qui va être comparé pour avoir la valeur médiane
    :type i: int
    :param j: entier qui va être comparé pour avoir la valeur médiane
    :type j: int
    :param k: entier qui va être comparé pour avoir la valeur médiane
    :type k: int
    :return: entier qui est entre les 2 autres entiers
    :rtype: int
    """
    if tab[j] >= tab[i] > tab[k]:
        return k
    if tab[j] <= tab[i] and tab[i] > tab[k]:
        return j
    return k

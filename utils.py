def permuter(tab, i, j):
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp
    return tab


def median(tab, i, j, k):
    if tab[i] <= tab[j] and tab[i] > tab[k]:
        return k
    if tab[j] <= tab[i] and tab[i] > tab[k]:
        return j
    return k

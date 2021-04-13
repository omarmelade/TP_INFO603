# fonction utiles
from utils import *


# fonction partition

def partition(t, i, j):
    m = median(t, i, j, (i + j) // 2)
    t = permuter(t, i, m)
    l = i + 1
    k = j
    n = len(t) - 1
    # 1
    print(f"--------- 1 ---------")
    print(f"i>=2 : {l + 1 >= 2}")  # l'indice du tab commence a 0 (on corrige le decalage pour coller au sujet)
    print(f"k <= n : {k <= n}")
    print(f"Pivot : {t[i]}")
    print(f"")

    while l <= k:

        # 2 Boucle de fin
        while t[k] > t[i] and l <= k:
            for x in range(k, k + 1):
                assert t[x] > t[i]
            print(f"--------- 2 ---------")
            print(f"∀x ∈ [k, j] t[x] > t[i]")
            print(f"k > i : {k > i}")
            print(f"")
            k -= 1

        # 3 Boucle de début
        while t[l] < t[i] and l <= k:
            for x in range(i + 1, l + 1):
                assert t[x] <= t[i]
            print(f"--------- 3 ---------")
            print(f"∀x ∈ [i-1, l] t[x] <= t[i]")
            print(f"k > i : {k > i}")
            print(f"")
            l += 1

        if l < k:
            t = permuter(t, l, k)
            l += 1
            k -= 1

        # 4 Permutation des bornes
        for x in range(i + 1, l):
            assert t[x] <= t[i]
        print(f"--------- 4_1 ---------")
        print(f"∀x ∈ [i+1, l-1] t[x] <= t[i]\n")

        for x in range(k + 1, j + 1):
            assert t[x] > t[i]
        print(f"--------- 4_2 ---------")
        print(f"∀x ∈ [k+1, j] t[x] > t[i]\n")

    # 5 placement du pivot a sa place
    print(f"--------- 5_1 ---------")
    print(f"l > k : {l > k}")
    for x in range(i + 1, k + 1):
        assert t[x] <= t[i]
    print(f"∀x ∈ [i+1, k], t[x] <= t[i]\n")

    print(f"--------- 5_2 ---------")
    for x in range(l, j + 1):
        assert t[x] > t[i]
    print(f"∀x ∈ [l, j], t[x] > t[i]\n")

    t = permuter(t, i, k)

    print(f"--------- 6_1 ---------")
    for x in range(i, l + 1):
        assert t[x] <= t[l]
    print(f"∀x ∈ [i, l], t[x] <= t[l]\n")

    print(f"--------- 6_2 ---------")
    for x in range(k + 1, j + 1):
        assert t[x] > t[k]
    print(f"∀x ∈ [k+1, j], t[x] <= t[l]\n")

    return k


# fonction boustrophedon

def boustrophedon(t, i, j):
    sens = True
    inf = i
    sup = j

    # Condition initial ?
    print(f"--------- 1 ---------")

    while inf < sup:

        # Début de boucle
        print(f"--------- 2_1 ---------")
        for x in range(i, inf):
            assert t[x] <= t[inf]
        print(f"∀x ∈ [i, inf-1], t[x] <= t[inf]\n")

        print(f"--------- 2_2 ---------")
        for x in range(sup + 1, j):
            assert t[x] >= t[sup]
        print(f"∀x ∈ [sup+1, j], t[x] >= t[sup]\n")
        #

        if sens:
            for x in range(inf, sup):
                if t[x] > t[x + 1]:
                    permuter(t, x, x + 1)
            sens = False
            sup -= 1
        else:
            for x in range(sup, inf - 1, -1):
                if t[x] > t[x + 1]:
                    permuter(t, x, x + 1)
            sens = True
            inf += 1
        print(t)

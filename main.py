# This is a sample Python script.
# --------Exo 1

# fonction utiles

from tri import boustrophedon, partition

# # exo 1 fonction partition
#
# t = [1, 6, 4, 21, 12, 7, 32, 35, 37]
# partition(t, 0, len(t) - 1)
#
#
# # ---------- Exo 2
# # fonction boustrophedon
#
# t = [24, 12, 68, 96, 25, 1]
# boustrophedon(t, 0, len(t) - 1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = input("Donnez moi un tableau (exemple : 1, 3, 5, 12) \n")
    arr = a.split(",")
    arr = [int(i) for i in arr]
    print(arr)
    print("Que voulez vous faire :\n  1 - partition\n  2 - tri boustrophedon\n")
    choice = input()
    if int(choice) == 1:
        partition(arr, 0, len(arr) - 1)
    elif int(choice) == 2:
        boustrophedon(arr, 0, len(arr) - 1)
    else:
        print("Cette fonctionnalité n'existe pas")
    print(f"le tableau après exécution : {arr}")

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# --------Exo 1


from tri import boustrophedon, partition

# exo 1 fonction partition

t = [1, 6, 4, 21, 12, 7, 32, 35, 37]
partition(t, 0, len(t) - 1)
print(t)

# ---------- Exo 2
# fonction boustrophedon

t = [24, 12, 68, 96, 25, 1]
boustrophedon(t, 0, len(t) - 1)
print(t)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    partition(t, 0, len(t) - 1)
    print(t)

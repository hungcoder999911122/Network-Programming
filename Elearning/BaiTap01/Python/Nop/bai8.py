def ChuSoDautien(arr):
    for x in arr:
        ChuSoDau = int(str(abs(x))[0])
        if ChuSoDau % 2 != 0:
            return x
    return None
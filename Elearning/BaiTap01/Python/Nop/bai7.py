def NhapMang():
    n = int(input("Nhap so luong phan tu cua mang: "))
    arr = []
    for i in range(n):
        so = int(input(f"Nhap phan tu thu {i+1}: "))
        arr.append(so)
    return arr

def XuatMang(arr):
    print("Mang vua nhap: ", end="")
    for x in arr: 
        print(x, end=" ")
    print()
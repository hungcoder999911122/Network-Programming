import math
# Bài 5
def SoNguyenTo(n):
    if n<2:
        return False
    for i in range (2, int(math.sqrt(n)+ 1)):
        if n % i == 0:
            return False
    return True

# Bài 7
def NhapMang():
    n= int(input("Nhap so luong phan tu cua mang: "))
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

# Bài 8
def ChuSoDautien(arr):
    for x in arr:
        ChuSoDau = int(str(abs(x)) [0])
        if ChuSoDau % 2 != 0:
            return x
    return None

if __name__ == "__main__":

    c = False
    while not c:
        print("""
    --- BÀI TẬP 5, 7, 8 ---
    1. BÀI 5: Kiểm tra số nguyên tố
    2. BÀI 7: Nhập, xuất mảng 1 chiều
    3. BÀI 8: Tìm số có chữ số đầu là lẻ
    0. Thoat khoi chuong trinh
    """)

        n = int(input("Nhap bai tap muon thuc hien: "))

        match n:
            case 1:
                print("---- BAI 5 ----")
                num = int(input("Nhap so nguyen can kiem tra: "))
                if SoNguyenTo(num):
                    print(f"{num} La so nguyen to")
                else:
                    print(f"{num} Khong la so nguyen to")
            case 2: 
                print("--- BAI 7 ---")
                MyList = NhapMang()
                XuatMang(MyList)
            case 3:
                print("--- BAI 8 ---")
                MyList1 = NhapMang()
                List1 = ChuSoDautien(MyList1)
                if List1 is not None:
                    print (f"Gia tri dau tien co chu so dau la le {List1}")
                else: 
                    print ("Khong co phan tu nao trong mang co chu so dau la chu so le.")
            case 0:
                print("Cam on vi da su dung!!!")
                c = True
            case _:
                print("Bai nhap khong hop le vui long nhap lai")
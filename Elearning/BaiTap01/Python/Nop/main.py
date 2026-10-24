from bai5 import SoNguyenTo
from bai7 import NhapMang, XuatMang
from bai8 import ChuSoDautien

if __name__ == "__main__":
    c = False
    while not c:
        print("""
    --- BAI TAP 5, 7, 8 ---
    1. BAI 5: Kiem tra so nguyen to
    2. BAI 7: Nhap, xuat mang 1 chieu
    3. BAI 8: Tim so co chu so dau la le trong mang
    0. Thoat khoi chuong trinh
    """)

        n = input("Nhap bai tap muon thuc hien: ")

        match n:
            case "1":
                print("---- BÀI 5 ----")
                num = int(input("Nhap so nguyen can kiem tra: ")) 
                if SoNguyenTo(num):
                    print(f"{num} La so nguyen to")
                else:
                    print(f"{num} Khong la so nguyen to")
            
            case "2": 
                print("--- BÀI 7 ---")
                MyList = NhapMang()
                XuatMang(MyList)
            
            case "3":
                print("--- BÀI 8 ---")
                MyList1 = NhapMang() 
                List1 = ChuSoDautien(MyList1) 
                
                if List1 is not None:
                    print(f"Gia tri dau tien co chu so dau la le: {List1}")
                else: 
                    print("Khong co phan tu nao trong mang co chu so dau la chu so le.")
            
            case "0":
                print("Cam on vi da su dung!!!")
                c = True
            
            case _:
                print("Bai nhap khong hop le vui long nhap lai")
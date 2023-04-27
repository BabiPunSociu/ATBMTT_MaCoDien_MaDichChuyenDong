
# Ma dich chuyen dong

import math


def showMenu():
    print('Chon cac chuc nang sau')
    print('1. Ma hoa')
    print('2. Giai ma')
    print('0. Thoat')
    return nhapSoNguyen("Lua chon cua ban la: ")  # luaChon

def nhapSoNguyen(mes):
    while True:
        a = input(mes).strip()
        try:
            a = int(a)
            if a>2 or a<0:
                print('Chi nhap so trong [0,2]')
            else: return a 
        except ValueError:
            print('Loi. Ban phai nhap so')
       
def inmtran():  # in ra man hinh ma tran mtran
    global mtran
    for x in mtran:
        print(x)

def getIndex(int_, list_): # Lấy chỉ số đầu tiên của 1 số trong 1 list
    for i in range(len(list_)):
        if int(list_[i]) == int_: return i 
    return -1

def ma_hoa(str_, khoa):
    global mtran

    # Buoc 1: Tao ma tran du kich thuoc de luu tru cac chu cai ban ro:
    hang = math.ceil(len(str_)/len(khoa))   # ceil de lam tron lên
    cot = len(khoa)
    # Tao ma tran rong kich thuoc: hang x len(khoa) 
    mtran = [[' ' for i in range(cot)] for j in range(hang)]

    # Buoc 2: Chen cac chu cai ban ro lan luot vao mtran
    index = 0 # Tao chi so index cho ban ro
    for i in range(hang):
        for j in range(cot):
            # Chen cac chu cai ban ro vao ma tran
            if index < len(str_):   
                mtran[i][j] = str_[index] 
                index += 1
            # Khi da chen het cac chu cai o ban ro thi chen cac ki tu khac
            else:
                mtran[i][j] = 'x'

    # Buoc 3: Doc ket qua (luu y: chi so cua cac so trong khoa tuong ung voi chi so cua cac cot can lay gia tri)
    ban_ma = '' 
    for x in range(cot): #    x: 0 -> cot-1
        chiSo = getIndex(x+1,khoa)  # Lay chi so cua so trong khoa, theo tu 1 -> cot-1
        for i in range(hang):
            ban_ma += mtran[i][chiSo]
            
    inmtran()
    return ban_ma

def tim_toado(mtran, hang, cot, khoa):
    for x in range(cot): #    x: 0 -> cot-1
        chiSo = getIndex(x+1,khoa)  # Lay chi so cua so trong khoa, theo tu 1 -> cot-1
        for i in range(hang):
            if mtran[i][chiSo]==" ": return i, chiSo

def giai_ma(str_, khoa):
    global mtran

    # Buoc 1: Tao ma tran du kich thuoc de luu tru cac chu cai ban ro:
    hang = math.ceil(len(str_)/len(khoa))   # ceil de lam tron lên
    cot = len(khoa)
    # Tao ma tran rong kich thuoc: hang x len(khoa) 
    mtran = [[' ' for i in range(cot)] for j in range(hang)]

    # Buoc 2: Dien cac chu cai o ban ma vao cac vi tri thich hop
    for x in str_:
        i, j = tim_toado(mtran, hang, cot, khoa) 
        mtran[i][j] = x 
    inmtran()
    
    # Buoc 3: Doc va tra ve ket qua -> ban ro
    ban_ro = ""
    for x in mtran:
        for y in x:
            ban_ro += str(y)
    return ban_ro.strip()

if __name__ == "__main__":
    while True:

        global mtran    # De tao ma tran zic zac

        luaChon = -1
        while luaChon<0 or luaChon>2:
            luaChon = showMenu()
        if luaChon == 0:
            print('Bye...')
            break
        elif luaChon ==1:
            # Ma hoa

            ban_ro = input('Nhap ban ro: ').upper().strip()
            khoa = input("Nhap khoa k (vi du: k='132654'): k = ")
            ban_ma = ma_hoa(ban_ro, khoa)
            print("Ban ma:",ban_ma)
            if input("Nhap bat ki de tiep tuc, nhap 'x' de thoat. Lua chon cua ban: ").strip().upper() == 'X':
                print('Bye...')
                break
        else:
            # Giai ma

            ban_ma = input('Nhap ban ma: ').upper().strip()
            khoa = input("Nhap khoa k (vi du: k='132654'): k = ")
            ban_ro = giai_ma(ban_ma, khoa) 
            print('Ban ro:,',ban_ro) 
            if input("Nhap bat ki de tiep tuc, nhap 'x' de thoat. Lua chon cua ban: ").strip().upper() == 'X':
                print('Bye...')
                break



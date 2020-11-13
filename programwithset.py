# Temukan masalah pada kehidupan sehari-hari yang dapat diselesaikan dengan menggunakan set
# buatlah defspek fungsi yang menyelesaikan masalah tersebut dengan memanfaatkan fungsi primitif set.

"""
Masalah : Membuat Himpunan dari Tahun Kabisat dan Mengurutkan Mulai dari
          Element Terbesar

Diberikan 5 buah list yang berisi tahun-tahun dengan interval 1000 <= tahun <= 3000
Semua element dalam List tersebut harus berisi tahun-tahun kabisat. Apabila ada
satu atau lebih element yang bukan merupakan tahun kabisat, maka list tersebut akan error.

Jika list tersebut dapat dikatakan sebagai List of Tahun Kabisat, maka list akan diubah
menjadi bentuk Set dan akan di urutkan mulai dari nilai terbesar. 
"""

# Realisasi
from setkonstruktif import *

#DefSpek
#mklist : kosong --> list
#mklist() membuat list L

def mklist1():
	return []

Set1 = mklist1()
Set2 = [2016, 2004, 2004, 2012,2020]
Set3 = [2015, 2019, 2040, 2001]
Set4 = [1000, 2000, 3000, 2004, 2003, 2001]
Set5 = [2016, 2004, 2004, 2012, 2020, 2002, 2024]

#DefSpek
#SortMax(L) : list of integer --> list of integer
#SortMax(L) menghasilkan list baru dimana mengurutkan elemen dari yang terbesar ke terkecil

def SortMax(L):
      if IsOneElmt(L):
            return L
      else:
            return Konso(ElmtMax(L),SortMax(Rember(ElmtMax(L),L)))

#DefSpek
#Is_Leap(year): integer --> boolean
#Is_Leap(year) true jika year adalah tahun kabisat

def Is_Leap(year):
    return ((year % 4 == 0) and (year % 100 != 0) or (year // 400 == 0))

#DefSpek
#Is_List_Leap(L) : list of integer --> boolean
#Is_List_Leap(L) bernilai true jika setiap elemen list adalah tahun kabisat

def Is_List_Leap(L):
    if IsOneElmt(L):
        return Is_Leap(FirstElmt(L))
    else:
        if Is_Leap(FirstElmt(L)):
            return Is_Leap(FirstElmt(Rember(FirstElmt(L),L)))
        else:
            return False

#DefSpek
#Make_Set_of_Leap: list --> set
#Make_Set_of_Leap(L) membentuk sebuah set dari List (membuang setiap kemunculan yang lebih dari 1 kali)
#                    dan juga mengurutkannya mulai dari nilai terbesar.

def Make_Set_of_Leap(L):
    if IsEmpty(L):
        return L
    elif Is_List_Leap(L):
        return SortMax(MakeSet(L))
    else:
        return "ValueError: The Input Integers should be Leap"

print('====')
print('-Is_List_Leap-')
print(Is_List_Leap(Set2))
print(Is_List_Leap(Set3))
print(Is_List_Leap(Set4))
print(Is_List_Leap(Set5))
print('====')
print(' ')
print('====')
print('-Make_Set_of_Leap-')
print(Make_Set_of_Leap(Set2))
print(Make_Set_of_Leap(Set3))
print(Make_Set_of_Leap(Set4))
print(Make_Set_of_Leap(Set5))
print('====')

#Nama		: 
#NIM		: 
#Tanggal	: 
#Deskripsi	: 

#DefSpek
#mklist : kosong --> list
#mklist() membuat list L

def mklist():
	return []

L1 = mklist()
L2 = [1, 2, 3, 4, 5, 6, 7]
L3 = [1, 2, 3, 2, 5, 2, 7]
L4 = [3, 2, 4, 90, 87, 6555, 32, 12, 5344, 51, 0]
L6 = [1]
L7 = ["a", "b", "c", "d", "e", "a", "i"]
L8 = ["apple", "banana", "avocado"]

#DefSpek
#Konso : elemen, list --> list
#Konso(e,L) menghasilkan sebuah list dari L dengan menambahkan e sebagai elemen pertama

def Konso(e, L):
	Ls = list(L)
	Ls.insert(0,e)
	return Ls

#DefSpek
#Kons0 : list, elemen --> list
#Kons0(l,e) menghasilkan sebuah list dari l dengan menambahkan e sebagai elemen terakhir

def Kons0(L,e):
	Ls = list(L)
	Ls.append(e)
	return Ls

#DefSpek
#Inverse : list --> list
#Inverse(L) memberikan list yang urutannya terbalik dari aslinya

def Inverse(L):
	Ls = list(L)
	Ls.reverse()
	return Ls

#DefSpek
#Tail : list tidak kosong --> list
#Tail(L) menghasilkan list selain elemen pertama dari list L

def Tail(L):
	Ls = list(L)
	del Ls[0]
	return Ls

#DefSpek
#Head : list tidak kosong --> list
#Head(L) menghasilkan list selain elemen terakhir dari list L

def Head(L):
	Ls = list(L)
	Ls.reverse()
	del Ls[0]
	Ls.reverse()
	return Ls

#DefSpek
#FirstElmt : list tidak kosong --> elemen
#FirstElmt(L) menghasilkan elemen pertama dari suatu list

def FirstElmt(L):
	return L[0]

#DefSpek
#LastElmt : list tidak kosong --> elemen
#LastElmt(L) menghasilkan elemen terakhir dari suatu list

def LastElmt(L):
	Ls = list(L)
	Ls.reverse()
	return Ls[0]

#DefSpek
#NbElmt : list --> integer
#NbElmt(L) menghitung banyaknya elemen dalam list L
def NbElmt(L):
	return len(L)

#DefSpek
#IsEmpty : list --> boolean
#IsEmpty(L) bernilai benar jika list kosong

def IsEmpty(L):
	if(L):
		return False
	else:
		return True

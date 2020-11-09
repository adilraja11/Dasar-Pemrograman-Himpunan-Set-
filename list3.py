#Nama		: 
#NIM		: 
#Tanggal	: 
#Deskripsi	: 

from list2 import *

list1 = [1, [2], 3, 4, [5,6]]

list2 = [1, [1,2,3], 3, 4, [4,5,6]]

Matrix1 =	[
				[1,2,3],
				[4,5,6],
				[7,8,9]
			]
		
Matrix2 =[[1,0,0],[0,1,0],[0,0,1]]
		

#DefSpek
#IsAtom : list --> boolean
#IsAtom(e) bernilai benar jika elemen list adalah sebuah atom

def IsAtom(e):
	if(type(e) != list):
		return True
	else:
		return False

#DefSpek
#IsList : list --> boolean
#IsList(e) bernilai benar jika element list adalah sebuah list

def IsList(e):
	if(type(e) == list):
		return True
	else:
		return False

#DefSpek
#NbLElmt : list --> integer
#NbLElmt(L) menghitung banyaknya elemen dalam list L

def NbLElmt(L):
	if(IsEmpty(L)):
		return 0
	elif(IsList(FirstElmt(L))):
		return NbLElmt(FirstElmt(L)) + NbLElmt(Tail(L))
	else:
		return 1 + NbLElmt(Tail(L))

#DefSpek
#Jumlah : list --> integer
#Jumlah (L) menghasilkan jumlah seluruh elemen dalam list

def Jumlah(L):
	if(IsEmpty(L)):
		return 0
	elif(IsList(FirstElmt(L))):
		return Jumlah(FirstElmt(L)) + Jumlah(Tail(L))
	else:	
		return FirstElmt(L) + Jumlah(Tail(L))
#Nama		: 
#NIM		: 
#Tanggal	: 
#Deskripsi	: 

from list1 import *

#DefSpek
#IsOneElmt : list --> boolean
#IsOneElmt(L) bernilai benar jika list L hanya mempunyai satu elemen

def IsOneElmt(L):
	if((not IsEmpty(L)) and (IsEmpty(Tail(L)))):
		return True
	else:
		return False

#DefSpek
#LGenap : list of integer --> list of integer
#LGenap(L) menghasilkan sebuah list of integer yang beranggotakan angka genap saja dengan menghilangkan elemen yang ganjil

def LGenap(L):
	if (IsEmpty(L)):
		return L
	else:
		if (FirstElmt(L) % 2 == 0):
			return Konso(FirstElmt(L), LGenap(Tail(L)))
		else:
			return LGenap(Tail(L))
			
#DefSpek
#LPrime : list of integer --> list of integer
#LPrime(L) menghasilkan sebuah list of integer yang beranggotakan angka prima saja dengan menghilangkan elemen yang bukan prima
			
def LPrime(L):
	if (IsEmpty(L)):
		return L
	else:
		if (IsPrima(FirstElmt(L))):
			return  Konso(FirstElmt(L),LPrime(Tail(L)))
		else:
			return LPrime(Tail(L))
#DefSpek
#ElmtMax : list of integer --> integer
#ElmtMax(L) menghasilkan elemen terbesar dari list L

def Max2(a,b):
	if(a > b):
		return a
	else:
		return b
		
def ElmtMax(L):
	if(IsEmpty(L)):
		return 0
	elif(IsOneElmt(L)):
		return FirstElmt(L)
	else:
		return Max2(FirstElmt(L), ElmtMax(Tail(L)))

#DefSpek
#ElmtKeN : integer >= 0, list tidak kosong --> elemen
#ElmtKeN(n,L) menghasilkan elemen ke-n dari list L

def ElmtKeN (n,L):
	if(IsEmpty(L)):
		raise ValueError("List kosong")
	else:
		if(n <= 0):
			raise ValueError("Urutan harus lebih dari 0")
		elif(n > NbElmt(L)):
			raise ValueError("Urutan lebih dari jumlah list")
		elif(n == 1):
			return FirstElmt(L)
		else:
			return ElmtKeN(n-1, (Tail(L)))

#DefSpek
#IsMember : elemen, list --> boolean
#IsMember(x,L) bernilai benar jika x adalah elemen dari list L

def IsMember(x,L):
	if(IsEmpty(L)):
		return False
	else:
		if(FirstElmt(L) == x):
			return True
		else:	
			return IsMember(x, Tail(L))

#DefSpek
#Rember: elemen, list --> list
#Rember(x,L) menghapus satu elemen x dari list

def Rember(x,L):
	if(IsMember(x,L)):
		if(IsEmpty(L)):
			return L
		elif(FirstElmt(L) == x):
			return Tail(L)
		else:
			return Konso(FirstElmt(L), Rember(x,Tail(L)))
	else:
		return L

#DefSpek
#MultiRember: elemen, list --> list
#MultiRember(x,L) menghapus setiap elemen x dari list

def MultiRember(x,L):
	if(IsMember(x,L)):
		if(IsEmpty(L)):
			return L
		elif(FirstElmt(L) == x):
			return MultiRember(x,Tail(L))
		else:
			return Konso(FirstElmt(L), MultiRember(x,Tail(L)))
	else:
		return L

#DefSpek
#Jmlh : list of integer --> integer
#Jmlh(L) menjumlahkan seluruh elemen list L

def Jmlh(L):
	if(IsEmpty(L)):
		return 0
	elif(IsOneElmt(L)):
		return FirstElmt(L)
	else:
		return FirstElmt(L) + Jmlh(Tail(L))

#DefSpek
#IsPalindrom : list of char --> boolean
#IsPalindrom(L) memeriksa apakah sebuah list of char merupakan kalimat palindrom

def IsEqual(L1,L2):
	return L1 == L2

def IsPalindrom(L):
	if(IsEmpty(L)):
		return True
	elif(IsEqual(L,Inverse(L))):
		return True
	else:
		return False

def IsPalindrom2(L):
	if IsEmpty(L) or IsOneElmt(L):
		return True
	elif FirstElmt(L)==LastElmt(L):
		return IsPalindrom2(Head(Tail(L)))
	else:
		return False

#Jumlah Prima

def faktor(n,count):
	if(n == count):
		return 1
	elif(n % count == 0):
		return 1 + faktor(n,count + 1)
	else:
		return faktor(n,count + 1)

#DefSpek
#Jmlh : list of integer --> integer
#Jmlh(L) menjumlahkan seluruh elemen list L

def IsPrima(n):
	if(faktor(n,1) == 2):
		return True
	else:
		return False
		
def JmlhPrime(L):
	if(IsEmpty(L)):
		return 0
	elif(IsPrima(FirstElmt(L))):
		return FirstElmt(L) + JmlhPrime(Tail(L))
	else:
		return JmlhPrime(Tail(L))
print(IsPalindrom(L3))


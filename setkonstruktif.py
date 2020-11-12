from list3 import *

#DefSpek
#MakeSet: list --> set
#MakeSet(L) membentuk sebuah set dari List (membuang setiap kemunculan yang lebih dari 1 kali)

def MakeSet(L):
    if IsEmpty(L):
        return L # Basis
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return MakeSet(Tail(L))
        else:
            return Konso(FirstElmt(L),MakeSet(Tail(L)))

#DefSpek
#IsSet: list --> boolean
#IsSet(L) bernilai True jika L adalah sebuah set

def IsSet(L):
    if IsEmpty(L):
        return True # List Kosong adalah Himpunan Kosong
    else:
        if IsMember(LastElmt(L),Head(L)):
            return False
        else:
            return IsSet(Head(L))

#DefSpek
#IsSubSet: 2 set --> Boolean
#IsSubSet(H1,H2) bernilai True jika semua elemen H1 adalah elemen H2

def IsSubSet(H1,H2):
    if IsEmpty(H1): # Basis
        return True
    else: # Analisa Kasus
        if not IsMember(LastElmt(H1),H2):
            return False
        else: # e anggota H2
            return IsSubSet(Head(H1),H2)

#DefSpek
#IsEQSet: 2 set --> Boolean
#IsEQSet(H1,H2) bernilai True jika elemen H1 sama dengan elemen H2

def IsEQSet(H1,H2):
    if IsSubSet(H1,H2) and IsSubSet(H2,H1):
        return True
    else:
        return False

#DefSpek
#IsIntersect: 2 set --> Boolean
#IsIntersect(H1,H2) bernilai True jika elemen H1 dan H2 interseksi

def IsIntersect(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return False
    elif not IsEmpty(H1) and IsEmpty(H2):
        return False
    elif IsEmpty(H1) and not IsEmpty(H2):
        return False
    elif IsMember(LastElmt(H1),H2):
        return True
    else:
        return IsIntersect(Head(H1),H2)

#DefSpek
#MakeIntersect: 2 set --> set
#MakeIntersect(H1,H2) membuat set interseksi H1 dan H2

def MakeIntersect(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),MakeIntersect(Tail(H1),H2))
        else:
            return MakeIntersect(Tail(H1),H2)

#DefSpek
#MakeUnion: 2 set --> set
#MakeUnion(H1,H2) membuat set union dari H1 dan H2

def MakeUnion(H1,H2):
    if(IsEmpty(H1) and IsEmpty(H2)):
        return []
    elif(not IsEmpty(H1) and IsEmpty(H2)):
        return H1
    elif(IsEmpty(H1) and not IsEmpty(H2)):
        return H2
    elif(not IsEmpty(H1) and not IsEmpty(H2)):
        if(IsMember(FirstElmt(H1),H2)):
            return MakeUnion(Tail(H1),H2)
        else:
            return Konso(FirstElmt(H1),MakeUnion(Tail(H1),H2))

#DefSpek
#MakeMinus: 2 set --> set
#MakeMinus(H1,H2) membuat set baru dimana anggota H1 yang bukan merupakan anggota H2

def MakeMinus(H1,H2):
    if IsEmpty(H1): 
        return []
    elif IsEmpty(H2):
        return H1
    elif IsMember(FirstElmt(H1),H2):
        return MakeMinus(Tail(H1),H2)
    else :
        return Konso(FirstElmt(H1),MakeMinus(Tail(H1),H2))

#DefSpek
#MakeKomplemen: 2 set --> set
#MakeKomplemen(H1,H2)   membuat set baru yang anggotanya adalah anggota semua anggota H1 dan H2
#                       tetapi bukan interseksi keduanya

def MakeKomplemen(H1,H2):
    return MakeMinus(H1,H2)+MakeMinus(H2,H1)



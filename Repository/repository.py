class RepositoryException(Exception):
    pass
class Repost:
    def __init__(self):
        self.__elems =[]

    def __len__(self):
        return len(self.__elems)
    def adaugarest(self ,st):
        if st in self.__elems:
            raise RepositoryException("element existent")
        self.__elems.append(st)
    """
    daca studentul e nou il adaugam in lista
    """

    def stergest(self ,key_student):
        if key_student not in self.__elems:
            raise RepositoryException("element inexistent\n")

        for i in range(0 ,len(self.__elems)):
            if self.__elems[i]==key_student:

                del self.__elems[i]

                return
    """
    daca id ul se gaseste in lista atunci se sterge studentul din lista
    """

    def updatest(self ,st):
        if st not in self.__elems:
            raise RepositoryException("element inexistent\n")
        for i in range(0 ,len(self.__elems)):
            if self.__elems[i ]==st:
                self.__elems[i ] =st
    """
    daca id ul se gaseste in lista se modifica studentul cu id ul dat
    """

    def searchst_1(self ,st):
        """
          se cauta elementul dupa id
          """
        if st not in self.__elems:
            raise RepositoryException("element inexistent\n")
        for i in range(0 ,len(self.__elems)):
            if self.__elems[i ]==st:
                return self.__elems[i]


    """
    COMPLEXITATE ---searchst_1:
    best case(daca studentul exista deja):T(n)=n                              ∈ O(n)-theta
    worst case(ultimul element): T(n)=n+suma de la (i=0) la (n-1) de 1=2*n    ∈ O(n)-theta
    caz mediu: T(n)=(n*n+1+...+n)/n=n+n*(n+1)/(2*n)=n+(n+1)/2                 ∈ O(n)-theta
    Complexitate 𝑂(𝑛)
    """
    def searchst_2(self ,st):
        ok=0
        for i in range(0, len(self.__elems)):
            if st.egal_nume(self.__elems[i])==True:
                ok=1
        if ok==0:
            raise RepositoryException("element inexistent\n")
        l=[]
        for i in range(0 ,len(self.__elems)):
            if st.egal_nume(self.__elems[i])==True:
                l.append(str(self.__elems[i]))
        return l[:]
    """
    se cauta elementele dupa nume
    """
    def searchst_3(self, st):
        ok = 0
        for i in range(0, len(self.__elems)):
            if st.egal_grup(self.__elems[i]) == True:
               ok = 1
        if ok == 0:
            raise RepositoryException("element inexistent\n")
        l = []
        for i in range(0, len(self.__elems)):
            if st.egal_grup(self.__elems[i]) == True:
                l.append(str(self.__elems[i]))
        return l[:]
    """
    se cauta elementele dupa grup
    """
    def find_nume(self,id):
        for el in self.__elems:
            if el.getstudentID()==id:
                return el.getnume()
    """
    returneaza numele unui student cu un id dat
    """
    def get_all(self):
        return self.__elems[:]
    def __str__(self):
        return str(self.get_all())

class Repopr:
    def __init__(self):
        self.__elems =[]

    def __len__(self):
        return len(self.__elems)

    def adaugarepr(self, pr):
        if pr in self.__elems:
            raise RepositoryException("element existent\n")
        self.__elems.append(pr)

    """
       daca problema e noua o adaugam in lista
       """

    def stergepr(self, key_prob,poz):
        if poz==-1:
            raise RepositoryException("element inexistent\n")
        if self.__elems[poz] == key_prob:
            del self.__elems[poz]
        else: return self.stergepr(key_prob,poz-1)
    #functie recursiva pt stergere problema
    """
    daca id ul se regaseste in lista atunci stergem problema cu id ul dat
    """

    """
    daca id ul se regaseste in lista atunci modificam problema cu id ul dat
    """
    def updatepr(self, pr,poz):
        if poz==-1:
            raise RepositoryException("element inexistent\n")
        if self.__elems[poz]==pr:
            self.__elems[poz]=pr
            return
        else: return self.updatepr(pr,poz-1)
    #functie recursiva pt update problema
    def searchpr_1(self, pr):

        if pr not in self.__elems:
            raise RepositoryException("element inexistent\n")
        for i in range(0, len(self.__elems)):
            if self.__elems[i] == pr:
                return self.__elems[i]
    """
    se cauta elementul dupa nrlab_nrprob
    
    """

    def searchpr_2(self, pr):
        ok=0
        for i in range(0, len(self.__elems)):
            if pr.egal_desc(self.__elems[i])==True:
                ok=1
        if ok==0:
            raise RepositoryException("element inexistent\n")
        l=[]
        for i in range(0 ,len(self.__elems)):
            if pr.egal_desc(self.__elems[i])==True:
                l.append(str(self.__elems[i]))
        return l[:]
    """
    se cauta elementele dupa descriere
    """
    def searchpr_3(self, pr):
        ok=0
        for i in range(0, len(self.__elems)):
            if pr.egal_deadline(self.__elems[i])==True:
                ok=1
        if ok==0:
            raise RepositoryException("element inexistent\n")
        l=[]
        for i in range(0 ,len(self.__elems)):
            if pr.egal_deadline(self.__elems[i])==True:
                l.append(str(self.__elems[i]))
        return l[:]
    """
    se cauta elementele dupa deadline
    """
    def get_all(self):
        return self.__elems[:]

    def get_items(self):
        return str(self.__elems[:])

    def __str__(self):
        return str(self.get_all())

class Repont:
    def __init__(self):
       self.__elems=[]
    def __len__(self):
        return len(self.__elems)

    def adaugarent(self, nt):
        if nt in self.__elems:
            raise RepositoryException("element existent\n")

        self.__elems.append(nt)
    """
    se adauga nota
    """

    def stergent(self, key_nota):
        if key_nota not in self.__elems:
            raise RepositoryException("element inexistent\n")

        for i in range(0, len(self.__elems)):
            if self.__elems[i] == key_nota:
                del self.__elems[i]
                return
    """
    daca id ul si nrlab_nrporb se regasesc in lista atuncis tergem elementul
    """
    def updatent(self, nt):
        if nt not in self.__elems:
            raise RepositoryException("element inexistent\n")
        for i in range(0, len(self.__elems)):
            if self.__elems[i] == nt:
                self.__elems[i] =nt
    """
    modificam o anumita nota
    """
    def searchnt(self, st):
        if st not in self.__elems:
            raise RepositoryException("element inexistent\n")
        for i in range(0, len(self.__elems)):
            if self.__elems[i] == st:
                return self.__elems[i]

    """
    cautam o nota dupa id student si nrlab_nrporb
    """
    def stergerent_st(self,st):
        i=0
        while i<len(self.get_all()):
            if self.__elems[i].getstudentID()==st.getstudentID():
                self.stergent(self.__elems[i])
            else: i=i+1
    """
    stergem notele studentului eliminat din lista
    """
    def stergerent_pr(self,pr):
        i=0
        while i<len(self.get_all()):
            if self.__elems[i].getnrlab_nrprob()==pr.getnrlab_nrprob():
                self.stergent(self.__elems[i])
            else: i=i+1
    """
    stergerm notele problemei eliminate din lista
    """

    def get_all(self):
        return self.__elems[:]

    def get_items(self):
        return str(self.__elems[:])

    def __str__(self):
        return str(self.get_all())

    def get_nrlabprob(self,nr):
        lista=[]
        for i in range(0, len(self.__elems)):
            if self.__elems[i].getnrlab_nrprob()==nr:
                lista.append(self.__elems[i])
        return lista[:]

    """
    returnam in lista toate notele de la un lab si o prob data
    """

    def get_idstud(self,id):
        lista=[]
        for i in range(0, len(self.__elems)):
            if self.__elems[i].getstudentID()==id:
                lista.append(self.__elems[i])
        return lista[:]
    """
    returnam in lista toate notele de la un id student dat
    """
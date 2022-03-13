from Domain.clsnota import Nota
from Domain.clsprobleme import Problema
from Domain.clsstudenti import Student
from Repository.repository import Repost, Repopr, Repont, RepositoryException


class Repost(Repost):
    def __init__(self,fileN):
        #Repost.__init__(self)
        self.__fName=fileN
    def __loadFromFile(self):
        """
          Load students from file
          raise CorruptedFileException if there is an error when reading from the file
        """
        try:
            f = open(self.__fName, "r")
        except IOError:
            #file not exist
            return
        line = f.readline().strip()
        rez = []
        while line!="":
            attrs = line.split(";")
            st = Student(attrs[0], attrs[1], attrs[2])
            rez.append(st)
            line = f.readline().strip()
        f.close()
        return rez

    def __storeToFile(self,sts):
        """
         Store all the students  in to the file
         raise CorruptedFileException if we can not store to the file
        """
        #open file (rewrite file)
        with open(self.__fName, "w") as f:
            for st in sts:
                strf = st.getstudentID()+";"+st.getnume()+";"+st.getgrup()+"\n"
                f.write(strf)

    #def adaugarest(self,st):
        #Repost.adaugarest(self,st)
        #self.__storeToFile(Repost.get_all())

    def adaugarest(self,st):
        """

        add student in the repository
        st - Student
        :raise RepositoryException if there is a student with the given id
        """
        all=self.__loadFromFile()
        if st in all:
            raise RepositoryException("element existent")
        all.append(st)
        self.__storeToFile(all)
    def updatest(self, st):
        """
          Update student in the repository
          st - Student, the updated student
          raise RepositoryException if there is no student with the given id
        """
        all = self.__loadFromFile()
        if st not in all:
            raise RepositoryException("element inexistent\n")
        all.remove(st)
        all.append(st)
        self.__storeToFile(all)


    def stergest(self, StudentKey):
        """
          remove a student from the repository
          id - string, the id of the student to be removed
          return student
          post: the repository not contains student with the given id
          raise ValueError if there is no student with the given id
        """
        all = self.__loadFromFile()

        if StudentKey not in all:
            raise RepositoryException("nota inexistenta")
        all.remove(StudentKey)
        self.__storeToFile(all)
        return StudentKey

    def searchst_1(self, studentkey):
        all = self.__loadFromFile()
        if studentkey not in all:
            raise RepositoryException("element inexistent\n")
        for st in all:
            if st == studentkey:
                return st

    def searchst_2(self, studentkey):
        all = self.__loadFromFile()
        ok=0
        for el in all:
            if el.getnume() == el.getnume():
                ok=1
        if ok==0:
            raise RepositoryException("element inexistent\n")
        l=[]
        for st in all:
            if st.getnume()==studentkey.getnume():
                l.append(st)
        return l[:]


    def searchst_3(self, studentkey):
        all = self.__loadFromFile()
        ok=0
        for el in all:
            if el.getgrup() == el.getgrup():
                ok=1
        if ok==0:
            raise RepositoryException("element inexistent\n")
        l=[]
        for st in all:
            if st.getgrup() == studentkey.getgrup():
                l.append(st)
        return l[:]
    def find_nume(self,id):
        all=self.__loadFromFile()
        for el in all:
            if el.getstudentID()==id:
                return el.getnume()
    def get_all(self):
        return self.__loadFromFile()

    def __len__(self):
        return len(self.__loadFromFile())
class Repopr(Repopr):
    def __init__(self,fileN):
        self.__fName=fileN
    def __loadFromFile(self):
        """
          Load students from file
          raise CorruptedFileException if there is an error when reading from the file
        """
        try:
            f = open(self.__fName, "r")
        except IOError:
            #file not exist
            return
        line = f.readline().strip()
        rez = []
        while line!="":
            attrs = line.split(";")
            st = Problema(attrs[0], attrs[1], attrs[2])
            rez.append(st)
            line = f.readline().strip()
        f.close()
        return rez

    def __storeToFile(self,prs):
        """
         Store all the problems  in to the file
         raise CorruptedFileException if we can not store to the file
        """
        #open file (rewrite file)
        with open(self.__fName, "w") as f:
            for pr in prs:
                strf = pr.getnrlab_nrprob()+";"+pr.getdescriere()+";"+pr.getdeadline()+"\n"
                f.write(strf)
    def adaugarepr(self,pr):
        """

        add problema in the repository
        pr - Problema
        :raise RepositoryException if there is a student with the given id
        """
        all=self.__loadFromFile()

        if pr in all:
            raise RepositoryException("element existenta")
        all.append(pr)
        self.__storeToFile(all)
    def updatepr(self, pr,poz):
        """
          Update problema in the repository
          pr - Problema
          raise RepositoryException if there is no problema with the given nrlab_nrprob
        """
        all = self.__loadFromFile()
        if poz==-1:
            raise RepositoryException("element inexistent\n")
        if all[poz]==pr:
            all[poz]=pr
        else: return self.updatepr(pr,poz-1)
        self.__storeToFile(all)
    #functie recursiva pentru update problema

    def stergepr(self, ProblemaKey,poz):
        """
          remove a student from the repository
          id - string, the id of the student to be removed
          return problema
          post: the repository not contains problema with the given nrlab_nrprob
          raise ValueError if there is no student with the given nrlab_nrprob
        """
        all = self.__loadFromFile()

        if poz==-1:
            raise RepositoryException("nota inexistenta")
        if all[poz]==ProblemaKey:
            del all[poz]
        else:
            return self.stergepr(ProblemaKey,poz-1)
        self.__storeToFile(all)
    # functie recursiva pentru stergere problema

    def searchpr_1(self, problemakey):
        all = self.__loadFromFile()
        if problemakey not in all:
            raise RepositoryException("element inexistent\n")
        for pr in all:
            if pr == problemakey:
                return pr
        return None
    """
    def searchpr_1(self, problemakey,poz):
        all = self.__loadFromFile()
        if poz==-1:
            raise RepositoryException("element inexistent\n")
        if all[poz] == problemakey:
            return problemakey
        return self.searchpr_1(problemakey,poz-1)
    """
    """
    functie de search problema recursiv
    """

    def searchpr_2(self, problemakey):
        all = self.__loadFromFile()
        ok=0
        for el in all:
            if el.getdescriere() == el.getdescriere():
                ok=1
        if ok==0:
            raise RepositoryException("element inexistent\n")
        l=[]
        for pr in all:
            if pr.getdescriere()==problemakey.getdescriere():
                l.append(pr)
        return l[:]

    def searchpr_3(self, problemakey):
        all = self.__loadFromFile()
        ok=0
        for el in all:
            if el.getdeadline() == el.getdeadline():
                ok=1
        if ok==0:
            raise RepositoryException("element inexistent\n")
        l=[]
        for pr in all:
            if pr.getdeadline() == problemakey.getdeadline:
                l.append(pr)
        return l[:]

    def get_all(self):
        return self.__loadFromFile()

    def __len__(self):
        return len(self.__loadFromFile())


class Repont(Repont):
    def __init__(self,fileN):
        self.__fname=fileN
    def __loadFromFile(self):
        """
        load grades from file
        se returneaza lista cu elementele din fisier
        """

        try:
            f=open(self.__fname,"r")
        except IOError:
            # file not exist
            return
        line=f.readline().strip()
        rez=[]

        while line != "":

            attrs = line.split(";")

            nt=Nota(attrs[0],attrs[1],attrs[2])
            rez.append(nt)
            line=f.readline().strip()
        f.close()
        return rez
    def __storeToFile(self,nts):
        """
        Store all the grades in the file
        """
        with open(self.__fname,"w") as f:
            for nt in nts:
                strf = nt.getstudentID()+";"+nt.getnrlab_nrprob()+";"+nt.getnota()+"\n"
                f.write(strf)
    def adaugarent(self, nt):
        all=self.__loadFromFile()
        if nt in all:
            raise RepositoryException("element existent\n")

        all.append(nt)
        self.__storeToFile(all)
    """
    se adauga nota in fisier
    """

    def stergent(self, key_nota):
        all=self.__loadFromFile()

        if key_nota  not in all:
            raise RepositoryException("nota inexistenta")
        all.remove(key_nota)
        self.__storeToFile(all)
        return key_nota

    """
    daca id ul si nrlab_nrporb se regasesc in fisier atunci stergem elementul
    """
    def updatent(self, nt):
        all=self.__loadFromFile()
        if nt not in all:
            raise RepositoryException("element inexistent\n")
        all.remove(nt)
        all.append(nt)
        self.__storeToFile(all)
    """
    modificam o anumita nota
    """
    def searchnt(self, ntkey):
        notes=self.__loadFromFile()
        if ntkey not in notes:
            raise RepositoryException("nota data nu exista")
        for nt in notes:
            if ntkey==nt:
                return nt


    """
    cautam o nota dupa id student si nrlab_nrporb
    """
    def stergerent_st(self,st):
        i=0
        all=self.__loadFromFile()
        while i<len(all):
            if all[i].getstudentID()==st.getstudentID():
                all.remove(all[i])
            else: i=i+1
        self.__storeToFile(all)
    """
    stergem notele studentului eliminat din fisier
    """

    def stergerent_pr(self,pr):
        i=0
        all=self.__loadFromFile()
        while i<len(all):
            if all[i].getnrlab_nrprob()==pr.getnrlab_nrprob():
                all.remove(all[i])
            else: i=i+1
        self.__storeToFile(all)
    """
    stergerm notele problemei eliminate din fisier
    """

    def get_all(self):
        return self.__loadFromFile()

    def get_items(self):
        return str(self.__loadFromFile())

    def __str__(self):
        return str(self.get_all())

    def get_nrlabprob(self,nr):
        lista=[]
        all=self.__loadFromFile()
        for i in range(0, len(all)):
            if all[i].getnrlab_nrprob()==nr:
                lista.append(all[i])
        return lista[:]
    """
    returnam in lista toate notele de la un lab si o prob data
    """
    def get_idstud(self,id):
        lista=[]
        all=self.__loadFromFile()
        for i in range(0, len(all)):
            if all[i].getstudentID()==id:
                lista.append(all[i])
        return lista[:]
    """
    returnam in lista toate notele de la un id student dat
    """
    def __len__(self):
        return len(self.__loadFromFile())
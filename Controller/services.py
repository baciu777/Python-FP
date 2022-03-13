from Domain.clsnota import Nota
from Domain.clsprobleme import Problema
from Domain.clsstudenti import Student


class Services_st():
    def __init__(self,repo,valid):
        self.__repo=repo
        self.__valid=valid

    def add_st(self,id_st,nume,grup):
        student=Student(id_st,nume,grup)

        self.__valid.valideaza_st(student)
        self.__repo.adaugarest(student)

    """
    se adauga in repository
    """
    def upd_st(self,id_st,nume,grup):
        student=Student(id_st,nume,grup)

        self.__valid.valideaza_st(student)
        self.__repo.updatest(student)

    """
    se modifica studentul din repository
    """
    def rem_st(self,id_st,nume,grup):
        student=Student(id_st,nume,grup)

        self.__valid.valideaza_st(student)
        self.__repo.stergest(student)

    """
    se sterge studentul din repository
    """
    def search_st_id(self,id_st,nume,grup):
        student=Student(id_st,nume,grup)

        self.__valid.valideaza_st(student)
        return self.__repo.searchst_1(student)
    """
    se cauta student dupa id
    """
    def search_st_nume(self,id_st,nume,grup):
        student=Student(id_st,nume,grup)
        self.__valid.valideaza_st(student)
        return self.__repo.searchst_2(student)
    """
    se cauta student dupa nume
    """
    def search_st_grup(self,id_st,nume,grup):
        student=Student(id_st,nume,grup)
        self.__valid.valideaza_st(student)
        return self.__repo.searchst_3(student)
    """
    se cauta studenti dupa grup
    """
    def get_no_st(self):
        return len(self.__repo)
    def get_st(self):
        return self.__repo.get_all()

class Services_pr():
    def __init__(self,repo,valid):
        self.__repo=repo
        self.__valid=valid

    def add_pr(self,nr,descriere,deadline):
        prob=Problema(nr,descriere,deadline)

        self.__valid.valideaza_pr(prob)
        self.__repo.adaugarepr(prob)
    """
    se adauga problema in repository
    """
    def upd_pr(self,nr,descriere,deadline):
        prob=Problema(nr,descriere,deadline)
        self.__valid.valideaza_pr(prob)
        self.__repo.updatepr(prob,self.get_no_pr()-1)
    """
    se modifica problema in repository
    """
    def rem_pr(self,nr,descriere,deadline):
        prob=Problema(nr,descriere,deadline)

        self.__valid.valideaza_pr(prob)
        self.__repo.stergepr(prob,self.get_no_pr()-1)
    """
    se sterge problema din repository
    """
    def search_pr_id(self,nr,descriere,deadline):
        prob=Problema(nr,descriere,deadline)
        self.__valid.valideaza_pr(prob)
        return self.__repo.searchpr_1(prob)
    """
    se cauta problema dupa nrlab_nrprob
    """
    def search_pr_nume(self,nr,descriere,deadline):
        prob=Problema(nr,descriere,deadline)
        self.__valid.valideaza_pr(prob)
        return self.__repo.searchpr_2(prob)
    """
    se cauta probleme dupa descriere
    """
    def search_pr_deadline(self,nr,descriere,deadline):
        prob=Problema(nr,descriere,deadline)
        self.__valid.valideaza_pr(prob)
        return self.__repo.searchpr_3(prob)
    """
    se cauta probleme dupa deadline
    """
    def get_no_pr(self):
        return len(self.__repo)
    def get_pr(self):
        return self.__repo.get_all()

class Services_nt():
    def __init__(self,repo,repost,repopr,valid):
        self.__repo=repo
        self.__repost=repost
        self.__repopr=repopr
        self.__valid=valid

    def add_nt(self,id,nr,nota):
        nota=Nota(id,nr,nota)
        student=Student(id,None,None)
        problema=Problema(nr,None,None)
        self.__repost.searchst_1(student)
        self.__repopr.searchpr_1(problema)
        self.__valid.valideaza_nt(nota)
        self.__repo.adaugarent(nota)
    """
    se adauga nota in repository daca exista studentul si problema
    """
    def upd_nt(self,id,nr,nota):
        nota=Nota(id,nr,nota)
        self.__valid.valideaza_nt(nota)
        self.__repo.updatent(nota)

    """
    se modifica nota in repository
    """
    def rem_nt(self,id,nr,nota):
        nota=Nota(id,nr,nota)
        self.__valid.valideaza_nt(nota)
        self.__repo.stergent(nota)

    """
    se sterge nota din repository
    """
    def rem_nt_st(self,id):
        nt=Nota(id,None,None)
        return self.__repo.stergerent_st(nt)
    """
    stergem note daca studentul nu mai e in lista
    return
    """
    def rem_nt_pr(self,nr):
        nt=Nota(None,nr,None)
        return self.__repo.stergerent_pr(nt)
    """
    stergem note daca problema nu mai e in lista
    return
    """
    def search_nt(self,id,nr,nt):
        nota=Nota(id,nr,nt)
        self.__valid.valideaza_nt(nota)
        return self.__repo.searchnt(nota)
    """
    se cauta nota in repository
    """
    def __keyp(self,o):
        return self.__repost.find_nume(o.getstudentID())
    def get_st_alfabetic(self,nr):
        problema=Problema(nr,"descriere","10/10/10")
        self.__repopr.searchpr_1(problema)
        toate=self.__repo.get_nrlabprob(nr)
        tot=self.__sort3(toate,self.__keyp,key2=lambda toate:toate.getnota())
        return tot
    """
    returam sirul de studenti care au note la o problema(sortat alfabetic:nume studenti)
    """
    def get_st_nota(self,nr):
        problema = Problema(nr, "descriere", "10/10/10")
        self.__repopr.searchpr_1(problema)
        toate = self.__repo.get_nrlabprob(nr)
        sir=self.__sort2(toate,key=lambda note:note.getnota())
        return sir
    """
    returam sirul de studenti care au note la o problema(sortat dupa note)
    """

    def get_st_sub5(self):
        note=self.__repo.get_all()
        studenti_unici=[]
        for el in note:
            studentID=el.getstudentID()
            if studentID not in studenti_unici:
                studenti_unici.append(studentID)
        medii = []
        for id in studenti_unici:
            toate=self.__repo.get_idstud(id)
            s=0
            for el in toate:
                nota=float(el.getnota())
                s=s+nota
            cate_note_are_studentul=len(toate)
            s=s/cate_note_are_studentul

            if s<5:
                id_medie=[id,s]
                medii.append(id_medie)
        return medii
    """
    formam o lista cu studentii care au note si le facem media, daca au media mai mica decat 5
    ii returnam intr o lista
    """
    def get_rap_note_gr(self):
        toate=self.__repo.get_all()
        dict= {}
        lista=[]
        for el in toate:
            if float(el.getnota())<7:
                studentkey=Student(el.getstudentID(),"nume","1")
                student = self.__repost.searchst_1(studentkey)
                dict[int(student.getgrup())]=0
        for el in toate:
            if float(el.getnota())<7:
                studentkey=Student(el.getstudentID(),"nume","1")
                student = self.__repost.searchst_1(studentkey)
                dict[int(student.getgrup())]=dict[int(student.getgrup())]+1
        dictlist=[]#schimbam din lista in dictionar
        for key, value in dict.items():
            temp = [key, value]
            dictlist.append(temp)
        rez=self.__sort1(dictlist,key=lambda dictlist:dictlist[1],reverse=True)
        return rez
    def get_no_nt(self):
        return len(self.__repo)
    def get_nt(self):
        return self.__repo.get_all()

    def __sort1(self,toate,key=lambda x:x,reverse=False):
        """
        selection sort
        """
        if reverse==False:
            for i in range(0,len(toate)-1):
                ind=i
                for j in range(i+1,len(toate)):
                    if key(toate[j])<key(toate[ind]):
                        ind =j
                if i<ind:
                    toate[i],toate[ind]=toate[ind],toate[i]
        else:
            for i in range(0,len(toate)-1):
                ind=i
                for j in range(i+1,len(toate)):
                    if key(toate[j])>key(toate[ind]):
                        ind =j
                if i<ind:
                    toate[i],toate[ind]=toate[ind],toate[i]
        return toate

    def __sort2(self,a,key=lambda x:x,reverse=False):
        """
        shake sort- un fel de spirala
        prima parcurgere e de la inceput la coada
        a doua de la coada la icneput
        """
        n = len(a)
        swapped = True
        start = 0
        end = n - 1
        while (swapped == True and reverse==False):
            swapped = False
            for i in range(start, end):
                if (key(a[i]) > key(a[i + 1])):
                    a[i], a[i + 1] = a[i + 1], a[i]
                    swapped = True
            if (swapped == False):
                break
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if (key(a[i]) > key(a[i + 1])):
                    a[i], a[i + 1] = a[i + 1], a[i]
                    swapped = True
            start = start + 1

        while (swapped == True and reverse==True):
            swapped = False
            for i in range(start, end):
                if (key(a[i]) < key(a[i + 1])):
                    a[i], a[i + 1] = a[i + 1], a[i]
                    swapped = True
            if (swapped == False):
                break
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if (key(a[i]) < key(a[i + 1])):
                    a[i], a[i + 1] = a[i + 1], a[i]
                    swapped = True
            start = start + 1
        return a


    def __sort3(self,toate,key1=lambda x:x,key2=lambda x:x,reverse=False):
        """
        selection sort
        """
        if reverse==False:
            for i in range(0,len(toate)-1):
                ind=i
                for j in range(i+1,len(toate)):
                    if key1(toate[j])<key1(toate[ind]):
                        ind =j
                if i<ind:
                    toate[i],toate[ind]=toate[ind],toate[i]
            for i in range(0,len(toate)-1):
                ind=i
                for j in range(i+1,len(toate)):
                    if key1(toate[j])==key1(toate[ind]) and key2(toate[j])<key2(toate[ind]) :
                        ind =j
                if i<ind:
                    toate[i],toate[ind]=toate[ind],toate[i]
        else:
            for i in range(0,len(toate)-1):
                ind=i
                for j in range(i+1,len(toate)):
                    if key1(toate[j])>key1(toate[ind]):
                        ind =j
                if i<ind:
                    toate[i],toate[ind]=toate[ind],toate[i]

            for i in range(0,len(toate)-1):
                ind=i
                for j in range(i+1,len(toate)):
                    if key1(toate[j])==key1(toate[ind]) and key2(toate[j])>key2(toate[ind]):
                        ind =j
                if i<ind:
                    toate[i],toate[ind]=toate[ind],toate[i]
        return toate








from random import randint

from Controller.valid import ValidatorException
from Repository.repository import RepositoryException


class UI():

    def __ui_add_st(self):
        id = (input("da id "))
        nume = input("da nume ")
        grup = (input("da grup "))
        try:
            self.__service_st.add_st(id,nume,grup)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
        """ 
        daca datele sunt valide adaugam student
        """
    def __ui_add_pr(self):
        id = (input("da nr "))
        descriere = input("da descriere ")
        deadline = (input("da deadline "))
        try:
            self.__service_pr.add_pr(id,descriere,deadline)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
        """
        daca datele sunt valide se adauga problema
        """
    def __ui_add_nt(self):
        id = (input("da id student "))
        nr = input("da nr lab_prob ")
        nota = (input("da nota "))
        try:
            self.__service_nt.add_nt(id,nr,nota)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    def __ui_upd_st(self):
        id = (input("da id "))
        nume = input("da nume ")
        grup = (input("da grup "))
        try:
            self.__service_st.upd_st(id,nume,grup)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
        """
        daca datele sunt valide se modifica un student
        """
    def __ui_upd_pr(self):
        id = (input("da nr "))
        descriere = input("da descriere ")
        deadline = (input("da deadline "))
        try:
            self.__service_pr.upd_pr(id,descriere,deadline)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
        """
        daca datele sunt valide se modifica o problema
        """

    def __ui_upd_nt(self):
        id = (input("da id student "))
        nr = input("da nr lab_prob ")
        nota = (input("da nota "))
        try:
            self.__service_nt.upd_nt(id,nr,nota)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    def __ui_rem_st(self):
        id = (input("da id "))
        nume = "nume"
        grup = "2"
        try:
            self.__service_st.rem_st(id,nume,grup)
            try:self.__service_nt.rem_nt_st(id)
            except ValueError:
                pass
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
        """
        daca datele sunt valide se sterge un student
        """
    def __ui_rem_pr(self):
        id = (input("da nr "))
        descriere = "descriere"
        deadline = "10/10/10"
        try:
            self.__service_pr.rem_pr(id,descriere,deadline)
            try:self.__service_nt.rem_nt_pr(id)
            except ValueError:
                pass
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
        """
        daca datele sunt valide se sterge o problema
        """
    def __ui_rem_nt(self):
        id = (input("da id student "))
        nr = input("da nr lab_prob ")
        nota = "10"
        try:
            self.__service_nt.rem_nt(id,nr,nota)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    def __ui_search_st_1(self):
        id = (input("da id "))
        nume = "nume"
        grup = "2"
        try:
            self.__service_st.search_st_id(id,nume,grup)
            print("student: ",self.__service_st.search_st_id(id,nume,grup))
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))

    """
        se afiseaza studentul cu id ul dat
        """
    def __ui_search_pr_1(self):
        id = (input("da nr "))
        descriere = "descriere"
        deadline = "10/10/10"
        try:
            self.__service_pr.search_pr_id(id,descriere,deadline)
            print("problema: ",self.__service_pr.search_pr_id(id,descriere,deadline))
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    """
    se afiseaza problema cu nrlab_nrprob dat
    """
    def __ui_search_nt(self):
        id = (input("da id student "))
        nr = input("da nr lab_prob ")
        nota = "10"
        try:
            self.__service_nt.search_nt(id,nr,nota)
            print("student: ",self.__service_nt.search_nt(id,nr,nota))
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    """
    se afiseaza studentul si nota dupa un id si nrlab_nrprob date
    """
    def __ui_search_st_2(self):
        id = "2"
        nume = input("da nume")
        grup = "2"
        try:
            self.__service_st.search_st_nume(id,nume,grup)
            lista=self.__service_st.search_st_nume(id,nume,grup)
            for el in lista:
                print("student: ",el)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    """
    se afiseaza studentii dupa un nume dat
    """
    def __ui_search_pr_2(self):
        id = "5_5"
        descriere = input("da descriere")
        deadline = "10/10/10"
        try:
            self.__service_pr.search_pr_nume(id,descriere,deadline)
            lista=self.__service_pr.search_pr_nume(id,descriere,deadline)
            for el in lista:
                print("problema: ",el)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    """
    se afiseaza problemele dupa o descriere data
    """
    def __ui_search_st_3(self):
        id = "2"
        nume = "nume"
        grup = input("da grupa")
        try:
            self.__service_st.search_st_grup(id,nume,grup)
            lista=self.__service_st.search_st_grup(id,nume,grup)
            for el in lista:
                print("student: ",el)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    """
    se afiseaza stundetii dupa o grupa data
    """
    def __ui_search_pr_3(self):
        id = "5_5"
        descriere = "desc"
        deadline = input("da deadline ")
        try:
            self.__service_pr.search_pr_deadline(id,descriere,deadline)
            lista=self.__service_pr.search_pr_deadline(id,descriere,deadline)
            for el in lista:
                print("problema: ",el)
        except ValidatorException as ve:
            print(str(ve))
        except RepositoryException as ve:
            print(str(ve))
    """
    se afiseaza problemele dupa deadline dat
    """
    def __afisare_st(self):
        stud=self.__service_st.get_st()
        if len(stud):
            for el in stud:
                print("student: ",el)
        else:
            print("nu sunt studenti")
        """
        st-service de stundenti
        se afiseaza lsita de studenti
        """
    def __afisare_pr(self):
        pr=self.__service_pr.get_pr()
        if len(pr):
            for el in pr:
                print("problema: ",el)
        else:
            print("nu sunt probleme,life is good")
        """
        pr-service de probleme
        se afiseaza lsita de sprobleme
        """
    def __afisare_nt(self):
        nt=self.__service_nt.get_nt()
        if len(nt):
            for el in nt:
                student=self.__service_st.search_st_id(el.getstudentID(),"nume","1")
                problema=self.__service_pr.search_pr_id(el.getnrlab_nrprob(),"greu","10/10/10")
                nr=problema.getnrlab_nrprob().split("_")
                print("student: ",student.getnume(),"numar lab",nr[0],"numar problema",nr[1],"nota: ",el.getnota())

        else:
            print("nu sunt note")
    """
    nt-service de note
    se afiseaza lista de note
    """
    def __afisare_meniu(self):
        for i in self.__meniu:
            print(self.__meniu[i][1])


    def __gen_randomst(self):
        contor=int(input("da cati studenti vrei"))
        listaChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i=1
        while i<=contor:
            id=str(randint(1,100))
            r1=randint(1,30)
            nume=listaChar[r1:r1+5]
            grup=str(randint(1,100))
            try:
                self.__service_st.add_st(id,nume,grup)
                i=i+1
            except:continue
    def __gen_randompr(self):
        contor = int(input("da cati probleme vrei"))
        listaChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 1
        while i <= contor:
            nr=str(randint(1,100))+"_"+str(randint(1,100))
            r1 = randint(1, 30)
            descriere=listaChar[r1:r1+10]
            deadline= str(randint(1,28))+"/"+str(randint(1,12))+"/"+str(randint(10,20))
            try:
                self.__service_pr.add_pr(nr,descriere,deadline)
                i=i+1
            except: continue
    def __ui_get_st_alfabetic(self):
        nr=input("da lab_pr")
        try:
            lista = self.__service_nt.get_st_alfabetic(nr)
            if len(lista)==0:
                print("nu sunt note")
            else:
                for el in lista:
                    student = self.__service_st.search_st_id(el.getstudentID(), "nume", "1")
                    print("student: ", student.getnume(), "nota: ", el.getnota())
        except RepositoryException as ve:
            print(str(ve))
    """
    se da o problema si un lab dat
    se afiseaza toti studentii dupa nume si nota in ordinea dupa note
    """
    def __ui_get_st_note(self):
        nr = input("da lab_pr")
        try:
            lista = self.__service_nt.get_st_nota(nr)
            if len(lista)==0:
                print("nu sunt note")
            else:
                for el in lista:
                    student = self.__service_st.search_st_id(el.getstudentID(), "nume", "1")
                    print("student: ", student.getnume(), "nota: ", el.getnota())
        except RepositoryException as ve:
            print(str(ve))
    """
    se da o problema si un lab dat
    se afiseaza toti studentii dupa nume si nota in ordine alfabetica
    """
    def __ui_get_st_restanta(self):
        try:
            lista=self.__service_nt.get_st_sub5()
            if len(lista)==0:
                print("nu sunt medii")
            else:
                for el in lista:
                    studentID=el[0]
                    student = self.__service_st.search_st_id(studentID, "nume", "1")
                    medie=el[1]
                    print("student: ", student.getnume(), "nota: ", medie)
        except RepositoryException as ve:
            print(str(ve))
    """
    afisam toti studentii dupa nume si medie daca au media mai mica decat 5
    """
    def __ui_get_gr_note(self):
        try:
            lista=self.__service_nt.get_rap_note_gr()
            if len(lista)==0:
                print("nu sunt grupe cu note mai mici decat 7")
            else:
                for el in lista:
                    print("grupa",el[0],"numar note:",el[1])
        except RepositoryException as ve:
            print(str(ve))

    def __init__(self,service_st,service_pr,service_nt):
        self.__service_st=service_st
        self.__service_pr=service_pr
        self.__service_nt=service_nt
        self.__meniu={}

        self.__meniu["0"]=[self.__afisare_st,"0 Afisare Studenti"]
        self.__meniu["1"] = [self.__ui_add_st, "1 Adauga Student"]
        self.__meniu["2"]=[self.__ui_upd_st, "2 Modifica Student"]
        self.__meniu["3"] = [self.__ui_rem_st, "3 Sterge Student"]
        self.__meniu["4"] = [self.__ui_search_st_1, "4 Cauta student dupa id"]
        self.__meniu["5"] = [self.__ui_search_st_2, "5 Cauta student dupa nume"]
        self.__meniu["6"] = [self.__ui_search_st_3, "6 Cauta student dupa grup"]
        self.__meniu["10"] = [self.__afisare_pr, "10 Afisare Probleme"]
        self.__meniu["11"] = [self.__ui_add_pr, "11 Adaugare Problema"]
        self.__meniu["12"] = [self.__ui_upd_pr, "12 Modifica Problema"]
        self.__meniu["13"] = [self.__ui_rem_pr, "13 Sterge Problema "]
        self.__meniu["14"] = [self.__ui_search_pr_1, "14 Cauta problema dupa lab_nr "]
        self.__meniu["15"] = [self.__ui_search_pr_2, "15 Cauta problema dupa descriere"]
        self.__meniu["16"] = [self.__ui_search_pr_3, "16 Cauta problema dupa deadline"]
        self.__meniu["20"] = [self.__afisare_nt, "20 Afiseaza note"]
        self.__meniu["21"] = [self.__ui_add_nt, "21 Adauga note studenti"]
        self.__meniu["22"] = [self.__ui_upd_nt, "22 Modifica note studenti"]
        self.__meniu["23"] = [self.__ui_rem_nt, "23 Sterge note studenti"]
        self.__meniu["31"] = [self.__gen_randomst,"31 genereaza random studenti"]
        self.__meniu["32"] = [self.__gen_randompr,"32 genereaza random probleme"]
        self.__meniu["33"] = [self.__ui_get_st_alfabetic,"33 Lista de studenti si notele lor la o prob data ord alfabetic,si dupa note"]
        self.__meniu["34"] = [self.__ui_get_st_note, "34 Lista de studenti si notele lor la o prob data ord dupa note"]
        self.__meniu["35"] = [self.__ui_get_st_restanta,"35 Studentii care au media mai mica decat 5:("]
        self.__meniu["36"]=[self.__ui_get_gr_note,"36 Afisam grupele dupa numarul de note mai mici decat 7"]

    def run(self):
        while True:
            print("-----------------------------------------------------")
            self.__afisare_meniu()

            cmd=input("comanda:")

            if cmd=='x': break;

            try:
                fct=self.__meniu[cmd][0]
                if int(cmd)<40 and int(cmd)>=0:
                    fct()

            except KeyError:
                print("Comanda gresita")
    """
    se ruleaza programul pana la intalnirea literei x
    se afiseaza meniul si se apeleaza functia dorita
    """
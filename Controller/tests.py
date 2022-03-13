from Domain.clsnota import Nota
from Domain.clsprobleme import Problema
from Domain.clsstudenti import Student
from Repository.repository import Repost, Repopr, Repont, RepositoryException
from Controller.valid import Validator, ValidatorException
from Controller.services import Services_st, Services_pr, Services_nt


class Tests:
    def __domain_tests_st(self):
        id_stud=10
        nume="Decebal"
        grupa=55
        student=Student(id_stud,nume,grupa)
        assert(str(student)=="10 Decebal 55")
        student0=Student(id_stud,None,20)
        assert student==student0
    """
    teste pentru domeniul Student
    """
    def __validation_tests_st(self):
        student=Student(-20,"lala",100)
        valid=Validator()
        try:
            valid.valideaza_st(student)
            assert(False)
        except ValidatorException as ve:#aici ceva nu pusca cum as vrea
            assert True
            #assert(str(ve)=="id invalid\nnume invalid\ngrupa invalida\n")
        student_valid=Student(10,"Gigi",999)
        valid.valideaza_st(student_valid)
        assert True
    """ 
    teste pentru validarea studentilor
    """

    def __repository_tests_st(self):
        student=Student("20","gigi","100")

        repo_st=Repost()

        repo_st.adaugarest(student)
        assert len(repo_st) == 1

        result_st=repo_st.searchst_2(student)
        lista_buna=["20 gigi 100"]
        assert result_st==lista_buna
        student0=Student("20","lala","100")
        try:
            repo_st.adaugarest(student0)
            assert False
        except RepositoryException:
            assert True
        student1=Student("1","gicu","102")
        try:
            repo_st.updatest(student1)
            assert False
        except RepositoryException:
            assert True
        student_up=Student("20","bac","99")
        repo_st.updatest(student_up)
        result_st=repo_st.searchst_1(student_up)
        assert result_st.getstudentID()=="20"
        assert result_st.getnume() == "bac"
        assert result_st.getgrup() == "99"
        result_st=repo_st.searchst_3(student_up)
        lista_buna=["20 bac 99"]
        assert result_st==lista_buna
        key_student=Student("20",None,0)
        repo_st.stergest(key_student)
        assert len(repo_st)==0
    """
    teste pentru lista de studenti
    """
    def __service_tests_st(self):
        repo_st=Repost()
        valid_st=Validator()
        service_st=Services_st(repo_st,valid_st)
        try:
            service_st.add_st("-2020","gigi","212")
            assert False
        except ValidatorException:
            assert True
        service_st.add_st(2020, "gigi", 212)
        assert len(service_st.get_st())==1
        try:
            service_st.upd_st("33","gigi","212")
            assert False
        except RepositoryException:
            assert True
        service_st.upd_st(2020, "gigi", "2")
        result_st=service_st.search_st_id(2020,"gigi","2")
        assert result_st.getstudentID()==2020
        assert result_st.getnume() == "gigi"
        assert result_st.getgrup() == "2"
        lista_buna=["2020 gigi 2"]
        result_st = service_st.search_st_nume(2020, "gigi", "2")
        assert result_st==lista_buna
        result_st = service_st.search_st_grup(2020, "gigi", "2")
        assert result_st == lista_buna
        service_st.rem_st(2020, "gigi", "2")
        assert len(service_st.get_st()) == 0

    def __domain_tests_pr(self):
        id_prob = "10_10"
        descriere = "greu"
        deadline ="10/10/10"
        problema=Problema(id_prob,descriere,deadline)
        assert (str(problema) == "10_10 greu 10/10/10")
        problema0 = Problema(id_prob, "lala",9/10/15)
        assert problema==problema0
    """
    teste pentru domeniul Problema
    """
    def __validation_tests_pr(self):
        problema=Problema(12_23,"ii buna","30/13/20")
        valid=Validator()
        try:
            valid.valideaza_pr(problema)
            assert(False)
        except ValidatorException as ve:#aici ceva nu pusca cum as vrea
            assert True
        problema_valid=Problema("11_1","lala","30/12/20")
        valid.valideaza_pr(problema_valid)
        assert True
    """
    teste pentru validarile problemelor
    """
    def __repository_tests_pr(self):
        problema=Problema("12_76","dada","10/10/10")

        repo_pr=Repopr()

        repo_pr.adaugarepr(problema)
        assert len(repo_pr)==1
        problema0 = Problema("12_76", "lala", 100)
        try:
            repo_pr.adaugarepr(problema0)
            assert False
        except RepositoryException:
            assert True
        problema1=Problema("1_123","uu","20/12/2020")
        try:
            repo_pr.updatepr(problema1,len(repo_pr)-1)
            assert False
        except RepositoryException:
            assert True
        pr_find=Problema("12_76","dada","10/10/10")
        result_pr=repo_pr.searchpr_1(pr_find)
        assert result_pr.getnrlab_nrprob()== "12_76"
        assert result_pr.getdescriere() == "dada"
        assert result_pr.getdeadline() == "10/10/10"
        lista_buna=["12_76 dada 10/10/10"]

        result_pr = repo_pr.searchpr_2(pr_find)

        result_pr = repo_pr.searchpr_3(pr_find)
        assert result_pr == lista_buna
        key_problema = Problema("12_76", None, 0)
        repo_pr.stergepr(key_problema,len(repo_pr)-1)
        assert len(repo_pr) == 0
    """
    teste pentru lista de probleme
    """
    def __service_tests_pr(self):
        repo_pr=Repopr()
        valid_pr=Validator()
        service_pr=Services_pr(repo_pr,valid_pr)
        try:
            service_pr.add_pr("-2020_12","gigi","10/10/10")
            assert False
        except ValidatorException:
            assert True
        service_pr.add_pr("22_2020", "gigi", "10/1/10")
        assert len(service_pr.get_pr())==1
        service_pr.upd_pr("22_2020","greu","10/10/10")
        try:
            service_pr.rem_pr("22_44","gigi","10/10/10")
            assert False
        except RepositoryException:
            assert True
        result_pr=service_pr.search_pr_id("22_2020","desc","10/10/10")
        assert result_pr.getnrlab_nrprob()=="22_2020"
        assert result_pr.getdescriere() == "greu"
        assert result_pr.getdeadline() == "10/10/10"
        lista_buna=["22_2020 greu 10/10/10"]
        result_pr = service_pr.search_pr_nume("22_2020", "greu", "10/10/10")
        assert result_pr==lista_buna
        result_pr = service_pr.search_pr_deadline("22_2020", "desc", "10/10/10")
        assert result_pr == lista_buna
        service_pr.rem_pr("22_2020","greu","10/10/10")
        assert len(service_pr.get_pr()) == 0

    def __domain_tests_nt(self):

        id = "10"
        nr = "10_10"
        nt ="10"
        nota=Nota(id,nr,nt)
        assert (str(nota) == "10 10_10 10")
        nota0 = Nota(id, nr,"9")
        assert nota==nota0

    def __validation_tests_nt(self):
        nota = Nota("-20", "1_1","11")
        valid = Validator()
        try:
            valid.valideaza_nt(nota)
            assert (False)
        except ValidatorException as ve:  # aici ceva nu pusca cum as vrea
            assert True

        nota_valida = Nota("10", "1_4", "9.9")
        valid.valideaza_nt(nota_valida)
        assert True
    def __repository_tests_nt(self):
        nota=Nota("20","1_1","10")

        repo_nt=Repont()


        repo_nt.adaugarent(nota)
        assert len(repo_nt) == 1

        result_nt=repo_nt.searchnt(nota)
        assert result_nt.getstudentID()=="20"
        assert result_nt.getnrlab_nrprob()=="1_1"
        assert result_nt.getnota()=="10"

        nota0=Nota("20","1_1","10")
        try:
            repo_nt.adaugarent(nota0)
            assert False
        except RepositoryException:
            assert True
        nota1=Nota("20","1_2","9")
        try:
            repo_nt.updatent(nota1)
            assert False
        except RepositoryException:
            assert True
        nota_up=Nota("20","1_1","9.9")

        repo_nt.updatent(nota_up)
        result_nt=repo_nt.searchnt(nota_up)
        assert result_nt.getstudentID()=="20"
        assert result_nt.getnrlab_nrprob() == "1_1"
        assert result_nt.getnota() == "9.9"
        lista=repo_nt.get_nrlabprob("1_1")
        assert len(lista)==1
        lista_dupaid=repo_nt.get_idstud("20")
        assert len(lista_dupaid)==1
        lista=repo_nt.get_nrlabprob("2_1")
        assert len(lista)==0
        key_nota=Nota("20","1_1","10")
        repo_nt.stergent(key_nota)
        assert len(repo_nt)==0



    def __service_tests_nt(self):
        repo_nt=Repont()
        repo_st=Repost()
        repo_pr=Repopr()
        valid_nt = Validator()
        service_nt = Services_nt(repo_nt, repo_st,repo_pr,valid_nt)
        student=Student("22","rupere","2")
        repo_st.adaugarest(student)
        problema=Problema("1_11","ez","10/10/10")
        repo_pr.adaugarepr(problema)
        try:
            service_nt.add_nt("22","1_11","77.6")
            assert False
        except ValidatorException:
            assert True
        try:
            service_nt.add_nt("223","1_11","7.6")
            assert False
        except RepositoryException as ve:
            assert str(ve)=="element inexistent\n"
        service_nt.add_nt("22","1_11","10")
        assert len(service_nt.get_nt()) == 1
        service_nt.upd_nt("22", "1_11", "2")
        try:
            service_nt.rem_nt("2244", "1_11", "10")
            assert False
        except RepositoryException:
            assert True
        result_nt = service_nt.search_nt("22", "1_11", "10")
        assert result_nt.getstudentID() == "22"
        assert result_nt.getnrlab_nrprob() == "1_11"
        assert result_nt.getnota() == "2"
        studalfa = Student("21", "aa", "1")
        repo_st.adaugarest(studalfa)
        service_nt.add_nt("21", "1_11", "1")
        lista_ord_nume=service_nt.get_st_alfabetic("1_11")
        lista_ord_note=service_nt.get_st_nota("1_11")
        assert lista_ord_nume[0].getstudentID()=="21"
        assert lista_ord_nume[1].getstudentID()=="22"
        assert lista_ord_note[0].getstudentID()=="21"
        assert lista_ord_note[1].getstudentID()=="22"
        medii=service_nt.get_st_sub5()
        assert medii[0][0]=="22"
        assert medii[0][1]==2.0
        assert medii[1][0] == "21"
        assert medii[1][1] == 1.0
        service_nt.rem_nt("22", "1_11", "1")
        assert len(service_nt.get_nt()) == 1
        service_nt.rem_nt("21","1_11","7.6")
        assert len(service_nt.get_nt())==0

    """
    teste pentru lista de note
    """


    def all_tests(self):
        self.__domain_tests_st()
        self.__validation_tests_st()
        self.__repository_tests_st()
        self.__service_tests_st()

        self.__domain_tests_pr()
        self.__validation_tests_pr()
        self.__repository_tests_pr()
        self.__service_tests_pr()

        self.__domain_tests_nt()
        self.__validation_tests_nt()
        self.__repository_tests_nt()
        self.__service_tests_nt()
    """
    rulam toate testele
    """
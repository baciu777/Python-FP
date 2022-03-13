import unittest

from Controller.services import Services_st, Services_pr, Services_nt
from Controller.valid import Validator, ValidatorException
from Domain.clsnota import Nota
from Domain.clsprobleme import Problema
from Domain.clsstudenti import Student
from Repository.repositoryfile import Repost, RepositoryException,Repopr,Repont


class TestCaseStudentService(unittest.TestCase):
    def setUp(self):
        #code executed before every testMethod
        open("sttest.txt").close()
        valid=Validator()
        repo=Repost("sttest.txt")
        self.__serv =Services_st(repo,valid)
        self.__serv.add_st("1","Ion","2")
    def tearDown(self):
        #cleanup code executed after every testMethod
        unittest.TestCase.tearDown(self)
        open("sttest.txt","w").close()


    def testAdaugare(self):
        self.assertTrue(self.__serv.get_no_st(),1)
        self.assertRaises(ValidatorException,self.__serv.add_st,"1","lala","-2")
        self.assertRaises(ValidatorException, self.__serv.add_st, "1", "", "2")
        self.assertRaises(ValidatorException, self.__serv.add_st, "1-", "lala", "-2")
        self.assertRaises(RepositoryException,self.__serv.add_st,"1","1","1")
    def testModificare(self):
        self.assertTrue(self.__serv.get_no_st(),1)
        self.assertRaises(ValidatorException,self.__serv.upd_st,"1","","4")
        self.assertRaises(RepositoryException,self.__serv.upd_st,"2","eh","6")
        self.__serv.upd_st("1","papa","100")
        self.assertTrue(self.__serv.search_st_id("1","None","5"),Student("1"," papa" ,"100"))
    def testStergere(self):
        self.assertTrue(self.__serv.get_no_st(), 1)
        self.assertRaises(ValidatorException, self.__serv.rem_st, "1", "", "4")
        self.assertRaises(RepositoryException, self.__serv.rem_st, "2", "eh", "6")
        self.__serv.rem_st("1", "papa", "100")
        self.assertTrue(self.__serv.get_no_st() == 0)
    def testCautare(self):
        self.assertRaises(ValidatorException,self.__serv.search_st_id,"2","ee","e")
        self.assertRaises(RepositoryException, self.__serv.search_st_id, "2", "ee", "2")
        self.assertTrue(self.__serv.search_st_id("1", "None", "5"),Student("1", "Ion", "2"))

class TestCaseProblemaService(unittest.TestCase):
    def setUp(self):
        #code executed before every testMethod
        open("sttest.txt").close()
        valid=Validator()
        repo=Repopr("prtest.txt")
        self.__serv =Services_pr(repo,valid)

        self.__serv.add_pr("1_1","greaaaaa","10/10/10")
    def tearDown(self):
        #cleanup code executed after every testMethod
        unittest.TestCase.tearDown(self)
        open("prtest.txt","w").close()

    def testAdaugare(self):
        self.assertTrue(self.__serv.get_no_pr(),1)
        self.assertRaises(ValidatorException,self.__serv.add_pr,"1_1","lala","-2")
        self.assertRaises(ValidatorException, self.__serv.add_pr, "1_1", "-", "2")
        self.assertRaises(ValidatorException, self.__serv.add_pr, "9", "lala", "2")
        self.assertRaises(RepositoryException,self.__serv.add_pr,"1_1","1","10/10/12")
    def testModificare(self):
        self.assertTrue(self.__serv.get_no_pr(),1)
        self.assertRaises(ValidatorException,self.__serv.upd_pr,"1_1","","4/2/2")
        self.assertRaises(RepositoryException,self.__serv.upd_pr,"1_2","eh","11/11/11")
        self.__serv.upd_pr("1_1","papa","20/12/20")
        self.assertTrue(self.__serv.search_pr_id("1_1","None","10/10/10"),Problema("1_1","papa" ,"20/12/20"))
    def testStergere(self):
        self.assertTrue(self.__serv.get_no_pr(),1)
        self.assertRaises(ValidatorException, self.__serv.rem_pr, "1_1", "", "4")
        self.assertRaises(RepositoryException, self.__serv.rem_pr, "1_2", "eh", "10/12/12")
        self.__serv.rem_pr("1_1", "papa", "20/12/20")
        self.assertTrue(self.__serv.get_no_pr() == 0)
    def testCautare(self):
        self.assertRaises(ValidatorException,self.__serv.search_pr_id,"2_2","nume","e")
        self.assertRaises(RepositoryException, self.__serv.search_pr_id, "1_2", "nume", "10/10/10")
        self.assertTrue(self.__serv.search_pr_id("1_1", "None", "10/10/10") == Problema("1_1", "grea", "10/10/10"))

class TestCaseNotaService(unittest.TestCase):
    def setUp(self):
        #code executed before every testMethod
        open("nt_st_fisier.txt","w").close()
        open("nt_pr_fisier.txt", "w").close()
        open("nttest.txt", "w").close()
        valid=Validator()
        repost=Repost("nt_st_fisier.txt")
        st=Student("1","Ion","2")
        repost.adaugarest(st)
        st = Student("2", "Gigi", "2")
        repost.adaugarest(st)
        st = Student("3", "AAA", "3")
        repost.adaugarest(st)
        repopr=Repopr("nt_pr_fisier.txt")
        pr=Problema("1_1","grea","10/10/10")
        repopr.adaugarepr(pr)
        repo=Repont("nttest.txt")
        self.__serv =Services_nt(repo,repost,repopr,valid)
        self.__serv.add_nt("1","1_1","2")


    def tearDown(self):
        #cleanup code executed after every testMethod
        unittest.TestCase.tearDown(self)
        open("nt_st_fisier.txt","w").close()
        open("nt_pr_fisier.txt", "w").close()
        open("nttest.txt", "w").close()

    def testAdaugare(self):
        self.assertTrue(self.__serv.get_no_nt()==1)
        self.assertRaises(ValidatorException, self.__serv.add_nt, "1", "1_1", "-1")
        self.assertRaises(RepositoryException,self.__serv.add_nt,"1","1_1","1")
    def testModificare(self):
        self.assertTrue(self.__serv.get_no_nt() == 1)
        self.assertRaises(ValidatorException, self.__serv.upd_nt, "2", "1", "6")
        self.assertRaises(RepositoryException,self.__serv.upd_nt,"2","1_1","6")
        self.__serv.upd_nt("1","1_1","10")
        self.assertTrue(self.__serv.search_nt("1","1_1","5")==Nota("1","1_1" ,"10"))
    def testStergere(self):
        self.assertTrue(self.__serv.get_no_nt() == 1)
        self.assertRaises(ValidatorException, self.__serv.rem_nt, "1", "1_1", "94")
        self.assertRaises(RepositoryException, self.__serv.rem_nt, "2", "1_1", "6")
        self.__serv.rem_nt("1", "1_1", "10")
        self.assertTrue(self.__serv.get_no_nt() == 0)
    def testCautare(self):
        self.assertRaises(ValidatorException,self.__serv.search_nt,"1","ee","4")
        self.assertRaises(RepositoryException, self.__serv.search_nt, "2", "1_1", "2")
        self.assertTrue(self.__serv.search_nt("1", "1_1", "5") == Nota("1", "1_1", "2"))

    def testget_st_alfabetic(self):
        self.__serv.add_nt("2", "1_1", "5")
        self.__serv.add_nt("3", "1_1", "6")
        lista=self.__serv.get_st_alfabetic("1_1")
        self.assertTrue(lista[0].getstudentID()=="3")
        self.assertTrue(lista[1].getstudentID()== "2")
        self.assertTrue(lista[2].getstudentID()== "1")

    def testget_st_nota(self):
        self.__serv.add_nt("2", "1_1", "5")
        self.__serv.add_nt("3", "1_1", "6")
        lista=self.__serv.get_st_nota("1_1")
        self.assertTrue(lista[0].getstudentID()=="1")
        self.assertTrue(lista[1].getstudentID()== "2")
        self.assertTrue(lista[2].getstudentID()== "3")

    def testget_get_st_sub5(self):
        self.__serv.add_nt("2", "1_1", "5")
        self.__serv.add_nt("3", "1_1", "6")
        lista=self.__serv.get_st_sub5()
        self.assertTrue(lista[0][0]=="1")
        self.assertTrue(lista[0][1]== 2.0)

    def testget_rap_note_gr(self):
        self.__serv.add_nt("2", "1_1", "5")
        self.__serv.add_nt("3", "1_1", "6")
        dict=self.__serv.get_rap_note_gr()
        self.assertTrue(dict[0][0]==2)
        self.assertTrue(dict[0][1]==2)
        self.assertTrue(dict[1][0]==3)
        self.assertTrue(dict[1][1]==1)



class TestCaseStudentRepo(unittest.TestCase):
    def setUp(self):
        #code executed before every testMethod
        open("sttest.txt","w").close()

        repost=Repost("sttest.txt")
        self.__repo=repost

    def tearDown(self):
        #cleanup code executed after every testMethod
        unittest.TestCase.tearDown(self)
        open("sttest.txt").close()

    def testAdaugare(self):
        st=Student("1","Ion","2")

        self.__repo.adaugarest(st)

        self.assertTrue(len(self.__repo),1)
        st=Student("2","fk","7")
        self.__repo.adaugarest(st)


    def testModificare(self):
        st=Student("1","Ion","2")
        self.__repo.adaugarest(st)
        self.assertTrue(len(self.__repo.get_all()),1)
        st=Student("1","papa","100")
        self.__repo.updatest(st)
        self.assertTrue(self.__repo.searchst_1(st),Student("1"," papa" ,"100"))
    def testStergere(self):
        st=Student("1","Ion","2")
        self.__repo.adaugarest(st)
        self.assertTrue(len(self.__repo.get_all()), 1)
        st=Student("1", "papa", "10")
        self.__repo.stergest(st)
        self.assertTrue(len(self.__repo.get_all())==0)
    def testCautare(self):
        st=Student("1","Ion","2")
        self.__repo.adaugarest(st)
        key_st=Student("1","nume","2")
        self.assertTrue(self.__repo.searchst_1(key_st),Student("1", "Ion", "2"))

class TestCaseProblemaRepo(unittest.TestCase):
    def setUp(self):
        #code executed before every testMethod
        open("prtest.txt","w").close()

        repopr=Repopr("prtest.txt")
        self.__repo=repopr

    def tearDown(self):
        #cleanup code executed after every testMethod
        unittest.TestCase.tearDown(self)
        open("prtest.txt").close()

    def testAdaugare(self):
        pr=Problema("1_1","usor","10/12/12")
        self.__repo.adaugarepr(pr)
        self.assertTrue(len(self.__repo),1)
        pr=Problema("2+_3","fk","7/10/12")
        self.__repo.adaugarepr(pr)
        self.assertTrue(len(self.__repo),2)


    def testModificare(self):
        pr=Problema("1_1","ez","10/10/13")
        self.__repo.adaugarepr(pr)
        self.assertTrue(len(self.__repo.get_all()),1)
        pr=Problema("1_1","papa","10/9/20")
        self.__repo.updatepr(pr,len(self.__repo)-1)
        self.assertTrue(self.__repo.searchpr_1(pr),Problema("1_1","papa" ,"10/9/20"))
    def testStergere(self):
        pr=Problema("1_1","grea","13/1/20")
        self.__repo.adaugarepr(pr)
        self.assertTrue(len(self.__repo.get_all()), 1)
        pr=Problema("1_1", "papa", "10/10/10")
        self.__repo.stergepr(pr,len(self.__repo)-1)
        self.assertTrue(len(self.__repo.get_all())==0)
    def testCautare(self):
        pr=Problema("1_10","uh","2/2/20")
        self.__repo.adaugarepr(pr)
        key_pr=Problema("1_10","nume","2")
        self.assertTrue(self.__repo.searchpr_1(key_pr),Problema("1_10", "uh", "2/2/20"))


class TestCaseNotaRepo(unittest.TestCase):
    def setUp(self):
        #code executed before every testMethod
        open("nttest.txt","w").close()

        repont=Repont("nttest.txt")
        self.__repo=repont

    def tearDown(self):
        #cleanup code executed after every testMethod
        unittest.TestCase.tearDown(self)
        open("nttest.txt").close()

    def testAdaugare(self):
        nt=Nota("1","1_1","2")

        self.__repo.adaugarent(nt)

        self.assertTrue(len(self.__repo),1)
        nt=Nota("2","fk","7")
        self.__repo.adaugarent(nt)
        self.assertTrue(len(self.__repo),2)
        


    def testModificare(self):
        nt=Nota("1","1_1","2")
        self.__repo.adaugarent(nt)
        self.assertTrue(len(self.__repo.get_all()),1)
        nt=Nota("1","1_1","1")
        self.__repo.updatent(nt)
        self.assertTrue(self.__repo.searchnt(nt),Nota("1"," 1_1" ,"1"))
    def testStergere(self):
        nt=Nota("1","2_2","2")
        self.__repo.adaugarent(nt)
        self.assertTrue(len(self.__repo.get_all()), 1)
        nt=Nota("1", "2_2", "10")
        self.__repo.stergent(nt)
        self.assertTrue(len(self.__repo.get_all())==0)
    def testCautare(self):
        nt=Nota("1","1_1","2")
        self.__repo.adaugarent(nt)
        key_nt=Nota("1","1_1","2")
        self.assertTrue(self.__repo.searchnt(key_nt),Student("1", "Ion", "2"))






import Controller.tests
from Controller.valid import Validator

from Controller.services import Services_pr, Services_st, Services_nt
from UI.user_interface import UI
alegere=input("1-fisiere/altfel")
if alegere=="1":
    from Repository.repositoryfile import Repopr, Repont
    from  Repository.repostnew import Repost

else: from Repository.repository import Repopr, Repost, Repont

if __name__ == '__main__':
    print("merge frate")
    tests = Controller.tests.Tests()
    tests.all_tests()
    if alegere=="1":
        repo_st = Repost("fisiernewst.txt","fisieraux.txt")
        repo_pr = Repopr("fisierRP.txt")
        repo_nt = Repont("fisierRN.txt")
    else:
        repo_st = Repost()
        repo_pr = Repopr()
        repo_nt = Repont()

    valid_st = Validator()
    valid_pr = Validator()
    valid_nt=Validator()
    service_st = Services_st(repo_st, valid_st)
    #service_st.add_st("1","gigi","1")
    #service_st.add_st("2", "a", "2")
    #service_st.add_st("3", "lala", "2")
    #service_st.add_st("4", "urs", "3")
    #service_st.add_st("5", "gigi", "2")
    #service_st.add_st("6", "lala", "5")

    service_pr = Services_pr(repo_pr, valid_pr)
    #service_pr.add_pr("1_1","grea","10/10/10")
    #service_pr.add_pr("1_2", "ez", "10/10/10")
    #service_pr.add_pr("1_3", "ezez", "10/10/10")
    service_nt=Services_nt(repo_nt,repo_st,repo_pr,valid_nt)
    #service_nt.add_nt("1","1_1","6")
    #service_nt.add_nt("1", "1_2", "5")
    #service_nt.add_nt("2", "1_1", "6")
    #service_nt.add_nt("2", "1_2", "8")
    #service_nt.add_nt("5", "1_1", "6")
    #service_nt.add_nt("5", "1_3", "1")
    #service_nt.add_nt("6", "1_1", "5")
    cons = UI(service_st, service_pr,service_nt)
    cons.run()

import datetime
class ValidatorException(Exception):
    pass
class Validator:

    def valideaza_st(self, student):
        errors = ""
        id_st=str(student.getstudentID())

        if id_st.isdigit()==False or int(student.getstudentID()) <0:
            errors += "id invalid\n"
        if student.getnume() == "":
            errors += "nume invalid\n"
        gr_st=str(student.getgrup())
        if gr_st.isdigit()==False or int(student.getgrup()) < 0 :
            errors += "grupa invalida\n"
        if len(errors) > 0:
            raise ValidatorException(errors)
    """
    verificam daca datele introduse sunt valide pentru un student
    """

    def valideaza_pr(self,problema):
        errors = ""
        id_pr=str(problema.getnrlab_nrprob()).split("_")
        if  len(id_pr)!=2 or id_pr[0].isdigit()==False or id_pr[1].isdigit()==False  \
                or int(id_pr[0]) <0 or int(id_pr[1])<0:
            errors += "nr invalid\n"
        if problema.getdescriere()=="":
            errors += "descriere invalida\n"
        try:
            datetime.datetime.strptime(problema.getdeadline(), '%d/%m/%y')
        except ValueError:
            errors += "deadline invalid\n"
        if len(errors) > 0:
            raise ValidatorException(errors)
        """
           verificam daca datele introduse sunt valide pentru o problema
        """
    def valideaza_nt(self,nota):
        errors= ""
        id_st = str(nota.getstudentID())

        if id_st.isdigit() == False or int(nota.getstudentID()) < 0:
            errors += "id invalid\n"
        id_pr = str(nota.getnrlab_nrprob()).split("_")
        if len(id_pr) != 2 or id_pr[0].isdigit() == False or id_pr[1].isdigit() == False \
                or int(id_pr[0]) < 0 or int(id_pr[1]) < 0:
            errors += "nr invalid\n"
        notaa=str(nota.getnota())
        if nota.getnota()=="" or float(nota.getnota())<1 or float(nota.getnota())>10:
            errors += "nota invalid\n"
        if len(errors) > 0:
            raise ValidatorException(errors)

        """
                   verificam daca datele introduse sunt valide pentru o nota
                """



class Problema():
    """
    clasa Problema defineste caracteristicile unei probleme
    1)caracteristicile instantei(nrprob,descriere,deadline)
    2)metode si operatii

    """
    def __init__(self, nrlab_nrprob, descriere, deadline):
        self.__nrlab_nrprob = nrlab_nrprob
        self.__descriere = descriere
        self.__deadline = deadline

    def getnrlab_nrprob(self):
        return self.__nrlab_nrprob

    def getdescriere(self):
        return self.__descriere

    def getdeadline(self):
        return self.__deadline

    def setnrlab_nrporb(self, nrlab_nrprob):
        self.__nrlab_nrprob = nrlab_nrprob

    def setdescriere(self, descriere):
        self.__descriere = descriere

    def setdeadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return str(self.__nrlab_nrprob) +" "+ str(self.__descriere) +" "+str(self.__deadline)
    def __eq__(self, other):
        return str(self.__nrlab_nrprob)==str(other.__nrlab_nrprob)
    def egal_desc(self,other):
        return self.__descriere == other.__descriere
    def egal_deadline(self,other):
        return self.__deadline == other.__deadline
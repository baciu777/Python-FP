class Nota:
    """
    clasa Nota defineste caracteristicile unei note
    1)caracteristicile instantei(studentID,nrlab_nrprob,nota)
    2)metode si operatii
    """
    def __init__(self,studentID,nrlab_nrprob,nota):
        self.__studentID=studentID
        self.__nrlab_nrprob=nrlab_nrprob
        self.__nota = nota
    def getstudentID(self):
        return self.__studentID
    def getnrlab_nrprob(self):
        return  self.__nrlab_nrprob
    def getnota(self):
        return self.__nota

    def __eq__(self, other):
        return str(self.__nrlab_nrprob)==str(other.__nrlab_nrprob) and str(self.__studentID)==str(other.__studentID)
    def __str__(self):
        return str(self.__studentID)+" "+str(self.__nrlab_nrprob)+" "+str(self.__nota)
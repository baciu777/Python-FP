class Student():
    """
    clasa student defineste caracteristicile unui student
    1)caracteristicile instantei(idstudent,nume,grupa)
    2)metode si operatii

    """
    def __init__(self, studentID, nume, grup):

        self.__studentID = studentID
        self.__nume = nume
        self.__grup = grup


    def getstudentID(self):
        return self.__studentID

    def getnume(self):
        return self.__nume

    def getgrup(self):
        return self.__grup

    def setstudentID(self, studentID):
        self.__studentID = studentID

    def setnume(self, nume):
        self.__nume = nume

    def setgrup(self, grup):
        self.__grup = grup

    def __str__(self):
        return str(self.__studentID)+" "+str(self.__nume)+" "+str(self.__grup)

    def __eq__(self, other):
        return self.__studentID==other.__studentID
    def egal_nume(self,other):
        return self.__nume == other.__nume
    def egal_grup(self,other):
        return self.__grup == other.__grup
import os

from Domain.clsstudenti import Student
from Repository.repository import RepositoryException


class Repost():
    def __init__(self,fileN,fileaux):
        self.__fName=fileN
        self.__fNameaux=fileaux


    def adaugarest(self,st):

        with open(self.__fName,"r") as f:
            while True:
                date=f.readline()
                if date.strip()!="":
                    date.strip()
                    attrs=date.split(";")
                    if attrs[0]==st.getstudentID():
                        raise RepositoryException("elm existent/n")
                if date.strip()=="":
                    break
        with open(self.__fName,"a") as f:
            date=f"{st.getstudentID()};{st.getnume()};{st.getgrup()}\n"
            f.write(date)

    def searchst_1(self, st):
        with open(self.__fName,"r") as f:
            while True:
                date=f.readline()
                if date.strip()!="":
                    date.strip()
                    attrs=date.split(";")
                    if attrs[0] == st.getstudentID():
                        found=Student(attrs[0],attrs[1],attrs[2])
                        return found
                if date.strip()=="":
                    raise RepositoryException("element inexistent\n")
    def searchst_2(self, st):
        l=[]
        ok=0
        with open(self.__fName,"r") as f:
            while True:
                date=f.readline()
                if date.strip()!="":
                    date.strip()
                    attrs=date.split(";")
                    if attrs[1] == st.getnume():
                        found=Student(attrs[0],attrs[1],attrs[2])
                        l.append(found)
                        ok=1
                if ok!=0 and date.strip()=="":
                    return l[:]
                if date.strip()=="":
                    raise RepositoryException("element inexistent\n")
    def searchst_3(self, st):
        l=[]
        ok=0
        with open(self.__fName,"r") as f:
            while True:
                date=f.readline()
                if date.strip()!="":
                    date.strip()
                    attrs=date.split(";")
                    if attrs[2] == st.getgrup():
                        found=Student(attrs[0],attrs[1],attrs[2])
                        l.append(found)
                        ok=1
                if ok!=0 and date.strip()=="":
                    return l[:]
                if date.strip()=="":
                    raise RepositoryException("element inexistent\n")

    def updatest(self,st):
        with open(self.__fName,"r") as f, open(self.__fNameaux,"w") as f2:
            while True:
                date = f.readline()
                if date.strip() != "":
                    date.strip()
                    attrs = date.split(";")
                    if attrs[0] == st.getstudentID():
                        f2.write(f"{st.getstudentID()};{st.getnume()};{st.getgrup()}\n")
                    else:
                        f2.write(date)
                if date.strip() == "":
                    break

        os.rename(self.__fName,"fisierauxaux.txt")
        os.rename(self.__fNameaux,self.__fName)
        os.rename("fisierauxaux.txt",self.__fNameaux)

    def stergest(self,st):
        with open(self.__fName, "r") as f, open(self.__fNameaux, "w") as f2:
            while True:
                date = f.readline()
                if date.strip() != "":
                    date.strip()
                    attrs = date.split(";")
                    if attrs[0] != st.getstudentID():
                        f2.write(f"{attrs[0]};{attrs[1]};{attrs[2]}")

                if date.strip() == "":
                    break

        os.rename(self.__fName,"fisierauxaux.txt")
        os.rename(self.__fNameaux,self.__fName)
        os.rename("fisierauxaux.txt",self.__fNameaux)
    def get_all(self):
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

    def find_nume(self,id):
        with open(self.__fName, "r") as f:
            while True:
                date = f.readline()
                if date.strip() != "":
                    date.strip()
                    attrs = date.split(";")
                    if attrs[0] == id:
                        return attrs[1]
                if date.strip() == "":
                    raise RepositoryException("element inexistent\n")

    def __len__(self):
        return len(self.get_all())

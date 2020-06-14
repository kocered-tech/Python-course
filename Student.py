
class Student:

    def __init__(self, name, surname, id, mail, department):
        self.__name = name
        self.__surname = surname
        self.__id = id
        self.__mail = mail
        self.__department  = department

    def __str__(self):
        return self.__name + " " + self.__surname


    def getName(self):
        return self.__name 

    def getSurname(self):
        return self.__surname 

    def getId(self):
        return self.__id 

    def getMail(self):
        return self.__mail 

    def getDepartment(self):
        return self.__department




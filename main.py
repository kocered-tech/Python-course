
"""

Öğrenciler
Sınav tarihleri görebilir
Schedule görbilir 
Meal 
Print quota
Notları görebilir


Öğretmenler 
Not değiştirme
Sınav tarihi değiştirebiliyor
Schedule görebilir


Sınav tarihini görebilir

"""

from Student import *
from Credential import *

def getStudentData(studentFile):

    studentList = []

    for line in studentFile :
        lineList = line.split(',') 
        
        #Converts raw string data to list
        # lineList = ["beyza","Bakır"...]


        #Temporary values 
        name = lineList[0]
        surname = lineList[1]
        id = lineList[2]
        mail = lineList[3]
        department = lineList[4]


        student = Student(name,surname,id,mail,department)
        studentList.append(student)
        return(studentList)

def getCredentialData(credentialFile):
    credentialList = []
    for line in credentialFile:
        lineData = line.split(',')
        
        email = lineData[0]
        password = lineData[1]
        whatIs = lineData[2]

        credentialList.append(Credential(email,password,whatIs))

    return credentialList


studentFile = open("students.txt",'r') #Opens students file and reads
credentialFile = open("signindata.txt",'r') #Opens signin data file
        
studentList = getStudentData(studentFile)
credentialList = getCredentialData(credentialFile)



print("Please enter your credentials to sign in:")
email = input("email: ")
password = input("password: ")


for credential in credentialList:
    if email == credential.email and password == credential.password:
        print("You are signed in.")



        


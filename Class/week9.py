def read():
    myFile = open("demofile.txt", "r")
    content = myFile.read()
    print(content)

def readNames():
    myFile1 = open("names.txt", "r")
    content1 = myFile1.read()
    content2 = myFile1.read(50)
    content3 = myFile1.readline()
    # print(content1)
    print(content2)
    # print(content3)

def write():
    myFile = open("names.txt", "w")
    myFile.write("Hello World!")
    myFile.flush()

def closeFile():
    myFile1 = open("names.txt", "r")
    content1 = myFile1.read()
    content2 = myFile1.read(50)
    content3 = myFile1.readline()
    # print(content1)
    print(content2)
    # print(content3)
    myFile1.close()

def split():
    s = "Hello,World,Blah,Blah"
    a = s.split(',')
    print(s)
    print(len(a))

def strip():
    s = " Hello      "
    print(len(s.strip()))

def email():
    s = "johndoe@muhlenberg.edu"
    pos = s.find("@")
    print(pos)
    userName = s[:pos]
    print(userName)

def grades():
    myFile = open("grades.csv", "r")
    list = myFile.split(',')


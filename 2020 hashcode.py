import random


file1 = open("f.txt","r")
lines = file1.readlines()
line1 = lines[0].split()
line2 = lines[1].split(" ")
global BOOKS
global DAY
global DEADLINE
global TOTALBOOKS
global TOTALLIB

BOOKS = list(line2)
DEADLINE = int(line1[2])
TOTALBOOKS = line2
TOTALLIB = line1[1]
BOOKS[len(BOOKS)-1] = str(546)



class library():
    def __init__(self,libID,books,signup,uniqueBooks,maxSend):
        self.libID = libID
        self.open = False
        self.books = books
        self.signup = signup
        self.uniqueBooks = uniqueBooks
        self.max = maxSend
        self.slots = (DEADLINE - self.signup) * self.max

    def slots(self) :
        pass



librarys = []
count = 0
count2 = 0
for x in lines[2:]:
    line = list(x.split())
    count += 1
    #print(line)
    if line == []:
        break
    if count == 1:
        lib = library(count2,[],int(line[1]),None,int(line[2]))
        count2 += 1
        librarys.append(lib)
    else:
            #print(TOTALBOOKS[int(book)])
            #score = TOTALBOOKS[int(book)]
            #print(score)
            #book = (int(score), book)
            #book = (book)
            #print(book)
        librarys[count2-1].books.append(x.split(" "))
        #sorted(librarys[count2-1].books)
        count = 0
from operator import itemgetter


sentbooks = []
sublibraries =[]
submitFile = open("f_ans.txt","w+")




libraries = []
while DEADLINE > 0:
    numb = random.randint(0,len(librarys)-1)
    DEADLINE = DEADLINE - librarys[numb].signup
    libraries.append((numb,librarys[numb].books))
submitFile.write(str(len(libraries)))
submitFile.write("\n")
for i in libraries:
    submitFile.write("%s %s " %(i[0],str(len(i[1]))))
    submitFile.write("\n")
    for x in i[1]:
        count = 0
        for l in x:
            if count < 1:
                count += 1
                submitFile.write(l)
                submitFile.write(" ")
        submitFile.write("\n")
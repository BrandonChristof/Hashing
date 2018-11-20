'''
    Brandon Christof
    Date: 2018-11-19
    
    This program implements a hash table to
    search for any of the listed 7200 eight
    letter words in AT MOST 10 steps and with
    an average of 0.67 steps
    
'''
import urllib.request
import math

m = 11989
T = ["empty"]*m
maxNum = 0

#Gets list of data from url
def readWordList():
    response = urllib.request.urlopen("http://sites.cs.queensu.ca/courses/cisc235/Assignments/Assignment%202/HOTNCU_potential_codenames_2018F.txt")
    html = response.readline()
    data = []

    while len(html) != 0:
        line = html.decode('utf-8').split()
        data.append(line)
        html = response.readline()
    return data

#Creates a unique key for a given string
def getKey(s):
    a = 5381
    for x in s:
        a = a*33 + ord(x)
    return a

#Gets a string's key value and inserts it into hash table
def createHashTable(w): 
    for i in w:
        insertKey(getKey(i[0]))


#Searches for a given key value
def searchKey(k):
    global m
    global T
    
    i = 0
    v = hashFunction(k)
    a = v
    
    while (i < m) and (T[a] != "empty") and (T[a] != k):
        i += 1
        a = probe(v, i)
    if T[a] == k:
        print("\nFOUND. Number of Steps:", i)
    else:
        print("FAILED")


def insertKey(k):
    global m
    global T
    global maxNum
    
    i = 0
    v = hashFunction(k)
    a = v
    
    while (i < m) and (T[a] != "empty"):
        i += 1
        if maxNum < i:
            maxNum = i
        a = probe(v, i)
    if T[a] == "empty":
        T[a] = k
        return i
    else:
        print("FAILED")

#Double hashing
def probe(v, i):
    global m
    
    a = (v*7207 + i**2)
    b = (a**2 + i*7207)
    
    return b % m
    

#Multiplication method using phi
def hashFunction(k):
    global m
    
    a = k % 131071                         #To fit with the number of decimals in v
    v = 0.6180339887498948482              #Phi
    
    return math.floor(m*((a*v) % 1)) % m

def main():
    print("\n                     Welcome to Word Finder")
    print("This program can search for any 8 letter word, or insert any word")
    
    codeList = readWordList()
    createHashTable(codeList)

    while True:
        d = input("\n[1]-Search\n[2]-Insert\n[3]-Exit\n")
        if d == "1":
            s = input("Give an 8 letter word:")
            searchKey(getKey(s))
        elif d == "2":
            r = input("Insert:")
            print("Inserting:", r, "\nNumber of Steps:", insertKey(getKey(r)))
        elif d == "3":
            break
        else:
            print("\nInvalid Input")

main()

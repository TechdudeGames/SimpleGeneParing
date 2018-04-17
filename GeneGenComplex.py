import random
import os
def creategenepool():
    tempgene=[]
    iscontinue = True
    while iscontinue:
        print("Type the gene you would like to add. Type in nothing and press enter if you are done inputing genes")
        genetype = input()
        if type(genetype) is str and len(list(genetype))==1:
            print("How many?")
            try:
              number=int(input())
              for i in range(0,number):
                tempgene.append(genetype)
            except:
              print("Invalid Input")
        elif genetype=='':
            print("Beginning pairing")
            iscontinue=False
        else:
            print("Invalid genetype. Must be a character.")
    return tempgene

genepool=creategenepool()
genespercombo=2
selectedgenes=[]
offspring=[]
finalresult=[]
while len(genepool) >= genespercombo:
    while len(selectedgenes) != genespercombo:
        selection=genepool[random.randrange(0,len(genepool))]
        selectedgenes.append(selection)
        genepool.remove(selection)
    for letternum in range(0,len(selectedgenes)):
        if selectedgenes[letternum] in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            finalresult.append(selectedgenes[letternum])
    for letternum in range(0,len(selectedgenes)):
        if selectedgenes[letternum] not in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            finalresult.append(selectedgenes[letternum])
    offspring.append(finalresult)
    finalresult=[]
    selectedgenes=[]




print("Children")
#print all the children
for child in offspring:
    print(child)
print("Leftover genes:"+str(genepool))

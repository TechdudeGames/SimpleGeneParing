import random
import os


def creategenepool():
    tempgene=[]
    continue = True
    while continue:
        print("Type the gene you would like to add:")
        genetype = input()
        if type(genetype) is str and len(list(genetype))==0:
            print("How many?")
            numberofgenes=input()
            if type(numberofgenes) is int:
                for i in range(0,numberofgenes):
                    tempgene.append(genetype)
            else:
                print("Invalid input")
        elif genetype='':
            print("Beginning pairing")
        else:
            print("Invalid genetype. Must be a character.")
    return temegene

genepool=creategenepool()
for l in genes:
    number_of_genetype=genes.get(l)
    for g in range(number_of_genetype):
        genepool.append(l)
    print(str(genes.get(l))+" "+l+" "+"genes.")
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

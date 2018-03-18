import random
genepool=[]
genespercombo=2
selectedgenes=[]
offspring=[]
genes={"G":8,"r":8,'B':9}
finalresult=[]
print("The genepool contains the following genes:")
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
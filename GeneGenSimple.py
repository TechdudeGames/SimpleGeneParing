import random
genepool=[]
offspring=[]
genes=['G','G','G','G','G','G','G','G','Y','Y','Y','Y','Y','Y','R','R','R','R','R','R','R','R']
numberofgenes=len(genes)
for gene in genes:
    genepool.append(gene)
while genepool!=[]:
        gene_choice1=genepool[random.randrange(0,numberofgenes)]
        genepool.remove(gene_choice1)
        numberofgenes-=1
        gene_choice2=genepool[random.randrange(0,numberofgenes)]
        genepool.remove(gene_choice2)
        numberofgenes -= 1
        offspring.append(str((gene_choice1 +" / " + gene_choice2)))
print("Number of offspring", len(offspring))
print("Genes of offspring:")
for kid in offspring:
    print(kid)

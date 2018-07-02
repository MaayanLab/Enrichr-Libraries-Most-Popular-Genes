# delete .DS_Store files, obtain list of file names to be read in folder
import os

os.system('find . -name ".DS_Store" -print -delete')
os.system('find . -name ".pydev*" -print -delete')
os.system('find . -name ".project*" -print -delete')
listOfFiles = os.listdir("/Users/maayanlab/Desktop/Megan/Enrichr")

# for each file, open file to read, open an output file,
# create dictionary to count the number times each gene occurs
for libraryFile in listOfFiles:
    if not libraryFile.endswith(".py"):
        if not libraryFile.endswith("_results.txt"):
            libraryDictionary = {}
            openFile = open(libraryFile, "r", encoding='utf-8')
            resultsFileName = libraryFile + "_results.txt"
            resultsFile = open(resultsFileName, "w")
            for line in openFile.readlines():
                newLine = line.rstrip()
                fields = newLine.split("\t")
                genes = fields[2:]
                print(genes)
                for gene in genes:
                    fields = gene.split(",")
                    geneName = fields[0]
                    if geneName in libraryDictionary.keys():
                        libraryDictionary[geneName] += 1
                    else:
                        libraryDictionary[geneName] = 1

            # sort dictionary keys by highest value to lowest value         
            # obtain top 100 genes and write to output file gene name and number of occurances
            highestToLowestGenes = sorted(libraryDictionary, key=libraryDictionary.get, reverse=True)
            top100Genes = highestToLowestGenes[0:100]
    
            # if there are multiple genes that occur at the 100th place, add them to the list
            # print length of most popular genes (target # should be ~100-120)  
            lastFrequency = (libraryDictionary[top100Genes[99]])
            for name,value in libraryDictionary.items():          
                if value == lastFrequency:
                    top100Genes.append(name)
            
            # print file name and length of most popular genes list to console         
            print(libraryFile, "\t", len(top100Genes))

            # write gene name and counts separated by a tab to output file
            for gene in top100Genes:
                resultsFile.write(gene + "\t" + str(libraryDictionary[gene]) + "\n")

# close all opened files 
openFile.close()
resultsFile.close()

'''
Created on Jan 10, 2018

@author: megan wojciechowicz maayan lab 

'''

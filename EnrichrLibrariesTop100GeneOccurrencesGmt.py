# delete .DS_Store, .project, and .pydevproject files, obtain list of file names to be read in folder
import os
os.system('find . -name ".DS_Store" -print -delete')
os.system('find . -name ".project" -print -delete')
os.system('find . -name ".pydevproject" -print -delete')
listOfFiles = os.listdir("/Users/maayanlab/Desktop/Megan/Enrichr")
resultsFile = open("EnrichrLibraryTopGenesSummmary", "w")
for file in listOfFiles:
    if not file.endswith(".py"):
        if not file.endswith("EnrichrLibraryTopGenesSummmary"):
            genelist = list()
            openFile = open(file, "r")
            for line in openFile.readlines():
                newLine = line.rstrip()
                fields = newLine.split("\t")
                genes = fields[0]
                genelist.append(genes)
            resultsFile.write(file +'\t'+'\t'.join(genelist))
            



# close all opened files 
openFile.close()
resultsFile.close()
'''
Created on Jan 10, 2018

@author: megan wojciechowicz, maayanlab
'''

def linearspectrum(peptid,aas,aasmass):
    prefixmass=list()
    prefixmass.append(0)
    for i in range(0,len(peptid)):
        for aa in aas:
            if aa == peptid[i]:
                p=aas.index(aa)
                somme=prefixmass[i]+int(aasmass[p])
                prefixmass.append(somme)
    linearspectrum=list()
    linearspectrum.append(0)
    for i in range(0,len(peptid)+1):
        for j in range(i+1,len(peptid)+1):
            somm=prefixmass[j]-prefixmass[i]
            linearspectrum.append(somm)
    linearspectrum.sort()
    for i in range(len(linearspectrum)):
        linearspectrum[i]=str(linearspectrum[i])
    return linearspectrum


def cyclicscore(spectrum1,experimentalspectrum):
    score=0
    for element in experimentalspectrum:
        if element in spectrum1:
            score+=1
            spectrum1.remove(element)
    return score


aas=list()
aasmass=list()

with open("Mass.txt","r") as v :
    lst=v.readlines()
    for line in lst:
        line=line.replace("\n","")
        lst1=line.split(" ")
        aas.append(lst1[0])
        aasmass.append(lst1[1])
    

with open("dataset.txt","r") as f:
    lst=f.readlines()
    peptid=lst[0].replace("\n","")
    experimentalspectrum=lst[1].split(" ")
    for i in range(len(experimentalspectrum)):
        experimentalspectrum[i]=experimentalspectrum[i].replace("\n","")

spectrum1=linearspectrum(peptid,aas,aasmass)
score=cyclicscore(spectrum1,experimentalspectrum)
print(score)
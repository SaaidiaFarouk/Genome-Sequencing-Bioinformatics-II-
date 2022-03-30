def cyclicspectrum(peptid,aas,aasmass):
    prefixmass=list()
    prefixmass.append(0)
    for i in range(0,len(peptid)):
        for aa in aas:
            if aa == peptid[i]:
                p=aas.index(aa)
                somme=prefixmass[i]+int(aasmass[p])
                prefixmass.append(somme)
    peptidmass=prefixmass[len(prefixmass)-1]
    cyclicspectrum=list()
    cyclicspectrum.append(0)
    for i in range(0,len(peptid)+1):
        for j in range(i+1,len(peptid)+1):
            somm=prefixmass[j]-prefixmass[i]
            cyclicspectrum.append(somm)
            if i>0 and j<len(peptid):
                somm=peptidmass-somm
                cyclicspectrum.append(somm)
    cyclicspectrum.sort()
    for i in range(len(cyclicspectrum)):
        cyclicspectrum[i]=str(cyclicspectrum[i])
    return cyclicspectrum


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
    experimentalspectrum=lst[0].split(" ")
    for i in range(len(experimentalspectrum)):
        experimentalspectrum[i]=experimentalspectrum[i].replace("\n","")

spectrum1=cyclicspectrum("MAMA",aas,aasmass)
score=cyclicscore(spectrum1,experimentalspectrum)
print(score)
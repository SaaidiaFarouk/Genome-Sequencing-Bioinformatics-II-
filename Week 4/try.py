
def fromnumbertoalpha(numpeptid,aas,aasmass):
    peptid=''
    for i in range(len(numpeptid)):
        for j  in range(len(aasmass)):
            if numpeptid[i] == aasmass[j]:
                peptid+=aas[j]
                break
    return peptid
def fromalphatonumpeptid(peptid,aas,aasmass):
    numpeptid=list()
    for i in range(len(peptid)):
        j=0
        for j in range(len(aas)):
            if peptid[i] == aas[j]:
                numpeptid.append(aasmass[j])
                break
    return numpeptid
def cyclicspectrum(peptid,aas,aasmass):
    peptid=fromnumbertoalpha(peptid,aas,aasmass)
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
def cyclicscore(spectrumm,experimentalspectrum):
    score=0
    spectrum1=spectrumm.copy()
    for element in experimentalspectrum:
        if element in spectrum1:
            score+=1
            spectrum1.remove(element)
    return score
def linearspectrum(peptid,aas,aasmass):
    peptid=fromnumbertoalpha(peptid,aas,aasmass)
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

aas=list()
aasmass=list()

with open("Mass.txt","r") as v :
    lst=v.readlines()
    for line in lst:
        line=line.replace("\n","")
        lst1=line.split(" ")
        aas.append(lst1[0])
        aasmass.append(lst1[1])



with open("dataset.txt","r") as f :
    data=f.read()
    data=data.replace("\n","")
    spectrum=data.split(" ")

peptid="PEEP"





peptid=fromalphatonumpeptid(peptid,aas,aasmass)
print(peptid)
spec=linearspectrum(peptid,aas,aasmass)
print(spec)
print(cyclicscore(spec,spectrum))
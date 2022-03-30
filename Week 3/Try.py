with open("Mas.txt","r") as v:
    masss=v.readlines()
for i in range(len(masss)):
    masss[i]=masss[i].replace("\n","")


with open("Mass.txt","r") as h :
    lst=h.readlines()
aas=list()
aasmass=list()
for line in lst:
    line=line.replace("\n","")
    lst1=line.split(" ")
    aas.append(lst1[0])
    aasmass.append(lst1[1])

with open("dataset.txt","r") as f: 
    data=f.read()
    f.close()
spectrum=data.split(" ")

def expande(candidatepeptids,masss):
    newcandidatepeptids=list()
    for cpeptid in candidatepeptids:
        for mass in masss:
            newcpeptid=cpeptid.copy()
            newcpeptid.append(mass)
            newcandidatepeptids.append(newcpeptid)
    return newcandidatepeptids

def consistencycheck(spectrum1,spectrum2):
    valu = True 
    for element in spectrum1:
        if element not in spectrum2:
            valu = False
    return valu

def fromnumbertoalpha(numpeptid,aas,aasmass):
    peptid=''
    for i in range(len(numpeptid)):
        j=0
        for j  in range(len(aasmass)):
            if numpeptid[i] == aasmass[j]:
                peptid+=aas[j]
                break
                

    return peptid

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

def maxs(peptid):
    weight=0
    for pep in peptid:
        weight+=int(pep)
    return weight


finalpeptids=list()
parentmass=0
val= True
for mass in spectrum:
    if int(mass) > parentmass:
        parentmass=int(mass)
candidatepeptids=[[]]
while len(candidatepeptids) != 0:
    newcandidatepeptids=expande(candidatepeptids,masss)
    candidatepeptids=newcandidatepeptids.copy()
    auxcandidatepeptids=candidatepeptids.copy()
    for peptid in candidatepeptids:
        print(peptid)
        val = consistencycheck(cyclicspectrum(peptid,aas,aasmass),spectrum)
        if maxs(peptid) == parentmass :
            if cyclicspectrum(peptid,aas,aasmass) == spectrum and peptid not in finalpeptids:
                finalpeptids.append(peptid)
            auxcandidatepeptids.remove(peptid)
        elif val == False :
            auxcandidatepeptids.remove(peptid)
        candidatepeptids=auxcandidatepeptids.copy()
    print(candidatepeptids)
    print("done")
print(finalpeptids,"=finalpeptids")
finalpeptids.sort()
print(finalpeptids,"=finalpeptids")
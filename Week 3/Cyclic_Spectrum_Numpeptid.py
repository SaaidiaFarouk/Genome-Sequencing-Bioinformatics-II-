def fromnumbertoalpha(numpeptid,aas,aasmass):
    peptid=''
    for i in range(len(numpeptid)):
        for j  in range(len(aasmass)):
            if numpeptid[i] == aasmass[j]:
                peptid+=aas[j]
                break
    return peptid

def cyclicspectrum(peptid,aas,aasmass):
    peptid=fromnumbertoalpha(peptid,aas,aasmass)
    print(peptid)
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
    return cyclicspectrum




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
    peptid=f.read()

###with open("answear.txt","w") as d:
###    for spect in cyclicspectrum(peptid,aas,aasmass):
###        d.write(str(spect) + " ")

numpeptid=['113','114']
print(cyclicspectrum(numpeptid,aas,aasmass))


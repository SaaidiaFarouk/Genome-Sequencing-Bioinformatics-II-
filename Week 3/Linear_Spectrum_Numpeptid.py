def fromnumbertoalpha(numpeptid,aas,aasmass):
    peptid=''
    for i in range(len(numpeptid)):
        for j  in range(len(aasmass)):
            if numpeptid[i] == aasmass[j]:
                peptid+=aas[j]
                break
    return peptid

def linearspectrum(peptid,aas,aasmass):
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
    linearspectrum=list()
    linearspectrum.append(0)
    for i in range(0,len(peptid)+1):
        for j in range(i+1,len(peptid)+1):
            somm=prefixmass[j]-prefixmass[i]
            linearspectrum.append(somm)
    linearspectrum.sort()
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


with open("dataset.txt","r") as f:
    peptid=f.read()

###with open("answear.txt","w") as d:
###    for spect in linearspectrum(peptid,aas,aasmass):
###        d.write(str(spect) + " ")

numpeptid=['186','128']
print(linearspectrum(numpeptid,aas,aasmass))


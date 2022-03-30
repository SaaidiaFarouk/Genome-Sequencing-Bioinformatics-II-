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

def fromalphatonumpeptid(peptid,aas,aasmass):
    numpeptid=list()
    for i in range(len(peptid)):
        j=0
        for j in range(len(aas)):
            if peptid[i] == aas[j]:
                numpeptid.append(aasmass[j])
                break
    return numpeptid

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

def maxs(peptid):
    weight=0
    for pep in peptid:
        weight+=int(pep)
    return weight

def expande(candidatepeptids,masss):
    newcandidatepeptids=list()
    for cpeptid in candidatepeptids:
        for mass in masss:
            newcpeptid=cpeptid.copy()
            newcpeptid.append(mass)
            newcandidatepeptids.append(newcpeptid)
    return newcandidatepeptids

def Trim(leaderboard,experimentalspectrum,n,aas,aasmass):
    if len(leaderboard)==0:
        return leaderboard
    auxleaderboard=list()
    linearscores=list()
    for i in range(len(leaderboard)):
        peptid=leaderboard[i]
        linearspect=linearspectrum(peptid,aas,aasmass)
        score=cyclicscore(linearspect,experimentalspectrum)
        linearscores.append(score)
    linearscores, leaderboard = (list(t) for t in zip(*sorted(zip(linearscores, leaderboard))))
    leaderboard.reverse()
    linearscores.reverse()
    auxleaderboard=leaderboard.copy()
    for i in range(n+1,len(leaderboard)):
        if linearscores[i]<linearscores[n]:
            for j in range(i-1,len(leaderboard)):
                auxleaderboard.pop()
            return auxleaderboard
    return auxleaderboard  

def leaderboardcyclosequencing(experimentalspectrum,n,masss):
    leaderboard=[[]]
    leaderpeptid=list()
    parentmass=0
    for mass in experimentalspectrum:
        if int(mass) > parentmass:
            parentmass=int(mass)
    while len(leaderboard) != 0 :
        newleaderboard=expande(leaderboard,masss)
        leaderboard=newleaderboard.copy()
        l=len(leaderboard)
        i=0
        while i < l:
            peptid=leaderboard[i]
            spectrum=cyclicspectrum(peptid,aas,aasmass)
            score=cyclicscore(spectrum,experimentalspectrum)
            leaderspectrum=cyclicspectrum(leaderpeptid,aas,aasmass)
            leaderscore=cyclicscore(leaderspectrum,experimentalspectrum)
            if maxs(peptid) == parentmass:
                if score > leaderscore:
                    leaderpeptid=peptid
            elif maxs(peptid) > parentmass :
                leaderboard.remove(peptid)
                i-=1
                l-=1
            i+=1
        leaderboard=Trim(leaderboard,experimentalspectrum,n,aas,aasmass) 
    return leaderpeptid






with open("dataset.txt","r") as f : 
    lst=f.readlines()
    for i in range(len(lst)):
        lst[i]=lst[i].replace("\n","")
    n=int(lst[0])
    experimentalspectrum=lst[1].split(" ")

aas=list()
aasmass=list()
with open("Mass.txt","r") as v :
    lst=v.readlines()
    for line in lst:
        line=line.replace("\n","")
        lst1=line.split(" ")
        aas.append(lst1[0])
        aasmass.append(lst1[1])

with open("Mas.txt","r") as g:
    masss=g.readlines()
for i in range(len(masss)):
    masss[i]=masss[i].replace("\n","")
stri=''
ans=leaderboardcyclosequencing(experimentalspectrum,n,masss)
with open("answear.txt","w") as d: 
    for a in ans : 
        stri+=a+"-"
        sto=stri[:len(stri)-1]
    d.write(sto)
def linearspectrum(peptid):
    prefixmass=list()
    prefixmass.append(0)
    for i in range(0,len(peptid)):
        for j in range(57,201):
            if int(peptid[i]) == j:
                somme=prefixmass[i]+j
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

def Trim(leaderboard,experimentalspectrum,n):
    if len(leaderboard)==0:
        return leaderboard
    auxleaderboard=list()
    linearscores=list()
    for i in range(len(leaderboard)):
        peptid=leaderboard[i]
        linearspect=linearspectrum(peptid)
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

def maxs(peptid):
    weight=0
    for pep in peptid:
        weight+=int(pep)
    return weight

def cyclicscore(spectrum,experimentalspectrum):
    score=0
    spectrum1=spectrum.copy()
    for element in experimentalspectrum:
        if element in spectrum1:
            score+=1
            spectrum1.remove(element)
    return score

def cyclicspectrum(peptid):
    prefixmass=list()
    prefixmass.append(0)
    for i in range(0,len(peptid)):
        for j in range(57,201):
            if int(peptid[i]) == j:
                somme=prefixmass[i]+j
                prefixmass.append(somme)
    peptidmass=prefixmass[len(prefixmass)-1]
    cyclicspectrum=list()
    cyclicspectrum.append(0)
    for i in range(0,len(peptid)):
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

def expande(candidatepeptids):
    newcandidatepeptids=list()
    for cpeptid in candidatepeptids:
        for i in range(57,201):
            newcpeptid=cpeptid.copy()
            newcpeptid.append(str(i))
            newcandidatepeptids.append(newcpeptid)
    return newcandidatepeptids

def l200leaderboardcyclosequencing(experimentalspectrum,n):
    leaderboard=[[]]
    leaderpeptid=list()
    parentmass=0
    leaderpeptids=list()
    leaderscores=list()
    for mass in experimentalspectrum:
        if int(mass) > parentmass:
            parentmass=int(mass)
    while len(leaderboard)!=0:
        newleaderboard=expande(leaderboard)
        leaderboard=newleaderboard.copy()
        l=len(leaderboard)
        i=0
        while i < l :
            peptid=leaderboard[i]
            spectrum=cyclicspectrum(peptid)
            score=cyclicscore(spectrum,experimentalspectrum)
            leaderspectrum=cyclicspectrum(leaderpeptid)
            leaderscore=cyclicscore(leaderspectrum,experimentalspectrum)
            if maxs(peptid) == parentmass:
                if score >= leaderscore:
                    leaderscores.append(score)
                    leaderpeptids.append(peptid)
                    leaderpeptid=peptid
                    print(score,leaderscore)
            elif maxs(peptid) > parentmass :
                leaderboard.remove(peptid)
                i-=1
                l-=1
            i+=1
        print("done")
        leaderboard=Trim(leaderboard,experimentalspectrum,n)
    l=len(leaderscores)
    i=0
    while i < l :
        if leaderscores[i]!=leaderscore:
            leaderpeptids.remove(leaderpeptids[i])
            leaderscores.remove(leaderscores[i])
            l-=1
            i-=1
        i+=1
    return leaderpeptids

    



with open("dataset.txt","r") as f : 
    lst=f.readlines()
    for i in range(len(lst)):
        lst[i]=lst[i].replace("\n","")
    n=int(lst[0])
experimentalspectrum=lst[1].split(" ")

ans=l200leaderboardcyclosequencing(experimentalspectrum,n)

with open("answear.txt","w") as d: 
    stri=''
    for b in ans : 
        stri=""
        for a in b :
            stri+=a+"-"
        sto=stri[:len(stri)-1]
        d.write(sto+" ")



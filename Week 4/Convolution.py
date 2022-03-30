def convolution(spectrum):
    composition=list()
    part=0
    for element in spectrum:
        for elemnt in spectrum:
            part=int(elemnt)-int(element)
            if part  > 0 :
                composition.append(str(part))
    composition.sort()
    return composition

    

with open("dataset.txt","r") as f : 
    data=f.read()
    data=data.replace("\n","")
    spectrum=data.split( )

convolution(spectrum)
with open("answear.txt","w") as d :
    stro=''
    for part in convolution(spectrum):
        stro+=part+" "
    sti=stro[:len(stro)-1]
    d.write(sti)
def isUniversal(kString, k):
    kmers = set()
    for i in range(len(kString) - k + 1):
        kmers.add(kString[i:i+k])
    return len(kmers) == len(kString) - k + 1

def gen_bin_strs(n):
    return [bin(i)[2:].zfill(n) for i in range(2**n)]

k = 9
count = 0
bin_strs = gen_bin_strs(2**k + k - 1)

for kString in bin_strs:
    if isUniversal(kString, k):
        print(kString)
        count += 1

print(count)



    
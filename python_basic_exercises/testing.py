def encode(n):
    L1 = [ord('9')-ord(c) for c in str(n)]
    L2 = [str(x) for x in L1]
    return int(''.join(L2) )

print(encode("88324576987143"))
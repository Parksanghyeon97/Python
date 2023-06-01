
# print(ord('A'),ord('Z'))  #65-91

'''
for i in range(65,91):
    print(i, chr(i))
'''
"""
encbook = {}
for i in range(0,26):
    # print(chr(i+65), i)
    encbook[chr(i+65)] = i
print(encbook)

decbook = {}
for k,v in encbook.items():
    decbook[v] = k

print(decbook)
"""

keytable = map(lambda  x: (chr(x+65),x), range(26))
encbook = dict(keytable)
decbook = {v: k for k,v in encbook.items()}

print(encbook)
print(decbook)
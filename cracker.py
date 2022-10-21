import hashlib
import sys

if (len(sys.argv) != 3):
    print("modo de uso: python3 ./cracker.py <hashes.txt> <wordlist.txt>")
    exit()

hashes = sys.argv[1]
wordlist = sys.argv[2]

file = open(hashes, "r")
to_crack = file.readlines()
file.close()

with open(wordlist, "r", encoding="utf-8") as file:
    for x in file:
        x = x.strip('\n')
        hash = hashlib.md5(x.encode())
        hash = hash.hexdigest()
        for i in to_crack:
            i = i.strip('\n')
            if i == hash:
                print(f"[*] found {x}:{i}")
            else:
                continue

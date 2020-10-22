import simplecrypt
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open('passwords.txt') as f:
    for line in f:
        try:
            x=simplecrypt.decrypt(line.strip(),encrypted)
            print(x)
            break
        except simplecrypt.DecryptionException:
            print('Bad password or corrupt / modified data.')



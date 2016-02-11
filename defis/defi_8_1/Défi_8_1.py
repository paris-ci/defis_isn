def cesarC(mot, cle):
    enc = ""
    l = len(mot)
    mot = mot.replace(" ", "")
    mot = mot.upper()

    for i in range(l):
        asc = ord(mot[i])
        mot = mot.replace(" ", "")
        if asc >= 65 or asc <= 90:
            asc += cle
            if asc > 91:
                asc -= 26
            if asc < 65:
                asc += 26
        enc += chr(asc)

    return enc

print(cesarC("europe", 5))

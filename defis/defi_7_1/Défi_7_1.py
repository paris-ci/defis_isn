import math

def triangle():
    nbases = int(input("entrer un entier impair qui seras la basede votre sapin de noël"))
    nbespacesext = math.floor(nbases / 2)
    nbespacesmil = 0
    premierelignedusapin = 0
    while nbespacesext > 0:
        ValeurAAfficher = ""
        if premierelignedusapin == 0:
            for i in range(0,nbespacesext):
                ValeurAAfficher += " "
            ValeurAAfficher += "*"
            for i in range(0,nbespacesext):
                ValeurAAfficher = ValeurAAfficher + " "
            print(ValeurAAfficher)
            ValeurAAfficher = ""
            premierelignedusapin = 1
            nbespacesext = nbespacesext - 1
            nbespacesmil = nbespacesmil + 1
        if nbases > 3:
            for i in range(0,nbespacesext):
                ValeurAAfficher = ValeurAAfficher + " "
            ValeurAAfficher = ValeurAAfficher + "*"
            for i in range(0,nbespacesmil):
                ValeurAAfficher = ValeurAAfficher + " "
            ValeurAAfficher = ValeurAAfficher + "*"
            for i in range(0,nbespacesext):
                ValeurAAfficher = ValeurAAfficher + " "
            print (ValeurAAfficher)
            nbespacesext = nbespacesext - 1
            nbespacesmil = nbespacesmil + 2
    print(nbases*"*")


triangle()
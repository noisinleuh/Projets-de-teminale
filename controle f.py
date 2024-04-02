# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:56:55 2024

@author: MBERRIN
"""

def controle_f(texte, mot):
    for lettre in range(len(texte)-(len(mot)-1)):
        if texte[lettre:lettre+(len(mot))]==mot:
            return lettre, controle_f(texte[lettre+1:], mot)
    return -1

def construction(m):
    T={}
    for a in range(32,254):
        T[chr(a)]=len(m)
    T['\n']=len(m)
    for k in range(0,len(m)-1):
        T[m[k]]=len(m)-k-1
    return T  

def recherche(m,texte):
    T=construction(m)
    j=len(m)-1
    while j<len(texte):
        if texte[j-(len(m)-1):j+1]==m:
            return j-(len(m)-1)
        else:
            j+=T[texte[j]]
            #print(j, texte[j:])
    return 'pas dans la chaine'
   
texte = "TOUS LES HOMMES NAISSENT ET DEMEURENT LIBRES ET EGAUX EN DROIT" 

print(recherche('LIBRES',texte))

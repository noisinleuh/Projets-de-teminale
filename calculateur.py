# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 08:41:49 2024

@author: MBERRIN
"""

from math import*
from numpy import*
from sympy import*

class pile:
    
    def __init__(self):
        self.int = []
        
    def __str__(self):
        return str(self.int)
    
    def est_vide(self):
        return len(self.int) == 0

    def empiler(self, el):
        self.int.append(el)

    def depiler(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        return self.int.pop()

    def sommet(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        return self.int[-1]

    def taille(self):
        return len(self.int)


def evaluer(chaine:str):
    """

    Parameters
    ----------
    chaine : str
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    
    liste=npi(chaine)
    nb=pile()
    for i in liste:
        if type(i)==float:
            nb.empiler(i)
        if i=='pi':
            nb.empiler(pi)
        elif i=='+':
            a=nb.depiler()
            b=nb.depiler()
            nb.empiler(b+a)
        elif i=='-':
            a=nb.depiler()
            b=nb.depiler()
            nb.empiler(b-a)
        elif i=='*':
            a=nb.depiler()
            b=nb.depiler()
            nb.empiler(b*a)
        elif i=='/':
            a=nb.depiler()
            b=nb.depiler()
            nb.empiler(b/a)
        elif i=='^':
            a=nb.depiler()
            b=nb.depiler()
            nb.empiler(b**a)
        elif i=='ln':
            a=nb.depiler()
            nb.empiler(log(a))
        elif i=='exp':
            a=nb.depiler()
            nb.empiler(exp(a))
        elif i=='cos':
            a=nb.depiler()
            nb.empiler(cos(a))
        elif i=='sin':
            a=nb.depiler()
            nb.empiler(sin(a))  
    return nb.depiler()
        
        
def npi(chaine):
    """

    Parameters
    ----------
    chaine : str
        DESCRIPTION.

    Returns
    -------
    out : list
        DESCRIPTION.

    """
    l=chaine
    Opérateurs=['+','/','*','-','^']
    Opé={'+':1,
         '-':1,
         '*':2,
         '/':2,
         'ln':4,
         'exp':4,
         'sin':4,
         'cos':4,
         '^':3}
    op=[]
    out=[]
    compt=0
    le=len(l)
    for j in range(le):
        if le-j==compt:
            break
        if l[j]=='p' and l[j+1]=='i':
            out.append(pi)
            l=l[:j]+l[j+1:]
            compt+=1
        elif l[j].isdigit():
            k=0
            while len(l[j:])>1 and (l[j+k].isdigit() or l[j+k]=='.'):
                k+=1
            if k!=0:
                out.append(float(l[j:j+k]))
            else:
                out.append(float(l[j]))
            for m in range(k-1):
                l=l[:j]+l[j+1:]
            if k!=0:
                compt+=k-1
        elif ord(l[j])<=122 and ord(l[j])>=97:
            k=0
            if l[j]=='x' or l[j]=='y':
                out.append(l[j])
            else:
                while len(l[j:])>1 and l[j+k]!='(':
                    k+=1
                op.append(l[j:j+k])
                for m in range(k-1):
                    l=l[:j]+l[j+1:]
                compt+=k-1
        elif l[j] in Opérateurs:
            while op!=[] and op[-1]!='(' and Opé[op[-1]]>=Opé[l[j]]:
                out.append(op.pop())
            op.append(l[j])
        elif l[j]=='(':
            op.append(l[j])
        elif l[j]==')':
            while op!=[] and op[-1]!='(':
                out.append(op.pop())
            op.pop()
    while op!=[]:
        out.append(op.pop())
    return out

def separation(expression):
    if expression=="" or expression==" ":
        raise SyntaxError
    for i, ex in enumerate(expression):
        if ex == '*':
            return [expression[:i]]+separation(expression[i+1:])
    return [expression]

def exprime(ex):
    for i in range(len( ex)):
        if ex[i][0]=='(':
            ex[i]=ex[i][1:-1]
    return ex

def tableur(ex):
    liste=[]
    ex+='+'
    for j in range(len(ex)):
        a=0
        b=1
        c=False
        if ex[j]=='+' or (ex[j]=='-' and j-1<0):
            g=j
            j=j-1
            while j!=-1 and ex[j]!='+' and ex[j]!='-':
                if ex[j]=='x' or ex[j]=='i':
                    a=0
                    break
                a=ex[j-1:g]
                j-=1
            a=float(a)
        elif ex[j]=='x':
            o=['+','-']
            if ex[j+1] in o: 
                b=1
            if ex[j+1]=='i': 
                c=True
                if ex[j+2] in o: 
                    b=1
            elif ex[j+1]=='^':
                g=j+2
                while g<len(ex) and ex[g]!='+' and ex[g]!='-':
                    b=ex[j+2:g+1]
                    g+=1
                b=int(b)
            if j-1<0:
                a=1
            else:
                if ex[j-1]=='+':
                    a=1
                elif ex[j-1]=='-':
                    a=-1
                else:
                    g=j
                    while j!=-1 and ex[j]!='+' and ex[j]!='-':
                        if ex[j]=='i':
                            c=True
                            if ex[j-1]=='+':
                                a=1
                                break
                            elif ex[j-1]=='-':
                                a=-1
                                break
                        a=ex[j:g]
                        j-=1
                    a=float(a)
            b=2*b+1
            if c:
                b-=1
        elif ex[j]=='i':
            if j+1>len(ex)  or  ex[j+1]=='x':
                None
            elif j-1<0 :
                a=1
                b=0
            elif ex[j-1]=='x':
                None
            else:
                b=0
                if ex[j-1]=='+': 
                    a=1
                elif ex[j-1]=='-':
                    a=-1
                else:
                    g=j
                    j=j-1
                    while j!=-1 and ex[j]!='+' and ex[j]!='-':
                        if ex[j]=='x':
                            a=0
                            break
                        a=ex[j-1:g]
                        j-=1
                    a=float(a)
        l=[]
        for m in range(b):
            l.append(0)
        l.append(a)
        liste=add(liste,l)
    return liste
            
            
def add(liste,l):
    if len(liste)>len(l):
        for r in range( len(liste)-len(l)):
            l.append(0)
    else:
        for r in range(len(l)-len(liste)):
            liste.append(0)
    for i in range(len(l)):
        liste[i]=liste[i]+l[i]
    return liste


def developpe(expression):
    expression=separation(expression)
    expression=exprime(expression)
    tableau=tableur(expression[0])
    rendre=[]
    for i in range(1,len(expression)):
        t=tableur(expression[i])
        if len(tableau)>len(t):
            for r in range( len(tableau)-len(t)):
                t.append(0)
        else:
            for r in range(len(t)-len(tableau)):
                tableau.append(0)
    for j in range(len(tableau)):
        for k in range(len(t)):
            if tableau[j]!=0 and t[k]!=0:
                l=[]
                if j%2!=k%2:
                    for m in range(j+k-1):
                        l.append(0)
                    l.append(tableau[j]*t[k])
                elif j%2==0 and k%2==0:
                    for m in range(j+k+1):
                        l.append(0)
                    l.append(-tableau[j]*t[k])
                elif j%2==1 and k%2==1:
                    for m in range(j+k-1):
                        l.append(0)
                    l.append(tableau[j]*t[k])
                rendre=add(rendre,l)
    rendre=ecr(rendre)
    return rendre

def ecr(liste):
    s=''
    first=True
    for i,ex in enumerate(liste):
        if ex!=0:
            if ex-int(ex)==0:
                ex=int(ex)
            if i==1:
                s+=str(ex)
            elif i==0:
                s+=str(ex)+'i'
            elif i==3:
                if ex>0 and not first:
                    s+='+'
                s+=str(ex)+'x'
            elif i==2:
                if ex>0 and not first:
                    s+='+'
                s+=str(ex)+'ix'
            elif i>3:
                if ex>0 and first==False:
                    s+='+'
                if i%2==1:
                    s+=str(ex)+'x^'+str(i//2)
                else:
                    s+=str(ex)+'ix^'+str(i//2)
            first=False
    return s

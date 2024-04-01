
#decimal en binaire
def decbin(x):
    rendre=""
    if x==0:
        return str(0)
    while x!=0:
        b=str(x%2)
        x=x//2
        rendre=b+rendre
    return rendre

#binaire en decimal
def bindec(x):
    st=str(x)
    n=len(st)
    rendre=0
    for i in range(n):
        rendre+=int(st[n-1-i])*2**i
    return rendre

#addition de nombre en binaire
def addibin(a,b):
    max_len=max(len(a),len(b))
    a=a.zfill(max_len)
    b=b.zfill(max_len)
    retenue=0
    résultat=""
    i=-1
    for k in range(max_len):
        c=int(a[i])+int(b[i])+retenue
        if c==0:
            résultat=str(0)+résultat
            retenue=0
        elif c==1:
            résultat=str(1)+résultat
            retenue=0
        elif c==2:
            résultat=str(0)+résultat
            retenue=1
        elif c==3:
            résultat=str(1)+résultat
            retenue=1
        i=i-1
    if retenue==1:
        résultat=str(retenue)+résultat
    return résultat

#addition en décimal fixe
def addibin_fixe(a,b,c):
    max_len=c
    a=a.zfill(max_len)
    b=b.zfill(max_len)
    retenue=0
    résultat=""
    i=-1
    for k in range(max_len):
        if int(a[i])+int(b[i])+retenue==0:
            résultat=str(0)+résultat
            retenue=0
        elif int(a[i])+int(b[i])+retenue==1:
            résultat=str(1)+résultat
            retenue=0
        elif int(a[i])+int(b[i])+retenue==2:
            résultat=str(0)+résultat
            retenue=1
        elif int(a[i])+int(b[i])+retenue==3:
            résultat=str(1)+résultat
            retenue=1
        i=i-1
    return résultat[-c:]

#soustraction de nombres binaire
def sousbin(a,b):
    max_len=max(len(a),len(b))
    a=a.zfill(max_len)
    b=b.zfill(max_len)
    retenue=0
    résultat=""
    i=-1
    for k in range(len(a)):
        if int(a[i])-(int(b[i])+retenue)==0:
            résultat=str(0)+résultat
            retenue=0
        elif int(a[i])-(int(b[i])+retenue)==1:
            résultat=str(1)+résultat
            retenue=0
        elif int(a[i])-(int(b[i])+retenue)==-1:
            résultat=str(1)+résultat
            retenue=1
        i=i-1
    return résultat

#base 16 --> base 10
def hexadec(x):
    st=str(x)
    n=len(st)
    rendre=0
    for i in range(n):
        a=st[n-1-i]
        code=ord(a)
        if code>=65 and code<=90:
            a=ord(a)-55
        rendre+=int(a)*16**i
    return rendre

#base 10 --> base 16
def dechexa(x):
    rendre=""
    if x==0:
        return str(0)
    while x!=0:
        b=(x%16)
        print(b)
        if b>=10 and b<=16:
            b=chr(b+55)
            print(b)
        x=x//16
        rendre=b+rendre
    return rendre

#conversion de n'importe quelle base à n'importe quelle autre entre 2 et 36
def base_en_base(a,b1,b2):
    st=str(a)
    n=len(st)
    rendre=0
    for i in range(n):
        x=st[n-1-i]
        code=ord(x)
        if code>=65 and code<=90:
            x=ord(x)-55
        rendre+=int(x)*b1**i
    résultat=""
    rendre=int(rendre)
    if rendre==0:
        return 0
    while rendre!=0:
        b=(rendre%b2)
        if b>=10 and b<=b2:
            b=chr(b+55)
        rendre=rendre//b2
        résultat=str(b)+résultat
    return résultat

#decimal en complément à deux
def decicompl(x):
    if x>=0:
        return str(0)+decbin(x)
    else:
        a=decbin(abs(x))
        chan=""
        for i in a:
            if i==str(1):
                chan=chan+str(0)
            if i==str(0):
                chan=chan+str(1)
        r=addibin(chan,"1")
        r=str(1)+r
        return r

#complément à deux en décimal
def compldeci(x):
    if x[0]==0:
        return bindec(x)
    else:
        a=sousbin(x,"1")
        chan=""
        for i in a:
            if i==str(1):
                chan=chan+str(0)
            if i==str(0):
                chan=chan+str(1)
        r=bindec(chan)
        return -r

#décimal flottant en binaire
def floatbin(x):
    a,b=str(x).split(".")
    a=decbin(int(a))
    b="0."+b
    rendre=""
    b=float(b)
    while b!=0:
        r=b*2
        c,b=str(r).split(".")
        b="0."+str(b)
        b=float(b)
        rendre+=c
    return a+"."+rendre

#binaire en décimal flottant
def binfloat(x):    
    a,b=str(x).split(".")
    a=bindec(a)
    rendre=0
    f=1
    for i in b:
        rendre+=int(i)*2**-f
        f+=1
    return a+rendre

#multiplication de nombres binaires    
def multibin(a,b):
    rendre="0"
    r=-1
    zéro=""
    for i in range(len(b)):
        part=""
        part=zéro
        x=-1
        for s in range(len(a)):
            part=str(int(b[r])*int(a[x]))+part
            x=x-1
        rendre=addibin(rendre, part)
        r=r-1
        zéro=zéro.zfill(1)
    return rendre

#multiplication de nombres binaires avec nombre de bits fixe
def multibin_fixe(a,b,c):
    rendre="0"
    r=-1
    zéro=""
    for i in range(len(b)):
        part=""
        part=zéro
        x=-1
        for s in range(len(a)):
            part=str(int(b[r])*int(a[x]))+part
            x=x-1
        rendre=addibin(rendre, part)
        r=r-1
        zéro=zéro.zfill(1)
    return rendre[-c:]


#decimal en ieee 754  
def decieee(x,bits):
    rendre=""
    exposant=0
    if type(x) is float:
        mantisse=x
        mantisse=floatbin(mantisse) 
        if x>1:
            avant,apres=str(mantisse).split(".")
            avant=avant[1:len(avant)]
            exposant=len(avant)
            mantisse=avant+apres
        else:
            avant,apres=str(mantisse).split(".")
            mantisse=avant+apres
            exposant=0
            while mantisse[0]=="0":
                exposant+=1
                mantisse=mantisse[1:len(mantisse)]
            mantisse=mantisse[1:len(mantisse)]
    else:
        mantisse=decbin(x)
        mantisse=mantisse
        mantisse=mantisse[1:len(mantisse)]
        exposant=len(mantisse)           
    if bits==1:
        exposant+=127
    if bits==2:
        exposant+=1023
    exposant=decbin(exposant)
    rendre=mantisse+rendre
    remplir=""
    if bits==1:
        remplir=remplir.zfill(23-len(mantisse))
    if bits==2:
        remplir=remplir.zfill(52-len(mantisse))
    rendre+=remplir
    if bits==1:
        rendre=exposant.zfill(8)+rendre
    if bits==2:
        rendre=exposant.zfill(11)+rendre
    if x>=0:
        rendre=str(0)+rendre
    else:
        rendre=str(1)+rendre
    return rendre

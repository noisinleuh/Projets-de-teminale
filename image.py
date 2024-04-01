from PIL.Image import*
imgin=str(input("nom complet de l'image "))


#PROGRAMME NON RECURSIF
"""
img=open(imgin)
largeur,hauteur=img.size
imgModif=new("RGB", (largeur,hauteur))

for i in range(largeur):
    for j in range(hauteur):
        R,V,B=img.getpixel((i,j))
        imgModif.putpixel((j,i), (R,V,B))
    
img.close()
imgModif.save(imgin)
imgModif.show() 
"""

#PROGRAMME RECURSIF
img=open(imgin)
largeur,hauteur=img.size
img.load()
def retourne(img, largeur, hauteur):
    #CONDITION D'ARRET (TAILLE DE L'IMAGE 2/2)
    if (largeur,hauteur)==(2,2):

        R1,V1,B1=img.getpixel((0,0))
        R2,V2,B2=img.getpixel((1,0))
        R3,V3,B3=img.getpixel((1,1))
        R4,V4,B4=img.getpixel((0,1))
        img.putpixel((1,0), (R4,V4,B4))
        img.putpixel((1,1), (R3,V3,B3))
        img.putpixel((0,1), (R1,V1,B1))
        img.putpixel((0,0), (R2,V2,B2))
        return img
    else:
        #CREATION DE REGIONS
        box1=(0,0,largeur//2,hauteur//2)
        box2=(largeur//2,0,largeur,hauteur//2)
        box3=(0,hauteur//2,largeur//2, hauteur)
        box4=(largeur//2,hauteur//2,largeur,hauteur)
        #DECOUPAGE DE L'IMAGE SELON CES REGIONS
        region1 = img.crop(box1)
        region2 = img.crop(box2)
        region3 = img.crop(box3)
        region4 = img.crop(box4)
        #PARTIE RECURSIVE (RETOURNE SUCCESSIVEMENT CHAQUE REGION)
        region1=retourne(region1, largeur//2, hauteur//2)
        region2=retourne(region2, largeur//2, hauteur//2)
        region3=retourne(region3, largeur//2, hauteur//2)
        region4=retourne(region4, largeur//2, hauteur//2)
        #CREATION DE LA NOUVELLE IMAGE ET COLLAGE DES REGIONS RETOURNEES
        nouv=new("RGB", (largeur,hauteur))
        nouv.paste(region1,box3)
        nouv.paste(region2,box1)
        nouv.paste(region3,box4)
        nouv.paste(region4,box2)
        return nouv

#OUVERTURE DE L'IMAGE ET LANCEMENT DU PROGRAMME        
imgModif=retourne(img,largeur,hauteur)
imgModif.show() 
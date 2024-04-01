from math import sqrt, pi
from random import randint
import pyxel

pyxel.init(512, 512, title="bubules")



class bulles:
    """
    Classe des bulles ennemies
    """
    def __init__(self, color):
        """
        Initialisation des bulles, prend en paramètre la couleur du joueur pour
        ne pas avoir de bulles de la même couleur
        """
#rayon au hasard entre 5 et 10 pixels
        self.rayon = randint(5,20) 
#position horizontale aléatoire
        self.x = randint(self.rayon,512-self.rayon)
#permets aux bulles d'apparaitre suffisamment loin du joueur (au centre)
        while self.x in [i for i in range(256-50,256+51)]:
            self.x = randint(self.rayon,512-self.rayon)
#position verticale aléatoire
        self.y = randint(self.rayon,512-self.rayon)
#permets aux bulles d'apparaitre suffisamment loin du joueur (au centre)
        while self.y in [i for i in range(256-50,256+51)]:
            self.y = randint(self.rayon,512-self.rayon)
#direction aléatoire (!= 0)
        self.dirx = float(randint(-3, 3))
        while self.dirx==0:
            self.dirx = float(randint(-3, 3))
        self.diry = float(randint(-3, 3))
        while self.diry==0:
            self.diry = float(randint(-3, 3))
#couleur aléatoire (!= couleur du joueur)
        self.couleur = randint(1, 15)
        while self.couleur==color:
            self.couleur = randint(1, 15)
    
    def bouge(self):
        """
        déplacament de la bulle

        """
        self.x+=self.dirx
        self.y+=self.diry
#empêche la bulle de dépasser le bord
        if self.x>512-self.rayon or self.x<self.rayon:
            self.dirx=-self.dirx
        if self.y>512-self.rayon or self.y<self.rayon:
            self.diry=-self.diry
           
    def __repr__(self):
        """
        purement pour des raisons pratiques, représentent les valeurs 
        contenues dans la bulle

        """
        return f"x = {self.x}\ny = {self.y}\ndirx = {self.dirx}\ndiry = {self.diry}\nrayon = {self.rayon}\ncouleur = {self.couleur}\n"

    def distance(self,b2):
        """
        Calcule la distance entre cette bulle et une autre
        """
        return sqrt(((b2.x-self.x)**2)+((b2.y-self.y)**2))

    def contact(self,b2):
        """
        Rend True si les bulles sont en contact
        """
        return self.distance(b2)<=self.rayon+b2.rayon//2


def premierlibre(Mousse):
    """
    Premier emplacement libre de la liste contenant toutes les bulles de l'écran
    """
    i=0
    while i<len(Mousse) and Mousse[i]!=None:
        i+=1
    return i

def place(b):
    """
    insère une nouvelle bulle dans la liste de bulle lorsqu'il en manque
    """
    i=premierlibre(Mousse)
    if i<len(Mousse):
        Mousse[i]=b


def collision(indp,indg,mousse):
    """
    Fais fusionner deux bulles lors d'une collision avec l'indice de la plus 
    petite des deux (indp), de la plus grand (indg) et l'entièreté de la liste
    """
    surfp=pi*mousse[indp].rayon**2
    surfg=pi*mousse[indg].rayon**2
    surfg+=surfp
#grossit la plus grande bulle
    mousse[indg].rayon=int(sqrt(surfg/pi))
#supprime la plus petite bulle
    mousse[indp]=None
    return mousse



class Jeu:
    """
    Classe de la bulle du joueur
    """
    def __init__(self,color):
        """
        Initialisation du joueur, prend en paramètre la couleur sélectionnée
        """
#rayon au début du jeu
        self.rayon = 20
#coordonnées au début du jeu (centre)
        self.x = 512//2
        self.y = 512//2
#direction initiale (aucune)
        self.dirx = 0
        self.diry = 0
#couleur (pré selectionnée)
        self.couleur = color
        
    def de(self):
        """
        direction du joueur en fonction des touches pressées
        """
        if pyxel.btnp(pyxel.KEY_UP):
            self.diry=-4
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.diry=4
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.dirx=4
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.dirx=-4

    def b(self):
        """
        déplacement du joueur en fonction de la direction
        """
#déplacement horizontale
        if self.x<512-self.rayon and self.x>self.rayon:
            self.x+=self.dirx
#empêche le joueur de sortir du cadre de jeu
        elif self.x>512-self.rayon:
            self.x=512-3-self.rayon 
            self.dirx=0
        elif self.x<self.rayon:
            self.x=3+self.rayon
            self.dirx=0
#déplacement horizontale
        if self.y<512-self.rayon and self.y>self.rayon:
            self.y+=self.diry
#empêche le joueur de sortir du cadre de jeu
        elif self.y>512-self.rayon:
            self.y=512-3-self.rayon 
            self.diry=0
        elif self.y<self.rayon:
            self.y=3+self.rayon
            self.diry=0
            
    def collision(self,ind,mousse):
        """
        collision entre le joueur et une bulle plus petite
        """
        surf=pi*self.rayon**2
        surfb=pi*mousse[ind].rayon**2
        surf+=surfb
#grossit la bulle du joueur
        self.rayon=int(sqrt(surf/pi))
#supprime la petite bulle
        mousse[ind]=None
        return mousse
    
    
        
"""
initialisation/création des paramètres communs à toutes fonctions au lancement 
du jeu
"""
#couleur par défaut
color=1
#indique que nous somme en phase d'initialisation au lancement du programme
ini=True
#variable utile pour le petit rectancle rouge de selection de couleur au lancement
fl=1
#indique si le joueur est en game over
G=False
#compteur d'itérarions de la fonction update (30 fois par seconde)
compteur=0
#compteur de secondes (+1 toutes les 30 "compteur")
c=0
#liste des scores faits par le joueur
score=[]
#variable utile pour l'affichage des scores
g=1
#indique si le jeu est en pause
P=False

def update():
    """ 
    mise à jour des valeurs 30 fois par seconde
    """
#définitions des variables modifiables pour l'ensemble du programme (qui ne se réinitialisent pas à chaque itération)
    global Mousse,J,G, compteur,c, ini, fl,color,g,score,P
#lorsque le joueur n'est ni dans la phase d'initialisation ni en pause
    if ini==False:
        if P==True:
#la pause s'arrete si le bouton espace est pressé, les paramètres ne sont plus mis à jour en attendant
            if pyxel.btnp(pyxel.KEY_SPACE):
                P=False
        else:
            #pour chaque bulle, si elle existe, se déplace
            for bulle in range(len(Mousse)):
                if Mousse[bulle]!=None:
                    Mousse[bulle].bouge()
#les bulles ennemoes rétrecissent d'un dixième de leur taille chaque seconde
                    if c%3==0 and compteur%30==0:
                        Mousse[bulle].rayon= Mousse[bulle].rayon-Mousse[bulle].rayon//10
#les bulles trop petites disparaissent
                    if Mousse[bulle].rayon<5:
                        Mousse[bulle]=None
#rajoute une bulle si il en manque
                place(bulles(color))
#mise à jour de la position et du déplacement du joueur
            J.de()
            J.b()
#pour chaque bulle, on teste la collision avec le joueur
            for i in range(len(Mousse)):
                if Mousse[i].distance(J)<=Mousse[i].rayon+J.rayon:
                    #si oui et le joueur et plus grand, la bulle est mangée
                    if J.rayon>Mousse[i].rayon:
                        Mousse=J.collision(i, Mousse)
                    #si oui et le joueur est plus petit, game over
                    elif J.rayon<Mousse[i].rayon:
                        G=True
#lorsque le joueur n'est pas en game over
            if G==False:
                compteur+=1
                #augmentation du compteur de seconde (score) chaque 30 itérations
                if compteur%30==0:
                    c+=1
                    compteur=0
                    if J.rayon>20:
#si le joueur à un rayon > 20, chaque seconde, son rayon rétrécie d'un dixieme
                        J.rayon= J.rayon-J.rayon//10
                g=1
#pause si espace est pressé
                if pyxel.btnp(pyxel.KEY_SPACE):
                    P=True
#lors d'un game over
            else:
                if g==1:
#ajout du score à la liste de score (le petit g permet de ne l'ajouter qu'une fois)
                    score.append(c)
                    g=0
#fin du game over si espace ou entrée est pressée
                if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN):
#réinitialisation de la liste de bulles, du joueur, du compteur et des indicateurs de game over et pause
                    Mousse=[]
                    for i in range(25):
                        Mousse.append(bulles(color))
                    J=Jeu(color)
                    G=False
                    compteur=0
                    c=0
                    P=False
#lors de l'initialisation
    else:
#déplacement vers la droite du petit rectangle de selection
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if fl<32*14:
                fl+=32
#déplacement vers la gauche du petit rectangle de selection
        if pyxel.btnp(pyxel.KEY_LEFT):
            if fl>=32:
                fl-=32
#début du jeu lorsque entrée est pressée
        if pyxel.btnp(pyxel.KEY_RETURN):
#choix de la couleur du joueur, initialisation du joueur, de la liste de bulle et fin de la phase d'initialisation
            color=(fl//32)+1
            J=Jeu(color)
            Mousse=[]
            for i in range(25):
                Mousse.append(bulles(color))
            ini=False
    


def draw():
    """
    dessine les bulles 30 fois par seconde
    """
#je ne vais pas vous mentir cette partie est bien moche mais elle fonctionne et j'ai trop peur de changer quoi que ce soit, tout devrait être dans la fonction update mais si j'essaye de les y mettre ça ne fonctionne plus
#définitions des variables modifiables pour l'ensemble du programme (qui ne se réinitialisent pas à chaque itération)
    global Mousse,J,G,c, ini,fl,score,P
#lorsque le joueur n'est pas en phase d'initialisation ni de game over
    if ini==False:
        if G==False:
            pyxel.cls(0)
#pour chaque bulle existante
            for bulle in range(len(Mousse)):
                if Mousse[bulle]==None:
                    None
                elif Mousse[bulle]!=None:
                    for bulle2 in range(len(Mousse)):
#pour toutes les autres bulles existantes
                        if Mousse[bulle2]==None or Mousse[bulle]==None:
                            None
                        elif bulle!=bulle2:
#si les deux bulles sont en contact, effectuer une collision
                            if Mousse[bulle].contact(Mousse[bulle2]):
                                if Mousse[bulle].rayon>Mousse[bulle2].rayon:
                                    Mousse=collision(bulle2, bulle, Mousse)
                                    pyxel.circ(Mousse[bulle].x, Mousse[bulle].y, Mousse[bulle].rayon, Mousse[bulle].couleur)
                                else:
                                    Mousse=collision(bulle, bulle2, Mousse)
                                    pyxel.circ(Mousse[bulle2].x, Mousse[bulle2].y, Mousse[bulle2].rayon, Mousse[bulle2].couleur)
#honnêtement je sais même plus à quoi servent les deux lignes suivantes mais si je les enlève ça ne marche plus donc je les laisse                    
                    if Mousse[bulle]!=None:
                        pyxel.circ(Mousse[bulle].x, Mousse[bulle].y, Mousse[bulle].rayon, Mousse[bulle].couleur)
#dessine le joueur
            pyxel.circ(J.x, J.y, J.rayon, J.couleur)
#si le jeu est en pause, le symbole pause s'affiche
            if P==True:
                pyxel.rect(233, 231, 20, 50, 7)
                pyxel.rect(259, 231, 20, 50, 7)
#si le jeu est en pause, fond noir, affichage du texte de game over
        else: 
            pyxel.cls(0)
            pyxel.text(245, 256, "GAME OVER :(", 8)
            pyxel.text(210, 270, "ESPACE OU ENTREE POUR REJOUER", 8)
            pyxel.text(450, 20, "YOUR SCORE", 8)
#affiche le score en colonne à droite (c'était galère donc on apprécie svp)
            for sc in range(len(score)):
                pyxel.text(450, 30+10*sc, f"{score[sc]}", 8)
        pyxel.text(15, 15, f"{c}", 8)
    else:
#pendant la phase d'initialisation, fond noir, ensemble de cercles de couleur, et rectangle rouge pour sélectionner
        pyxel.cls(0)
        for i in range(1,16):
            pyxel.circ((512//16)*i, 256, 6, i)
        pyxel.text(210,200,"ENTREE POUR CHOISIR LA COULEUR",7 )
        pyxel.rectb(23+fl,247,20,20,8)
        

#lancement du jeu à chaque lancement du programme   
pyxel.run(update, draw)  






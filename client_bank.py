from datetime import date

class Client:
    def saisie(cl):
        cl.cin=input('entrer le numéro cin : ')
        cl.nom=input('entrer le nom : ')
        cl.prenom=input('entrer le prénom : ')
class Compte:
    n=0
    def saisie(c):
        Compte.n+=1
        c.__numCompte=Compte.n
        y=int(input("entrer l'année"))
        m=int(input("entrer le mois"))
        d=int(input("entrer le jour"))
        c.dateCreation=date(y,m,d)
        c.solde=float(input('entrer le solde'))
        cl=Client()
        cl.saisie()
        c.client=cl
class Banque:
    def __init__(b):
        b.listeComptes=[]
        
    def saisie(b):        
        b.nom=input('entrer le nom de la banque')
    def ajoutCompte(b):
        c=Compte()
        c.saisie()
        b.listeComptes.append(c)
        print("Un compte vient d'être crée")


maBanque=Banque()
maBanque.ajoutCompte()
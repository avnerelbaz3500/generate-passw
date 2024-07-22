import secrets
import re

class Dico():
    
    def __init__(self,n=4,separator= '/'):
        self.n =n
        self.dict = dict
        self.separator =separator

    def __str__(self):
        return "Dictionnaire"


    def dicolist(self):
        
        """
        Cette fonction lit un fichier dictionnaire .dic, enlève ce qui est après les slashs 
        pour chaque mot, et retourne une liste de mots nettoyés.
        """
         
        mots = []
        with open('password/maincode/fr_FR.dic', 'r', encoding='utf-8')  as lignes:
            for ligne in lignes:
                ligne =  ligne.strip() 
                mot = ligne.split('/')[0]
                if mot:
                    mots.append(mot)
        return mots

    def password(self):
            
            """
            Cette fonction utilise la fonction dicolist pour générer un mot de passe de longueur choisie par l'utilisateur.
            """
            words = self.dicolist()
            
            password = (self.separator).join(secrets.choice(words) for _ in range(self.n))
            return password




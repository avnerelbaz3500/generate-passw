#Génère une série ASCII aléatoire




import random as rd

import string 

class Create():


    def __init__(self,entier,special=True,simple =False):
        self.n = entier
        self.passw = ''
        self.pwnd = self.knownpassw()
        self.special = special
        self.simple = simple

    
    def __str__(self):
        return "self.mdpANSII()"

    def genal(self):
        letters = list(string.printable)
        

        self.passw = ''
        provisory = []
        if self.simple:
            if self.special:
                provisory = rd.choices(string.ascii_letters,k = (self.n - 2)) 
                provisory += [rd.choice(string.punctuation), rd.choice(string.digits)]
                
            else :
                
                provisory = rd.choices(string.ascii_letters,k= (self.n - 1))
                provisory += [rd.choice(string.digits)]
            rd.shuffle(provisory)
            self.passw = "".join(provisory)
            return self.passw

        else:

            if self.special:
                unwanted = list(string.whitespace)
            else:
                unwanted = list(string.whitespace) + list(string.punctuation)
        
            for _ in range (self.n):
                char = rd.choice(letters)
                while char in unwanted:
                    char = rd.choice(letters)
                self.passw += char
            return self.passw





        

    # Creation et affichage d'une liste des mdp les plus utilisés

    def knownpassw(self):

        """

        Retourne la liste des mots de passes pwned

        """

        fichier=open('password/maincode/password.txt','r')
        ensemble_mdp = set(ligne.strip('\n') for ligne in fichier.readlines())
        fichier.close()
        return ensemble_mdp
    

    


    def false_mdp(self,mdp):
        """
        Teste si un mot de passe est faux

        """
        
        c1 = set(mdp).intersection(set(string.ascii_lowercase)) 
        c2 = set(mdp).intersection(set(string.ascii_uppercase))
        c3 = set(mdp).intersection(set(string.digits))
        c4 = set(mdp).intersection(set(string.punctuation))
        v= set()

        if self.special:
            return (c1 == v)  or (c2 ==v) or (c3 ==v) or (c4 ==v) 
        else:
            return (c1 == v)  or (c2 ==v) or (c3 ==v) or (mdp in self.pwnd)

    #Générateur de mot de Passe valide selon L'ANSSI

    def genpass(self):
        mdp = self.genal()
        while self.false_mdp(mdp):
            mdp = self.genal()
        return mdp

    
    def generate_passphrase(self, phrase):
        """
        
        Génère un mot de passe à partir des premiers éléments d'une phrase.


        """
        passphrase = ''
        word_started = False

        for i, char in enumerate(phrase):
            if char.isalpha():
                if not word_started:
                    passphrase += char
                    word_started = True
            elif char == ' ':
                word_started = False
            else:
                word_started = False
                passphrase += char

        return passphrase
                

        return passphrase

    #Mot de passe personnalisé

    def mdpANSII(self):
        print("Nous allons vous générer un mot de passe sécurisé selon les règles établies par l'Agence nationale de la sécurité des systèmes d'information (ANSSI).")
        print("Indication vous aurez besoin d'un mot de passe de compléxité moyenne (12 caractères) pour un employé avec des données moyennement sensible et de 15 caractères pour des données très sensibles ")
        demande = input("Pour un mot de passe très fort tapez 0, fort tapez 1, moyen tapez 2, faible tapez 3 ")
        print([demande])
        if demande == '0':
            print(self.genpass(20))
        elif demande == '1':
            print(self.genpass(15))
        elif demande == '2':
            print(self.genpass(12))
        else :
            print(self.genpass(8))

dico = Create(5)
print(dico.generate_passphrase("Le rire seul échappe à notre surveillance. Natalie Cliffort-Barney, 1920."))



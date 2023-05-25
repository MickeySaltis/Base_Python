### Orienté Objet

# Entité / Class

class EtreVivant: # Class Parent
    #Variable de classe
    FAMILLE = "Non Identifié"

    # Afficher une Variable de classe
    def AfficherFamilleetreVivant(self):
            print(f"Info être vivant: {self.FAMILLE}.")


class Chat(EtreVivant): # Class Enfant
    #Variable de classe
    FAMILLE = "Félin"


class Personne(EtreVivant): # Class Enfant

    #Variable de classe
    FAMILLE = "Hominidé"
    ESPECE_ETRE_VIVANT = "Humain"

    #Constructeur
    def __init__(self, nom: str = "", age: int = 0):

        #Variable d'instance
        self.nom = nom 
        self.age = age

        # Condition
        if nom == "":
            self.DemanderNom()

        print(f"Construction de la personne {self.nom}.")


    def SePresenter(self):
        #Variable
        info_prenom = "Bonjour, je m'appelle " + self.nom

        if self.age == 0:
            print(f"{info_prenom}.")
        else:
            print(f"{info_prenom} et j'ai {self.age} ans.")

            if self.EstMajeur():
                print(f"Je suis majeur.")
            else:
                print(f"Je ne suis pas majeur.")

    # Afficher une Variable de classe
    def AfficherInfosetreVivant(self):
            print(f"Info être vivant: {self.ESPECE_ETRE_VIVANT}.")
        # Ou avec une méthode de classe
        # def AfficherInfosetreVivant(self):
            # print(f"Info être vivant: {Personne.ESPECE_ETRE_VIVANT}.")
        # Ou avec une méthode de classe
        # def AfficherInfosetreVivant():
            # print(f"Info être vivant: {Personne.ESPECE_ETRE_VIVANT}.")
                # == Personne.AfficherInfosetreVivant()

    # Boolean
    def EstMajeur(self):
       return self.age >= 18
    
    # Demander Nom
    def DemanderNom(self):
        self.nom = input("Nom de la personne: ")


class Etudiant(Personne): # Class Enfant

    # Constructeur
    def __init__(self, nom: str, age: int, etudes: str):
        super().__init__(nom, age) # Appel du constructeur de la classe parent Personne
        self.etudes = etudes

    # Méthode basé sur une Méthode du parent
    def SePresenter(self):
        super().SePresenter() # Appel de la méthode "Se présenter" de la classe parent Personne
        print(f"Je suis étudiant en {self.etudes}")



# Utilisation
print("Instancier")
personne1 = Personne("Mickey", 69) #Instancier 
personne2 = Personne("Jesus", 2023)
personne3 = Personne("Bébé", 1)
personne4 = Personne("Zorro")
personne5 = Personne(age = 16)
print("")

# Tableau
liste_personnes = [Personne("Pierre", 56), Personne("Paul", 45), Personne("Jack", 64)]

# Ajouter une personne dans le Tableau
personne6 = Personne(age = 666)
liste_personnes.append(personne6)

# Modifier l'instance basé sur une variable de classe
liste_personnes[3].ESPECE_ETRE_VIVANT = "Ange"


# Méthode d'instance
print("Se présenter // Méthode Instance")
personne1.SePresenter() #Appel de la fonction SePresenter
personne2.SePresenter()
personne3.SePresenter()
personne4.SePresenter()
personne5.SePresenter()
liste_personnes[1].SePresenter()
print()


# Boucle avec un Tableau
print("Se présenter [Tableau]")
for personne in liste_personnes:
    personne.SePresenter()
    personne.AfficherInfosetreVivant()
    print()


# Méthode de la classe
print("Se présenter // Méthode de Classe")
Personne.SePresenter(personne1) #Appel de la fonction SePresenter
Personne.ESPECE_ETRE_VIVANT = "Métamorphe"
print("")

# Boucle avec un Tableau
print("Se présenter [Tableau]")
for personne in liste_personnes:
    Personne.SePresenter(personne)
    Personne.AfficherInfosetreVivant(personne)
    print()


# Méthode hérité
ovni = EtreVivant()
chat1 = Chat()

print("Afficher Variable de classe")
ovni.AfficherFamilleetreVivant()
chat1.AfficherFamilleetreVivant()
print("")

print("Etudiant")
etudiant1 = Etudiant("Henry", 19, "chanson française")
etudiant1.SePresenter()
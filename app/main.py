### BASE

# Variables
variable_str = "Skynet"
variable_int = 2
addition = 0

# Fonction
def additionner_2_int_fonction(nom_utilisateur):
    global addition

    # Boucle While
    while addition == 0:
        age_utilisateur = input("Quel est ton âge "+ nom_utilisateur + "?")
        try:
            addition = variable_int + int(age_utilisateur)
        except:
            print("Dis moi juste le nombre qui indique ton age :)")

    # Boolean
    condition = int(age_utilisateur) >= 18

    # Conditions
    if condition:
        print("Oh! Tu es majeur!")
    elif int(age_utilisateur) == 17:
        print("Bientôt majeur!")
    elif 16 > int(age_utilisateur) > 13:
        print("Ah tu es adolescent!")
    elif int(age_utilisateur) < 13 and int(age_utilisateur) == 2:
        print("Ah tu as le même âge que moi !!!")
    else:
        print("Ah tu es mineur.")

    return addition

# Fonction avec une boucle for
def boucle_for(addition_int):
    global variable_int
    multiplication = 0

    # Boucle For
    for i in range(0, 5):
        multiplication += variable_int * addition_int
    
    return multiplication

# Fonction avec un 3e argument optionnel
def fonction_avec_paramètre_optionnel(a, b, c = 0):
    somme = a + b + c
    return somme


### 
# Application

nom_utilisateur = input("Comment tu t'appelles?")

print("Coucou " + nom_utilisateur + ". Je suis " + variable_str + ". Et j'ai " + str(variable_int) + " ans.")

addition_int = additionner_2_int_fonction(nom_utilisateur)

print("A nous deux nous avons " + str(addition_int) + " ans.")

multiplication_int = boucle_for(addition_int)

# Version 1 concaténage
print("Si on multiplie " + str(addition_int) + " par mon âge, qui est " + str(variable_int) + " ans, 5 fois.")

# Version 2 concaténage
print(f"ca nous donne le nombre {str(multiplication_int)}.")

# Version 3 concaténage
age = addition_int - variable_int
print("Quitte à me répéter! Tu t'appelle %s et tu as %s ans" % (nom_utilisateur, age))

# Print sur plusieurs lignes
print("""
            888888888888
          8888888888888888
        8888   888888   8888
       8888     8888     8888
       88888   888888   88888    ___________________________
       8888888888888888888888   /                           \
       8888888888888888888888  |  Meuh ! Meuh, meuh, meuh    |
       8888888888888888888888  |                             |
        88888888888888888888   |  meuh !!!                   |
         888888888888888888     \  _________________________/
          8888888  8888888      / /
           88888    88888  ____/ /
            88888  88888  <_____/
              88888888
                8888
""")
## Reverse string

# Boucle
def reverse_string_for(str):
    r=""

    for l in str:
        r = l + r

    return r

# Slice
def reverse_string_slice(str):
    return str[::-1]

# Utilisation
str = "Ce n'est qu'une phrase."

print("Reverse string")
print(f"Méthode boucle: {reverse_string_for(str)}")
print(f"Méthode slice: {reverse_string_slice(str)}")
print("")

################################################################

# Mot le plus court / le plus long
def get_min_and_max_words(str):
    words = str.split(" ") # Mot séparé par un espace blanc

    min_word = min(words, key=len)
    max_word = max(words, key=len)

    return (min_word, max_word)

min_word, max_word = get_min_and_max_words(str)

print("Mot le plus court et le mot le plus long")
print(f"Le mot le plus court est '{min_word}' et le mot le plus long est '{max_word}'")
print("")

## Par ordre alphabétique

### Méthode 1
def get_min_and_max_words_sorted(str):
    words = str.split(" ") # Mot séparé par un espace blanc

    min_word, max_word = get_min_and_max_words(str)

    # Ajoute les mots dans un tableau dont la longueur est égale au mot cible
    all_min_words = [w for w in words if len(w) == len(min_word)] 
    all_max_words = [w for w in words if len(w) == len(max_word)]

    # Trie les éléments par ordre croissant
    all_min_words.sort() 
    all_max_words.sort()

    return(all_min_words[0], all_max_words[0])

### Méthode 2
def get_min_and_max_words_sorted_speed(str):
    words = str.split(" ") # Mot séparé par un espace blanc
    words.sort() # Trie les éléments par ordre croissant
    
    min_word = min(words, key=len)
    max_word = max(words, key=len)

    return (min_word, max_word)


words = "z a b c anticonstitutionnellement intergouvernementalisation"

min_word, max_word = get_min_and_max_words_sorted(words)

print("Mot le plus court et le mot le plus long classé par ordre alphabétique")
print(f"Le mot le plus court est '{min_word}' et le mot le plus long est '{max_word}'")
print("ou")

min_word, max_word = get_min_and_max_words_sorted_speed(words)
print(f"Le mot le plus court est '{min_word}' et le mot le plus long est '{max_word}' avec la 2e méthode")
print("")

# Tris

## Tris par sélection
l = [5,9,6,1,69,11]

def tri_select(l):
    # Boucle
    for unsorted_index in range(0, len(l) - 1):

        min = l[unsorted_index]
        min_index = unsorted_index

        for i in range(unsorted_index + 1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i               #[5, 3, 2, 1]
        l[min_index] = l[unsorted_index]    #[5, 3, 2, 5]
        l[unsorted_index] = min             #[1, 3, 2, 5]

    return l

print("tri select")
print(f"Original {l}")
f = tri_select(l)
print(f"Classé {f}")
print("")

# Génération de liste random 
import random

def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

rand = generate_random_list(10, -10, 10)
print(f"Liste random: {rand}")
print("")
tri = tri_select(rand)
print(f"Liste trié: {tri}")
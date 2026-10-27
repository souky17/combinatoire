"""Jeux de combinatoire et probabilités — cours de 3 heures.
Lancer : python jeux_combinatoire.py
Aucune bibliothèque externe nécessaire.
"""
from itertools import permutations, combinations, product
from math import factorial, comb, perm
import random


def saisir_choix(message, valeurs):
    while True:
        choix = input(message).strip()
        if choix in valeurs:
            return choix
        print('Choix non reconnu. Essaie encore.')


def annoncer_et_comparer(possibilites, formule):
    print(f'Python énumère {len(possibilites)} possibilités.')
    print(f'La formule donne {formule} possibilités.')
    print('Même résultat ?', len(possibilites) == formule)


def jeu_permutation():
    print('\n=== JEU 1 : CHAISES MUSICALES (PERMUTATION) ===')
    noms = ('A', 'B', 'C', 'D')
    print('4 personnes occupent 4 chaises numérotées.')
    input('Avant de voir la réponse, prédis le nombre de placements. Entrée pour révéler... ')
    solutions = list(permutations(noms))
    for numero, placement in enumerate(solutions, start=1):
        print(f'{numero:2}.', '-'.join(placement))
    annoncer_et_comparer(solutions, factorial(4))
    print('Règle : on utilise TOUTES les personnes, et changer de place change le résultat.')


def jeu_arrangement():
    print('\n=== JEU 2 : PODIUM (ARRANGEMENT) ===')
    joueurs = ('A', 'B', 'C', 'D', 'E')
    print('5 personnes, mais 3 médailles DIFFERENTES (or, argent, bronze).')
    input('Combien de podiums possibles ? Entrée pour révéler... ')
    solutions = list(permutations(joueurs, 3))
    for numero, podium in enumerate(solutions, start=1):
        print(f'{numero:2}. Or={podium[0]}, Argent={podium[1]}, Bronze={podium[2]}')
    annoncer_et_comparer(solutions, perm(5, 3))
    print('Règle : on ne prend qu’une PARTIE du groupe, et l’ORDRE compte.')


def jeu_combinaison():
    print('\n=== JEU 3 : EQUIPES (COMBINAISON) ===')
    joueurs = ('A', 'B', 'C', 'D', 'E')
    print('Choisir 3 personnes parmi 5, sans attribuer de fonction ou de rang.')
    input('Combien d’équipes différentes ? Entrée pour révéler... ')
    solutions = list(combinations(joueurs, 3))
    for numero, equipe in enumerate(solutions, start=1):
        print(f'{numero:2}.', ', '.join(equipe))
    annoncer_et_comparer(solutions, comb(5, 3))
    print('Pourquoi ABC et BAC sont-ils la même équipe ? Parce que l’ordre ne compte pas.')
    print('Compare : arrangement de 3 parmi 5 =', perm(5, 3))
    print('Chaque équipe apparaît 3! =', factorial(3), 'fois parmi les podiums.')


def jeu_code():
    print('\n=== JEU 4 : CODE SECRET ET PROBABILITE ===')
    chiffres = '01234'
    longueur = 3
    print('Code de 3 chiffres choisis parmi 0,1,2,3,4. Le zéro initial est autorisé.')
    choix = saisir_choix('Répétition autorisée ? (o/n) : ', ('o', 'n'))
    if choix == 'o':
        possibilites = list(product(chiffres, repeat=longueur))
        attendu = len(chiffres) ** longueur
        print('Formule : 5 × 5 × 5 = 5³.')
    else:
        possibilites = list(permutations(chiffres, longueur))
        attendu = perm(5, longueur)
        print('Formule : 5 × 4 × 3 = A(5,3).')
    annoncer_et_comparer(possibilites, attendu)
    print('Premiers codes :', [''.join(c) for c in possibilites[:10]])
    print(f'Probabilité de réussir du premier coup : 1/{len(possibilites)} = {100/len(possibilites):.3f} %')
    secret = random.choice(possibilites)
    essai = input('Propose un code à 3 chiffres : ').strip()
    if len(essai) != longueur or any(c not in chiffres for c in essai):
        print('Code invalide : il faut 3 chiffres entre 0 et 4.')
    elif choix == 'n' and len(set(essai)) != longueur:
        print('Code invalide : chiffres tous différents demandés.')
    else:
        print('Gagné !' if essai == ''.join(secret) else 'Raté !')
    print('Le code secret était :', ''.join(secret))


def defi_final():
    print('\n=== MINI-QUIZ : QUELLE FORMULE ? ===')
    questions = [
        ('Ranger 5 livres différents sur une étagère', 'p', factorial(5)),
        ('Attribuer 2 rôles distincts à 6 personnes', 'a', perm(6, 2)),
        ('Choisir 2 bénévoles parmi 6, sans rôle', 'c', comb(6, 2)),
        ('Créer un code de 4 chiffres (0–9), répétition autorisée', 'r', 10**4),
        ('Placer 4 personnes sur 4 sièges distincts', 'p', factorial(4)),
        ('Choisir 3 livres parmi 7, sans ordre', 'c', comb(7, 3)),
    ]
    score = 0
    for i, (question, bonne, resultat) in enumerate(questions, 1):
        print(f'\n{i}. {question}')
        reponse = saisir_choix('p=permutation, a=arrangement, c=combinaison, r=avec répétition : ', ('p','a','c','r'))
        if reponse == bonne:
            score += 1
            print('Bonne catégorie !')
        else:
            print(f'Catégorie attendue : {bonne}')
        print('Nombre de possibilités :', resultat)
    print(f'\nScore : {score}/{len(questions)}')


def main():
    jeux = {'1': jeu_permutation, '2': jeu_arrangement, '3': jeu_combinaison,
            '4': jeu_code, '5': defi_final}
    while True:
        print('\nMENU : 1 Chaises | 2 Podium | 3 Equipes | 4 Code | 5 Quiz | 0 Quitter')
        choix = saisir_choix('Ton choix : ', ('0','1','2','3','4','5'))
        if choix == '0':
            print('Fin de la séance !')
            break
        jeux[choix]()


if __name__ == '__main__':
    main()

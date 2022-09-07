#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    motnve = ""
    for i in mot:
        motnve += chr(ord(i)-32)
    
    return motnve


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

    

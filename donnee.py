




def entrainer_ai():
    phrase_entrainement = [
    ("C'est vraiment une expérience incroyable", "positif"),
    ("Je suis tellement heureux de ce résultat", "positif"),
    ("Quel bonheur de voir ça aujourd'hui", "positif"),
    ("C'est génial et super bien fait", "positif"),
    ("Une réussite totale j'adore", "positif"),
    ("C'est top et très fluide à utiliser", "positif"),
    ("Franchement c'est parfait rien à dire", "positif"),
    ("Un moment merveilleux et passionnant", "positif"),
    ("Je recommande vivement c'est magnifique", "positif"),
    ("Bravo c'est un travail fantastique", "positif"),
    ("Je suis content", "positif"),

    
    ("C'est une catastrophe totale", "negatif"),
    ("Je suis vraiment déçu par ce service", "negatif"),
    ("C'est nul et très mal expliqué", "negatif"),
    ("Je déteste cette interface c'est horrible", "negatif"),
    ("Quel échec c'est vraiment médiocre", "negatif"),
    ("C'est insupportable et trop lent", "negatif"),
    ("Une perte de temps monumentale", "negatif"),
    ("C'est moche et pas du tout pratique", "negatif"),
    ("Je suis en colère car ça ne marche pas", "negatif"),
    ("C'est affreux et très ennuyeux", "negatif"),
    ("C'est triste", "negatif")

    
    ]
    frequence_pos = {}
    frequence_neg = {}

    for phrase, label in phrase_entrainement:
        phrase = phrase.lower()
        symboles = "_-,;./:!?"

        for s in symboles: 
            phrase = phrase.replace(s, "")
        mots = phrase.split()
        

        for m in mots:
            if label == "positif":  
                if m in frequence_pos:
                    frequence_pos[m] += 1 
                else:
                    frequence_pos[m] = 1
            elif label == "negatif":
                if m in frequence_neg:
                    frequence_neg[m] += 1
                else:
                    frequence_neg[m] = 1
    return frequence_neg, frequence_pos
    
   




   











































x= int(input("saisir un entier"))
match x :
    case 1 :
        print ("Lundi")
    case 2 :
        print ("Mardi")
    case 3 :
        print ("Mercredi")
    case 4 :
        print ("jeudi")
    case 5 :
        print ("Vendredi")
    case 6 :
        print ("Samedi")
    case 7 :
        print ("Dimanche")
    case _:
        print ("Chiffre invalide (choisir entre 1 et 7)")
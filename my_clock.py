import time 
import keyboard

heures = 0
minutes = 0
secondes = 0
hour_tuple = (heures, minutes, secondes)
heures_alarme = None
minutes_alarme = None
secondes_alarme = None 
choix = 0

# ----------------------------------------
#                  MENU
# ----------------------------------------

def menu(choix):

    print(
        """
    Bienvenue dans notre horloge !
    Merci de choisir un mode d'affichage.

    Une fois lancé, Vous aurez différentes options en maintenant certaines touches enfoncées :
        - Touche 'h' : Permet de régler l'heure
        - Touche 'p' : Permet de mettre l'horloge en pause

    __________________________________
    Choississez le mode d'affichage de l'heure :
        1 - 24 heures
        2 - 12 heures
        3 - Quitter
    __________________________________
    """)

    choix = int(input("Entrez le numéro : "))
    match choix:
        case 1:
            display_24_hours(heures, minutes, secondes)
        case 2:
            display_12_hours(heures, minutes, secondes)
        case 3:
            quit("A bientôt !")
    
# ----------------------------------------
#                ALARME
# ----------------------------------------
def alarm(heures_alarme, minutes_alarme, secondes_alarme):
    heures_alarme = 0
    minutes_alarme = 0
    secondes_alarme = 30
    alarm_tuple = (heures_alarme, minutes_alarme, secondes_alarme)
    return alarm_tuple

# ----------------------------------------
#            COMPTEUR 24 HEURES
# ----------------------------------------
def display_24_hours(heures, minutes, secondes):
    global heures_alarme, minutes_alarme, secondes_alarme

    # Définir l'heure :  
    heures = int(input("Entrez HH : "))
    while heures >= 24 or heures < 0 :
        heures = int(input("Entrez une heure hh VALIDE : "))

    minutes = int(input("Entrez MM : "))
    while minutes >= 60 or minutes < 0 :
        minutes = int(input("Entrez des minutes mm VALIDES : "))

    secondes = int(input("Entrez SS : "))
    while secondes >= 60 or secondes < 0 :
        secondes = int(input("Entrez des secondes ss VALIDES : "))

    # Système d'incrémentation
    while True:
            if secondes == 59:
                secondes = 00
                minutes +=1
            else:
                secondes += 1
            
            if minutes == 60:
                minutes = 00
                heures += 1
            
            if heures == 24:
                heures = 00

            hour_tuple = (heures, minutes, secondes)
            # Affichage de l'heure sur une seule ligne et avec la bonne notation :
            print("\r", "%02d" % (heures,), ":", "%02d" % (minutes,), ":", "%02d" % (secondes,), end="")

            time.sleep(1) # Permet d'attendre 1 secondes avant de relancer la boucle

            if alarm(heures_alarme, minutes_alarme, secondes_alarme) == hour_tuple:
                print(" \n Ding Dong !!!")

            if keyboard.is_pressed('h'):
                change_hour_24_hour(heures, minutes, secondes)
            elif keyboard.is_pressed('p'):
                take_a_break()



# ----------------------------------------
#            COMPTEUR 12 HEURES
# ----------------------------------------
def display_12_hours(heures, minutes, secondes):

    heures = int(input("Entrez HH : "))
    while heures >= 24 or heures < 0 :
        heures = int(input("Entrez une heure HH VALIDE : "))

    minutes = int(input("Entrez MM : "))
    while minutes >= 60 or minutes < 0 :
        minutes = int(input("Entrez des minutes MM VALIDES : "))

    secondes = int(input("Entrez SS : "))
    while secondes >= 60 or secondes < 0 :
        secondes = int(input("Entrez des secondes SS VALIDES : "))
    
    while True:
            # Système d'incrémentation :
            if secondes == 59:
                secondes = 00
                minutes +=1
            else:
                secondes += 1
            
            if minutes == 60:
                minutes = 00
                heures += 1
            
            if heures == 24:
                heures = 00

            hour_tuple = (heures, minutes, secondes)

            # Affichage de l'heure : 
            if heures == 0 :
                period = "AM"
                print("\r", "12", ":", "%02d" % (minutes,), ":", "%02d" % (secondes,), period, end="")
            elif heures == 12 :
                period = "PM"
                print("\r", "12", ":", "%02d" % (minutes,), ":", "%02d" % (secondes,), period, end="")
            elif heures > 12 :
                period = "PM"
                heures_pm = heures - 12
                print("\r", "%02d" % (heures_pm,), ":", "%02d" % (minutes,), ":", "%02d" % (secondes,), period, end="")
            else:
                period = "AM"
                print("\r", "%02d" % (heures,), ":", "%02d" % (minutes,), ":", "%02d" % (secondes,), period, end="")

            if alarm(heures_alarme, minutes_alarme, secondes_alarme) == hour_tuple:
                print(" \n Ding Dong !!!")
            
            if keyboard.is_pressed('h'):
                change_hour_12_hour(heures, minutes, secondes)
            elif keyboard.is_pressed('p'):
                take_a_break()

            time.sleep(1)
    


# ----------------------------------------
#            REGLER L'HEURE 
# ----------------------------------------

# Il y a une fonction pour chaque mode d'affichage.
#  Cependant, comme dans mes fonctions display les premières instructions sont de rentrer une heure, celles
#  qui suivent le servent pas en réalité, on aurait pu simplement renvoyer les fonctions display

def change_hour_24_hour(heures, minutes, secondes):
    global choix
    print("\n Merci de renseigner la nouvelle heure : ")
    heures = int(input("Entrez HH : "))
    while heures >= 24 or heures < 0 :
        heures = int(input("Entrez une heure HH VALIDE : "))

    minutes = int(input("Entrez MM : "))
    while minutes >= 60 or minutes < 0 :
        minutes = int(input("Entrez des minutes MM VALIDES : "))

    secondes = int(input("Entrez SS : "))
    while secondes >= 60 or secondes < 0 :
        secondes = int(input("Entrez des secondes SS VALIDES : "))
    
    display_24_hours(heures, minutes, secondes)


def change_hour_12_hour(heures, minutes, secondes):
    global choix
    print("\n Merci de renseigner la nouvelle heure : ")
    heures = int(input("Entrez HH : "))
    while heures >= 24 or heures < 0 :
        heures = int(input("Entrez une heure HH VALIDE : "))

    minutes = int(input("Entrez MM : "))
    while minutes >= 60 or minutes < 0 :
        minutes = int(input("Entrez des minutes MM VALIDES : "))

    secondes = int(input("Entrez SS : "))
    while secondes >= 60 or secondes < 0 :
        secondes = int(input("Entrez des secondes SS VALIDES : "))

    display_12_hours(heures, minutes, secondes)


# ----------------------------------------
#            METTRE EN PAUSE
# ----------------------------------------
def take_a_break():
    print("\nL'horloge est en pause")
    going_back = input("Voulez vous reprendre ? Oui ou Non : ")
    while going_back != "Oui":
        going_back = input("Voulez vous reprendre ? Oui ou Non : ")


# ----------------------------------------
#                  MAIN
# ----------------------------------------
def main():
    global choix
    menu(choix)

main()

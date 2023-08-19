

""""
Pour cet exercice de code, vous allez réaliser un programme de type "minuteur" qui permettra d'afficher en temps réel le temps restant de cuisson.


-> Votre programme proposera 3 options :

- Oeufs à la coque : 3 minutes

- Oeufs mollets : 6 minutes

- Oeufs durs : 9 minutes


Une fois l'option choisie, votre programme commencera à attendre la durée concernée.

A chaque seconde, vous afficherez un "." sur une même ligne (afin que l'on voit un effet de progression).

Et toutes les 10 secondes vous irez à la ligne suivante en affichant le temps restant."""

import time
import beepy

def Choisir_cuisson():
    print("--Bonjour amateur d'oeuf-- ")
    print("* Pour des oeufs à la coque (3MIN)- Tapez - 1 *")
    print("* Pour des oeufs mollets (6MIN)- Tapez - 2 *")
    print("* Pour des durs  (9MIN)- cliquez - Tapez 3 *")



def Timer_oeuf():

    #mettre 10 secondes

    for i in range(10):
        time.sleep(1)

        print(".", end="", flush=True)

    print("")

    #print("Durée restante : 01:50" ".",end="",flush=True)
        #print("il reste le temps totals moin cinq")


def Sonnerie():
    print('votre oeuf est prêt')
    beepy.beep(sound="ping")


def Calul_cuisson(min,sec,interval):


    remaining_time = f"Durée restante : {min:02d}:{sec:02d}"
    print(remaining_time, end=" ", flush=True)
    # Soustraction de l'intervalle
    min -= interval // 60
    sec -= interval % 60

    if sec < 0:
        min -= 1
        sec += 60

    Timer_oeuf()
    return min, sec






Choisir_cuisson()

choix_utilisateur= input( "Entrez la cuisson de votre choix ")




if choix_utilisateur == "1":
    interval = 10
    durée_coque_seconde_total = 180-interval
    min_coque = durée_coque_seconde_total // 60
    sec_coque = durée_coque_seconde_total - min_coque * 60

    print("oeufs coque")
    print("")
    print("Cuisson en cours"".", end="", flush=True)
    Timer_oeuf()
    print("")
    while min_coque > 0:

        min_coque, sec_coque = Calul_cuisson(min_coque,sec_coque,interval)
    Sonnerie()


elif choix_utilisateur == "2":
    durée_mollets_seconde_total = 360
    min_mollets = durée_mollets_seconde_total // 60
    sec_mollets = durée_mollets_seconde_total - min_mollets * 60
    interval = 10
    print("oeuf mollets")
    while min_mollets > 0:
        min_coque, sec_coque = Calul_cuisson(min_mollets, sec_mollets, interval)
    Sonnerie()

elif choix_utilisateur == "3":
    durée_dur_seconde_total = 540
    min_dur = durée_dur_seconde_total // 60
    sec_dur = durée_dur_seconde_total - min_dur * 60
    interval = 10
    print("oeuf mollets")
    while min_dur > 0:
        min_dur, sec_coque = Calul_cuisson(min_dur, sec_dur, interval)
    Sonnerie()

else:
    print("vous devez choisir 1, 2 ou 3. Veuillez sélectionner un choix valide")


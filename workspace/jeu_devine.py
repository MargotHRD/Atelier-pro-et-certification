import random


def devine_le_nombre():
  nombre_secret = random.randint(1, 100)
  essai = 0
  trouve = False

  print("Bienvenue dans le jeu du 'Devine le nombre' !")
  print("J'ai choisi un nombre entre 1 et 100. À vous de le deviner.")

  while not trouve:
    try:
      saisie = input("Votre proposition : ")
      proposition = int(saisie)
      essai += 1

      if proposition < nombre_secret:
        print("C'est plus !")
      elif proposition > nombre_secret:
        print("C'est moins !")
      else:
        trouve = True
        print(
            f"Bravo ! Vous avez trouvé le nombre {nombre_secret} en {essai}"
            " essais."
        )
    except ValueError:
      print("Veuillez entrer un nombre entier valide.")


if __name__ == "__main__":
  devine_le_nombre()


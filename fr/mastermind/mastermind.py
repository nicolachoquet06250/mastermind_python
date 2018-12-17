# coding: utf-8
from pip._vendor.distlib.compat import raw_input


class Mastermind(object):
    enabled_colors: list = ['R', 'N', 'B', 'J', 'V', 'G', 'M']
    nb_colors: int = 5
    nb_trials: int = 5
    increment: int = 1
    X: str = 'X'
    Y: str = 'Y'
    nb_players: int = 2
    players: list = []

    @staticmethod
    def valid_char(c: str):
        for color in Mastermind.enabled_colors:
            if c == color:
                return True
        return False

    @staticmethod
    def set_color():
        colors = []
        colors_string = raw_input('Entrez vos couleurs: \n')
        _colors = colors_string.split(' ')
        for i in range(0, len(_colors)):
            if Mastermind.valid_char(_colors[i]):
                colors.append(_colors[i])
        return colors

    @staticmethod
    def check_well_placed(vec1: list, vec2: list):
        cumulates = 0
        for i in range(0, Mastermind.nb_colors):  # faut le 5 car ca le boucle ne regroupe pas le 5
            if vec1[i] == vec2[i]:
                cumulates += Mastermind.increment
                vec1[i] = Mastermind.X
                vec2[i] = Mastermind.Y
                print(i, Mastermind.X, Mastermind.Y, vec1, vec2)
        print(cumulates)
        return cumulates

    @staticmethod
    def check_misplaced(vec1: list, vec2: list):
        cumulates = 0
        for i in range(0, Mastermind.nb_colors):
            for j in range(0, Mastermind.nb_colors):
                if vec1[i] == vec2[j]:
                    cumulates += Mastermind.increment
                    vec1[i] = Mastermind.X
                    vec2[j] = Mastermind.Y
        return cumulates

    @staticmethod
    def set_players():
        for i in range(0, Mastermind.nb_players):
            Mastermind.players.append(raw_input('Joueur n°' + str(i+1) + ', quel est votre pseudo ?\n'))

    @staticmethod
    def get_player(num_player):
        if Mastermind.players[num_player-1] is not None:
            return Mastermind.players[num_player-1]
        return None

    @staticmethod
    def run():
        # --- Saisie des pseudos des joueurs ---
        Mastermind.set_players()

        # --- Saisie de la combinaison de depart ---
        print(Mastermind.get_player(1))
        print("Entrer couleur: ")
        print(Mastermind.enabled_colors)
        original = Mastermind.set_color()

        # --- Boucle sur les essais ---
        print(Mastermind.get_player(2))
        nb_trial = 0

        # --- Affichage final ---
        while True:
            print("Essais ", nb_trial)

            print("Entrer couleur: ")
            trial = Mastermind.set_color()
            copy = original[:]

            well_placed = Mastermind.check_well_placed(copy, trial)
            misplaced   = Mastermind.check_misplaced(copy, trial)

            print(well_placed)
            print(misplaced)

            nb_trial += 1

            if well_placed < Mastermind.nb_trials:
                break

        # --- Affichage final ---
        print("Vous avez trouvé en ", nb_trial, " essais : ")

        if nb_trial < 5:
            print("Bravo")
        elif nb_trial < 10:
            print("Correct")
        else:
            print("Decevant")

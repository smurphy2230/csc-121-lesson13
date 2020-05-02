from athletePoly import Athlete

class BasketballPlayer(Athlete):

    def __init__(self, name):
        super().__init__(name, "basketball")
        self.__ppg = 0.0  # points per game
        self.__rpg = 0.0  # rebounds per game
        self.__apg = 0.0  # assists per game

    def inputStat(self):
        self.__ppg = float(input("Enter points per game: "))
        self.__rpg = float(input("Enter rebounds per game: "))
        self.__apg = float(input("Enter assists per game: "))

    def displayStat(self):
        print("Points per game: ", self.__ppg)
        print("Rebounds per game: ", self.__rpg)
        print("Assists per game: ", self.__apg)


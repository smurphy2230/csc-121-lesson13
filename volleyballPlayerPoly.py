from athletePoly import Athlete

class VolleyballPlayer(Athlete):
    def __init__(self, name):
        super().__init__(name, "volleyball")
        self.__kpg = 0.0  # kills per game
        self.__dpg = 0.0  # digs per game
        self.__apg = 0.0  # assists per game

    def inputStat(self):
        self.__kpg = float(input("Enter kills per game: "))
        self.__dpg = float(input("Enter digs per game: "))
        self.__apg = float(input("Enter assists per game: "))

    def displayStat(self):
        print("Kills per game: ", self.__kpg)
        print("Digs per game: ", self.__dpg)
        print("Assists per game: ", self.__apg)

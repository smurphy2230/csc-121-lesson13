from basketballPlayerPoly import BasketballPlayer
from volleyballPlayerPoly import VolleyballPlayer


def main():
    print("Adding athletes")
    athletes_list = []
    choice = 0
    while choice != 3:
        choice = int(input("Enter 1 for basketball player, 2 for volleyball player, "
                           "3 to exit: "))
        if choice == 1:
            name = input("Enter name: ")
            player = BasketballPlayer(name)
            player.inputStat()
            athletes_list.append(player)
        if choice == 2:
            name = input("Enter name: ")
            player = VolleyballPlayer(name)
            player.inputStat()
            athletes_list.append(player)
        print()

    print("Number of athletes: ", len(athletes_list))
    print()

    for player in athletes_list:
        player.displayInfo()
        player.displayStat()
        print()


main()


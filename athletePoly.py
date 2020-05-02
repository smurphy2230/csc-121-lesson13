#  this is an abstract class. It serves as a template for its derived classes
class Athlete:

    def __init__(self, name, sport):
        self.__name = name
        self.__sport = sport

    def displayInfo(self):
        print("Name: ", self.__name)
        print("Sport: ", self.__sport)

    # abstract methods. The actual code will be written in the subclasses
    def inputStat(self):
        raise NotImplementedError("Method inputStat not implemented")

    def displayStat(self):
        raise NotImplementedError("Method displayStat not implemented")

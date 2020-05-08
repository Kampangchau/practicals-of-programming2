CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""
    def __init__(self, name, year, cost):
        """constructor that takes three parameters and registers the result"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """A string representing a guitar object"""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """way to get age of guitar"""
        return (2018 - self.year)

    def is_vintage(self):
        """way to determine if a guitar is vintage"""
        age = self.get_age()
        if age >= 50:
            return True
        return False


def unit_test():
    """test of guitar"""

    # create test instances
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    # test get_age()
    print("{} get_age() - Expected 96. Got {}".format(
        gibson_guitar, gibson_guitar.get_age()))
    print("{} get_age() - Expected 6. Got {}".format(
        another_guitar, another_guitar.get_age()))

    # test is_vintage()
    print("{} is_vintage() - Expected True. Got {}".format(
        gibson_guitar, gibson_guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(
        another_guitar, another_guitar.is_vintage()))
    print("{} is_vintage() - Expected True. Got {}".format(
        fifty_guitar, fifty_guitar.is_vintage()))


if __name__ == "__main__":
    unit_test()
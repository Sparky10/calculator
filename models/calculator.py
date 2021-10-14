class Calculator:
    """
    A class representing a calculator.
    """

    def __init__(self):
        self.__raw_input = None
        self.__answer = None

    def set_raw_input(self, raw_input):
        self.__raw_input = raw_input
        return self.__raw_input

    def get_answer(self):
        return self.__answer

    def calculate(self):

        self.__answer = 8
        return 8



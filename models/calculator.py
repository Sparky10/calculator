from services.compute_service import ComputeService
from models.compute_engines import ComputeError

class Calculator:
    """
    A class representing a calculator.
    The calculator uses the ComputeService to inject a compute engine into the model.  The compute engine handles parsing and calculations.
    There are two versions of the engine, simple and complex.  The service defaults to using the complex engine but this can be easily overridden here if needed.
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

        try:
            compute_engine = ComputeService().inject_compute_engine()
            compute_engine.parse(self.__raw_input)
        except ComputeError as err:
            raise ComputeError('A compute error occured during parse: ', err)
        else:
            try:
                self.__answer = compute_engine.make_calculation()
            except ComputeError as err:
                raise ComputeError('A compute error occured during calculation: ', err)



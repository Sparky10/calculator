from models.compute_engines import SimpleComputeEngine
from models.compute_engines import ComplexComputeEngine

class Service:
    def __init__(self):
        self._dependency = None


class ComputeService(Service):

    # This could be set in a number if ways, such as an environment variable
    # Here we allow over-riding by passing as an argument to the injector method
    
    ENGINE = 'simple'

    def __init__(self):
        super().__init__()

    def inject_compute_engine(self, engine=ENGINE):
        if engine == 'simple':
            self.__dependency = SimpleComputeEngine()
        elif engine == 'complex':
            self.__dependency = ComplexComputeEngine()
        else:
            raise ComputeError('Unable to inject unknown engine: ', engine)

        return self.__dependency

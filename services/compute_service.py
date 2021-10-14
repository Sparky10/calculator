from models.compute_engines import ComputeEngine

class Service:
    def __init__(self):
        self._dependency = None


class ComputeService(Service):

    def __init__(self):
        super().__init__()

    def inject_compute_engine(self):

        self._dependency = ComputeEngine()
        return self._dependency


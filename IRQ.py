

class IRQ():
    def __init__(self, interruption_type):
        self._type = interruption_type
        self._parameters = []

    def setType(self, interruption_type):
        self._type = interruption_type

    def add_parameters(self, param):
        self._parameters.append(param)

    @property
    def type(self):
        return self._type

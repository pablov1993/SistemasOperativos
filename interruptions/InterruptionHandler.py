class InterruptionHandler():
    def __init__(self, kernel):
        self._kernel = kernel

    def exec(self, program):
        pass

    @property
    def kernel(self):
        return self._kernel

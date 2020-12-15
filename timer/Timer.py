class Timer:
    def _init_(self, interruptVector, quantum):
        self._quantum = quantum  # cantidad máxima de de ciclos “a correr”
        self._interruptVector = interruptVector
        self._tickCount = 0  # cantidad de de ciclos “ejecutados” por el proceso actual

    def tick(self):
        # registro que el proceso en CPU corrio un ciclo mas
        self._tickCount += 1
        if self._tickCount >= self._quantum:
            # se cumplio el limite de ejecuciones
            self._interruptVector.handle("TIME_OUT")

    def reset(self):
        self._tickCount =0

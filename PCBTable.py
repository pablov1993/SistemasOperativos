class PCBTable():
    def __init__(self):
        self._pid = 0
        self._table = {}
        self._runningPCB = 0

    def add(self, pcb):

        print("llegue a agregar en la pcbTABLE")
        self._table[self._pid] = pcb


    def get(self, pid):
        pcb = self._table[pid]
        return pcb

    def getNewPid(self):

        print("EL kernel funciono y setie")
        current = self._pid
        self._pid += 1
        return current
        # return self._pid + 1

    def setRunningPCB(self, pcb):
        self._runningPCB = pcb

    def remove(self, pid):
        for p in self._table:
            if p == pid:
                del self._table[p]

    @property
    def runningPCB(self):
        return self._runningPCB



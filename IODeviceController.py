from queue import Queue

from InterruptVector import InterruptVector


class IODeviceController():

    def __init__(self, runTime):
        self._runTime = runTime
        self._waiting_queue = Queue()
        self._currentPCB = None
        self._tickCount = 0
        self._iv = None

    def tick(self):
        if self._currentPCB:
            self.keep_running()

        else:
            self.load_from_waiting_queue()

    def keep_running(self):
        self._tickCount += 1
        if self._runTime <= self._tickCount:
            self._iv.handleIOOUT(self.getCurrentPCB())
            self.load_from_waiting_queue()

    def load_from_waiting_queue(self):
        if not self._waiting_queue.empty():
            self._currentPCB= self.getNext()
            self._tickCount=1

    def getNext(self):
        return self._waiting_queue.get()

    def add(self, pcb):
        self._waiting_queue.put(pcb)

    def getCurrentPCB(self):
        pcb = self._currentPCB
        self._currentPCB = None
        return pcb

    @property
    def interruptVector(self):
        return self._iv

    @interruptVector.setter
    def interruptVector(self, value):
        self._iv = value









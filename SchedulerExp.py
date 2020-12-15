from queue import PriorityQueue, Queue

from PCBTable import PCBTable
from Scheduler import Scheduler
from Dispatcher import Dispatcher
from PCB import PCB
from Timer import Timer


class SchedulerExpPorPrioridad:

    def __init__(self, maxSize):
        self._queue = []
        self._maxSize = maxSize
        for i in range(0, maxSize):
            self._queue.append([])


    def queue(self):
        return self._queue

    def add(self,pcb):
        self._queue[pcb.getPriority].append(pcb)

    def getNext(self):
        for i in range(0, self._maxSize):
            if not self.isEmptyList(self._queue[i]):
                return self._queue[i].pop()

    def isEmptyList(self, queue):
        return len(queue) == 0

    def isEmpty(self):
        for i in range(0, self._maxSize):
            if not self.isEmptyList(self._queue[i]):
                return False
        return True

    @staticmethod
    def mustExpropiate(pcbincpu, pcbtoadd):
        return pcbtoadd.getPriority < pcbincpu.getPriority







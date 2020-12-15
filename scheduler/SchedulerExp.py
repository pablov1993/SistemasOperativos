from queue import PriorityQueue, Queue

from timer.Timer import Timer


class SchedulerExpPorPrioridad:

    def __init__(self, dispatcher):
        self._queue = PriorityQueue()
        self._dispatcher = dispatcher

    def queue(self):
        return self._queue

    def add(self,pcb):
        self._queue.put(pcb.getPriority, pcb)

    def getNext(self):
        return self._queue.get()

    def isEmpty(self):
        return self._queue.empty()

    @staticmethod
    def mustExpropiate(pcbincpu, pcbtoadd):
        return pcbtoadd.getPriority < pcbincpu.getPriority



class SchedulerExpPorRoundRobin:

    def __init__(self, dispatcher):
        self._queue = Queue()
        self._dispatcher = dispatcher
        self._timer = Timer()

    def add(self, pcb):
        self._queue.put(pcb)

    def queue(self):
        return self._queue

    def getNext(self):
        return self._queue.get()

    @staticmethod
    def mustExpropiate(pcbincpu, pcbtoadd):
        return pcbtoadd.getPriority < pcbincpu.getPriority







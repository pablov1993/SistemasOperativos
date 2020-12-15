from queue import Queue


class Scheduler():
    "Tiene que ser FIFO"

    def __init__(self):
        self._queue = Queue()

    @property
    def queue(self):
        return self._queue

    def add(self, pcb):
        self._queue.put(pcb)

    def getNext(self):
        return self._queue.get()

    def isEmpty(self):
        return self._queue.empty()

    @staticmethod
    def mustExpropiate(pcbincpu, pcbtoadd):
        return False


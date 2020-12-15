from Scheduler import Scheduler


class SchedulerNoExp:
    def __init__(self, maxSize):
        self._queue = []
        self._maxSize = maxSize
        for i in range(0, maxSize):
            self._queue.append([])

    def queue(self):
        return self._queue

    def add(self, pcb):
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
        return False




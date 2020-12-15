from PageTable import PageTable


class MemoryManager:

    def __init__(self, memory, frameSize):

        self._memory = memory
        self._freeFrames = []
        self._frameSize = frameSize
        self._pageTables = PageTable()
        self.setUpFreeFrames()


    @property
    def getFreeFrames(self):
        return self._freeFrames

    @property
    def getFrameSize(self):
        return self._frameSize

    @property
    def getFreeFrameSize(self):
        return len(self.getFreeFrames)

    @property
    def pageTables(self):
        return self._pageTables

    def getRequestFreeFrames(self, n):

        requestFrames = []

        for n in range(0, n):

            requestFrames.append(self._freeFrames.pop(0))

        return requestFrames

    def setUpFreeFrames(self):

       for i in range(0 , (self._memory.getSize // self._frameSize)):

           self._freeFrames.append(i)















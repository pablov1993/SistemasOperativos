import logging


class MMU():
    def __init__(self, memory):
        self._memory = memory
        self._baseDir = 0

    @property
    def baseDir(self):
        return self._baseDir

    def setBaseDir(self, baseDir):
        self._baseDir = baseDir

    def fetch(self, pc):
        dirFisica = self._baseDir + pc
        return self._memory.fetch(dirFisica)


class MMUPagination:
    def __init__(self, memory, frameSize, logger):
        self._memory = memory
        self._frameSize = frameSize
        self._pageTable = None
        self._logger = logger

    def fetch(self, pc):
        offSet = pc % self._frameSize
        page = pc // self._frameSize
        # frame = self.pageTable.table[page].frame
        frame = self.pageTable[page]
        pcDir = frame * self._frameSize + offSet
        self._logger.info("-fromDir: {dir}".format(dir=pcDir))
        return self._memory.fetch(pcDir)

    @property
    def pageTable(self):
        return self._pageTable

    @pageTable.setter
    def pageTable(self, pageTable):
        self._pageTable = pageTable


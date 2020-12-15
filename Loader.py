from InstrEXIT import EXIT
from PageTable import *

class Loader:

    def __init__(self, memory, fileSystem):
        self._memory = memory
        self._fileSystem = fileSystem
        self._pointer = 0

    def loadInstructions(self, instructions):
        instructionsToLoad = instructions
        baseDir = self._pointer
        for inst in instructionsToLoad:
            self._memory.put(self._pointer, inst)
            self._pointer += 1
        return baseDir

    def load(self, pcb):
        instructions = self._fileSystem.getProgram(pcb.path)
        baseDir = self.loadInstructions(instructions)
        pcb.baseDir = baseDir

class LoaderPaging:

    def __init__(self, memory, memoryManager, fileSystem,):
        self._memory = memory
        self._memoryManager = memoryManager
        self._fileSystem = fileSystem
        self._frameSize = self._memoryManager.getFrameSize

    def getFreeFrame(self, n):

        return self._memoryManager.getRequestFreeFrames(n)

    def getPage(self, path, pageNumber):

        return self._fileSystem.getProgram(path, pageNumber)

    def load(self, pcb):
        path = pcb.path

        programSize = self._fileSystem.getProgramSize(path)

        cantPages = (programSize // self._frameSize) + (programSize % self._frameSize)

        frames = self.getFreeFrame(cantPages)

        pageTable = {}

        for page in range(0, cantPages):

            frame = frames[page]
            pageTable[page] = frame
            self.loadPage(path, page, frame)

        # pageTable = PageTable()
        self._memoryManager.pageTables.add(pageTable)
        return pageTable


    def loadPage(self, path, pageNumber, frame):

        frameBaseDir = frame * self._frameSize
        paginatedProgram = self._fileSystem.getProgram(path, pageNumber)
        displacement = 0

        for instruction in paginatedProgram:

            self._memory.put(frameBaseDir + displacement, instruction)
            displacement += 1


















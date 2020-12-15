from CPU import Cpu
from Clock import Clock
from DummyTimer import DummyTimer
from FileSystem import FileSystem, FileSystemContiguous
from IODeviceController import IODeviceController
from InterruptVector import InterruptVector
from Loader import Loader, LoaderPaging
from MMU import MMU, MMUPagination
from Memory import Memory
from MemoryManager import MemoryManager
from Timer import Timer


class Hardware():
    def __init__(self, logger):
        # Hardware
        self._memory = Memory(32)
        self._mmu = MMU(self.memory)                                                       #Para memoria continua
        # self._mmu = MMUPagination(self._memory, 3, logger)                               #para paginacion
        self._interruptVector = InterruptVector(self)
        self._cpu = Cpu(self, logger)
        self._ioDevice = IODeviceController(2)
        self.ioDevice.interruptVector = self.interruptVector
        # self._timer = DummyTimer()                                                       #sin RR
        self._timer = Timer(self._interruptVector, 2)                                      #para RR
        self._clock = Clock(self.cpu, self._timer, self._ioDevice)
        self._memoryManager = MemoryManager(self._memory, 3)                               #para paginacion
        self._fileSystem = FileSystemContiguous()
        # self._fileSystem = FileSystem(3)                                                 #para paginacion
        self._loader = Loader(self._memory, self._fileSystem)
        # self._loader = LoaderPaging(self._memory, self._memoryManager, self._fileSystem) #para paginacion

    @property
    def cpu(self):
        return self._cpu

    @property
    def mmu(self):
        return self._mmu

    @property
    def ioDevice(self):
        return self._ioDevice

    @property
    def memory(self):
        return self._memory

    @property
    def interruptVector(self):
        return self._interruptVector

    @property
    def fileSystem(self):
        return self._fileSystem

    @property
    def timer(self):
        return self._timer

    @property
    def clock(self):
        return self._clock

    @property
    def loader(self):
        return self._loader



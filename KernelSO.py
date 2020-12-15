from Dispatcher import Dispatcher, DispatcherPages
from Hardware import *
from IO_INHandler import IO_INHandler
from IO_OUTHandler import IO_OUTHandler
from IRQ import IRQ
#from InterruptVector import InterruptVector
from KillHandler import KillHandler
from NewHandler import NewHandler
from Scheduler import Scheduler
from PCBTable import PCBTable


class KernelSO():
    def __init__(self, logger, hardware, scheduler):
        # Logger
        self._logger = logger

        # Inicio el Hardware que me llega por parametros
        self._hardware = hardware

        # Software
        self._dispatcher = Dispatcher(self._hardware.cpu, self._hardware.mmu, self._hardware.timer)        #para continuo
        # self._dispatcher = DispatcherPages(self._hardware.cpu, self._hardware.mmu, self._hardware.timer) #para paginacion
        self._scheduler = scheduler
        self._pcbTable = PCBTable()
        self._interruptVector = hardware.interruptVector

        self._interruptVector.setKernel(self)


        # IRQ
      #  self._newIRQ = IRQ("NEW")
        self._killIRQ = IRQ("KILL")
      #  self._ioInIRQ = IRQ("IO_IN")
      #  self._ioOutIRQ = IRQ("IO_OUT")
      #  self._timeOut = IRQ("TIME_OUT")

        # Por ahora interruptVector es un hibrido (Hard/Soft)
        #self._interruptVector.sekernel = self

        # Interrupt Handlers config
        self._interruptVector.register(self._killIRQ.type, KillHandler(self))
      #  self._interruptionVector.register(self._newIRQ.type, NewHandler(self))
       # self._interruptionVector.register(self._ioInIRQ.type , IO_INHandler(self , self._hardware.ioDevice))
        #self._interruptionVector.register(self._ioOutIRQ.type, IO_OUTHandler(self, self._hardware.ioDevice))

   # def runPrograms(self, progams):
    #    for p in list(progams):
      #      self.exec(p)

   # def exec(self, prog):
        # IrqNew
        #self._interruptionVector.handle(self._newIRQ)
       # self._logger.info(self)
       # self.cpu.pc = 0

        # run all program instructions
        #inst_count = len(prog.instructions)
       # for num in range(0, inst_count):
         #   self.cpu.tick()

    @property
    def cpu(self):
        return self._hardware.cpu

    def __repr__(self):
        return "{cpu}\n{mem}".format(cpu=self.hardware.cpu, mem=self.hardware.memory)

    @property
    def dispatcher(self):
        return self._dispatcher

    @property
    def scheduler(self):
        return self._scheduler

    @property
    def hardware(self):
        return self._hardware

    @property
    def pcbTable(self):
        return self._pcbTable

    @property
    def interruptVector(self):
        return self._interruptVector

    #@property
    #def newIRQ(self):
       # return self._newIRQ
#

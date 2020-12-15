from Hardware import Hardware
from KernelSO import KernelSO
from Scheduler import *
from SchedulerExp import SchedulerExpPorPrioridad
from SchedulerNoExp import SchedulerNoExp


class SO:
    def __init__(self, logger):
        # Logger
        self._logger = logger

        # Hardware of OS
        self._hardware = Hardware(self._logger)

        # Kernel of OS
        self._kernel = KernelSO(self._logger, self._hardware, Scheduler())

    def start(self, programs):

        print("ejecuto")

        self.executePrograms(programs)
        self._hardware.clock.start()

    def executePrograms(self, programs):

        for program in programs:
            print("prioridad del programa a cargar: {pid}".format(pid=program.priority))
            self._hardware.fileSystem.save(program)
            self.exec(program)

    def exec(self, program):

        print("llegue hasta aca")

        print(program.name)


        self._kernel.hardware.interruptVector.newHandler(program)
       # print(self._kernel.newIRQ.type)

from Memory import *
from Program import *
from KernelSO import *
from PCB import *


class InterruptVector():

    def __init__(self, hardware):
        self._handlers = {}
        self._kernel = None
        self._hardware = hardware

    def register(self, interruption_type, interruption_handler):
        self._handlers[interruption_type] = interruption_handler

    def handle(self, irq, program=None):

        if irq.type == "NEW":
            self.newHandler(program)
        else:
            self._handlers[irq].exec(self)

    @property
    def kernel(self):
        return self._kernel

    @property
    def hardware(self):
        return self._hardware

    def setKernel(self, kernel):
        self._kernel = kernel

    def newHandler(self, program):

        print("arrived to new")
        # baseDir = self._kernel.memory.load(program)

        pcb = self.createNewPCB(program)

        print("pid del pcb creado: {pid}".format(pid=pcb.pid))
        #pcb._baseDir = baseDir

        print("no setie")

        print("agregue")

        pcbToExpropiate = self.kernel.pcbTable.runningPCB

        if self.kernel.pcbTable.runningPCB == 0:
            print("ANIADIDO")
            pcb.setState("STATE_RUNNING")
            self._kernel.dispatcher.load(pcb)
            self._kernel.pcbTable.setRunningPCB(pcb)
        else:
            if self.kernel.scheduler.mustExpropiate(pcbToExpropiate, pcb):
                print("EXPROPIADO")
                pcbToExpropiate.setState("STATE_READY")
                self.kernel.dispatcher.save(pcbToExpropiate)
                self.kernel.scheduler.add(pcbToExpropiate)
                pcb.setState("STATE_RUNNING")
                self.kernel.dispatcher.load(pcb)
                self.kernel.pcbTable.setRunningPCB(pcb)
            else:
                print("NO EXPROPIADO")
                pcb.setState("STATE_READY(constante)")
                self.kernel.scheduler.add(pcb)
                print("pid enviado a scheduler: {pid}".format(pid=pcb.pid))

    def handleExit(self):
        pcb = self.kernel.pcbTable.runningPCB
        pcb.setState("STATE_TERMINATED")
        self._kernel.dispatcher.save(pcb)
        self.kernel.pcbTable.setRunningPCB(None)
        print("PID del pcb finalizado: {pid}".format(pid=pcb.pid))
        if not self.kernel.scheduler.isEmpty():
            print("Cargado el siguiente despues de KILL...")
            newPCB = self.kernel.scheduler.getNext()
            newPCB.setState("STATE_RUNNING")
            self.kernel.dispatcher.load(newPCB)
            self.kernel.pcbTable.setRunningPCB(newPCB)

    def handleIOIN(self):
        pcb = self.kernel.pcbTable.runningPCB
        pcb.setState("STATE_WAITING")
        self._kernel.dispatcher.save(pcb)
        self.hardware.ioDevice.add(pcb)
        print("PID del pcb que hizo IO: {pid}".format(pid=pcb.pid))
        if not self.kernel.scheduler.isEmpty():
            print("Cargando el siguiente despues de IO...")
            newPCB = self.kernel.scheduler.getNext()
            newPCB.setState("STATE_RUNNING")
            self.kernel.dispatcher.load(newPCB)
            self.kernel.pcbTable.setRunningPCB(newPCB)

    def handleIOOUT(self, pcb):
        runningPCB = self.kernel.pcbTable.runningPCB
        print("PRIORIDADES: {runningPCB}, {pcb}".format(runningPCB= runningPCB.getPriority, pcb=pcb.getPriority))
        if runningPCB is not None:
            if self.kernel.scheduler.mustExpropiate(runningPCB, pcb):
                print("El que reemplaza al actual: {pid}".format(pid=pcb.pid))
                runningPCB.setState("STATE_READY")
                self.kernel.dispatcher.save(runningPCB)
                self.kernel.scheduler.add(runningPCB)
                pcb.setState("STATE_RUNNING")
                self.kernel.dispatcher.load(pcb)
                self.kernel.pcbTable.setRunningPCB(pcb)
            else:
                print("NO SE EXPROPIO")
                pcb.setState("STATE_READY")
                self.kernel.scheduler.add(pcb)
        else:
            print("NO HABIA NADA EN EL SCHEDULER")
            pcb.setState("STATE_RUNNING")
            self.kernel.dispatcher.load(pcb)
            self.kernel.pcbTable.setRunningPCB(pcb)

    def handleTimeOut(self):
        print("TIMEOUT")
        if self.kernel.pcbTable.runningPCB is not None:
            runningPCB = self.kernel.pcbTable.runningPCB
            self.kernel.dispatcher.save(runningPCB)
            if self.kernel.scheduler.isEmpty():
                self.kernel.dispatcher.load(runningPCB)
            else:
                nextPCB = self.kernel.scheduler.getNext()
                nextPCB.setState("STATE_RUNNING")
                runningPCB.setState("STATE_READY")
                self.kernel.dispatcher.load(nextPCB)
                self.kernel.scheduler.add(runningPCB)
                self.kernel.pcbTable.setRunningPCB(nextPCB)



    def putPCBInCPU(self, pcb):

        if pcb is not None:
                pcb.setState("STATE_RUNNING")
                self.kernel.dispatcher.load(pcb)
                self.kernel.pcbTable.setRunningPCB(pcb)

    def createNewPCB(self, program):
        print("estoy creando un nuevo pcb")
        #baseDir = self._kernel.hardware.memory.load(program)
        pcb = PCB()
        pcb.setPath(program.path)
        pcb.setPid(self.kernel.pcbTable.getNewPid())
        # pcb._baseDir = program.baseDir
        pcb.setPriority(program.priority)
        pcb.pageTable = self.hardware.loader.load(pcb)
        self.kernel.pcbTable.add(pcb)
        print("PRIORIDAD CREADA: {pcb}".format(pcb=pcb.getPriority))
        return pcb








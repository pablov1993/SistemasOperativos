from InterruptionHandler import InterruptionHandler
from PCB import PCB


class NewHandler(InterruptionHandler):
    def __init__(self, kernel):

        super().__init__(kernel)

    def exec(self, program):

        print("arrived to new")
        #baseDir = self._kernel.memory.load(program)

        pcb = self.createNewPCB(program)

        print(pcb.pid)
        #pcb._baseDir = baseDir

        print("no setie")




        print("agregue")
        pcbToExpropiate = self.kernel.pcbTable.runningPCB

        if self.kernel.pcbTable.runningPCB == 0:
            pcb.setState("STATE_RUNNING")
            self._kernel.dispatcher.load(pcb)
            self._kernel.pcbTable.setRunningPCB(pcb)
        else:
            if self.kernel.scheduler.mustExpropiate(pcbToExpropiate, pcb):
                pcbAExpropiar.setState("STATE_READY")
                self.kernel.dispatcher.save(pcbAExpropiar)
                self.kernel.scheduler.add(pcbAExpropiar)
                pcb.setState("STATE_RUNNING")
                self.kernel.dispatcher.load(pcb)
                self.kernel.pcbTable.setRunningPCB(pcb)
            else:
                pcb.setState("STATE_READY(constante)")
                self.kernel.scheduler.add(pcb)

    def putPCBInCPU(self, pcb):

        if pcb is not None:

            pcb.setState("STATE_RUNNING")
            self.kernel.dispatcher.load(pcb)
            self.kernel.pcbTable.setRunningPCB(pcb)

    def createNewPCB(self, program):

        print("estoy creando un nuevo pcb")

        pcb = PCB()
        pcb.setPid(self.kernel.pcbTable.getNewPid)

        print("el pid ya esta")

        pcb.setPriority = None
        self.kernel.pcbTable.add(pcb)
        return pcb




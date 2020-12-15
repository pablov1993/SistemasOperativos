from PCB import PCB
from interruptions.InterruptionHandler import InterruptionHandler


class NewHandler(InterruptionHandler):
    def __init__(self, kernel):
        super().__init__(kernel)

    def exec(self, program):

        pcb = PCB()
        pcb.setPid(self.kernel.pcbTable.getNewPid())
        pcb.setPath(program.name)
        pcb.setPageTable(self.kernel.hardware.loader.load(pcb.path))
        self.kernel.pcbTable.add(pcb)
        pcbAExpropiar = self.kernel.pcbTable.runningPCB

        if self.kernel.pcbTable.runningPCB == None:
            pcb.setState("STATE_RUNNING")
            self._kernel.dispatcher.load(pcb)
            self._kernel.pcbTable.setRunningPCB(pcb)
        else:
            if self.kernel.scheduler.mustExpropiate(pcbAExpropiar, pcb):
                pcbAExpropiar.setState("STATE_READY")
                self.kernel.dispatcher.save(pcbAExpropiar)
                self.kernel.scheduler.add(pcbAExpropiar)
                pcb.setState("STATE_RUNNING")
                self.kernel.dispatcher.load(pcb)
                self.kernel.pcbTable.setRunningPCB(pcb)
            else:
                pcb.setState("STATE_READY(constante)")
                self.kernel.scheduler.add(pcb)





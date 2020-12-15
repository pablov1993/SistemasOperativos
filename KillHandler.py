from InterruptionHandler import InterruptionHandler


class KillHandler(InterruptionHandler):
    def __init__(self, kernel):
        super().__init__(kernel)

    def exec(self, program):
        pcb = self._kernel.pcbTable.runningPCB()
        self.kernel.dispatcher.save(pcb)
        pcb.setState("STATE_TERMINATE")
        self.kernel.pcbTable.setRunningPCB(0)
        if not (self.kernel.scheduler.isEmpty()):
            nextPcb = self.kernel.scheduler.getNext()
            nextPcb.setState("STATE_RUNNING")
            self.kernel.dispatcher.load(next)
            self.kernel.pcbTable.add(next)

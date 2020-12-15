from interruptions.InterruptionHandler import InterruptionHandler

class IO_INHandler(InterruptionHandler):

    def __init__(self, kernel , ioDevice):
        super().__init__(kernel)
        self._ioDevice = ioDevice 

    def exec(self, program):

        pcbRunning = self._kernel.pcbTable.runningPCB
        self._kernel.dispatcher.save(pcbRunning)
        if self._kernel.scheduler.isEmpty():
            pcbRunning.setState("STATE_WAITING")
            self._ioDevice.add(pcbRunning)
            pcbToAdd = self._kernel.scheduler.getNext()
            pcbToAdd.setState("STATE_RUNNIG")
            self._kernel.dispatcher.load(pcbToAdd)
            self._kernel.pcbTable.runningPCB(pcbToAdd)
        else:
            pcbRunning.setState("STATE_RUNNIG")
            self._kernel.dispatcher.load(pcbRunning)
            self._kernel.pcbTable.runningPCB(pcbRunning)
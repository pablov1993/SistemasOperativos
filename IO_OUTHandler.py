from InterruptionHandler import InterruptionHandler


class IO_OUTHandler(InterruptionHandler):

    def __init__(self, kernel, ioDevice):
        super().__init__(kernel)
        self._ioDevice = ioDevice

    def exec(self, program):
        pcbOut = self._ioDevice.currentPCB #vuelve del io in
        pcbRunning = self._kernel.pcbtable.runningPCB
        if not pcbRunning == None :
            if self._kernel.scheduler.mustExpropiate(pcbRunning, pcbOut):

                pcbRunning.setState("STATE_READY")
                self._kernel.dispatcher.save(pcbRunning)
                self._kernel.scheduler.add(pcbRunning)
                pcbOut.setState("STATE_RUNNING")
                self._kernel.pcbtable.runningPCB(pcbOut)
                self._kernel.dispatcher.load(pcbOut)
            else:
                pcbOut.setState("STATE_READY")
                self._kernel.scheduler.add(pcbOut)
        else:
            pcbOut.setState("STATE_RUNNING")
            self._kernel.dispatcher.load(pcbOut)
            self._kernel.pcbtable.runningPCB(pcbOut)
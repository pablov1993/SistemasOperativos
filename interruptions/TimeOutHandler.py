from interruptions.InterruptionHandler import InterruptionHandler


class TimeOutHandler(InterruptionHandler):

    def __init__(self , kernel):
        InterruptionHandler.__init__(self , kernel)

    def exec(self, program):
        pcbInCpu = self._kernel.pcbTable.runningPCB
        self._kernel.dispatcher.save(pcbInCpu)


        if self._kernel.scheduler.isEmpty():
            pcbInCpu.setState("STATE_RUNNING")
            self._kernel.dispatcher.load(pcbInCpu)
        else:
            #Agrego un nuevo proceso a ejecutar
            pcbInCpu.setState("STATE_WAITING")
            self._
            kernel.scheduler.add(pcbInCpu)
            pcbToAdd = self._kernel.scheduler.getNext()
            pcbToAdd.setState("STATE_RUNNING")
            self._kernel.pcbTable.runningPCB(pcbToAdd)
            self._kernel.dispatcher.load(pcbToAdd)




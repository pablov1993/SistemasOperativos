class Dispatcher():
    def __init__(self, cpu, mmu, timer):
        self._cpu = cpu
        self._mmu = mmu
        self._timer = timer

    def load(self, pcb):
        self._cpu.pc = pcb.getPC
        self._mmu.setBaseDir(pcb.getBaseDir)
        self._timer.reset()

    def save(self, pcb):
        pcb._pc = self._cpu._pc
        self._cpu._pc = -1


class DispatcherPages():
    def __init__(self, cpu, mmu, timer):
        self._cpu = cpu
        self._mmu = mmu
        self._timer = timer

    def load(self, pcb):
        self._cpu.pc = pcb.getPC
        print("pid a cargar: {pid}".format(pid=pcb.pid))
        self._mmu.pageTable = pcb.pageTable
        self._timer.reset()

    def save(self, pcb):
        pcb._pc = self._cpu._pc
        self._cpu._pc = -1

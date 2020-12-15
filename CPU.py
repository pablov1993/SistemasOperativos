from IRQ import IRQ


class Cpu():
    def __init__(self, hardware, log):
        self._logger = log
        self._hardware = hardware
        self._pc = -1
        self._ir = None

    def tick(self):
        if self._pc > -1:
            self._fetch()
            self._decode()
            self._execute()

    def _fetch(self):
        self._ir = self._hardware.mmu.fetch(self._pc)
        self._pc += 1

    def _decode(self):
        # el decode no hace nada en este emulador
        pass

    def _execute(self):
        # modificar variable IRQ

        irq = None

        if self._ir.isExit():
            self._hardware.interruptVector.handleExit()

        if self._ir.isIO():
            irq = "IO_IN"
            self._hardware.interruptVector.handleIOIN()
        else:
            self._logger.info("Exec: {op}, PC={pc}".format(op=self._ir, pc=self._pc))

    @property
    def pc(self):
        return self._pc

    @pc.setter
    def pc(self, addr):
        self._pc = addr

    def __repr__(self):
        return "CPU(PC={pc})".format(pc=self._pc)

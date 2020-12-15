from time import sleep


class Clock:
    def __init__(self, cpu, timer, ioDevice):
        self._cpu = cpu
        self._timer = timer
        self._ioDevice = ioDevice

    def start(self):
        while True:
            self._cpu.tick()
            self._timer.tick()
            self._ioDevice.tick()
            sleep(0.5)



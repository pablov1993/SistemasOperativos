from Instructions import Instruction


class CPU(Instruction):
    def __repr__(self):
        if self._count:
            return "CPU({count})".format(count=self._count)
        else:
            return "CPU"

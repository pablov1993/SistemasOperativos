from Instructions import Instruction


class IO(Instruction):
    def __repr__(self):
        if self._count:
            return "IO({count})".format(count=self._count)
        else:
            return "IO"

    def isIO(self):
        return True
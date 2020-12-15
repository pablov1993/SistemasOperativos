from Instructions import Instruction


class EXIT(Instruction):

    def isExit(self):
        return True

    def __repr__(self):
        return "EXIT"

from tabulate import tabulate


class Memory:
    def __init__(self, size):
        self._memory = {}
        self._size = size
        self.setUpMemory()

    def load(self, programs):
        self._memory = programs.instructions


    def fetch(self, addr):
        return self._memory[addr]

    def put(self, addr, instruction):
            self._memory[addr] = instruction

    def __repr__(self):
        return tabulate(enumerate(self._memory), tablefmt='psql')

    def setUpMemory(self):
        for i in range(0 , self._size):
            self._memory[i] = None
    @property
    def getSize(self):
        return len(self._memory)
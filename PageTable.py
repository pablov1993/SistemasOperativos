
class PageTable():
    def __init__(self):
        self._pageTable = []

    def add(self, pageTable):
        self._pageTable.append(pageTable)

    @property
    def table(self):
        return self._pageTable

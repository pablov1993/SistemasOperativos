class PCB():
    def __init__(self):
        self._pid = 0
        self._baseDir = 0
        self._pc = 0
        self._state = "STATE_NEW(constante)"
        self._path = ""
        self._priority = 0
        self._pageTable = None

    @property
    def state(self):
        return self._state

    def setPriority(self, priority):
        self._priority = priority

    @property
    def getPriority(self):
        return self._priority

    @property
    def getPC(self):
        return self._pc

    @property
    def getBaseDir(self):
        return self._baseDir

    @property
    def pid(self):
        return self._pid

    @property
    def path(self):
        return self._path

    def setState(self, state):
        self._state = state

    def setPath(self, path):

        print("hasta aca")
        self._path = path

    def setPid(self, nro):
        print("me dieron uno")
        self._pid = nro

    @property
    def pageTable(self):
        return self._pageTable

    @pageTable.setter
    def pageTable(self, value):
        self._pageTable = value

    @getBaseDir.setter
    def baseDir(self, baseDir):
        self._baseDir = baseDir

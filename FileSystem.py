
class FileSystemContiguous:

    def __init__(self):
        self._slots = {}

    def save(self, program):
        self._slots[program.path] = program.instructions

    def getProgram(self, path):
        return self._slots[path]


class FileSystem:

    def __init__(self, frameSize):
        self._programs = {} #misProgramas
        self._frameSize = frameSize #tamaño del frame
        self._pages = {} #Diccionario de paginas con instrucciones

    def save(self, program):
        # Agrego un programa a diccionario de programas
        self._programs[program.path] = program
        #lista de instrucciones del programa
        instructions = program.instructions

        self._pages[program.path] = []
        page = []

        for instruction in instructions:

            page.append(instruction)

            if len(page) == self._frameSize:
                self._pages[program.path].append(page)
                page = []

        if len(page) != 0:
            self._pages[program.path].append(page)
        print("cargue el programa")

    def getProgram(self, path, page):
        paginatedProgram = self._pages[path]
        return paginatedProgram[page]

    def getProgramSize(self, path):

        return len(self._programs[path].instructions)

































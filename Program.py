from InstrEXIT import EXIT


class Program():

    def __init__(self, name, instructions,path, priority):
        self._name = name
        self._instructions = self.expand(instructions)
        self._path = path
        self._priority = priority


    @property
    def path(self):
        return self._path
    @property
    def name(self):
        return self._name

    @property
    def instructions(self):
        return self._instructions

    @property
    def priority(self):
        return self._priority

    def expand(self, instructions):
        expanded = []

        for instr in instructions:
            expanded.extend(instr.expand())

        if not expanded[-1].isExit():
            expanded.append(EXIT(0))

        return expanded

    def __repr__(self):
        return "Program({name}, {instructions})".format(name=self._name, instructions=self._instructions)

from Logger import *
from InstrCPU import CPU
from InstrIO import IO
from SO import SO
from Program import Program

if __name__ == '__main__':

    logger.setLevel(logging.DEBUG)
    logger.info('Starting emulator')

    # Sigo iniciando el emulador

    so = SO(logger)

    # Cargar programas
    p1 = Program("test.exe", [CPU(2), IO(1), CPU(3)], "C", 1)
    p2 = Program("test1.exe", [CPU(2), CPU(1), CPU(2)], "C", 4)
    p3 = Program("test2.exe", [CPU(5), CPU(3)], "C", 2)

    programs = [p1, p2, p3]

    # Inicio de ejecucion

    so.start(programs)


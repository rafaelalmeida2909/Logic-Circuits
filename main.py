from Circuit import Circuit
from os import listdir


def main():
    files = listdir("descriptions")
    for file_ in files:
        obj = Circuit(file_)
        obj.read()
        obj.inputGates()
        obj.solveGates()
        obj.writeTrueTable()


main()

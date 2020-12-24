from Stack import LinkedStack
from os import path
from Gates import Gates
from tabulate import tabulate


class Circuit():
    desc = []

    def __init__(self, file_name):
        self.file_name = file_name
        self.inputs = []
        self.outputs = []
        self.n_inputs = 0
        self.n_outputs = 0
        self.n_gates = 0
        self.points = {}

    @staticmethod
    def decToBin(num, length=0):
        stack = LinkedStack()
        bins = []
        while num != 0:
            stack.push(num % 2)
            num = num//2
        while not stack.empty():
            bins.append(stack.pop())
        while len(bins) < length:
            bins.insert(0, 0)
        return bins

    def read(self):
        try:
            with open(path.join("descriptions", self.file_name), "r") as description:
                lines = description.readlines()
                Circuit.desc = lines[3::]
                for line in lines:
                    desc = line.split(",")
                    if desc[0] == "n_inputs":
                        self.n_inputs = int(desc[1])
                        for inpt in desc[2::]:
                            self.points.setdefault(inpt.split()[0], [])
                            self.inputs.append(inpt.split()[0])
                    elif desc[0] == "n_outputs":
                        self.n_outputs = int(desc[1])
                        for output in desc[2::]:
                            self.points.setdefault(output.split()[0], [])
                            self.outputs.append(output.split()[0])
                    elif desc[0] == "n_gates":
                        self.n_gates = int(desc[1])
                    else:
                        for inpts in desc[3::]:
                            self.points.setdefault(inpts.split()[0], [])
        except FileNotFoundError:
            print("File not found")

    def inputGates(self):
        for i in range(2**self.n_inputs):
            bins = self.decToBin(i, self.n_inputs)
            count = 0
            for inpt in self.inputs:
                self.points[inpt].append(bins[count])
                count += 1

    def solveGates(self):
        solved = self.inputs.copy()
        gates = Gates()
        dic = {"and": gates.AND, "or": gates.OR, "xor": gates.XOR,
               "nor": gates.NOR, "nand": gates.NAND, "xnor": gates.XNOR,
               "not": gates.NOT}
        while Circuit.desc.count(None) != self.n_gates:
            count = 0
            for line in self.desc:
                ver = True
                if line is None:
                    count += 1
                    continue
                gate = line.split()[0][1::].split(",")[1::]
                for inpt in gate[2::]:
                    if inpt not in solved:
                        ver = False
                        break
                if ver:
                    if gate[0] in dic.keys():
                        bins = [self.points[bin] for bin in gate[2::]]
                        self.points[gate[1]] = dic[gate[0]](bins)
                        solved.append(gate[1])
                        self.desc[count] = None
                    else:
                        raise Exception(
                            f"Gate type: {gate[0].lower}, invalid!")
                count += 1

    def writeTrueTable(self):
        try:
            with open(path.join("true tables", f"True Table - {self.file_name}.txt"), "w+") as t:
                count = 0
                table = []
                for _ in range(2**self.n_inputs):
                    aux = []
                    for j in self.inputs:
                        aux.append(self.points[j][count])
                    for j in self.outputs:
                        aux.append(self.points[j][count])
                    table.append(aux)
                    count += 1
                t.write(tabulate(table, headers=self.inputs +
                                 self.outputs, tablefmt="orgtbl"))
        except FileNotFoundError:
            print("File not found")

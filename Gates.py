class Gates():
    def AND(self, input):
        bins = input.copy()
        aux = []
        for index in range(len(bins[0])):
            if bins[0][index] == 1 and bins[1][index] == 1:
                aux.append(1)
            else:
                aux.append(0)
        bins.insert(0, aux)
        del bins[1]
        del bins[1]
        if len(bins) == 1:
            return bins[0]
        return self.AND(bins)

    def OR(self, input):
        bins = input.copy()
        aux = []
        for index in range(len(bins[0])):
            if bins[0][index] == 1 or bins[1][index] == 1:
                aux.append(1)
            else:
                aux.append(0)
        bins.insert(0, aux)
        del bins[1]
        del bins[1]
        if len(bins) == 1:
            return bins[0]
        return self.OR(bins)

    def XOR(self, input):
        bins = input.copy()
        aux = []
        for index in range(len(bins[0])):
            if (bins[0][index] == 1 and bins[1][index] == 0) or \
                    (bins[0][index] == 0 and bins[1][index] == 1):
                aux.append(1)
            else:
                aux.append(0)
        bins.insert(0, aux)
        del bins[1]
        del bins[1]
        if len(bins) == 1:
            return bins[0]
        return self.XOR(bins)

    def NAND(self, input):
        return self.NOT(self.AND(input))

    def NOR(self, input):
        return self.NOT(self.OR(input))

    def XNOR(self, input):
        return self.NOT(self.XOR(input))

    def NOT(self, input):
        if len(input) == 1:
            input = input[0]
        list_return = []
        for bin in input:
            if bin == 1:
                list_return.append(0)
            else:
                list_return.append(1)
        return list_return

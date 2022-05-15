class ReadFromFile:
    @staticmethod
    def read():
        capacity = 0
        amount = 0
        values = []
        weights = []

        f = open("f3_l-d_kp_4_20", "r")
        line = f.readline()
        index = 0

        while bool(line.strip()):
            index += 1
            line_data = line.split()
            if index == 1:
                amount = int(line_data[0])
                capacity = int(line_data[1])
            else:
                values.append(int(line_data[0]))
                weights.append(int(line_data[1]))
            line = f.readline()

        return capacity, amount, values, weights

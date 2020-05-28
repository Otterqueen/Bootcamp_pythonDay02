import sys


class CsvReader:

    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.fd = None
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.datas = []

    def __enter__(self):
        try:
            self.fd = open(self.filename, "r")
            self.read_file()
            return self
        except FileNotFoundError:
            return None
        self.read_file()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fd:
            self.fd.close()

    def read_file(self):
        data = self.fd.readlines()[self.skip_top:]
        del data[:self.skip_bottom]
        if self.header is True:
            self.header = data[0][:-1].split(self.sep)
            for i in range(1, len(data)):
                new_dict = {}
                line_split = data[i][:-1].split(self.sep)
                for j in range(0, len(self.header)):
                    new_dict[self.header[j]] = line_split[j]
                self.datas.append(new_dict)
        else:
            for line in data:
                self.datas.append(line[:len(line) - 1].split(self.sep))

    def getdata(self):
        return self.datas

    def getheader(self):
        return self.header


# main de test
if __name__ == "__main__":
    with CsvReader('test.csv') as file:
        if file is None:
            print("File is corrupted or not found")
            sys.exit()
        data = file.getdata()
        header = file.getheader()
        print(data)

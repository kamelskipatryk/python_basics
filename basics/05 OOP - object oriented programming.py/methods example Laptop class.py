
class Laptop:
    def __init__(self, cpu, ram = 4096, gpu = 'AMD', price = 2000):
        self.set_cpu(cpu)
        self.set_ram(ram)
        self.gpu = gpu
        self.price = price

    def set_cpu(self, cpu):
        if cpu.lower() == 'amd' or cpu.lower() == 'intel' or cpu.lower() == 'arm':
            self.cpu = cpu
            print('nadałem cpu')
        else:
            self.cpu = 'unknown'
    
    def set_ram(self, ram):
        if type(ram) == int and ram >= 2048:
            self.ram = ram
        else:
            self.ram = 2048

    def print_data(self):
        print(self.cpu, self.ram, self.gpu, self.price)

laptop_1 = Laptop('INTEL')
laptop_1.print_data()

laptop_2 = Laptop('amd', 32000)
laptop_2.print_data()
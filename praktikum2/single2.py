class Motor:
    def __init__(self, nama, cc):
        self.nama = nama
        self.cc = cc

    def kecepatan(self):
        print(f"{self.nama} berkecepatan tinggi")

class Ducati(Motor):
    def __init__(self, nama, cc, jenis):
        super().__init__(nama, cc)
        self.jenis = jenis

    def balapan(self):
        print(f"{self.nama} dengan jenis {self.jenis} sedang balapan")
        
ducatiA = Ducati("Ducati", 1099 , "S")
ducatiA.kecepatan() 
ducatiA.balapan() 
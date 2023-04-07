class kendaraan:
    def move(self):
        print("kendaraan beroda")

class mobil(kendaraan):
    def move(self):
        print("mobil beroda empat")

class motor(kendaraan):
    def move(self):
        print("motor beroda dua")

A = kendaraan()
B = mobil()
C = motor()

A.move()    
B.move()    
C.move()    
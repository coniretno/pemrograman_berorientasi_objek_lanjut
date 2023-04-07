from abc import ABC, abstractmethod

class kendaraan(ABC):
    @abstractmethod
    def start(self):
        pass

class mobil(kendaraan):
    def start(self):
        print("mobil memerlukan kunci")

class motor(kendaraan):
    def start(self):
        print("motor memerlukan kunci")

class sepeda(kendaraan):
    def start(self):
        print("sepeda tidak memerlukan kunci")



A = mobil()
B = motor()
C = sepeda()

A.start()    
B.start()    
C.start()    
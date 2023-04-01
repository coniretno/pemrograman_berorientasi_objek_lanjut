class Kuliner:
    def __init__(self, nama, daerah):
        self.nama = nama
        self.daerah = daerah

    def khas(self):
        print(self.nama, "makanan khas indonesia")
        
class Surabaya(Kuliner):
    def __init__(self, nama, karakter, jenis_makanan):
        super().__init__(nama, karakter)
        self.jenis_makanan = jenis_makanan
        
    def rasa(self):
        print("cenderung pedas")
        
surabayaA = Surabaya("Lontong Balap","Lontong" , "Berat")
surabayaA.khas() 
surabayaA.rasa() 
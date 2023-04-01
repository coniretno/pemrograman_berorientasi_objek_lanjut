class kendaraan:
    def __init__(self, brand, model, tahun):
        self.brand = brand
        self.model = model
        self.tahun = tahun
    
    def drive(self):
        pass
    
class mobil(kendaraan):
    def __init__(self, brand, model, tahun, jml_pintu):
        super().__init__(brand, model, tahun)
        self.jml_pintu = jml_pintu
    
    def drive(self):
        return "Mengendarai Mobil  " + self.brand + " " + self.model
    
class motor(kendaraan):
    def __init__(self, brand, model, tahun, cc):
        super().__init__(brand, model, tahun)
        self.cc = cc
    
    def drive(self):
        return "Mengendarai Motor " + self.brand + " " + self.model
    
class mobil_listrik(mobil):
    def __init__(self, brand, model, tahun, jml_pintu, kapasitas_baterai):
        super().__init__(brand, model, tahun, jml_pintu)
        self.kapasitas_baterai = kapasitas_baterai
    
    def charge(self):
        return "Mengisi Daya Mobil " + self.brand + " " + self.model + " dengan daya" + str(self.kapasitas_baterai) + " kWh"
    
mbl_saya = mobil("Toyota", "Rush", 2021, 3)
mtr_saya = motor("Honda", "Vario", 2019, "125 cc")
ev_saya = mobil_listrik("Wuling", "Air EV", 2018, 2, 100)

print(mbl_saya.drive())
print(mtr_saya.drive())
print(ev_saya.drive())
print(ev_saya.charge())
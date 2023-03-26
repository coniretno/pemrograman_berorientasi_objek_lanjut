class celctemp:
    def __init__(self, celcius):
        self.celcius = celcius

    def fahrenheit(self):
        return (self.celcius * 9/5) + 32
    def reamur(self):
        return (self.celcius * 4/5)
    def kelvin(self):
        return (self.celcius + 273.15)
    

    print("Suhu Celcius")
celc1 = celctemp(23)
print(f"Konversi dari Celcius ke Fahrenheit: {celc1.fahrenheit()}")
celc2 = celctemp(34)
print(f"Konversi dari Celcius ke Reamur: {celc2.reamur()}")
celc3 = celctemp(45)
print(f"Konversi dari Celcius ke Kelvin: {celc3.kelvin()}")
print("="*45)
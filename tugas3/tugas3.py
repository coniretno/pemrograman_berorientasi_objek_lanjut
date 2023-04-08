
from suara import suara

class Hewan:
    suara = "hewan.mp3"

    def mainkan_suara(self):
        suara(self.suara)

class Singa(Hewan):
    suara = "singa.mp3"

class Serigala(Hewan):
    suara = "serigala.mp3"

class Ayam(Hewan):
    suara = "ayam.mp3"

class Sapi(Hewan):
    suara = "sapi.mp3"

class Gajah(Hewan):
    suara = "gajah.mp3"

class Jangkrik(Hewan):
    suara = "jangkrik.mp3"

class Katak(Hewan):
    suara = "katak.mp3"

class Bebek(Hewan):
    suara = "bebek.mp3"

class Burung(Hewan):
    suara = "burung.mp3"

class Tokek(Hewan):
    suara = "tokek.mp3"


singa=Singa()
serigala=Serigala()
ayam=Ayam() 
sapi=Sapi()
gajah=Gajah()
jangkrik=Jangkrik()
katak=Katak()
bebek=Bebek()
burung=Burung()
tokek=Tokek()


singa.mainkan_suara()
serigala.mainkan_suara()
ayam.mainkan_suara()
sapi.mainkan_suara()
gajah.mainkan_suara()
jangkrik.mainkan_suara()
katak.mainkan_suara()
bebek.mainkan_suara()
burung.mainkan_suara()
tokek.mainkan_suara()
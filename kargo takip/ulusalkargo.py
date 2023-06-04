from kargo import Kargo

# UlusalKargo sınıfı
class UlusalKargo(Kargo):
    def __init__(self, numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici, sehir):
        super().__init__(numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici)
        self.sehir = sehir
    
    def getInfo(self):
        return super().getInfo() + f"\nŞehir: {self.sehir}"

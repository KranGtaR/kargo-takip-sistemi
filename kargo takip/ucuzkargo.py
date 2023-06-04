from kargo import Kargo

# UcuzKargo sınıfı
class UcuzKargo(Kargo):
    def __init__(self, numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici, fiyat):
        super().__init__(numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici)
        self.fiyat = fiyat
    
    def getInfo(self):
        return super().getInfo() + f"\nFiyat: {self.fiyat}"

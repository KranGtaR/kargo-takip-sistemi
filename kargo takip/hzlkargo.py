from kargo import Kargo

class HizliKargo(Kargo):
    def __init__(self, numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres,gonderici, hiz):
        super().__init__(numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres,gonderici)
        self.hiz = hiz
    
    def getInfo(self):
        return super().getInfo() + f"\nHız: {self.hiz}"
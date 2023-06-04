# Kargo sınıfı
class Kargo:
    def __init__(self, numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres,gonderici):
        self.numara = numara
        self.teslimat_durumu = teslimat_durumu
        self.teslim_edilebilme_durumu = teslim_edilebilme_durumu
        self.gonderi_tarihi = gonderi_tarihi
        self.alici_ad = alici_ad
        self.alici_adres = alici_adres
        self.teslimat_tarihi = None
        self.gonderici=gonderici
        
    def odeme_yap(self, odeme_tutari):
        # Ödeme işlemleri burada yapılır.
        self.teslimat_durumu = "Ödeme Yapıldı"
    def teslim_edilebilir_mi(self):
        if self.teslim_edilebilme_durumu == "Evet":
            return True
        else:
            return False
    
    def teslimat_tarihi_belirle(self, teslimat_tarihi):
        self.teslimat_tarihi = teslimat_tarihi
        
    def getInfo(self):
        return f"Takip numarası: {self.numara}\nGönderici: {self.gonderici}\nAlıcı: {self.alici_ad}\nTeslim durumu: {self.teslim_edilebilme_durumu}"
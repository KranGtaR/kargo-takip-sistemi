
# TeslimEdilebilir sınıfı
class TeslimEdilebilir:
    def __init__(self, teslim_edilebilme_durumu):
        self.teslim_edilebilme_durumu = teslim_edilebilme_durumu
    
    def teslim_edilebilir_mi(self):
        if self.teslim_edilebilme_durumu == "Evet":
            return True
        else:
            return False

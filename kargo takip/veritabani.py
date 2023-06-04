
# Veritabani sınıfı
class Veritabani():
    def __init__(self):
        self.kargo_listesi = []
    
    def kargo_ekle(self, kargo):
        self.kargo_listesi.append(kargo)
    
    def kargo_sorgula(self, numara):
        for kargo in self.kargo_listesi:
            if kargo.numara == numara:
                return kargo
        return "Kargo bulunamadı."
    
    def kargo_sil(self, numara):
        for kargo in self.kargo_listesi:
            if kargo.numara == numara:
                self.kargo_listesi.remove(kargo)
                return "Kargo silindi."
        return "Kargo bulunamadı."
    
    def teslimat_sorgula(self, numara):
        for kargo in self.kargo_listesi:
            if kargo.numara == numara:
                return kargo.teslimat_sorgula()
        return "Kargo bulunamadı."

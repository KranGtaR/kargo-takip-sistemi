import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QDateEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QDate
from teslimedilebilir import TeslimEdilebilir
from kargo import Kargo

class KargoAraci(QWidget,TeslimEdilebilir,Kargo):
    def __init__(self):
        super().__init__(teslim_edilebilme_durumu=True)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Kargo Takip Aracı")

        self.initUI()

    def initUI(self):
        # Girdi alanları
        self.entry_numara_description = QLabel("Kargo Takip Numarası:", self)
        self.entry_numara = QLineEdit(self)
        self.entry_teslimat_durumu_description = QLabel("Teslimat Durumu:", self)
        self.entry_teslimat_durumu = QLineEdit(self)
        self.entry_teslim_edilebilme_durumu_description = QLabel("Teslim Edilebilme Durumu:", self)
        self.entry_teslim_edilebilme_durumu = QLineEdit(self)
        self.entry_gonderi_tarihi_description = QLabel("Gönderi Tarihi:", self)
        self.entry_gonderi_tarihi = QLineEdit(self)
        self.entry_alici_ad_description = QLabel("Alici Adı:", self)
        self.entry_alici_ad = QLineEdit(self)
        self.entry_alici_adres_description = QLabel("Alici Adresi:", self)
        self.entry_alici_adres = QLineEdit(self)
        self.entry_gonderici_description = QLabel("Gönderici:", self)
        self.entry_gonderici = QLineEdit(self)


        # Butonlar
        self.button_odeme_yap = QPushButton("Ödeme Yap", self)
        self.button_odeme_yap.clicked.connect(self.odeme_yap)
        self.button_teslim_edilebilir_mi = QPushButton("Teslim Edilebilir mi?", self)
        self.button_teslim_edilebilir_mi.clicked.connect(self.teslim_edilebilir_mi)
        self.button_takip_et = QPushButton("Kargo Takip Et", self)
        self.button_takip_et.clicked.connect(self.kargo_takip_et)
        
        # Tarih seçici
        self.date_teslimat_tarihi = QDateEdit(self)
        self.date_teslimat_tarihi.setDate(QDate.currentDate())

        # Etiket
        self.label_bilgi = QLabel("", self)

        # Yerleşim
        vbox = QVBoxLayout()
        vbox.addWidget(self.entry_numara_description)
        vbox.addWidget(self.entry_numara)
        vbox.addWidget(self.entry_teslimat_durumu_description)
        vbox.addWidget(self.entry_teslimat_durumu)
        vbox.addWidget(self.entry_teslim_edilebilme_durumu_description)
        vbox.addWidget(self.entry_teslim_edilebilme_durumu)
        vbox.addWidget(self.entry_gonderi_tarihi_description)
        vbox.addWidget(self.entry_gonderi_tarihi)
        vbox.addWidget(self.entry_alici_ad_description)
        vbox.addWidget(self.entry_alici_ad)
        vbox.addWidget(self.entry_alici_adres_description)
        vbox.addWidget(self.entry_alici_adres)
        vbox.addWidget(self.entry_gonderici_description)
        vbox.addWidget(self.entry_gonderici)
        vbox.addWidget(self.button_odeme_yap)
        vbox.addWidget(self.button_teslim_edilebilir_mi)
        vbox.addWidget(self.date_teslimat_tarihi)
        vbox.addWidget(self.label_bilgi)
        vbox.addWidget(self.button_takip_et)
        self.setLayout(vbox)
        self.show()
        
    def odeme_yap(self):
        numara = self.entry_numara.text()
        teslimat_durumu = self.entry_teslimat_durumu.text()
        teslim_edilebilme_durumu = self.entry_teslim_edilebilme_durumu.text()
        gonderi_tarihi = self.entry_gonderi_tarihi.text()
        alici_ad = self.entry_alici_ad.text()
        alici_adres = self.entry_alici_adres.text()
        gonderici = self.entry_gonderici.text()

        self.kargo = Kargo(numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici)
        self.kargo.odeme_yap(0)
        self.label_bilgi.setText("Ödeme yapıldı!")
    
    def teslim_edilebilir_mi(self):
        numara = self.entry_numara.text()
        teslimat_durumu = self.entry_teslimat_durumu.text()
        teslim_edilebilme_durumu = self.entry_teslim_edilebilme_durumu.text()
        gonderi_tarihi = self.entry_gonderi_tarihi.text()
        alici_ad = self.entry_alici_ad.text()
        alici_adres = self.entry_alici_adres.text()
        gonderici = self.entry_gonderici.text()

        self.kargo = Kargo(numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici)
        if self.kargo.teslim_edilebilir_mi():
            self.label_bilgi.setText("Teslim edilebilir.")
        else:
            self.label_bilgi.setText("Teslim edilemez.")
    def kargo_takip_et(self):
        numara = self.entry_numara.text()
        teslimat_durumu = self.entry_teslimat_durumu.text()
        teslim_edilebilme_durumu = self.entry_teslim_edilebilme_durumu.text()
        gonderi_tarihi = self.entry_gonderi_tarihi.text()
        alici_ad = self.entry_alici_ad.text()
        alici_adres = self.entry_alici_adres.text()
        gonderici = self.entry_gonderici.text()

        self.kargo = Kargo(numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici)
        self.kargo.takip_et()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    arac = KargoAraci()
    sys.exit(app.exec_())


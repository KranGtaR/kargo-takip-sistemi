from arayüz import KargoAraci
from hızlıkargo import HizliKargo
from international import InternationalKargo
from kargo import Kargo 
from kargofirmasi import KargoFirmasi
from teslimedilebilir import TeslimEdilebilir
from ucuzkargo import UcuzKargo
from ulusalkargo import UlusalKargo
from veritabani import Veritabani
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QDateEdit, QPushButton, QVBoxLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    arac = KargoAraci()
    sys.exit(app.exec_())

import sys
import os
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QVBoxLayout, QTextEdit, qApp, QMainWindow, QAction, QMessageBox
from PyQt5.QtCore import QDateTime


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()

        self.resize(600, 400)
        yazi_alani = QWidget()
        self.setCentralWidget(yazi_alani)

        layout = QVBoxLayout(yazi_alani)
        layout.setContentsMargins(0, 0, 0, 0)

        self.text_area = QTextEdit()
        layout.addWidget(self.text_area)
        
        

        self.setWindowTitle("Notepad")
        self.show()



        # dosya baslangic

        dosya = menubar.addMenu("Dosya")

        yeni = QAction("Yeni", self)
        yeni.setShortcut("Ctrl+N")

        yeni_pencere = QAction("Yeni Pencere", self)
        yeni_pencere.setShortcut("Ctrl+Shift+N")

        ac = QAction("Aç...", self)
        ac.setShortcut("Ctrl+O")

        kaydet = QAction("Kaydet", self)
        kaydet.setShortcut("Ctrl+S")

        farkli_kaydet = QAction("Farkli Kaydet", self)
        farkli_kaydet.setShortcut("Ctrl+Shift+S")

        sayfa_yapisi = QAction("Sayfa Yapisi", self)
        yazdir = QAction("Yazdir...", self)
        yazdir.setShortcut("Ctrl+P")
        cikis = QAction("Çikiş", self)


        yeni.triggered.connect(self.yeni)
        yeni_pencere.triggered.connect(self.yeni_pence)
        farkli_kaydet.triggered.connect(self.farkli_kayde)
        ac.triggered.connect(self.ac)
        cikis.triggered.connect(self.cikis)
        kaydet.triggered.connect(self.kaydet)

        dosya.addAction(yeni)
        dosya.addAction(yeni_pencere)
        dosya.addAction(ac)
        dosya.addAction(kaydet)
        dosya.addAction(farkli_kaydet)
        dosya.addAction(sayfa_yapisi)
        dosya.addAction(yazdir)
        dosya.addAction(cikis)



        # duzen baslangic

        duzen = menubar.addMenu("Düzen")

        geri_al = QAction("Geri Al", self)
        geri_al.setShortcut("Ctrl+Z")

        kes = QAction("Kes", self)
        kes.setShortcut("Ctrl+X")

        kopyala = QAction("Kopyala", self)
        kopyala.setShortcut("Ctrl+C")

        yapistir = QAction("Kopyala", self)
        yapistir.setShortcut("Ctrl+V")

        sil = QAction("Sil", self)
        sil.setShortcut("Del")

        bing = QAction("Bing ile ara...", self)
        bing.setShortcut("Ctrl+E")

        bul = QAction("Bul...", self)
        bul.setShortcut("Ctrl+F")

        sonraki = QAction("Sonrakini Bul", self)
        sonraki.setShortcut("F3")

        önceki = QAction("Öncekini Bul", self)
        önceki.setShortcut("Shift+F3")

        degis = QAction("Degistir", self)
        degis.setShortcut("Ctrl+H")

        git = QAction("Git...", self)
        git.setShortcut("Ctrl+G")

        tümü = QAction("Tümünü Sec", self)
        tümü.setShortcut("Ctrl+A")

        tarih = QAction("Tarih/Saat", self)
        tarih.setShortcut("F5")



        tarih.triggered.connect(self.saat)



        duzen.addAction(geri_al)
        duzen.addAction(kes)
        duzen.addAction(kopyala)
        duzen.addAction(yapistir)
        duzen.addAction(sil)
        duzen.addAction(bing)
        duzen.addAction(bul)
        duzen.addAction(sonraki)
        duzen.addAction(önceki)
        duzen.addAction(degis)
        duzen.addAction(git)
        duzen.addAction(tümü)
        duzen.addAction(tarih)



        # bicim baslangic

        bicim = menubar.addMenu("Bicim")
         
        kaydir = QAction("Sözcük kaydir", self)
        yazi_tip = QAction("Yazi Tipi...", self)


        bicim.addAction(kaydir)
        bicim.addAction(yazi_tip)

       # gorunum baslangic              

        gorunum = menubar.addMenu("Görünüm")

        yaklastir = gorunum.addMenu("Yaklastir")
        yaklas = QAction("Yaklastir", self)
        yaklas.setShortcut("Ctrl+Arti")

        uzaklas = QAction("Uzaklastir", self)
        varsayilan = QAction("Varsayilan Yaklastirmayi Geri Yükle", self)




        durum = QAction("Durum Cubugu", self)


        yaklastir.addAction(yaklas)
        yaklastir.addAction(uzaklas)
        gorunum.addAction(durum)
        yaklastir.addAction(varsayilan)



        # yardım baslangic

        yardim = menubar.addMenu("Yardım")

        yardimi = QAction("Yardımı Görüntüle", self)
        geri_gonder = QAction("Geri Bildirim Gönder", self)
        hakkinda = QAction("Not Defteri Hakkında", self)



        hakkinda.triggered.connect(self.hakkinda)
        yardim.addAction(hakkinda)
        

        yardim.addAction(yardimi)
        yardim.addAction(geri_gonder)
        yardim.addAction(hakkinda)


        self.setWindowTitle("Notepad")
        self.show()

    



    def yeni(self):

        yeni_pencere = Menu()
        yeni_pencere.show()
        

    def yeni_pence(self):

        yeni_pencere = Menu()
        yeni_pencere.show()
        

    def ac(self):
        
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))

        if dosya_ismi:
            with open(dosya_ismi, "r") as file:
                self.text_area.setText(file.read())

    def kaydet(self):

        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("HOME"))
        try:

            with open(dosya_ismi, "w") as file:
                file.write(self.text_area.toPlainText())
        except Exception as e:
            print(f"Hata : {e}")


    def farkli_kayde(self):
         
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Farkli Kaydet",os.getenv("HOME"))

        try:

            with open(dosya_ismi[0],"w") as file:
                file.write(self.yazi_alani.toPlainText())
        except Exception as e:
            print(f"Hata: {e}")


    def sayfa_yapı(self):

        pass

    def yazdi(self):

        pass
   
    def cikis(self):

        qApp.quit()

    def geri(self):

        pass

    def kes(self):

        pass

    def kopya(self):

        pass

    def yap(self):

        pass

    def siil(self):

        pass

    def ara(self):

        pass

    def bull(self):


        pass

    def sonra_bull(Self):

        pass

    def önce_bull(self):

        pass

    def degis(self):

        pass

    def giit(self):

        pass

    def sec(self):

        pass

    def saat(self):

        tarih = QDateTime.currentDateTime().toString("dd.MM.yyyy hh:mm:ss")
        cursor = self.text_area.textCursor()
        cursor.insertText(tarih)

    def kaydir(self):

        pass

    def yazi(self):

        pass

    def yaklass(self):

        pass

    def uzaklass(self):

        pass

    def varsay(self):

        pass

    def durum_cubuk(self):

        pass

    def yardimm(self):

        pass

    def gerii(self):

        pass

    def hakkinda(self):


        QMessageBox.about(self, "Hakkinda", """---------- THT  ?? ----------\n
                          Are you OK ?""")



    def dosya_clicked(self, action):
        print(f'Clicked: {action.text()}')

    def duzen_clicked(self, action):
        print(f'Düzen Clicked: {action.text()}')


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())

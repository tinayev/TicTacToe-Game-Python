from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
sutunSayi=3
setirSayi=3
w=600
btnW=h/3
h=600
btnH=h/3
btnX=0
btnY=0

btnStatus=True

app=QApplication()

game=QWidget()
game.resize(w,h)

class TicButton(QPushButoon):
    def __init__(self,*args):
        QPushButton.__init__(self,*args):
        self.clicked.connect(self,clickFunc)
        self.setStyleSheet('backgraund:lightgray;font-size:25px')
        
        
        def clickFunc(self):
            global btnStatus
            self.clickCount+=1
            is self.clickCount<=1:
                if btnStatus:
                    self.setText('X')
                    btnstatus=False
                else:
                    self.settext('O')
                    btnStatus=True
                
        print(self.clickCount)     
          
        
        
        
        
        
    for setir in range(1,setirSayi+1):
        for sutun in range(1,sutunSayi+1):
            btn=TicButton('',game)
            btn.setGeometry(btnX,btnY,btnH)
            btn.setStyleSheet('backgraund:lightgray')
            btnX+=btnW
        btnX=0
        btnY+=btnH
        
        
game.show()


app.exec_()
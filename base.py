from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

def convertir():
    n = win.ch.text()
    b1 = int(win.cb1.currentText())
    b2 = int(win.cb2.currentText())

    if verif(n) == False:
        QMessageBox.critical(win, "error", "verifier la saisie de nombre")

    elif b1 == b2:
        QMessageBox.critical(win, "error", "Base 1 et Base 2 doivent etre differentes")

    else:
        x = convb10(n, b1)
        z = convb10_bb(x, b2)
        win.aff.setText(z)
        
def verif(x):
    test=True
    i=0
    while i<len(x) and test :
        if "0"<=x[i]<="9":
            i+=1
        else:
            test=False
            
    return test
        
def convertion(n,b1,b2):
    n=int(n)
    x=convbb_b10(n,b1)
    z=convb10_bb(x,b2)
    return z

def convb10_bb(x, b):
    if x == 0:
        return "0"
    
    ch = ""
    
    while x > 0:
        r = x % b
        if r < 10:
            ch = str(r) + ch
        else:
            ch = chr(r + 55) + ch
        x = x // b
    
    return ch
def convb10(x, b):
    x = str(x)
    res = 0
    i = 0

    while i < len(x):
        c = x[len(x) - 1 - i]

        if '0' <= c <= '9':
            val = int(c)
        else:
            val = ord(c.upper()) - 55

        res = res + val * (b ** i)
        i += 1

    return res
        

app = QApplication([])
win= loadUi ("bases.ui")
win.show()
win.BT.clicked.connect (convertir)
app.exec_()
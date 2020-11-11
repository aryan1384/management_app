import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

#def file
def new():
	pass

def open_other():
    option = QFileDialog.Options()
    widget = QWidget()
    myfile = QFileDialog.getOpenFileName(widget,'save file','JPEG (*.jpg;*jpeg;*.jpe;*.jfif);;PNG (*.png);;PDF (*.pdf);;', options = option)
    #print(myfile)
    return myfile[0]

def open_file():
    option = QFileDialog.Options()
    widget = QWidget()
    myfile = QFileDialog.getOpenFileName(widget,'save file','default.jpg','All Files (*.*)', options = option)
    #print(myfile)
    return myfile[0]

def save():
	pass

def save_as():
    option = QFileDialog.Options()
    widget = QWidget()
    myfile = QFileDialog.getSaveFileName(widget,'save file','default.jpg','All Files (*.*)', options = option)
    #print(myfile)
    return myfile[0]

#lists

def Bank_balances():
	pass

def Documents():
	pass

def Crafts_and_Consumption():
	pass

def Checks_issued():
	pass

def Expenses():
	pass

def Assets():
	pass

def Stocks():
	pass

def Employees():
	pass

def Customers():
	pass

#Advice and predicts

def Bank_balances_advice():
	pass

def Stocks_advice():
	pass

def Employees_advice():
	pass

def Customers_advice():
	pass
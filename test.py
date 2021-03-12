def jam_ragham(n):
    n_c = n
    t = 0
    while n_c != 0:
        t += n_c%10
        n_c //= 10

    return t

t = 0
for i in range(10 ** 9,10 ** 10):
    if jam_ragham(i) == 4:
        t+=1
        print(i)

print(t) 


'''import os
entries = os.listdir('information/Expences')

print(entries)
'''

'''
# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 


class Window(QMainWindow): 

    def __init__(self): 
        super().__init__() 

        # setting title 
        self.setWindowTitle("Python ") 

        # setting geometry 
        self.setGeometry(100, 100, 500, 400) 

        # calling method 
        self.UiComponents() 

        # showing all the widgets 
        self.show() 



    # method for components 
    def UiComponents(self): 

        # creating a QListWidget 
        list_widget = QListWidget(self) 

        # setting geometry to it 
        list_widget.setGeometry(0, 0, 350, 120) 

        # list widget items 
        item1 = QListWidgetItem("PyQt5 Geeks for Geeks") 
        item2 = QListWidgetItem("B") 
        item3 = QListWidgetItem("C") 
        item4 = QListWidgetItem("D") 
        item5 = QListWidgetItem("e") 
        item6 = QListWidgetItem("r") 
        item7 = QListWidgetItem("t") 

        # adding items to the list widget 
        list_widget.addItem(item1) 
        list_widget.addItem(item2) 
        list_widget.addItem(item3) 
        list_widget.addItem(item4) 
        list_widget.addItem(item5) 
        list_widget.addItem(item6) 
        list_widget.addItem(item7) 

        # scroll bar 
        scroll_bar = QScrollBar(self) 

        # setting style sheet to the scroll bar 
        #scroll_bar.setStyleSheet("background : lightgreen;") 

        # setting vertical scroll bar to it 
        list_widget.setVerticalScrollBar(scroll_bar) 

        # creating a label 
        #label = QLabel("GeesforGeeks", self) 

        # setting geometry to the label 
        #label.setGeometry(230, 80, 280, 80) 

        # making label multi line 
        #label.setWordWrap(True) 




# create pyqt5 app 
App = QApplication(sys.argv) 

# create the instance of our Window 
window = Window() 

# start the app 
sys.exit(App.exec()) 
'''
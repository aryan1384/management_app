from PyQt5 import QtCore, QtGui, QtWidgets
import functions
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout, QFileDialog

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import tkinter 
import pandas as pd

root = tkinter.Tk()
#variables
#window
width_window = root.winfo_screenwidth()
height_window = root.winfo_screenheight()
#print(width_window , height_window)

#tools
width_tools = width_window // 4
height_tools = height_window - (height_window // 7)
x_tools = width_window // 40
y_tools = height_window // 25

#detail
width_details = width_window // 5 * 3
height_details = height_tools
x_details = x_tools + width_tools + (width_window // 15)
y_details = y_tools 

y_buttons = 50
class button(object):
    detail = ""
    text = ""
    def show_text(self):
        pass
    


class Ui_MainWindow(object):
    buttons = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width_window, height_window)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        #groupBox_tool
        
        self.groupBox_tool = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_tool.setGeometry(QtCore.QRect(x_tools, y_tools, width_tools, height_tools))
        self.groupBox_tool.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_tool.setObjectName("groupBox_tool")

        self.groupBox_detail = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_detail.setGeometry(QtCore.QRect(x_details, y_details, width_details, height_details))
        self.groupBox_detail.setObjectName("groupBox_detail")

        self.label_detail = QtWidgets.QLabel(self.groupBox_detail)
        self.label_detail.setGeometry(QtCore.QRect(width_details // 2 - 30, height_details // 2 - 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_detail.setFont(font)
        self.label_detail.setObjectName("label_detail")

        #formLayout =QFormLayout()
        #labelLis = []
        #comboList = []
        #for i in  range(50):
        #    labelLis.append(QLabel("Label"))
        #    comboList.append(QPushButton("Click Me"))
        #    formLayout.addRow(labelLis[i], comboList[i])
        #self.groupBox_detail.setLayout(formLayout)
        #scroll = QScrollArea()
        #scroll.setWidget(self.groupBox_detail)
        #scroll.setWidgetResizable(True)
        #scroll.setFixedHeight(400)
        #layout = QVBoxLayout()
        #layout.addWidget(scroll)

        '''self.label_tool = QtWidgets.QLabel(self.groupBox_tool)
        self.label_tool.setGeometry(QtCore.QRect(width_tools // 2 - 45, height_tools // 2 - 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_tool.setFont(font)
        self.label_tool.setObjectName("label_tool")'''

        self.addFile_button = QtWidgets.QPushButton(self.groupBox_tool)
        y_addFile_button = len(self.buttons)*70 + 50
        self.addFile_button.setGeometry(QtCore.QRect(70, y_addFile_button, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.addFile_button.setFont(font)
        self.addFile_button.setObjectName("addFile_button")
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuReccomendation = QtWidgets.QMenu(self.menubar)
        self.menuReccomendation.setObjectName("menuReccomendation")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLists = QtWidgets.QMenu(self.menubar)
        self.menuLists.setObjectName("menuLists")
        self.menuReports = QtWidgets.QMenu(self.menuLists)
        self.menuReports.setObjectName("menuReports")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionOpen_other = QtWidgets.QAction(MainWindow)
        self.actionOpen_other.setObjectName("actionOpen_other")
        self.actionBank_balances = QtWidgets.QAction(MainWindow)
        self.actionBank_balances.setObjectName("actionBank_balances")
        self.actionDocuments = QtWidgets.QAction(MainWindow)
        self.actionDocuments.setObjectName("actionDocuments")
        self.actionCrafts_and_Consumption = QtWidgets.QAction(MainWindow)
        self.actionCrafts_and_Consumption.setObjectName("actionCrafts_and_Consumption")
        self.actionChecks_issued = QtWidgets.QAction(MainWindow)
        self.actionChecks_issued.setObjectName("actionChecks_issued")
        self.actionExpenses = QtWidgets.QAction(MainWindow)
        self.actionExpenses.setObjectName("actionExpenses")
        self.actionAssets = QtWidgets.QAction(MainWindow)
        self.actionAssets.setObjectName("actionAssets")
        self.actionStocks = QtWidgets.QAction(MainWindow)
        self.actionStocks.setObjectName("actionStocks")
        self.actionEmployees = QtWidgets.QAction(MainWindow)
        self.actionEmployees.setObjectName("actionEmployees")
        self.actionCustomers = QtWidgets.QAction(MainWindow)
        self.actionCustomers.setObjectName("actionCustomers")
        self.actionBank_balances_Advice = QtWidgets.QAction(MainWindow)
        self.actionBank_balances_Advice.setObjectName("actionBank_balances_Advice")
        self.actionStocks_Advice = QtWidgets.QAction(MainWindow)
        self.actionStocks_Advice.setObjectName("actionStocks_Advice")
        self.actionEmployees_Advice = QtWidgets.QAction(MainWindow)
        self.actionEmployees_Advice.setObjectName("actionEmployees_Advice")
        self.actionCustomers_Advice = QtWidgets.QAction(MainWindow)
        self.actionCustomers_Advice.setObjectName("actionCustomers_Advice")
        self.menuOpen.addAction(self.actionOpen_other)
        self.menuOpen.addAction(self.actionOpen_file)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuReccomendation.addAction(self.actionBank_balances_Advice)
        self.menuReccomendation.addAction(self.actionStocks_Advice)
        self.menuReccomendation.addAction(self.actionEmployees_Advice)
        self.menuReccomendation.addAction(self.actionCustomers_Advice)
        self.menuReports.addAction(self.actionDocuments)
        self.menuReports.addAction(self.actionCrafts_and_Consumption)
        self.menuLists.addAction(self.actionBank_balances)
        self.menuLists.addAction(self.menuReports.menuAction())
        self.menuLists.addAction(self.actionChecks_issued)
        self.menuLists.addAction(self.actionExpenses)
        self.menuLists.addAction(self.actionAssets)
        self.menuLists.addAction(self.actionStocks)
        self.menuLists.addAction(self.actionEmployees)
        self.menuLists.addAction(self.actionCustomers)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLists.menuAction())
        self.menubar.addAction(self.menuReccomendation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.groupBox_detail.setLayout(formLayout)
        #scroll = QScrollArea()
        #scroll.setWidget(self.groupBox_detail)
        #scroll.setWidgetResizable(True)
        #scroll.setFixedHeight(600)
        #layout = QVBoxLayout()
        #layout.addWidget(scroll)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #groupBox_text
        self.groupBox_tool.setTitle(_translate("MainWindow", "Tools"))
        self.addFile_button.setText(_translate("MainWindow", "+"))

        self.label_detail.setText(_translate("MainWindow", "No detail"))
        self.label_detail.adjustSize()
        self.groupBox_detail.setTitle(_translate("MainWindow", "Detail"))

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuReccomendation.setTitle(_translate("MainWindow", "Advice and Predicts"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuLists.setTitle(_translate("MainWindow", "Lists"))
        self.menuReports.setTitle(_translate("MainWindow", "Reports"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setStatusTip(_translate("MainWindow", "Save file as"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "New file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionOpen_file.setStatusTip(_translate("MainWindow", "Open main file"))
        self.actionOpen_file.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionOpen_other.setText(_translate("MainWindow", "Open other"))
        self.actionOpen_other.setStatusTip(_translate("MainWindow", "Open partial file"))
        self.actionOpen_other.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionBank_balances.setText(_translate("MainWindow", "Bank balances"))
        self.actionDocuments.setText(_translate("MainWindow", "Documents"))
        self.actionCrafts_and_Consumption.setText(_translate("MainWindow", "Crafts and Consumption"))
        self.actionChecks_issued.setText(_translate("MainWindow", "Checks issued"))
        self.actionExpenses.setText(_translate("MainWindow", "Expenses"))
        self.actionAssets.setText(_translate("MainWindow", "Assets"))
        self.actionStocks.setText(_translate("MainWindow", "Stocks"))
        self.actionEmployees.setText(_translate("MainWindow", "Employees"))
        self.actionCustomers.setText(_translate("MainWindow", "Customers"))
        self.actionBank_balances_Advice.setText(_translate("MainWindow", "Bank balances"))
        self.actionStocks_Advice.setText(_translate("MainWindow", "Stocks"))
        self.actionEmployees_Advice.setText(_translate("MainWindow", "Employees"))
        self.actionCustomers_Advice.setText(_translate("MainWindow", "Customers"))

        #click_addFile
        self.addFile_button.clicked.connect(self.addbutton)

        #file
        self.actionNew.triggered.connect(lambda: self.functionNew())
        self.actionOpen_other.triggered.connect(lambda: self.functionOpen_other())
        self.actionOpen_file.triggered.connect(lambda: self.functionOpen_file())
        self.actionSave.triggered.connect(lambda: self.functionSave())
        self.actionSave_as.triggered.connect(lambda: self.functionSave_as())

    #file
    def functionNew(self):
        print('New clicked!')
        pass

    def functionOpen_other(self):
        pass

    def functionOpen_file(self):
        print('Open file clicked')
        address = functions.open_file()
        print(address)
        pass

    def functionSave(self):
        pass

    def functionSave_as(self):
        pass

    def addbutton(self):
        #print('hello')
        option = QFileDialog.Options()
        widget = QWidget()
        myfile = QFileDialog.getOpenFileName(widget,'save file','default.jpg','All Files (*.*)', options = option)
        #print(myfile[0] , 'this is')

        #self.create_button()
        text_file_ = open(myfile[0] , 'r')
        text_file = text_file_.readlines()
        text_file_.close()
        print(text_file)
        self.show_text(text_file)
        detail = pd.read_csv(myfile[0])
        #self.show_table(detail)


    def show_text(self,text_file):
        mytext = ''
        for i in text_file:
            mytext += i
        self.label_detail.setText(mytext)
        self.label_detail.setGeometry(QtCore.QRect(20, 20, 450, 450))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_detail.setFont(font)
        self.label_detail.adjustSize()

    def show_table(self,detail):
        self.createTable(detail)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        self.show()

    def createTable(self,detail):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(5)
        for i in range(2):
            for j in range(5):
                self.tableWidget.setItem(i,j, QTableWidgetItem(detail.loc[i][j]))
                print(detail.loc[i][j])        
        self.tableWidget.move(0,0)

        # table selection change
        #self.tableWidget.doubleClicked.connect(self.on_click)


    def create_button(self):
        self.num = 2

        #creating a button to be clicked
        '''button1 = QPushButton('Button-1', self)
        button1.move(100, 70)'''
        self.addFile_button.clicked.connect(self.on_click)     

        self.layout = QVBoxLayout(self.groupBox_tool) 
        self.layout.addWidget(self.addFile_button)        

    #@pyqtSlot()
    def on_click(self):
        print('Button-{} will be created'.format(self.num))
        button2 = QPushButton('Button-{}'.format(self.num), self.groupBox_tool)
        #self.another_button = QtWidgets.QPushButton(self.groupBox_tool)
        button2.clicked.connect(lambda : print(button2.text()))
#        button2.move(100, 200)

        self.layout.addWidget(button2)
        self.num += 1


        

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_())
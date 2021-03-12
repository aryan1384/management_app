
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout, QFileDialog, QLayout, QTableWidget, QTableWidgetItem

import os

import sys
import tkinter
import pandas as pd

root = tkinter.Tk()
#variables
#window
width_window = root.winfo_screenwidth()
height_window = root.winfo_screenheight() - 70
#print(width_window , height_window)

#tools
width_tools = width_window // 4
height_tools = height_window - (height_window // 9)
x_tools = width_window // 40
y_tools = height_window // 25

#detail
width_details = width_window // 5 * 3
height_details = height_tools
x_details = x_tools + width_tools + (width_window // 15)
y_details = y_tools 
height_tools = height_tools - (height_tools // 5)

#option
width_option = width_tools
height_option = height_details - height_tools - (height_tools // 15)
x_option = x_tools
y_option = y_tools + height_tools + (height_tools // 15)  


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width_window, height_window)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        #groupBox --------------------------------------------------
        '''formLayout =QFormLayout()'''


        self.groupBox_tool = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_tool.setGeometry(QtCore.QRect(x_tools, y_tools, width_tools, height_tools))
        self.groupBox_tool.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_tool.setObjectName("groupBox_tool")

        self.groupBox_detail = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_detail.setGeometry(QtCore.QRect(x_details, y_details, width_details, height_details))
        self.groupBox_detail.setObjectName("groupBox_detail")

        self.groupBox_option = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_option.setGeometry(QtCore.QRect(x_option, y_option, width_option, height_option))
        self.groupBox_option.setObjectName("groupBox_option")

        '''self.groupBox_detail.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(self.groupBox_detail)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout()
        layout.addWidget(scroll)'''

        #label in groupBox --------------------------------------------

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(x_tools, y_tools - 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")


        self.label_detail = QtWidgets.QLabel(self.groupBox_detail)
        self.label_detail.setGeometry(QtCore.QRect(width_details // 2 - 30, height_details // 2 - 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_detail.setFont(font)
        self.label_detail.setObjectName("label_detail")

        self.label_tool = QtWidgets.QLabel(self.groupBox_tool)
        self.label_tool.setGeometry(QtCore.QRect(width_tools // 2 - 45, height_tools // 2 - 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_tool.setFont(font)
        self.label_tool.setObjectName("label_tool")

        #menu   ------------------------------------------------------

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
        '''self.actionOpen_other = QtWidgets.QAction(MainWindow)
        self.actionOpen_other.setObjectName("actionOpen_other")'''
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
        #self.menuOpen.addAction(self.actionOpen_other)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        #groupBox_text ------------------------------------------------

        self.groupBox_tool.setTitle(_translate("MainWindow", "Tools"))
        self.label_tool.setText(_translate("MainWindow", "No tool"))
        
        self.label_tool.adjustSize()
        self.label_detail.setText(_translate("MainWindow", "No detail"))
        self.label_detail.adjustSize()
        self.groupBox_detail.setTitle(_translate("MainWindow", "Detail"))
        self.groupBox_option.setTitle(_translate("MainWindow", "Option"))

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
        self.actionOpen_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        #self.actionOpen_other.setText(_translate("MainWindow", "Open other"))
        #self.actionOpen_other.setStatusTip(_translate("MainWindow", "Open partial file"))
        #self.actionOpen_other.setShortcut(_translate("MainWindow", "Ctrl+O"))
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

        #click_menu

        #file
        self.actionNew.triggered.connect(lambda: self.functionNew())
        #self.actionOpen_other.triggered.connect(lambda: self.functionOpen_other())
        self.actionOpen_file.triggered.connect(lambda: self.functionOpen_file())
        self.actionSave.triggered.connect(lambda: self.functionSave())
        self.actionSave_as.triggered.connect(lambda: self.functionSave_as())
        #lists
        self.actionBank_balances.triggered.connect(lambda: self.functionBank_balances())
        self.actionDocuments.triggered.connect(lambda: self.functionDucuments())
        self.actionCrafts_and_Consumption.triggered.connect(lambda: self.functionCraft_and_Consumption())
        self.actionChecks_issued.triggered.connect(lambda: self.functionChecks_issued())
        self.actionExpenses.triggered.connect(lambda: self.functionExpenses())
        self.actionAssets.triggered.connect(lambda: self.functionAsset())
        self.actionStocks.triggered.connect(lambda: self.functionStocks())
        self.actionEmployees.triggered.connect(lambda: self.functionEmployees())
        self.actionCustomers.triggered.connect(lambda: self.functionCustomers())
        #advice and predict
        self.actionBank_balances_Advice.triggered.connect(lambda: self.functionBank_balances_Advice())
        self.actionStocks_Advice.triggered.connect(lambda: self.functionStocks_Advice())
        self.actionEmployees_Advice.triggered.connect(lambda: self.functionEmployees_Advice())
        self.actionCustomers_Advice.triggered.connect(lambda: self.functionCustomers_Advice())

        #varaible ----------------------------------------
        self.flag_layout_tool = False
        self.flag_layout_option = False
        self.map_option = self.show_text
        self.currunt_map = "text"


    def scroll_tools(self):
        pass

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

    #lists

    def functionBank_balances(self):
        self.check_previous()

        self.label_name.setText("‌Bank balances")
        self.label_name.adjustSize()
        self.make_plus_button()

        self.show_option(['text','table'])

        print(self.currunt_map)
        self.shown_file_address = "information/" + "Ducuments" + "/" + str(self.currunt_map) 
        self.shown_file = os.listdir(self.shown_file_address)

        for i in range(len(self.shown_file)):
            self.make_tool_button(self.shown_file[i])

        print(self.shown_file)

    def functionDucuments(self):
        self.check_previous()

        self.label_name.setText("Ducuments")
        self.label_name.adjustSize()
        self.make_plus_button()

        self.show_option(['text','pic'])

    def functionCraft_and_Consumption(self):
        self.check_previous()

        self.label_name.setText("‌Craft and Consumptions")
        self.label_name.adjustSize()
        self.make_plus_button()

        self.show_option(['text','pic','table','chart'])

    def functionChecks_issued(self):
        self.check_previous()

        self.label_name.setText("‌Checks issued")
        self.label_name.adjustSize()
        self.make_plus_button()

        self.show_option(['text','pic','table'])

    def functionExpenses(self):
        self.check_previous()

        self.label_name.setText("‌Expences")
        self.label_name.adjustSize()
        self.make_plus_button()

        self.show_option(['text','table','chart'])

    def functionAsset(self):
        self.check_previous()

        self.label_name.setText("‌Assets")
        self.label_name.adjustSize()
        self.make_plus_button()

        self.show_option(['text','pic','table','chart'])

    def functionStocks(self):
        self.check_previous()

        self.label_name.setText("‌Stocks")
        self.label_name.adjustSize()
        self.make_plus_button()

        self.show_option(['text','table','stock'])

    def functionEmployees(self):
        self.check_previous()

        self.label_name.setText("‌Employees")
        self.label_name.adjustSize()
        self.make_plus_button()

        self.show_option(['text','pic','table'])

    def functionCustomers(self):
        pass
    #advice and predict
    def functionBank_balances_Advice(self):
        pass

    def functionStocks_Advice(self):
        pass

    def functionEmployees_Advice(self):
        pass

    def functionCustomers_Advice(self):
        pass


    #functions -------------------------------------------------------
    
    def make_plus_button(self):
        self.addFile_button = QtWidgets.QPushButton(self.groupBox_tool)
        #y_addFile_button = len(self.buttons)*70 + 50
        #self.addFile_button.setGeometry(QtCore.QRect(70, y_addFile_button, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.addFile_button.setFont(font)
        self.addFile_button.setObjectName("addFile_button")
        self.button_file = []
        if not self.flag_layout_tool:
            self.make_layout()

        self.layout_tool.addWidget(self.addFile_button)
        self.addFile_button.clicked.connect(self.addbutton)

        self.addFile_button.setText("+")
        self.num=1


    def make_layout(self):

        #click_addFile
        self.layout_tool = QVBoxLayout(self.groupBox_tool) 

        self.flag_layout_tool = True

    def addbutton(self):
        option = QFileDialog.Options()
        widget = QWidget()
        myfile = QFileDialog.getOpenFileName(widget,'open file','default.txt','All Files (*.*)', options = option)
        try:
            text_file_ = open(myfile[0] , 'r')
            text_file = text_file_.readlines()
            text_file_.close()
            #print(text_file)
            self.map_option(text_file)
            #self.show_table("information/Expences/X.csv")
            self.button_file.append(text_file)
            #print('Button-{} will be created'.format(self.num))
            button_tool = QPushButton(str(self.num) , self.groupBox_tool)
            button_tool.clicked.connect(lambda : self.show_text(self.button_file[int(button_tool.text()) - 1]))
            #button2.move(100, 200)
            self.layout_tool.addWidget(button_tool)
            self.num += 1

        except:
            pass

    def make_tool_button(self, address):
        try:
            text_file_ = open(address , 'r')
            text_file = text_file_.readlines()
            text_file_.close()
            #print(text_file)
            self.map_option(text_file)
            
            self.button_file.append(text_file)
            #print('Button-{} will be created'.format(self.num))
            button_tool = QPushButton(str(self.num) , self.groupBox_tool)
            button_tool.clicked.connect(lambda : self.show_text(self.button_file[int(button_tool.text()) - 1]))
            #button2.move(100, 200)
            self.layout_tool.addWidget(button_tool)
            self.num += 1

        except:
            pass


    def change_map(self, new_map):
        if new_map == "text":
            self.map_option = self.show_text

        if new_map == "pic":
            self.map_option = self.show_picture

        if new_map == "table":
            self.map_option = self.show_table

        if new_map == "chart":
            self.map_option = self.show_chart 

        self.currunt_map = new_map

        self.check_previous()        

    def show_text(self,text_file):
        #print('here')
        mytext = ''
        for i in text_file:
            mytext += i

        self.label_detail.setText(mytext)
        self.label_detail.setGeometry(QtCore.QRect(20, 20, 450, 450))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_detail.setFont(font)
        self.label_detail.adjustSize()   


    def show_table(self, address):
        
        # Create table
        self.info = pd.read_csv(address)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(6)
        print(self.info.loc[1][1])
        for i in range(2):
            for j in range(5):
                self.tableWidget.setItem(i,j, QTableWidgetItem(self.info.loc[i][j]))
                print(self.info.loc[i][j])        
        self.tableWidget.move(100,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

        self.layout = QVBoxLayout(self.groupBox_detail)
        self.layout.addWidget(self.tableWidget) 


    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def show_picture(self,img):
        #img.save("trash.jpg")
        image = Image.open(img)
        width_img, height_img = image.size
        while width_img > width_details or height_img > height_details:
            image = image.resize((int(width_img // 1.05), int(height_img // 1.05)))
            width_img, height_img = image.size
        image.save("trash.jpg")    
        #print(width_img, height_img)
        self.label_detail.setPixmap(QtGui.QPixmap("trash.jpg"))
        self.label_detail.setGeometry(QtCore.QRect(0, 0, width_img ,height_img))
        os.remove('trash.jpg')
        #self.label_detail.adjustSize()

    def show_chart(self):
        print("show_chart")

    def deleteLayout(self, cur_lay):
        #QtGui.QLayout(cur_lay)
        
        if cur_lay is not None:
            while cur_lay.count():
                item = cur_lay.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            #delete(cur_lay)

    def check_previous(self):
        if not self.flag_layout_tool:
            self.label_tool.clear()

        if self.flag_layout_tool:
            self.deleteLayout(self.layout_tool)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.label_detail.setFont(font)
            self.label_detail.setText("No detail")
            self.label_detail.setGeometry(QtCore.QRect(width_details // 2 - 30, height_details // 2 - 20, 91, 51))
            self.label_detail.adjustSize()


    def show_option(self, option_list):
        if not self.flag_layout_option:
            self.layout_option = QHBoxLayout(self.groupBox_option)
            self.flag_layout_option = True

        self.deleteLayout(self.layout_option)
        #option_list = len(option_list)
        self.option_text = [''] * len(option_list)
        self.option_button = [''] * len(option_list)
        for i in range(len(option_list)):
            self.option_text[i] = option_list[i]
            self.option_button[i] = QPushButton(self.option_text[i], self.groupBox_option)
            self.layout_option.addWidget(self.option_button[i])
        self.option_button[0].clicked.connect(lambda : self.change_map(self.option_button[0].text()))
        self.option_button[1].clicked.connect(lambda : self.change_map(self.option_button[1].text()))
        if len(option_list) > 2:
            self.option_button[2].clicked.connect(lambda : self.change_map(self.option_button[2].text()))
            if len(option_list) > 3:
                self.option_button[3].clicked.connect(lambda : self.change_map(self.option_button[3].text()))

    def function_option(self, text_button):
        print(text_button)
            
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
#MainWindow.showMaximized()
    
MainWindow.show()
sys.exit(app.exec_())
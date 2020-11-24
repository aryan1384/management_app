
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import functions

import sys
import tkinter

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


class Ui_MainWindow(object):
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

        self.label_tool = QtWidgets.QLabel(self.groupBox_tool)
        self.label_tool.setGeometry(QtCore.QRect(width_tools // 2 - 45, height_tools // 2 - 20, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_tool.setFont(font)
        self.label_tool.setObjectName("label_tool")
        
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #groupBox_text
        self.groupBox_tool.setTitle(_translate("MainWindow", "Tools"))
        self.label_tool.setText(_translate("MainWindow", "No tool"))
        self.label_tool.adjustSize()
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

        #click_menu

        #file
        self.actionNew.triggered.connect(lambda: self.functionNew())
        self.actionOpen_other.triggered.connect(lambda: self.functionOpen_other())
        self.actionOpen_file.triggered.connect(lambda: self.functionOpen_file())
        self.actionSave.triggered.connect(lambda: self.functionSave())
        self.actionSave_as.triggered.connect(lambda: self.functionSave_as())
        #lists
        self.actionBank_balances.triggered.connect(lambda: self.functionBank_balances())
        self.actionDocuments.triggered.connect(lambda: self.functionDucuments())
        self.actionCrafts_and_Consumption.triggered.connect(lambda: self.functionCraft_and_Consumption())
        self.actionChecks_issued.triggered.connect(lambda: self.functionChecks_issued())
        self.actionExpenses.triggered.connect(lambda: self.functionExpenses())
        self.actionAssets.triggered.connect(lambda: self.functionAssert())
        self.actionStocks.triggered.connect(lambda: self.functionStocks())
        self.actionEmployees.triggered.connect(lambda: self.functionEmployees())
        self.actionCustomers.triggered.connect(lambda: self.functionCustomers())
        #advice and predict
        self.actionBank_balances_Advice.triggered.connect(lambda: self.functionBank_balances_Advice())
        self.actionStocks_Advice.triggered.connect(lambda: self.functionStocks_Advice())
        self.actionEmployees_Advice.triggered.connect(lambda: self.functionEmployees_Advice())
        self.actionCustomers_Advice.triggered.connect(lambda: self.functionCustomers_Advice())

        #actions of click


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
        pass

    def functionDucuments(self):
        pass

    def functionCraft_and_Consumption(self):
        pass

    def functionChecks_issued(self):
        pass

    def functionExpenses(self):
        pass

    def functionAssert(self):
        pass

    def functionStocks(self):
        pass

    def functionEmployees(self):
        pass

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




if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.showMaximized()
    
    MainWindow.show()
    sys.exit(app.exec_())
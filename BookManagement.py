# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookManagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect("Management.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS BookManagementTable (TITLE, AUTHOR, PBLICATION_DATE, PRICE_PER_UNIT, QUANTITY, EDITION_DATE, EDITOR, SUPPLIER)")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -1, 1111, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(6, -8, 1111, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("homepageimage.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(160, -10, 20, 581))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.BookInsertButton = QtWidgets.QPushButton(self.tab_2)
        self.BookInsertButton.setGeometry(QtCore.QRect(490, 130, 75, 23))
        self.BookInsertButton.setObjectName("BookInsertButton")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 151, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 151, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 151, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 151, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 400, 151, 31))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 350, 151, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.BookTitleText = QtWidgets.QLineEdit(self.tab_2)
        self.BookTitleText.setGeometry(QtCore.QRect(10, 40, 151, 20))
        self.BookTitleText.setObjectName("BookTitleText")
        self.BookAuthorText = QtWidgets.QLineEdit(self.tab_2)
        self.BookAuthorText.setGeometry(QtCore.QRect(10, 100, 151, 20))
        self.BookAuthorText.setObjectName("BookAuthorText")
        self.BookPublicatioDateText = QtWidgets.QLineEdit(self.tab_2)
        self.BookPublicatioDateText.setGeometry(QtCore.QRect(10, 160, 151, 20))
        self.BookPublicatioDateText.setObjectName("BookPublicatioDateText")
        self.BookPricePerUnitText = QtWidgets.QLineEdit(self.tab_2)
        self.BookPricePerUnitText.setGeometry(QtCore.QRect(10, 210, 151, 20))
        self.BookPricePerUnitText.setObjectName("BookPricePerUnitText")
        self.BookQuantityText = QtWidgets.QLineEdit(self.tab_2)
        self.BookQuantityText.setGeometry(QtCore.QRect(10, 260, 151, 20))
        self.BookQuantityText.setObjectName("BookQuantityText")
        self.BookEditionDateText = QtWidgets.QLineEdit(self.tab_2)
        self.BookEditionDateText.setGeometry(QtCore.QRect(10, 320, 151, 20))
        self.BookEditionDateText.setObjectName("BookEditionDateText")
        self.BookEditorText = QtWidgets.QLineEdit(self.tab_2)
        self.BookEditorText.setGeometry(QtCore.QRect(10, 380, 151, 20))
        self.BookEditorText.setObjectName("BookEditorText")
        self.BookSupplierText = QtWidgets.QLineEdit(self.tab_2)
        self.BookSupplierText.setGeometry(QtCore.QRect(10, 440, 151, 20))
        self.BookSupplierText.setObjectName("BookSupplierText")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(180, -20, 20, 581))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.BookDeleteButton = QtWidgets.QPushButton(self.tab_2)
        self.BookDeleteButton.setGeometry(QtCore.QRect(580, 130, 75, 23))
        self.BookDeleteButton.setObjectName("BookDeleteButton")
        self.BookClearButton = QtWidgets.QPushButton(self.tab_2)
        self.BookClearButton.setGeometry(QtCore.QRect(490, 170, 311, 23))
        self.BookClearButton.setObjectName("BookClearButton")
        self.BookRefreshButton = QtWidgets.QPushButton(self.tab_2)
        self.BookRefreshButton.setGeometry(QtCore.QRect(670, 130, 131, 23))
        self.BookRefreshButton.setObjectName("BookRefreshButton")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(190, 210, 921, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(190, 10, 911, 111))
        self.label_11.setStyleSheet("background-color: rgb(170, 170, 255);\n"
        "font: 75 18pt \"MS Shell Dlg 2\";\n"
        "font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.EditorLocationText = QtWidgets.QLineEdit(self.tab_5)
        self.EditorLocationText.setGeometry(QtCore.QRect(10, 150, 151, 20))
        self.EditorLocationText.setObjectName("EditorLocationText")
        self.EditorEditionDateText = QtWidgets.QLineEdit(self.tab_5)
        self.EditorEditionDateText.setGeometry(QtCore.QRect(10, 330, 151, 20))
        self.EditorEditionDateText.setObjectName("EditorEditionDateText")
        self.line_3 = QtWidgets.QFrame(self.tab_5)
        self.line_3.setGeometry(QtCore.QRect(160, -20, 20, 581))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.EditorInsertButton = QtWidgets.QPushButton(self.tab_5)
        self.EditorInsertButton.setGeometry(QtCore.QRect(490, 120, 75, 23))
        self.EditorInsertButton.setObjectName("EditorInsertButton")
        self.EditionDate = QtWidgets.QLabel(self.tab_5)
        self.EditionDate.setGeometry(QtCore.QRect(10, 300, 151, 31))
        self.EditionDate.setAlignment(QtCore.Qt.AlignCenter)
        self.EditionDate.setObjectName("EditionDate")
        self.EditorRefreshButton = QtWidgets.QPushButton(self.tab_5)
        self.EditorRefreshButton.setGeometry(QtCore.QRect(670, 120, 131, 23))
        self.EditorRefreshButton.setObjectName("EditorRefreshButton")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 151, 31))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.EditorPhoneNumberText = QtWidgets.QLineEdit(self.tab_5)
        self.EditorPhoneNumberText.setGeometry(QtCore.QRect(10, 210, 151, 20))
        self.EditorPhoneNumberText.setObjectName("EditorPhoneNumberText")
        self.EmailText = QtWidgets.QLabel(self.tab_5)
        self.EmailText.setGeometry(QtCore.QRect(10, 230, 151, 31))
        self.EmailText.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailText.setObjectName("EmailText")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(10, 110, 151, 31))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(190, 0, 911, 111))
        self.label_18.setStyleSheet("background-color: rgb(170, 170, 255);\n"
        "font: 75 18pt \"MS Shell Dlg 2\";\n"
        "font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.EditorNameText = QtWidgets.QLineEdit(self.tab_5)
        self.EditorNameText.setGeometry(QtCore.QRect(10, 90, 151, 20))
        self.EditorNameText.setObjectName("EditorNameText")
        self.EditorDeleteButton = QtWidgets.QPushButton(self.tab_5)
        self.EditorDeleteButton.setGeometry(QtCore.QRect(580, 120, 75, 23))
        self.EditorDeleteButton.setObjectName("EditorDeleteButton")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_2.setGeometry(QtCore.QRect(190, 200, 921, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.line_4 = QtWidgets.QFrame(self.tab_5)
        self.line_4.setGeometry(QtCore.QRect(180, -30, 20, 581))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.EditorClearButton = QtWidgets.QPushButton(self.tab_5)
        self.EditorClearButton.setGeometry(QtCore.QRect(490, 160, 311, 23))
        self.EditorClearButton.setObjectName("EditorClearButton")
        self.EditorEmailText = QtWidgets.QLineEdit(self.tab_5)
        self.EditorEmailText.setGeometry(QtCore.QRect(10, 260, 151, 20))
        self.EditorEmailText.setObjectName("EditorEmailText")
        self.PhoneNumberText = QtWidgets.QLabel(self.tab_5)
        self.PhoneNumberText.setGeometry(QtCore.QRect(10, 170, 151, 31))
        self.PhoneNumberText.setAlignment(QtCore.Qt.AlignCenter)
        self.PhoneNumberText.setObjectName("PhoneNumberText")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(190, 210, 921, 261))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(10, 210, 151, 31))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(190, 0, 911, 111))
        self.label_20.setStyleSheet("background-color: rgb(170, 170, 255);\n"
        "font: 75 18pt \"MS Shell Dlg 2\";\n"
        "font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.AuthorRefreshButton = QtWidgets.QPushButton(self.tab_3)
        self.AuthorRefreshButton.setGeometry(QtCore.QRect(670, 130, 131, 23))
        self.AuthorRefreshButton.setObjectName("AuthorRefreshButton")
        self.AuthorClearButton = QtWidgets.QPushButton(self.tab_3)
        self.AuthorClearButton.setGeometry(QtCore.QRect(490, 170, 311, 23))
        self.AuthorClearButton.setObjectName("AuthorClearButton")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(10, 160, 151, 31))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(10, 270, 151, 31))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.AuthorInsertButton = QtWidgets.QPushButton(self.tab_3)
        self.AuthorInsertButton.setGeometry(QtCore.QRect(490, 130, 75, 23))
        self.AuthorInsertButton.setObjectName("AuthorInsertButton")
        self.AuthorDeleteButton = QtWidgets.QPushButton(self.tab_3)
        self.AuthorDeleteButton.setGeometry(QtCore.QRect(580, 130, 75, 23))
        self.AuthorDeleteButton.setObjectName("AuthorDeleteButton")
        self.line_5 = QtWidgets.QFrame(self.tab_3)
        self.line_5.setGeometry(QtCore.QRect(180, -20, 20, 581))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.AuthorNameText = QtWidgets.QLineEdit(self.tab_3)
        self.AuthorNameText.setGeometry(QtCore.QRect(10, 190, 151, 20))
        self.AuthorNameText.setObjectName("AuthorNameText")
        self.GenderText = QtWidgets.QLineEdit(self.tab_3)
        self.GenderText.setGeometry(QtCore.QRect(10, 250, 151, 20))
        self.GenderText.setObjectName("GenderText")
        self.line_6 = QtWidgets.QFrame(self.tab_3)
        self.line_6.setGeometry(QtCore.QRect(160, -10, 20, 581))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.AgeText = QtWidgets.QLineEdit(self.tab_3)
        self.AgeText.setGeometry(QtCore.QRect(10, 310, 151, 20))
        self.AgeText.setObjectName("AgeText")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.line_8 = QtWidgets.QFrame(self.tab_4)
        self.line_8.setGeometry(QtCore.QRect(150, -20, 20, 581))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(0, 260, 151, 31))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(180, 200, 921, 261))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(180, 0, 921, 111))
        self.label_25.setStyleSheet("background-color: rgb(170, 170, 255);\n"
        "font: 75 18pt \"MS Shell Dlg 2\";\n"
        "font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.SupplierPhoneNumberText = QtWidgets.QLineEdit(self.tab_4)
        self.SupplierPhoneNumberText.setGeometry(QtCore.QRect(0, 300, 151, 20))
        self.SupplierPhoneNumberText.setObjectName("SupplierPhoneNumberText")
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setGeometry(QtCore.QRect(0, 150, 151, 31))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.line_7 = QtWidgets.QFrame(self.tab_4)
        self.line_7.setGeometry(QtCore.QRect(170, -30, 20, 581))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.SupplierNameText = QtWidgets.QLineEdit(self.tab_4)
        self.SupplierNameText.setGeometry(QtCore.QRect(0, 180, 151, 20))
        self.SupplierNameText.setObjectName("SupplierNameText")
        self.AuthorInsertButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.AuthorInsertButton_2.setGeometry(QtCore.QRect(480, 120, 75, 23))
        self.AuthorInsertButton_2.setObjectName("AuthorInsertButton_2")
        self.AuthorDeleteButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.AuthorDeleteButton_2.setGeometry(QtCore.QRect(570, 120, 75, 23))
        self.AuthorDeleteButton_2.setObjectName("AuthorDeleteButton_2")
        self.SupplierLocationText = QtWidgets.QLineEdit(self.tab_4)
        self.SupplierLocationText.setGeometry(QtCore.QRect(0, 240, 151, 20))
        self.SupplierLocationText.setObjectName("SupplierLocationText")
        self.AuthorRefreshButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.AuthorRefreshButton_2.setGeometry(QtCore.QRect(660, 120, 131, 23))
        self.AuthorRefreshButton_2.setObjectName("AuthorRefreshButton_2")
        self.AuthorClearBuitton = QtWidgets.QPushButton(self.tab_4)
        self.AuthorClearBuitton.setGeometry(QtCore.QRect(480, 160, 311, 23))
        self.AuthorClearBuitton.setObjectName("AuthorClearBuitton")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(0, 200, 151, 31))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(0, 330, 151, 31))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.SupplierEmailText = QtWidgets.QLineEdit(self.tab_4)
        self.SupplierEmailText.setGeometry(QtCore.QRect(0, 370, 151, 20))
        self.SupplierEmailText.setObjectName("SupplierEmailText")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "HOME"))
        self.BookInsertButton.setText(_translate("MainWindow", "INSERT"))
        self.label_2.setText(_translate("MainWindow", "TITLE"))
        self.label_3.setText(_translate("MainWindow", "AUTHOR"))
        self.label_4.setText(_translate("MainWindow", "PUBLICATION DATE"))
        self.label_5.setText(_translate("MainWindow", "QUANTITY"))
        self.label_6.setText(_translate("MainWindow", "EDITION DATE"))
        self.label_7.setText(_translate("MainWindow", "PRICE PER UNIT"))
        self.label_8.setText(_translate("MainWindow", "SUPPLIER"))
        self.label_9.setText(_translate("MainWindow", "EDITOR"))
        self.BookDeleteButton.setText(_translate("MainWindow", "DELETE"))
        self.BookClearButton.setText(_translate("MainWindow", "CLEAR TEXT FIELDS"))
        self.BookRefreshButton.setText(_translate("MainWindow", "VIEW/REFRESH DATABASE ITEMS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TITLE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "AUTHOR"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PDATE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PRICE/U"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "QTY"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "EDATE"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "EDITOR"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "SUPPLIER"))
        self.label_11.setText(_translate("MainWindow", "BOOK MANAGEMENT PAGE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "BOOK"))
        self.EditorInsertButton.setText(_translate("MainWindow", "INSERT"))
        self.EditionDate.setText(_translate("MainWindow", "EDITION DATE"))
        self.EditorRefreshButton.setText(_translate("MainWindow", "VIEW/REFRESH DATABASE ITEMS"))
        self.label_14.setText(_translate("MainWindow", "NAME"))
        self.EmailText.setText(_translate("MainWindow", "EMAIL"))
        self.label_16.setText(_translate("MainWindow", "LOCATION"))
        self.label_18.setText(_translate("MainWindow", "EDITOR MANAGEMENT PAGE"))
        self.EditorDeleteButton.setText(_translate("MainWindow", "DELETE"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "COMPANY NAME"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LOCATION"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PHONE NUMBER"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "EMAIL"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "EDITION DATE"))
        self.EditorClearButton.setText(_translate("MainWindow", "CLEAR TEXT FIELDS"))
        self.PhoneNumberText.setText(_translate("MainWindow", "PHONE NUMBER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "EDITOR"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "GENDER"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "AGE"))
        self.label_17.setText(_translate("MainWindow", "GENDER"))
        self.label_20.setText(_translate("MainWindow", "AUTHOR MANAGEMENT PAGE"))
        self.AuthorRefreshButton.setText(_translate("MainWindow", "VIEW/REFRESH DATABASE ITEMS"))
        self.AuthorClearButton.setText(_translate("MainWindow", "CLEAR TEXT FIELDS"))
        self.label_21.setText(_translate("MainWindow", "NAME"))
        self.label_22.setText(_translate("MainWindow", "AGE"))
        self.AuthorInsertButton.setText(_translate("MainWindow", "INSERT"))
        self.AuthorDeleteButton.setText(_translate("MainWindow", "DELETE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "AUTHOR"))
        self.label_23.setText(_translate("MainWindow", "PHONE NUMBER"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LOCATION"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PHONE NUMBER"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "EMAIL"))
        self.label_25.setText(_translate("MainWindow", "SUPPLIER MANAGEMENT PAGE"))
        self.label_24.setText(_translate("MainWindow", "NAME"))
        self.AuthorInsertButton_2.setText(_translate("MainWindow", "INSERT"))
        self.AuthorDeleteButton_2.setText(_translate("MainWindow", "DELETE"))
        self.AuthorRefreshButton_2.setText(_translate("MainWindow", "VIEW/REFRESH DATABASE ITEMS"))
        self.AuthorClearBuitton.setText(_translate("MainWindow", "CLEAR TEXT FIELDS"))
        self.label_19.setText(_translate("MainWindow", "LOCATION"))
        self.label_26.setText(_translate("MainWindow", "EMAIL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "SUPPLIER"))

        self.BookRefreshButton.clicked.connect(self.BookRefreshButtonClicked)
        self.BookInsertButton.clicked.connect(self.BookInsertButtonClicked)
        self.BookClearButton.clicked.connect(self.BookClearButtonClicked)
        
    def BookClearButtonClicked(self):
        a = self.BookTitleText.setText("")
        b = self.BookAuthorText.setText("")
        co = self.BookPublicatioDateText.setText("")
        d = self.BookPricePerUnitText.setText("")
        f = self.BookQuantityText.setText("")
        g = self.BookEditionDateText.setText("")
        h = self.BookEditorText.setText("")
        i = self.BookSupplierText.setText("")

    def BookInsertButtonClicked(self):
        conn = sqlite3.connect("Management.db")
        c = conn.cursor()
        
        a = self.BookTitleText.text()
        b = self.BookAuthorText.text()
        co = self.BookPublicatioDateText.text()
        d = self.BookPricePerUnitText.text()
        f = self.BookQuantityText.text()
        g = self.BookEditionDateText.text()
        h = self.BookEditorText.text()
        i = self.BookSupplierText.text()
        
        c.execute("INSERT INTO BookManagementTable (TITLE, AUTHOR, PBLICATION_DATE, PRICE_PER_UNIT, QUANTITY, EDITION_DATE, EDITOR, SUPPLIER) VALUES(?,?,?,?,?,?,?,?)", (a,b,co,d,f,g,h,i))
        
        if conn:
            conn.commit()
            c.close()
            conn.close()
    
    def BookRefreshButtonClicked(self):
        conn = sqlite3.connect("Management.db")
        c = conn.cursor()
        table = c.execute("SELECT * FROM BookManagementTable")
        
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(table):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
        
        if conn:
            conn.commit()
            c.close()
            conn.close()

        self.BookRefreshButton.clicked.connect(self.BookRefreshButtonClicked)
        self.BookInsertButton.clicked.connect(self.BookInsertButtonClicked)
        self.BookClearButton.clicked.connect(self.BookClearButtonClicked)
        
    def BookClearButtonClicked(self):
        a = self.BookTitleText.setText("")
        b = self.BookAuthorText.setText("")
        co = self.BookPublicatioDateText.setText("")
        d = self.BookPricePerUnitText.setText("")
        f = self.BookQuantityText.setText("")
        g = self.BookEditionDateText.setText("")
        h = self.BookEditorText.setText("")
        i = self.BookSupplierText.setText("")

    def BookInsertButtonClicked(self):
        conn = sqlite3.connect("Management.db")
        c = conn.cursor()
        
        a = self.BookTitleText.text()
        b = self.BookAuthorText.text()
        co = self.BookPublicatioDateText.text()
        d = self.BookPricePerUnitText.text()
        f = self.BookQuantityText.text()
        g = self.BookEditionDateText.text()
        h = self.BookEditorText.text()
        i = self.BookSupplierText.text()
        
        c.execute("INSERT INTO BookManagementTable (TITLE, AUTHOR, PBLICATION_DATE, PRICE_PER_UNIT, QUANTITY, EDITION_DATE, EDITOR, SUPPLIER) VALUES(?,?,?,?,?,?,?,?)", (a,b,co,d,f,g,h,i))
        
        if conn:
            conn.commit()
            c.close()
            conn.close()
    
    def BookRefreshButtonClicked(self):
        conn = sqlite3.connect("Management.db")
        c = conn.cursor()
        table = c.execute("SELECT * FROM BookManagementTable")
        
        self.tableWidget.setRowCount(0)
        
        for row_number, row_data in enumerate(table):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
        
        if conn:
            conn.commit()
            c.close()
            conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

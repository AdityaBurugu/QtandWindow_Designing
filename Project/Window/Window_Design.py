import os
import pathlib

from PyQt5.QtWidgets import QApplication, QMainWindow,QDateEdit,QFrame, QPushButton,QTextEdit, QLabel,\
    QLineEdit,QComboBox, QMenu, QAction
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect, QRegExp
import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Student Performance Report"
        left = 200
        top = 70
        width = 736
        height = 570
        Icon = "Icon.png"
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(Icon))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.CustomizeWindowHint)
        self.setGeometry(left,  top, width, height)
        self.UiComponents()
        self.show()
    def UiComponents(self):
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        newFileAct = QAction("New", self)
        newFileAct.setShortcut("Ctrl+N")
        Editmenu = menubar.addMenu("Edit")
        Viewmenu = menubar.addMenu("View")
        Formatmenu = menubar.addMenu("Format")
        Helpmenu = menubar.addMenu("Help")
        openfiledeskAct = QAction("import from desk", self)
        openfiledeskAct.setShortcut("Ctrl+Alt+D")
        openfilecldAct = QAction("import from cloud", self)
        openfilecldAct.setShortcut("Ctrl+Alt+C")
        openFileMenu = QMenu('Open', self)
        #savefileAct = QAction("Save", self)
        #savefileAct.setShortcut("Ctrl+S")
        saveasfileAct = QAction("Save", self)
        Icon = 'Save.png'
        saveasfileAct.setIcon(QtGui.QIcon(Icon))
        saveasfileAct.setShortcut("Ctrl+S")
        printfileAct = QAction("Print", self)
        printfileAct.setShortcut("Ctrl+P")
        Exit = QAction("Exit", self)
        Exit.setShortcut("Esc")
        Undo = QAction("Undo", self)
        Undo.setShortcut("Ctrl+Z")
        Redo = QAction("Redo", self)
        Redo.setShortcut("Ctrl+Y")
        Cut = QAction("Cut", self)
        Cut.setShortcut("Ctrl+X")
        Copy = QAction("Copy", self)
        Copy.setShortcut("Ctrl+C")
        Paste = QAction("Paste", self)
        Paste.setShortcut("Ctrl+V")
        Delete = QAction("Delete", self)
        Delete.setShortcut("Del")
        SA = QAction("Select All", self)
        SA.setShortcut("Ctrl+A")
        Font = QAction("Font", self)
        StatusBar = QAction("Status Bar", self)
        StatusBar.setShortcut("F7")
        VH = QAction("View Help", self)
        openFileMenu.addAction(openfiledeskAct)
        openFileMenu.addAction(openfilecldAct)
        filemenu.addAction(newFileAct)
        filemenu.addMenu(openFileMenu)
        #filemenu.addAction(savefileAct)
        filemenu.addAction(saveasfileAct)
        filemenu.addAction(printfileAct)
        filemenu.addAction(Exit)
        Editmenu.addAction(Undo)
        Editmenu.addAction(Redo)
        Editmenu.addAction(Cut)
        Editmenu.addAction(Copy)
        Editmenu.addAction(Paste)
        Editmenu.addAction(Delete)
        Editmenu.addAction(SA)
        Formatmenu.addAction(Font)
        Viewmenu.addAction(StatusBar)
        Helpmenu.addAction(VH)
        self.label_4 = QLabel("...Memorandom of Marks...",self)  # Creates Label
        self.label_4.move(250,10)
        self.label_4.resize(350,31)
        self.label_4.setGeometry(QRect(250, 20, 350, 31))  # Dimensions of Label
        font = QtGui.QFont()  # Sets Font
        font.setFamily("Myanmar Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.max = QLabel("Max Marks : 6x100",self)  # Creates Label Max
        self.max.setGeometry(QRect(590, 30, 125, 20))  # Dimensions of Label Max
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.max.setFont(font)
        self.Student_name = QLabel("Student Name :",self)  # Creates Label Student Name
        self.Student_name.setGeometry(QRect(20, 55, 101, 16))  # Dimensions of Label Student Name
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Student_name.setFont(font)
        self.Father_name = QLabel("Father's Name :",self)  # Creates Label Father's Name
        self.Father_name.setGeometry(QRect(20, 82, 101, 16))  # Dimensions of Label Father's Name
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Father_name.setFont(font)
        self.Hall_Ticket_Number = QLabel("Hall Ticket Number :",self)  # Creates Label Hall_Ticket_Number
        self.Hall_Ticket_Number.setGeometry(QRect(360, 55, 140, 16))  # Dimensiopns of Label Hall_Ticket_Number
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Hall_Ticket_Number.setFont(font)
        self.Class = QLabel("Class :",self)  # Creates Label Class
        self.Class.setGeometry(QRect(360, 82, 101, 16))  # Dimensions of Label Class
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Class.setFont(font)
        self.DOB = QLabel("Date of Birth :",self)  # Creates Label DOB
        self.DOB.setGeometry(QRect(20, 110, 100, 20))  # Dimensions of Label DOB
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.DOB.setFont(font)
        self.Telugu = QLabel("Telugu :",self)  # Creates Label Telugu
        self.Telugu.setGeometry(QRect(80, 145, 55, 16))  # Dimensions of Label Telugu
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Telugu.setFont(font)
        self.Hindi = QLabel("Hindi :",self)  # Creates Label Hindi
        self.Hindi.setGeometry(QRect(80, 182, 55, 21))  # Dimensions of Label Hindi
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Hindi.setFont(font)
        self.English = QLabel("English :",self)  # Creates Label English
        self.English.setGeometry(QRect(80, 225, 55, 16))  # Dimensions of Label Hindi
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.English.setFont(font)
        self.Maths = QLabel("Maths :",self)  # Creates Label Maths
        self.Maths.setGeometry(QRect(80, 265, 81, 16))  # Dimensions of Label Maths
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Maths.setFont(font)
        self.Science = QLabel("Science :",self)  # Creats Label Science
        self.Science.setGeometry(QRect(80, 305, 55, 16))  # Dimensions of Label Science
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Science.setFont(font)
        self.Social = QLabel("Social :",self)  # Creates Label Social
        self.Social.setGeometry(QRect(80, 345, 55, 16))  # Dimensions of Label Social
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Social.setFont(font)
        self.Total = QLabel("Total",self)  # Creates Label Total
        self.Total.setGeometry(QRect(450, 170, 93, 28))  # Dimensions of Label Total
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Total.setFont(font)
        self.Average = QLabel("Average",self)  # Creaates Label Average
        self.Average.setGeometry(QRect(450, 210, 93, 28))  # Dimensions of Label Average
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Average.setFont(font)
        self.Percentage = QLabel("Percentage",self)  # Creates Label Percentage
        self.Percentage.setGeometry(QRect(450, 250, 93, 28))  # Dimensions of Label Percentage
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Percentage.setFont(font)
        self.Division = QLabel("Division",self)  # Creates Label Division
        self.Division.setGeometry(QRect(280, 410, 93, 28))  # Dimensions of Label Division
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Division.setFont(font)
        self.Result = QLabel("Result",self)  # Creates Label Result
        self.Result.setGeometry(QRect(280, 450, 104, 31))  # Dimensions of Label Result
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Result.setFont(font)
        self.Message = QLabel("Message",self)  # Creates Label Message
        self.Message.setGeometry(QRect(280, 500, 100, 28))  # Dimensions of Label Message
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Message.setFont(font)

        self.lineEdit_Student_name = QLineEdit(self)  # Creates Line Edit for Student Name
        self.lineEdit_Student_name.setGeometry(QRect(130, 55, 211, 22))  # Dimensions of Line Edit of Student Name
        self.lineEdit_Student_name.setPlaceholderText("Enter Student Name")
        self.lineEdit_Student_name.setToolTip("Enter Student Name")
        self.lineEdit_Father_name = QLineEdit(self)  # Creates Line Edit for Father's Name
        self.lineEdit_Father_name.setGeometry(QRect(130, 80, 211, 22))  # Dimensions of Line Edit of Father's Name
        self.lineEdit_Father_name.setPlaceholderText("Enter Father's Name")
        self.lineEdit_Father_name.setToolTip("Enter Father's Name")
        self.lineEdit_Hall_Ticket_Number = QLineEdit(self)  # Creates Line Edit for Hall Ticket Number
        self.lineEdit_Hall_Ticket_Number.setGeometry(QRect(495, 55, 211, 22))  # Dimensions of Line Edit of Hall Ticket Number
        self.lineEdit_Hall_Ticket_Number.setPlaceholderText("Enter Hall Ticket Number")
        self.lineEdit_Hall_Ticket_Number.setToolTip("Enter Hall Ticket Number")
        self.comboBox_Class = QComboBox(self)  # Creates Combo Box for Class
        self.comboBox_Class.setGeometry(QRect(410, 80, 128, 22))  # Dimensions of Combo Box of Class
        self.comboBox_Class.setEditable(False)
        self.comboBox_Class.setObjectName("comboBox_Class")  # Sets Object Name
        self.comboBox_Class.setObjectName("comboBox_Class")  # Sets Object Name
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.dateEdit = QDateEdit(self)  # Creates Date Edit
        self.dateEdit.setGeometry(QRect(130, 110, 100, 22))  # Dimensions of Date Edit
        Palette = QtGui.QPalette()
        Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.blue)
        self.dateEdit.setPalette(Palette)
        self.dateEdit.setToolTip("Enter Your Date of Birth")
        self.textEdit_Telugu = QLineEdit(self)  # Creates TExt Edit for Telugu
        self.textEdit_Telugu.setGeometry(QRect(160, 140, 130, 25))
        self.textEdit_Telugu.setPlaceholderText("Enter Telugu Marks")
        self.textEdit_Telugu.setToolTip("Enter Telugu Marks")
        self.textEdit_Telugu.setMaxLength(3)
        self.textEdit_Hindi = QLineEdit(self)  # Creates Text Edit for Hindi
        self.textEdit_Hindi.setGeometry(QRect(160, 180, 130, 25))
        self.textEdit_Hindi.setPlaceholderText("Enter Hindi Marks")
        self.textEdit_Hindi.setToolTip("Enter Hindi Marks")
        self.textEdit_Hindi.setMaxLength(3)
        self.textEdit_English = QLineEdit(self)  # Creates Text Edit for English
        self.textEdit_English.setGeometry(QRect(160, 220, 130, 25))
        self.textEdit_English.setPlaceholderText("Enter English Marks")
        self.textEdit_English.setToolTip("Enter English Marks")
        self.textEdit_English.setMaxLength(3)
        self.textEdit_Maths = QLineEdit(self)  # Creates Text Edit for Maths
        self.textEdit_Maths.setGeometry(QRect(160, 260, 130, 25))
        self.textEdit_Maths.setPlaceholderText("Enter Mathematics Marks")
        self.textEdit_Maths.setToolTip("Enter Mathematics Marks")
        self.textEdit_Maths.setMaxLength(3)
        self.textEdit_Science = QLineEdit(self)  # Creates Text Edit for Science
        self.textEdit_Science.setGeometry(QRect(160, 300, 130, 25))
        self.textEdit_Science.setPlaceholderText("Enter Science Marks")
        self.textEdit_Science.setToolTip("Enter Science Marks")
        self.textEdit_Science.setMaxLength(3)
        self.textEdit_Social = QLineEdit(self)  # Creates Text Edit for Social
        self.textEdit_Social.setGeometry(QRect(160, 340, 130, 25))
        self.textEdit_Social.setPlaceholderText("Enter Social Marks")
        self.textEdit_Social.setToolTip("Enter Social Marks")
        self.textEdit_Social.setMaxLength(3)
        self.textEdit_Total = QLineEdit(self)  # Creates Text Edit for Total Marks
        self.textEdit_Total.setGeometry(QRect(540, 170, 104, 31))
        self.textEdit_Average = QLineEdit(self)  # Creates Text Edit for Average Marks
        self.textEdit_Average.setGeometry(QRect(540, 210, 104, 31))
        self.textEdit_Percentage = QLineEdit(self)  # Creates Text Edit for Percentage of the Total Marks
        self.textEdit_Percentage.setGeometry(QRect(540, 250, 104, 31))
        self.textEdit__Division = QLineEdit(self)  # Creates Text Edit for Division
        self.textEdit__Division.setGeometry(QRect(360, 410, 141, 31))
        self.textEdit_Result = QLineEdit(self)  # Creates Text Edit for Result
        self.textEdit_Result.setGeometry(QRect(360, 450, 104, 31))
        self.textEdit__Message = QTextEdit("Fill up your Data and Enter Your Marks of all Subjects",self)  # Creates Text Edit for Message
        self.textEdit__Message.setGeometry(QRect(360, 490, 260, 45))
        Palette = QtGui.QPalette()
        Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        self.textEdit__Message.setPalette(Palette)
        self.pushButton_Get_Result = QPushButton("Get Result",self)  # Creates Push Button Get Result
        self.pushButton_Get_Result.setGeometry(QRect(450, 120, 93, 28))  # Dimensions of Push Button Get Result
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_Get_Result.setFont(font)
        self.pushButton_Reset = QPushButton("Reset",self)  # Creates Push Button Reset Button
        self.pushButton_Reset.setGeometry(QRect(560, 120, 93, 28))  # Dimensions of Push Button Reset
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setWeight(75)
        self.pushButton_Reset.setFont(font)
        self.pushbutton_Graph = QPushButton("Graph",self)
        self.pushbutton_Graph.setGeometry(100,430,93,28)
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setWeight(75)
        self.pushbutton_Graph.setFont(font)
        self.pushbutton_Graph.hide()
        self.pushbutton_Pie = QPushButton("Pie Chart", self)
        self.pushbutton_Pie.setGeometry(100, 470, 93, 28)
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setWeight(75)
        self.pushbutton_Pie.setFont(font)
        self.pushbutton_Pie.hide()
        self.pushbutton_Save = QPushButton("Save", self)
        self.pushbutton_Save.setGeometry(100, 510, 93, 28)
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setWeight(75)
        self.pushbutton_Save.setFont(font)
        self.pushbutton_Save.hide()
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(250, 400, 375, 145))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QFrame(self)
        self.frame_2.setGeometry(QRect(530, 160, 131, 131))
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Percent = 0
        self.retranslateUi()
        self.pushButton_Get_Result.clicked.connect(self.Total_Result)
        self.pushButton_Get_Result.clicked.connect(self.Calculate)
        self.pushButton_Reset.clicked.connect(self.Reset)
        self.pushbutton_Graph.clicked.connect(self.Graph)
        self.pushbutton_Pie.clicked.connect(self.Pie)
        self.pushbutton_Save.clicked.connect(self.Save)
        saveasfileAct.triggered.connect(self.Save)
        openfilecldAct.triggered.connect(self.Open)
        openfiledeskAct.triggered.connect(self.Open)
        Undo.triggered.connect(self.Undo)
        Redo.triggered.connect(self.Redo)
        Cut.triggered.connect(self.Cut)
        Copy.triggered.connect(self.Copy)
        Paste.triggered.connect(self.Paste)
        Delete.triggered.connect(self.Delete)
        SA.triggered.connect(self.SelectAll)
        StatusBar.triggered.connect(self.Status_Bar)
        Exit.triggered.connect(self.Exit)
        self.pushButton_Get_Result.setDisabled(True)
        self.lineEdit_Student_name.textChanged.connect(self.Disable)
        self.lineEdit_Father_name.textChanged.connect(self.Disable)
        self.lineEdit_Hall_Ticket_Number.textChanged.connect(self.Disable)
        self.textEdit_Telugu.textChanged.connect(self.Disable)
        self.textEdit_Hindi.textChanged.connect(self.Disable)
        self.textEdit_English.textChanged.connect(self.Disable)
        self.textEdit_Maths.textChanged.connect(self.Disable)
        self.textEdit_Science.textChanged.connect(self.Disable)
        self.textEdit_Social.textChanged.connect(self.Disable)

    def Disable(self):
        if len(self.lineEdit_Student_name.text()) > 0 and len(self.lineEdit_Father_name.text()) > 0 and len(self.lineEdit_Hall_Ticket_Number.text()) > 0 and len(self.textEdit_Telugu.text()) > 0 and len(self.textEdit_Hindi.text()) > 0 and len(self.textEdit_English.text()) > 0 and len(self.textEdit_Maths.text()) > 0 and len(self.textEdit_Science.text()) > 0 and len(self.textEdit_Social.text()) > 0:
            self.pushButton_Get_Result.setEnabled(True)

        if len(self.lineEdit_Student_name.text()) == 0 or len(self.lineEdit_Father_name.text()) == 0 or len(self.lineEdit_Hall_Ticket_Number.text()) == 0 or len(self.textEdit_Telugu.text())==0 or len(self.textEdit_Hindi.text())==0 or len(self.textEdit_English.text())==0 or len(self.textEdit_Maths.text())==0 or len(self.textEdit_Science.text())==0 or len(self.textEdit_Social.text())==0:
            self.pushButton_Get_Result.setDisabled(True)
            self.pushbutton_Graph.hide()
            self.pushbutton_Pie.hide()
            self.pushbutton_Save.hide()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.comboBox_Class.setToolTip("Class")
        self.comboBox_Class.setItemText(0, _translate("MainWindow","Select Your Class"))
        self.comboBox_Class.setItemText(1, _translate("MainWindow", "1st Class"))
        self.comboBox_Class.setItemText(2, _translate("MainWindow", "2nd Class"))
        self.comboBox_Class.setItemText(3, _translate("MainWindow", "3rd Class"))
        self.comboBox_Class.setItemText(4, _translate("MainWindow", "4th Class"))
        self.comboBox_Class.setItemText(5, _translate("MainWindow", "5th Class"))
        self.comboBox_Class.setItemText(6, _translate("MainWindow", "6th Class"))
        self.comboBox_Class.setItemText(7, _translate("MainWindow", "7th Class"))
        self.comboBox_Class.setItemText(8, _translate("MainWindow", "8th Class"))
        self.comboBox_Class.setItemText(9, _translate("MainWindow", "9th Class"))
        self.comboBox_Class.setItemText(10, _translate("MainWindow", "10th Class"))

    def Undo(self):
       pass

    def Redo(self):
       pass

    def Cut(self):
        pass

    def Copy(self):
        pass

    def Paste(self):
        pass

    def Delete(self):
        pass

    def SelectAll(self):
        pass

    def Calculate(self):
        try:
            if float(self.textEdit_Telugu.text()) > 100 and float(self.textEdit_Hindi.text()) > 100 and float(
                    self.textEdit_English.text()) > 100 and float(self.textEdit_Maths.text()) > 100 and float(
                    self.textEdit_Science.text()) > 100 and float(self.textEdit_Social.text()) > 100:
                self.textEdit_Result.clear()
                self.textEdit__Division.clear()
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), "Input Error",
                                              "Please Enter Your Marks of all Subjects in Range 1 to 100")
                self.textEdit__Message.setText("Please Enter Your Marks of all Subjects in Range 1 to 100")
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
                self.pushbutton_Graph.hide()
                self.pushbutton_Pie.hide()
                self.pushbutton_Save.hide()
            elif float(self.textEdit_Telugu.text()) > 100:
                self.textEdit_Result.clear()
                self.textEdit__Division.clear()
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), "Input Error",
                                              "Please Enter Your Telugu Marks in Range 1 to 100")
                self.textEdit__Message.setText("Please Enter Your Telugu Marks in Range 1 to 100")
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
                self.pushbutton_Graph.hide()
                self.pushbutton_Pie.hide()
                self.pushbutton_Save.hide()
            elif float(self.textEdit_Hindi.text()) > 100:
                self.textEdit_Result.clear()
                self.textEdit__Division.clear()
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), "Input Error",
                                              "Please Enter Your Hindi Marks in Range 1 to 100")
                self.textEdit__Message.setText("Please Enter Your Hindi Marks in Range 1 to 100")
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
                self.pushbutton_Graph.hide()
                self.pushbutton_Pie.hide()
                self.pushbutton_Save.hide()
            elif float(self.textEdit_English.text()) > 100:
                self.textEdit_Result.clear()
                self.textEdit__Division.clear()
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), "Input Error",
                                              "Please Enter Your English Marks in Range 1 to 100")
                self.textEdit__Message.setText("Please Enter Your English Marks in Range 1 to 100")
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
                self.pushbutton_Graph.hide()
                self.pushbutton_Pie.hide()
                self.pushbutton_Save.hide()
            elif float(self.textEdit_Maths.text()) > 100:
                self.textEdit_Result.clear()
                self.textEdit__Division.clear()
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), "Input Error",
                                              "Please Enter Your Maths Marks in Range 1 to 100")
                self.textEdit__Message.setText("Please Enter Your Maths Marks in Range 1 to 100")
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
                self.pushbutton_Graph.hide()
                self.pushbutton_Pie.hide()
                self.pushbutton_Save.hide()
            elif float(self.textEdit_Science.text()) > 100:
                self.textEdit_Result.clear()
                self.textEdit__Division.clear()
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), "Input Error",
                                              "Please Enter Your Science Marks in Range 1 to 100")
                self.textEdit__Message.setText("Please Enter Your Science Marks in Range 1 to 100")
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
                self.pushbutton_Graph.hide()
                self.pushbutton_Pie.hide()
                self.pushbutton_Save.hide()
            elif float(self.textEdit_Social.text()) > 100:
                self.textEdit_Result.clear()
                self.textEdit__Division.clear()
                QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(), "Input Error",
                                              "Please Enter Your Social Marks in Range 1 to 100")
                self.textEdit__Message.setText("Please Enter Your Social Marks in Range 1 to 100")
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
                self.pushbutton_Graph.hide()
                self.pushbutton_Pie.hide()
                self.pushbutton_Save.hide()
            elif float(self.textEdit_Telugu.text()) < 35 or \
                    float(self.textEdit_Hindi.text()) < 35 or \
                    float(self.textEdit_English.text()) < 35 or \
                    float(self.textEdit_Maths.text()) < 35 or \
                    float(self.textEdit_Science.text()) < 35 or \
                    float(self.textEdit_Social.text()) < 35:
                self.textEdit_Result.setText("Failed")
                self.textEdit__Division.clear()
                self.textEdit__Message.clear()
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
            elif float(self.textEdit_Telugu.text()) <= 100 and float(self.textEdit_Telugu.text()) >= 35 and \
                    float(self.textEdit_Hindi.text()) <= 100 and float(self.textEdit_Hindi.text()) >= 35 and \
                    float(self.textEdit_English.text()) <= 100 and float(self.textEdit_English.text()) >= 35 and \
                    float(self.textEdit_Maths.text()) <= 100 and float(self.textEdit_Maths.text()) >= 35 and \
                    float(self.textEdit_Science.text()) <= 100 and float(self.textEdit_Science.text()) >= 35 and \
                    float(self.textEdit_Social.text()) <= 100 and float(self.textEdit_Social.text()) >= 35:
                self.textEdit_Result.setText("Passed")
                self.textEdit__Message.clear()
            else:
                self.textEdit_Result.clear()
                self.textEdit__Division.clear()
                self.textEdit__Message.clear()
                self.textEdit_Total.clear()
                self.textEdit_Average.clear()
                self.textEdit_Percentage.clear()
        except:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(),"Input Error","Invalid Input Given")
        #####  Creating a Function Named Total_Result   ######
    def Total_Result(self):
        try:
            totalsum = (float(self.textEdit_Telugu.text()) + float(self.textEdit_Hindi.text()) + float(
                self.textEdit_English.text()) + float(self.textEdit_Maths.text()) + float(
                self.textEdit_Science.text()) + float(self.textEdit_Social.text()))
            self.textEdit_Total.setText(str("{:.2f}".format(totalsum)))
            Avg = (float(self.textEdit_Telugu.text()) + float(self.textEdit_Hindi.text()) + float(
                self.textEdit_English.text()) + float(self.textEdit_Maths.text()) + float(
                self.textEdit_Science.text()) + float(self.textEdit_Social.text())) / 6
            self.textEdit_Average.setText(str("{:.2f}".format(Avg)))
            self.Percent = ((float(self.textEdit_Telugu.text()) + float(self.textEdit_Hindi.text()) + float(
                self.textEdit_English.text()) + float(self.textEdit_Maths.text()) + float(
                self.textEdit_Science.text()) + float(self.textEdit_Social.text())) / 600) * 100
            self.textEdit_Percentage.setText(str("{:.1f} %".format(self.Percent)))

            if self.Percent >= 70:
                self.textEdit__Division.setText("Distinction")
                self.textEdit__Message.clear()
            elif self.Percent >= 60:
                self.textEdit__Division.setText("First Class")
                self.textEdit__Message.clear()
            elif self.Percent >= 45:
                self.textEdit__Division.setText("Second Class")
                self.textEdit__Message.clear()
            elif self.Percent >= 35:
                self.textEdit__Division.setText(" ")
                self.textEdit__Message.clear()
            else:
                self.textEdit__Division.setText(" ")
                self.textEdit__Message.clear()
            self.pushbutton_Graph.show()
            self.pushbutton_Pie.show()
            self.pushbutton_Save.show()
        except:
            QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(),"Input Error","Invalid Input Given")
        #####  Creating a Function Named Reset   ######
    def Reset(self):
        self.textEdit_Telugu.clear()
        self.textEdit_Hindi.clear()
        self.textEdit_English.clear()
        self.textEdit_Maths.clear()
        self.textEdit_Science.clear()
        self.textEdit_Social.clear()
        self.textEdit__Division.clear()
        self.textEdit_Result.clear()
        self.textEdit_Total.clear()
        self.textEdit_Average.clear()
        self.textEdit_Percentage.clear()
        self.lineEdit_Student_name.clear()
        self.lineEdit_Father_name.clear()
        self.lineEdit_Hall_Ticket_Number.clear()
        self.textEdit__Message.clear()
        self.textEdit__Message.setText("Fill up your Data and Enter Your Marks of all Subjects")
        self.comboBox_Class.clear()
        _translate = QtCore.QCoreApplication.translate
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.addItem("")
        self.comboBox_Class.setItemText(0, _translate("Dialog", "Select Your Class"))
        self.comboBox_Class.setItemText(1, _translate("Dialog", "1st Class"))
        self.comboBox_Class.setItemText(2, _translate("Dialog", "2nd Class"))
        self.comboBox_Class.setItemText(3, _translate("Dialog", "3rd Class"))
        self.comboBox_Class.setItemText(4, _translate("Dialog", "4th Class"))
        self.comboBox_Class.setItemText(5, _translate("Dialog", "5th Class"))
        self.comboBox_Class.setItemText(6, _translate("Dialog", "6th Class"))
        self.comboBox_Class.setItemText(7, _translate("Dialog", "7th Class"))
        self.comboBox_Class.setItemText(8, _translate("Dialog", "8th Class"))
        self.comboBox_Class.setItemText(9, _translate("Dialog", "9th Class"))
        self.comboBox_Class.setItemText(10, _translate("Dialog", "10th Class"))
        self.pushbutton_Graph.hide()
        self.pushbutton_Pie.hide()
        self.pushbutton_Save.hide()

        #####  Creating a Function Named Save   ######
    def Save(self):
        path = "../Details/"
        folder = pathlib.Path(path)
        if folder.exists():
            filename = path + self.lineEdit_Student_name.text() + "{" + self.lineEdit_Hall_Ticket_Number.text() + "}.txt"
            file = open(filename, 'w')
        else:
            print("Folder does not exist")
            print("Creating Folder")
            os.mkdir(path)
            filename = path+self.lineEdit_Student_name.text()+"{"+self.lineEdit_Hall_Ticket_Number.text()+"}.txt"
            file = open(filename, 'w')
        file.write("******************************Memorandom of Marks******************************")
        text0 = self.lineEdit_Student_name.text(),
        text1 = self.lineEdit_Father_name.text(),
        text2 = self.comboBox_Class.currentText(),
        text3 = self.lineEdit_Hall_Ticket_Number.text(),
        text4 = self.dateEdit.text(),
        text5 = self.textEdit_Telugu.text(),
        text6 = self.textEdit_Hindi.text(),
        text7 = self.textEdit_English.text(),
        text8 = self.textEdit_Maths.text(),
        text9 = self.textEdit_Science.text(),
        text10 = self.textEdit_Social.text(),
        text11 = self.textEdit_Total.text(),
        text12 = self.textEdit_Average.text(),
        text13 = self.textEdit_Percentage.text(),
        text14 = self.textEdit__Division.text(),
        text15 = self.textEdit_Result.text(),
        file.write("\nStudent Name                                          :   ")
        file.writelines(text0)
        file.write("\nFather's Name                                         :   ")
        file.writelines(text1)
        file.write("\nClass                                                 :   ")
        file.writelines(text2)
        file.write("\nHall Ticket Number                                    :   ")
        file.writelines(text3)
        file.write("\nDate of Birth                                         :   ")
        file.writelines(text4)
        file.write("\nTotal Telugu Marks Obtained Out of 100.00             :   ")
        file.writelines(text5)
        file.write("/100.00")
        file.write("\nTotal Hindi Marks Obtained Out of 100.00              :   ")
        file.writelines(text6)
        file.write("/100.00")
        file.write("\nTotal English Marks Obtained Out of 100.00            :   ")
        file.writelines(text7)
        file.write("/100.00")
        file.write("\nTotal Mathematics Marks Obtained Out of 100.00        :   ")
        file.writelines(text8)
        file.write("/100.00")
        file.write("\nTotal Science Marks Obtained Out of 100.00            :   ")
        file.writelines(text9)
        file.write("/100.00")
        file.write("\nTotal Social Marks Obtained Out of 100.00             :   ")
        file.writelines(text10)
        file.write("/100.00")
        file.write("\nTotal Marks Obtained by the Student Out of 600.00     :   ")
        file.writelines(text11)
        file.write("/600.00")
        file.write("\nAverage of the Total Marks Obtained Out of 100.00     :   ")
        file.writelines(text12)
        file.write("/100.00")
        file.write("\nPercentage of the Total Marks Obtained Out of 100.00% :   ")
        file.writelines(text13)
        file.write("/100.00%")
        file.write("\nDivision                                              :   ")
        file.writelines(text14)
        file.write("\nResult                                                :   ")
        file.writelines(text15)
        file.write("\n*******************************************************************************")
        file.close()
        sys.exit()

    def Open(self):
        pass

    def Status_Bar(self):
        self.statusBar().showMessage("Aditya Burugu's Program")
        self.statusBar().setStyleSheet("background-color : lightgreen")

    def Graph(self):
        T = float(self.textEdit_Telugu.text())
        H = float(self.textEdit_Hindi.text())
        E = float(self.textEdit_English.text())
        M = float(self.textEdit_Maths.text())
        SC = float(self.textEdit_Science.text())
        SO = float(self.textEdit_Social.text())
        names = [' T ', ' H ', ' E', ' M ',' Sci ', ' Soc']
        names_= [' Telugu ', ' Hindi ', ' English', ' Maths ',' Science ', ' Social']
        values = [T,H,E,M,SC,SO]
        plt.figure(figsize=(12.4, 4))
        plt.subplot(131)
        plt.xlabel("Subjects",color='blue')
        plt.ylabel("Marks",color='blue')
        plt.bar(names, values,color='blue')
        plt.subplot(132)
        plt.xlabel("Subjects",color='magenta')
        plt.ylabel("Marks",color='magenta')
        plt.scatter(names_, values,color='magenta',marker='x')
        plt.subplot(133)
        plt.xlabel("Subjects",color='red')
        plt.ylabel("Marks",color='red')
        plt.plot(names_, values,color='red',marker = 'o',
        path_effects = [patheffects.SimpleLineShadow(),
        patheffects.Normal()])
        path_effects = [patheffects.withSimplePatchShadow()]
        plt.suptitle('Performance Report')
        path = "../Graphs/"
        folder = pathlib.Path(path)
        if folder.exists():
            graph = "Graph of "
            plt.savefig(path+graph + self.lineEdit_Student_name.text() + "{" + self.lineEdit_Hall_Ticket_Number.text() + "}")
        else:
            print("Folder does not exist")
            print("Creating Folder")
            os.mkdir(path)
            graph="Graph of "
            plt.savefig(path+graph+self.lineEdit_Student_name.text()+"{"+self.lineEdit_Hall_Ticket_Number.text()+"}")
        plt.show()

    def Pie(self):
        # Data to plot
        T = float(self.textEdit_Telugu.text())
        H = float(self.textEdit_Hindi.text())
        E = float(self.textEdit_English.text())
        M = float(self.textEdit_Maths.text())
        SC = float(self.textEdit_Science.text())
        SO = float(self.textEdit_Social.text())
        labels = 'Telugu', 'Hindi', 'English', 'Mathematics', 'Science', 'Social'
        sizes = [T, H, E, M, SC, SO]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'blue', 'red']
        explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=180)

        plt.axis('equal')
        path = "../Pie Chart Graphs/"
        folder = pathlib.Path(path)
        if folder.exists():
            pie = "Pie Chart of "
            plt.savefig(path+pie + self.lineEdit_Student_name.text() + "{" + self.lineEdit_Hall_Ticket_Number.text() + "}")
        else:
            print("Folder does not exist")
            print("Creating Folder")
            os.mkdir(path)
            pie="Pie Chart of "
            plt.savefig(path+pie+self.lineEdit_Student_name.text()+"{"+self.lineEdit_Hall_Ticket_Number.text()+"}")
        plt.show()

    def Exit(self):
        QtWidgets.QApplication.quit()

def Main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    Main()

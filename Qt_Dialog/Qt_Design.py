####################   Install PyQt5 Package and Import PyQt5 Package   ####################
from tkinter import filedialog
from PyQt5 import  QtCore, QtGui, QtWidgets
import os
import sys
####################   Creating Class Ui_Dialog   ####################
class Ui_Dialog(object):
    def setupUi(self, Dialog):   #Creating Function SetupUi
        Dialog.setObjectName("Dialog")   #Seting Object/Argument Name : Dialog
        Dialog.resize(736, 565)   #Setting the size of the Dialog
        Dialog.setWindowOpacity(1.0)

        #####  Creating Label for Displaying ...Student Report...  ######
        self.label_4 = QtWidgets.QLabel(Dialog)   #Creates Label
        self.label_4.setGeometry(QtCore.QRect(250, 10, 350, 31))   #Dimensions of Label
        font = QtGui.QFont()   #Sets Font
        font.setFamily("Myanmar Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")   #Sets Object Name

        #####  Creating Label for Displaying Maximum Marks  ######
        self.max = QtWidgets.QLabel(Dialog)   #Creates Label Max
        self.max.setGeometry(QtCore.QRect(590, 30, 125, 20))   #Dimensions of Label Max
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.max.setFont(font)
        self.max.setObjectName("max marks")   #Sets Object Name

        #####  Creating Label For Displaying Student Name:  ######
        self.Student_name = QtWidgets.QLabel(Dialog)   #Creates Label Student Name
        self.Student_name.setGeometry(QtCore.QRect(20, 55, 101, 16))   #Dimensions of Label Student Name
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Student_name.setFont(font)
        self.Student_name.setObjectName("Student_name")   #Sets Object Name

        #####  Creating Label for Displaying Father's Name :  ######
        self.Father_name = QtWidgets.QLabel(Dialog)      #Creates Label Father's Name
        self.Father_name.setGeometry(QtCore.QRect(20, 82, 101, 16))   #Dimensions of Label Father's Name
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Father_name.setFont(font)
        self.Father_name.setObjectName("Father's_name")   #Sets Object Name

        #####  Creating Label for Displaying Hall-Ticket-Number :  ######
        self.Hall_Ticket_Number = QtWidgets.QLabel(Dialog)   #Creates Label Hall_Ticket_Number
        self.Hall_Ticket_Number.setGeometry(QtCore.QRect(360, 55, 140, 16))   #Dimensiopns of Label Hall_Ticket_Number
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Hall_Ticket_Number.setFont(font)
        self.Hall_Ticket_Number.setObjectName("Hall_Ticket_Number")   #Sets Object Name

        #####  Creating Label for Displaying Class :  ######
        self.Class = QtWidgets.QLabel(Dialog)   #Creates Label Class
        self.Class.setGeometry(QtCore.QRect(360, 82, 101, 16))   #Dimensions of Label Class
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Class.setFont(font)
        self.Class.setObjectName("Class")   #Sets Object Name

        #####  Creating Label for Displaying Date_of_Birth :  ######
        self.DOB = QtWidgets.QLabel(Dialog)   #Creates Label DOB
        self.DOB.setGeometry(QtCore.QRect(20, 110, 100, 20))   #Dimensions of Label DOB
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.DOB.setFont(font)
        self.DOB.setObjectName("Date_of_Birth")   #Sets Object Name

        #####  Creating Label for Displaying Telugu  ######
        self.Telugu = QtWidgets.QLabel(Dialog) #Creates Label Telugu
        self.Telugu.setGeometry(QtCore.QRect(80, 148, 55, 16))   #Dimensions of Label Telugu
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Telugu.setFont(font)
        self.Telugu.setObjectName("Telugu")   #Sets Object Name

        #####  Creating Label for Displaying Hindi  ######
        self.Hindi = QtWidgets.QLabel(Dialog)   #Creates Label Hindi
        self.Hindi.setGeometry(QtCore.QRect(80, 185, 55, 21))   #Dimensions of Label Hindi
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Hindi.setFont(font)
        self.Hindi.setObjectName("Hindi")   #Sets Object Name

        #####  Creating Label for Displaying English  ######
        self.English = QtWidgets.QLabel(Dialog)   #Creates Label English
        self.English.setGeometry(QtCore.QRect(80, 230, 55, 16))   #Dimensions of Label Hindi
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.English.setFont(font)
        self.English.setObjectName("English")   #Sets Object Name

        #####  Creating Label for Displaying Maths  ######
        self.Maths = QtWidgets.QLabel(Dialog)   #Creates Label Maths
        self.Maths.setGeometry(QtCore.QRect(80, 270, 81, 16))   #Dimensions of Label Maths
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Maths.setFont(font)
        self.Maths.setObjectName("Maths")   #Sets Object Name

        #####  Creating Label for Displaying Science  ######
        self.Science = QtWidgets.QLabel(Dialog)   #Creats Label Science
        self.Science.setGeometry(QtCore.QRect(80, 310, 55, 16))   #Dimensions of Label Science
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Science.setFont(font)
        self.Science.setObjectName("Science")   #Sets Object Name

        #####  Creating Label for Displaying Social  ######
        self.Social = QtWidgets.QLabel(Dialog)   #Creates Label Social
        self.Social.setGeometry(QtCore.QRect(80, 350, 55, 16))   #Dimensions of Label Social
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Social.setFont(font)
        self.Social.setObjectName("Social")   #Sets Object Name

        #####  Creating Label for Displaying Total  ######
        self.Total = QtWidgets.QLabel(Dialog)   #Creates Label Total
        self.Total.setGeometry(QtCore.QRect(450, 170, 93, 28))   #Dimensions of Label Total
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Total.setFont(font)
        self.Total.setObjectName("Total")   #Sets Object Name

        #####  Creating Label for Displaying Average  ######
        self.Average = QtWidgets.QLabel(Dialog)   #Creaates Label Average
        self.Average.setGeometry(QtCore.QRect(450, 210, 93, 28))   #Dimensions of Label Average
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Average.setFont(font)
        self.Average.setObjectName("Average")   #Sets Object Name

        #####  Creating Label for Displaying Percentage  ######
        self.Percentage = QtWidgets.QLabel(Dialog)   #Creates Label Percentage
        self.Percentage.setGeometry(QtCore.QRect(450, 250, 93, 28))   #Dimensions of Label Percentage
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Percentage.setFont(font)
        self.Percentage.setObjectName("Average")   #Sets Object Name

        #####  Creating Label for Displaying Division  ######
        self.Division = QtWidgets.QLabel(Dialog)   #Creates Label Division
        self.Division.setGeometry(QtCore.QRect(280, 410, 93, 28))   #Dimensions of Label Division
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Division.setFont(font)
        self.Division.setObjectName("Division")   #Sets Object Name

        #####  Creating Label for Displaying Result  ######
        self.Result = QtWidgets.QLabel(Dialog)   #Creates Label Result
        self.Result.setGeometry(QtCore.QRect(280, 450, 104, 31))   #Dimensions of Label Result
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Result.setFont(font)
        self.Result.setObjectName("Result")   #Sets Object Name

        #####  Creating Label for Displaying Message  ######
        self.Message = QtWidgets.QLabel(Dialog)   #Creates Label Message
        self.Message.setGeometry(QtCore.QRect(280, 500, 100, 28))   #Dimensions of Label Message
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Message.setFont(font)
        self.Message.setObjectName("Message")   #Sets Object Name

        #####  Creating a Line Edit to Input Student Name   ######
        self.lineEdit_Student_name = QtWidgets.QLineEdit(Dialog)   #Creates Line Edit for Student Name
        self.lineEdit_Student_name.setGeometry(QtCore.QRect(130, 55, 211, 22))   #Dimensions of Line Edit of Student Name
        self.lineEdit_Student_name.setObjectName("lineEdit_student_name")   #Sets Object Name

        #####  Creating a Line Edit to Input Father's Name   ######
        self.lineEdit_Father_name = QtWidgets.QLineEdit(Dialog)   #Creates Line Edit for Father's Name
        self.lineEdit_Father_name.setGeometry(QtCore.QRect(130, 80, 211, 22))   #Dimensions of Line Edit of Father's Name
        self.lineEdit_Father_name.setObjectName("lineEdit_Father_name")   #Sets Object Name

        #####  Creating a Line Edit to Input Hall-Ticket-Number   ######
        self.lineEdit_Hall_Ticket_Number = QtWidgets.QLineEdit(Dialog)   #Creates Line Edit for Hall Ticket Number
        self.lineEdit_Hall_Ticket_Number.setGeometry(QtCore.QRect(495, 55, 211, 22))   #Dimensions of Line Edit of Hall Ticket Number
        self.lineEdit_Hall_Ticket_Number.setObjectName("lineEdit_Hall_Ticket_Number")   #Sets Object Name

        #####  Creating a Combo Box to Input Class   ######
        self.comboBox_Class = QtWidgets.QComboBox(Dialog)   #Creates Combo Box for Class
        self.comboBox_Class.setGeometry(QtCore.QRect(410, 80, 128, 22))   #Dimensions of Combo Box of Class
        self.comboBox_Class.setEditable(True)
        self.comboBox_Class.setObjectName("comboBox_Class")   #Sets Object Name
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

        #####  Creating a Date Edit to Input Date-of-Birth    ######
        self.dateEdit = QtWidgets.QDateEdit(Dialog)   #Creates Date Edit
        self.dateEdit.setGeometry(QtCore.QRect(130, 110, 100, 22))   #Dimensions of Date Edit
        self.dateEdit.setObjectName("dateEdit")   #Sets Object Name

        #####  Creating a Text Edit to Input Telugu Marks   ######
        self.textEdit_Telugu = QtWidgets.QTextEdit(Dialog)   #Creates TExt Edit for Telugu
        self.textEdit_Telugu.setGeometry(QtCore.QRect(160, 140, 104, 31))   #Dimensions of Text Edit Telugu
        self.textEdit_Telugu.setObjectName("textEdit_Telugu")   #Sets Object Name

        #####  Creating a Text Edit to Input Hindi Marks   ######
        self.textEdit_Hindi = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Hindi
        self.textEdit_Hindi.setGeometry(QtCore.QRect(160, 180, 104, 31))   #Dimensions of Text Edit Hindi
        self.textEdit_Hindi.setObjectName("textEdit_Hindi")   #Sets Object Name

        #####  Creating a Text Edit to Input English Marks   ######
        self.textEdit_English = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for English
        self.textEdit_English.setGeometry(QtCore.QRect(160, 220, 104, 31))   #Dimensions of Text Edit English
        self.textEdit_English.setObjectName("textEdit_English")   #Sets Object Name

        #####  Creating a Text Edit to Input Maths Marks   ######
        self.textEdit_Maths = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Maths
        self.textEdit_Maths.setGeometry(QtCore.QRect(160, 260, 104, 31))   #Dimensions of Text Edit Maths
        self.textEdit_Maths.setObjectName("textEdit_Maths")   #Sets Object Name

        #####  Creating a Text Edit to Input Science Marks   ######
        self.textEdit_Science = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Science
        self.textEdit_Science.setGeometry(QtCore.QRect(160, 300, 104, 31))   #Dimensions of Text Edit Science
        self.textEdit_Science.setObjectName("textEdit_Science")   #Sets Object Name

        #####  Creating a Text Edit to Input Social Marks   ######
        self.textEdit_Social = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Social
        self.textEdit_Social.setGeometry(QtCore.QRect(160, 340, 104, 31))   #Dimensions of Text Edit Social
        self.textEdit_Social.setObjectName("textEdit_Social")   #Sets Object Name

        #####  Creating a Text Edit to Display Total Marks   ######
        self.textEdit_Total = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Total Marks
        self.textEdit_Total.setGeometry(QtCore.QRect(540, 170, 104, 31))   #Dimensions of Text Edit Total Marks
        self.textEdit_Total.setObjectName("textEdit")   #Sets Object Name

        #####  Creating a Text Edit to Display Average Marks   ######
        self.textEdit_Average = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Average Marks
        self.textEdit_Average.setGeometry(QtCore.QRect(540, 210, 104, 31))   #Dimensions of Text Edit Average Marks
        self.textEdit_Average.setObjectName("textEdit_2")   #Sets Object Name

        #####  Creating a Text Edit to Display Percentage of the Total Marks   ######
        self.textEdit_Percentage = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Percentage of the Total Marks
        self.textEdit_Percentage.setGeometry(QtCore.QRect(540, 250, 104, 31))   #Dimensions of text Edit Percentage of the Total Marks
        self.textEdit_Percentage.setObjectName("textEdit_3")   #Sets Object Name

        #####  Creating a Text Edit to Find out the Division   ######
        self.textEdit__Division = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Division
        self.textEdit__Division.setGeometry(QtCore.QRect(360, 410, 141, 31))   #Dimensions of Text Edit Division
        self.textEdit__Division.setObjectName("textEdit__Division")   #Sets Object Name

        #####  Creating a Text Edit to Find out the Result   ######
        self.textEdit_Result = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Result
        self.textEdit_Result.setGeometry(QtCore.QRect(360, 450, 104, 31))   #Dimensions of Text Edit Result
        self.textEdit_Result.setObjectName("textEdit_Result")   #Sets Object Name

        #####  Creating a Text Edit to Find out Errors if any   ######
        self.textEdit__Message = QtWidgets.QTextEdit(Dialog)   #Creates Text Edit for Message
        self.textEdit__Message.setGeometry(QtCore.QRect(360, 490, 260, 45))   #Dimensions of Text Edit Message
        self.textEdit__Message.setObjectName("textEdit__Message")   #Sets Object Name

        #####  Creating Get Result  button  ######
        self.pushButton_Get_Result = QtWidgets.QPushButton(Dialog)   #Creates Push Button Get Result
        self.pushButton_Get_Result.setGeometry(QtCore.QRect(450, 120, 93, 28))   #Dimensions of Push Button Get Result
        self.pushButton_Get_Result.setObjectName("pushButton_Get_Result")   #Sets Object Name
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_Get_Result.setFont(font)

        #####  Creating Reset button  ######
        self.pushButton_Reset = QtWidgets.QPushButton(Dialog)   #Creates Push Button Reset Button
        self.pushButton_Reset.setGeometry(QtCore.QRect(560, 120, 93, 28))   #Dimensions of Push Button Reset
        self.pushButton_Reset.setObjectName("pushButton_Reset")   #Sets Object Name
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setWeight(75)
        self.pushButton_Reset.setFont(font)

        #####  Creating Save button  ######
        self.pushButton_Save = QtWidgets.QPushButton(Dialog)   #Creates Push Button Save
        self.pushButton_Save.setGeometry(QtCore.QRect(640, 445, 80, 28))   #Dimensions of Push Button Save
        self.pushButton_Save.setObjectName("pushButton_Save")   #Sets Object Name
        font = QtGui.QFont()   #Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_Save.setFont(font)

        #####  Creating a Button Box with Cancel Push Button in it  ######
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)  # Creates Button Box
        self.buttonBox.setGeometry(QtCore.QRect(640, 480, 80, 80))  # Dimensions of Buttonbox
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)  # Displays Buttonbox Vertically
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)  # Creates Cancel Push Button
        self.buttonBox.setObjectName("buttonBox")  # Sets Object Name
        font = QtGui.QFont()  # Sets Font
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        font.setWeight(75)
        self.buttonBox.setFont(font)

        ###### Creating Frame #########
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(250, 400, 375, 145))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(530, 160, 131, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        #####  Initializing Value of self.Percent   ######
        self.Percent = 0

        #####  Creating RetranslateUi    ######
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #####  Connecting a Function to a Push Button   ######
        self.pushButton_Get_Result.clicked.connect(self.Total_Result)
        self.pushButton_Get_Result.clicked.connect(self.Calculate)
        self.pushButton_Reset.clicked.connect(self.Reset)
        self.pushButton_Save.clicked.connect(self.Save)

    #####  Creating a Function Named retranslateUi   ######
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Student Performance Report"))
        self.label_4.setText(_translate("Dialog", "...Memorandom of Marks..."))
        self.max.setText(_translate("Dialog", "max marks: 6x100"))
        self.Student_name.setText(_translate("Dialog", "Student Name :"))
        self.Father_name.setText(_translate("Dialogue", "Father's Name :"))
        self.Hall_Ticket_Number.setText(_translate("Dialogue", "Hall Ticket Number :"))
        self.Class.setText(_translate("Dialogue", "Class :"))
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
        self.DOB.setText(_translate("Dialog", "Date_of_Birth :"))
        self.Telugu.setText(_translate("Dialog", "Telugu"))
        self.Hindi.setText(_translate("Dialog", "Hindi"))
        self.English.setText(_translate("Dialog", "English"))
        self.Maths.setText(_translate("Dialog", "Maths"))
        self.Science.setText(_translate("Dialog", "Science"))
        self.Social.setText(_translate("Dialog", "Social"))
        self.Result.setText(_translate("Dialog", "Result"))
        self.Total.setText(_translate("Dialog","Total"))
        self.Average.setText(_translate("Dialog","Average"))
        self.Percentage.setText(_translate("Dialog","Percentage"))
        self.Division.setText(_translate("Dialog","Division"))
        self.Message.setText(_translate("Dialog", "Message"))
        self.pushButton_Get_Result.setText(_translate("Dialog", "Get Result"))
        self.pushButton_Reset.setText(_translate("Dialog", "Reset"))
        self.pushButton_Save.setText(_translate("Dialog", "Save  As"))

        #####  Initialising Values & Texts  ######
        self.textEdit__Message.setText("Fill up your Data and Enter Your Marks of all Subjects")
        self.textEdit_Telugu.setText("0")
        self.textEdit_Hindi.setText("0")
        self.textEdit_English.setText("0")
        self.textEdit_Maths.setText("0")
        self.textEdit_Science.setText("0")
        self.textEdit_Social.setText("0")

    #####  Creating a Function Named Calculate   ######
    def Calculate(self):
        if float(self.textEdit_Telugu.toPlainText()) and float(self.textEdit_Hindi.toPlainText()) and float(self.textEdit_English.toPlainText()) and float(self.textEdit_Maths.toPlainText()) and float(self.textEdit_Science.toPlainText()) and float(self.textEdit_Social.toPlainText()) > 100:
            self.textEdit_Result.clear()
            self.textEdit__Division.clear()
            self.textEdit__Message.setText("Please Enter Your Marks of all Subjects in Range 1 to 100")
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()
        elif float(self.textEdit_Telugu.toPlainText()) > 100:
            self.textEdit_Result.clear()
            self.textEdit__Division.clear()
            self.textEdit__Message.setText("Please Enter Your Telugu Marks in Range 1 to 100")
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()
        elif float(self.textEdit_Hindi.toPlainText()) > 100:
            self.textEdit_Result.clear()
            self.textEdit__Division.clear()
            self.textEdit__Message.setText("Please Enter Your Hindi Marks in Range 1 to 100")
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()
        elif float(self.textEdit_English.toPlainText()) > 100:
            self.textEdit_Result.clear()
            self.textEdit__Division.clear()
            self.textEdit__Message.setText("Please Enter Your English Marks in Range 1 to 100")
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()
        elif float(self.textEdit_Maths.toPlainText()) > 100:
            self.textEdit_Result.clear()
            self.textEdit__Division.clear()
            self.textEdit__Message.setText("Please Enter Your Maths Marks in Range 1 to 100")
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()
        elif float(self.textEdit_Science.toPlainText()) > 100:
            self.textEdit_Result.clear()
            self.textEdit__Division.clear()
            self.textEdit__Message.setText("Please Enter Your Science Marks in Range 1 to 100")
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()
        elif float(self.textEdit_Social.toPlainText()) > 100:
            self.textEdit_Result.clear()
            self.textEdit__Division.clear()
            self.textEdit__Message.setText("Please Enter Your Social Marks in Range 1 to 100")
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()
        elif float(self.textEdit_Telugu.toPlainText()) < 35 or \
                float(self.textEdit_Hindi.toPlainText()) < 35 or \
                float(self.textEdit_English.toPlainText()) < 35 or \
                float(self.textEdit_Maths.toPlainText()) < 35 or \
                float(self.textEdit_Science.toPlainText()) < 35 or \
                float(self.textEdit_Social.toPlainText()) < 35:
            self.textEdit_Result.setText("Failed")
            self.textEdit__Division.clear()
            self.textEdit__Message.clear()
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()
        elif float(self.textEdit_Telugu.toPlainText()) <= 100 and float(self.textEdit_Telugu.toPlainText()) >=35 and \
             float(self.textEdit_Hindi.toPlainText()) <= 100 and float(self.textEdit_Hindi.toPlainText()) >=35 and\
             float(self.textEdit_English.toPlainText()) <= 100 and float(self.textEdit_English.toPlainText()) >=35 and \
             float(self.textEdit_Maths.toPlainText()) <= 100 and float(self.textEdit_Maths.toPlainText()) >=35 and \
             float(self.textEdit_Science.toPlainText()) <= 100 and float(self.textEdit_Science.toPlainText()) >=35 and \
             float(self.textEdit_Social.toPlainText())<= 100 and float(self.textEdit_Social.toPlainText()) >=35:
                self.textEdit_Result.setText("Passed")
                self.textEdit__Message.clear()
        else:
            self.textEdit_Result.clear()
            self.textEdit__Division.clear()
            self.textEdit__Message.clear()
            self.textEdit_Total.clear()
            self.textEdit_Average.clear()
            self.textEdit_Percentage.clear()

    #####  Creating a Function Named Total_Result   ######
    def Total_Result(self):
        totalsum = float(self.textEdit_Telugu.toPlainText()) + float(self.textEdit_Hindi.toPlainText()) + float(self.textEdit_English.toPlainText()) + float(self.textEdit_Maths.toPlainText()) + float(self.textEdit_Science.toPlainText()) + float(self.textEdit_Social.toPlainText())
        self.textEdit_Total.setText(str("{:.2f}".format(totalsum)))
        Avg = (float(self.textEdit_Telugu.toPlainText()) + float(self.textEdit_Hindi.toPlainText()) + float(
            self.textEdit_English.toPlainText()) + float(self.textEdit_Maths.toPlainText()) + float(
            self.textEdit_Science.toPlainText()) + float(self.textEdit_Social.toPlainText())) / 6
        self.textEdit_Average.setText(str("{:.2f}".format(Avg)))
        self.Percent = ((float(self.textEdit_Telugu.toPlainText()) + float(self.textEdit_Hindi.toPlainText()) + float(
            self.textEdit_English.toPlainText()) + float(self.textEdit_Maths.toPlainText()) + float(
            self.textEdit_Science.toPlainText()) + float(self.textEdit_Social.toPlainText())) / 600) * 100
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
        self.textEdit_Telugu.setText("0")
        self.textEdit_Hindi.setText("0")
        self.textEdit_English.setText("0")
        self.textEdit_Maths.setText("0")
        self.textEdit_Science.setText("0")
        self.textEdit_Social.setText("0")
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

    #####  Creating a Function Named Save   ######
    def Save(self):
        files = [('Text Document', '*.txt'),('Python File', '*.py'), ("Excel File",'*.XLS'), ("Word Document File",'.doc')]
        file = filedialog.asksaveasfile(mode="w",filetypes = files, defaultextension = files)
        file.write("******************************Memorandom of Marks******************************")
        text0 = self.lineEdit_Student_name.text(),
        text1 = self.lineEdit_Father_name.text(),
        text2 = self.comboBox_Class.currentText(),
        text3 = self.lineEdit_Hall_Ticket_Number.text(),
        text4 = self.dateEdit.text(),
        text5 = self.textEdit_Telugu.toPlainText(),
        text6 = self.textEdit_Hindi.toPlainText(),
        text7 = self.textEdit_English.toPlainText(),
        text8 = self.textEdit_Maths.toPlainText(),
        text9 = self.textEdit_Science.toPlainText(),
        text10 = self.textEdit_Social.toPlainText(),
        text11 = self.textEdit_Total.toPlainText(),
        text12 = self.textEdit_Average.toPlainText(),
        text13 = self.textEdit_Percentage.toPlainText(),
        text14 = self.textEdit__Division.toPlainText(),
        text15 = self.textEdit_Result.toPlainText(),
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

def Main():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()
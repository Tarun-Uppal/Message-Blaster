from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import whatsapp
import excel_reader as excel
import sys
import threading
            
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 478)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:\"black\"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vertical_layout_1.setContentsMargins(6, 6, 6, 6)
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.login_button.setFont(font)
        self.login_button.setMouseTracking(True)
        self.login_button.setAutoFillBackground(False)
        self.login_button.setStyleSheet("background-color:\"#85c78f\"")
        self.login_button.setCheckable(False)
        self.login_button.setObjectName("login_button")
        self.vertical_layout_1.addWidget(self.login_button)
        spacerItem = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_1.addItem(spacerItem)
        self.login_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.login_info.sizePolicy().hasHeightForWidth())
        self.login_info.setSizePolicy(sizePolicy)
        self.login_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.login_info.setFont(font)
        self.login_info.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.login_info.setAutoFillBackground(False)
        self.login_info.setStyleSheet("background-color:\"#85c78f\"")
        self.login_info.setScaledContents(False)
        self.login_info.setAlignment(QtCore.Qt.AlignCenter)
        self.login_info.setOpenExternalLinks(True)
        self.login_info.setObjectName("login_info")
        self.vertical_layout_1.addWidget(self.login_info)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_1.addItem(spacerItem1)
        self.excel_button = QtWidgets.QPushButton(self.centralwidget)
        self.excel_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.excel_button.sizePolicy().hasHeightForWidth())
        self.excel_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.excel_button.setFont(font)
        self.excel_button.setMouseTracking(True)
        self.excel_button.setAutoFillBackground(False)
        self.excel_button.setStyleSheet("background-color:\"#85c78f\"")
        self.excel_button.setCheckable(False)
        self.excel_button.setObjectName("excel_button")
        self.vertical_layout_1.addWidget(self.excel_button)
        spacerItem2 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_1.addItem(spacerItem2)
        self.excel_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.excel_info.sizePolicy().hasHeightForWidth())
        self.excel_info.setSizePolicy(sizePolicy)
        self.excel_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.excel_info.setFont(font)
        self.excel_info.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.excel_info.setAutoFillBackground(False)
        self.excel_info.setStyleSheet("background-color:\"#85c78f\"")
        self.excel_info.setScaledContents(False)
        self.excel_info.setAlignment(QtCore.Qt.AlignCenter)
        self.excel_info.setOpenExternalLinks(True)
        self.excel_info.setObjectName("excel_info")
        self.vertical_layout_1.addWidget(self.excel_info)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_1.addItem(spacerItem3)
        self.message_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.message_checkbox.setFont(font)
        self.message_checkbox.setStyleSheet("background-color:\"#85c78f\"")
        self.message_checkbox.setObjectName("message_checkbox")
        self.vertical_layout_1.addWidget(self.message_checkbox)
        spacerItem4 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_1.addItem(spacerItem4)
        self.message_textbox = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.message_textbox.setFont(font)
        self.message_textbox.setStyleSheet("color: white")
        self.message_textbox.setObjectName("message_textbox")
        self.vertical_layout_1.addWidget(self.message_textbox)
        spacerItem5 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_1.addItem(spacerItem5)
        self.message_submit_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.message_submit_button.sizePolicy().hasHeightForWidth())
        self.message_submit_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.message_submit_button.setFont(font)
        self.message_submit_button.setStyleSheet("background-color:\"#85c78f\"")
        self.message_submit_button.setObjectName("message_submit_button")
        self.vertical_layout_1.addWidget(self.message_submit_button)
        spacerItem6 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_1.addItem(spacerItem6)
        self.message_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.message_info.sizePolicy().hasHeightForWidth())
        self.message_info.setSizePolicy(sizePolicy)
        self.message_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.message_info.setFont(font)
        self.message_info.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.message_info.setAutoFillBackground(False)
        self.message_info.setStyleSheet("background-color:\"#85c78f\"")
        self.message_info.setScaledContents(False)
        self.message_info.setAlignment(QtCore.Qt.AlignCenter)
        self.message_info.setOpenExternalLinks(True)
        self.message_info.setObjectName("message_info")
        self.vertical_layout_1.addWidget(self.message_info)
        self.horizontalLayout.addLayout(self.vertical_layout_1)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.vertical_layout_2.setContentsMargins(6, 6, 6, 6)
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.attachment_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.attachment_checkbox.setFont(font)
        self.attachment_checkbox.setStyleSheet("background-color:\"#85c78f\"")
        self.attachment_checkbox.setObjectName("attachment_checkbox")
        self.vertical_layout_2.addWidget(self.attachment_checkbox)
        spacerItem7 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_2.addItem(spacerItem7)
        self.attachment_first_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.attachment_first_checkbox.setFont(font)
        self.attachment_first_checkbox.setStyleSheet("background-color:\"#85c78f\"")
        self.attachment_first_checkbox.setObjectName("attachment_first_checkbox")
        self.vertical_layout_2.addWidget(self.attachment_first_checkbox)
        spacerItem8 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_2.addItem(spacerItem8)
        self.attachment_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.attachment_button.sizePolicy().hasHeightForWidth())
        self.attachment_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.attachment_button.setFont(font)
        self.attachment_button.setMouseTracking(True)
        self.attachment_button.setAutoFillBackground(False)
        self.attachment_button.setStyleSheet("background-color:\"#85c78f\"")
        self.attachment_button.setCheckable(False)
        self.attachment_button.setObjectName("attachment_button")
        self.vertical_layout_2.addWidget(self.attachment_button)
        spacerItem9 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_2.addItem(spacerItem9)
        self.attachment_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.attachment_info.sizePolicy().hasHeightForWidth())
        self.attachment_info.setSizePolicy(sizePolicy)
        self.attachment_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.attachment_info.setFont(font)
        self.attachment_info.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.attachment_info.setAutoFillBackground(False)
        self.attachment_info.setStyleSheet("background-color:\"#85c78f\"")
        self.attachment_info.setScaledContents(False)
        self.attachment_info.setAlignment(QtCore.Qt.AlignCenter)
        self.attachment_info.setOpenExternalLinks(True)
        self.attachment_info.setObjectName("attachment_info")
        self.vertical_layout_2.addWidget(self.attachment_info)
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_2.addItem(spacerItem10)
        self.sender_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.sender_button.sizePolicy().hasHeightForWidth())
        self.sender_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.sender_button.setFont(font)
        self.sender_button.setMouseTracking(True)
        self.sender_button.setAutoFillBackground(False)
        self.sender_button.setStyleSheet("background-color:\"#85c78f\"")
        self.sender_button.setCheckable(False)
        self.sender_button.setObjectName("sender_button")
        self.vertical_layout_2.addWidget(self.sender_button)
        spacerItem11 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_2.addItem(spacerItem11)
        self.sender_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.sender_info.sizePolicy().hasHeightForWidth())
        self.sender_info.setSizePolicy(sizePolicy)
        self.sender_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.sender_info.setFont(font)
        self.sender_info.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sender_info.setAutoFillBackground(False)
        self.sender_info.setStyleSheet("background-color:\"#85c78f\"")
        self.sender_info.setScaledContents(False)
        self.sender_info.setAlignment(QtCore.Qt.AlignCenter)
        self.sender_info.setOpenExternalLinks(True)
        self.sender_info.setObjectName("sender_info")
        self.vertical_layout_2.addWidget(self.sender_info)
        spacerItem12 = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vertical_layout_2.addItem(spacerItem12)
        self.horizontalLayout.addLayout(self.vertical_layout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_button.setText(_translate("MainWindow", "Login to Whasapp"))
        self.login_info.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.pcenthusiast.tech/post/how-to-use-our-whatsapp-message-blaster#viewer-3epfk\"><span style=\" text-decoration: underline; color:#0000ff;\">Whatsapp Login Instructions</span></a></p></body></html>"))
        self.excel_button.setText(_translate("MainWindow", "Please Choose a Excel File with the Phone Numbers and Names"))
        self.excel_info.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.pcenthusiast.tech/post/how-to-use-our-whatsapp-message-blaster#viewer-fco0p\"><span style=\" text-decoration: underline; color:#0000ff;\">Excel File Formatting Instructions</span></a></p></body></html>"))
        self.message_checkbox.setText(_translate("MainWindow", "Would you like to send a message"))
        self.message_textbox.setPlaceholderText(_translate("MainWindow", "Please enter your message here"))
        self.message_submit_button.setText(_translate("MainWindow", "Submit Text"))
        self.message_info.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.pcenthusiast.tech/post/how-to-use-our-whatsapp-message-blaster#viewer-8t5tp\"><span style=\" text-decoration: underline; color:#0000ff;\">Message Instructions and formatting</span></a></p></body></html>"))
        self.attachment_checkbox.setText(_translate("MainWindow", "Would you like to send a attachment"))
        self.attachment_first_checkbox.setText(_translate("MainWindow", "Would you like the attachment to be sent first"))
        self.attachment_button.setText(_translate("MainWindow", "Please enter the Attacment you would like to send"))
        self.attachment_info.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.pcenthusiast.tech/post/how-to-use-our-whatsapp-message-blaster#viewer-6fk2k\"><span style=\" text-decoration: underline; color:#0000ff;\">Instructions before you add the attachment</span></a></p></body></html>"))
        self.sender_button.setText(_translate("MainWindow", "Start Sending Messages"))
        self.sender_info.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.pcenthusiast.tech/post/how-to-use-our-whatsapp-message-blaster#viewer-8bknl\"><span style=\" text-decoration: underline; color:#0000ff;\">Instructions before you start sending the messsages</span></a></p></body></html>"))
        
        self.login_button.clicked.connect(login_info)
        self.excel_button.clicked.connect(excel_button)
        self.message_submit_button.clicked.connect(message_submit)
        self.attachment_button.clicked.connect(attachment_button)
        self.sender_button.clicked.connect(sender_button)


def login_info():
    global ui, _translate, login_status
    val = whatsapp.whatsapp_login()
    if val == True:
        ui.login_button.setText(_translate("MainWindow", "Logged in to Whatasapp"))
        login_status = True
    
def excel_button():
    global contacts_path, ui, _translate, contacts_status
    while True:
        filename = QFileDialog.getOpenFileName()
        contacts_path = filename[0]
        filename = contacts_path.split('.')
        try:
            if filename[1] == 'xlsx' or filename[1] == 'xlsb':
                val = excel.read_file(contacts_path)
                if val == None:
                    continue
                else:
                    ui.excel_button.setText(_translate("MainWindow", "Excel File : Chosen"))
                    contacts_status = True
                    break
        except IndexError:
            break

def attachment_button():
    global attachment_path, ui, _translate, attachment_status, attachment_choice
    
    if ui.attachment_checkbox.checkState() == 2:
        attachment_choice = True
    else:
        attachment_choice = False  
        
    if attachment_choice == True:
        while True:
            filename = QFileDialog.getOpenFileName()
            try:
                attachment_path = filename[0]
                print(filename[0])
                extension = attachment_path.split('.')[1]
                valid_extensions = ['xlsb', 'xlsx', 'doc', 'docx', 'ppt', 'pptx', 'pdf', 'jpg', 'gif', 'png', 'mp4', 'avi']
                if extension.lower() in valid_extensions:
                    ui.attachment_button.setText(_translate("MainWindow", "Attacment : Chosen"))
                    attachment_status = True
                    break
            except IndexError:
                break
            
def sender_button():
    global message, contacts_path, attachment_path, ui, message_status, attachment_status, contacts_status, login_status
    global attachment_choice, message_choice, attachment_first, message_choice, attachment_choice
    
    if ui.attachment_first_checkbox.checkState() == 2:
        attachment_first = True
    else:
        attachment_first = False  
        
    if ui.message_checkbox.checkState() == 2:
        message_choice = True
    else:
        message_choice = False  
        # message_status = False
        
    if ui.attachment_checkbox.checkState() == 2:
        attachment_choice = True
    else:
        attachment_choice = False
        # attachment_status = False
    
    if contacts_status == True and login_status == True:
        if (message_choice == True and message_status == True) or (attachment_choice == True and attachment_status == True):
            ui.sender_button.setText(_translate("MainWindow", "Sending Messages : Please Wait"))
            thread = threading.Thread(target=send_message)
            thread.start()
            ui.sender_button.setText(_translate("MainWindow", "Start Sending Messages"))
	    

def send_message():
    global message, contacts_path, attachment_path, ui, message_status, attachment_status, contacts_status, login_status
    global attachment_choice, message_choice, attachment_first, message_choice, attachment_choice
    ui.sender_button.setText(_translate("MainWindow", "Sending Messages : Please Wait"))
    (contacts, numbers) = excel.read_file(contacts_path)
    whatsapp.sender(numbers, contacts, attachment_choice, attachment_path, message_choice, 
                            message, attachment_first)
    ui.sender_button.setText(_translate("MainWindow", "Start Sending Messages"))
    
    
def message_submit():
    global ui, message, _translate, message_status, message_choice
    if ui.message_checkbox.checkState() == 2:
        message_choice = True
    else:
        message_choice = False  
        
    if message_choice == True:
        message = ui.message_textbox.text()
        if message != '':
            ui.message_submit_button.setText(_translate("MainWindow", "Message : Submitted"))
            message_status = True

ui = None
message = None
attachment_path = None
contacts_path = None
_translate = QtCore.QCoreApplication.translate
login_status = False
contacts_status = False
message_status = False
attachment_status = False
message_choice = None
attachment_choice = None
attachment_first = None
message_choice = None
attachment_choice = None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
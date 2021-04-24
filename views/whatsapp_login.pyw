# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'whatsapp_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, image_path):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 520))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 520))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 974, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progress_vertical_layout = QtWidgets.QVBoxLayout()
        self.progress_vertical_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.progress_vertical_layout.setContentsMargins(10, 20, 10, 30)
        self.progress_vertical_layout.setSpacing(30)
        self.progress_vertical_layout.setObjectName("progress_vertical_layout")
        self.setup_progress = QtWidgets.QProgressBar(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setup_progress.sizePolicy().hasHeightForWidth())
        self.setup_progress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(10)
        self.setup_progress.setFont(font)
        self.setup_progress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setup_progress.setAutoFillBackground(True)
        self.setup_progress.setStyleSheet("")
        self.setup_progress.setProperty("value", 24)
        self.setup_progress.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.setup_progress.setTextVisible(False)
        self.setup_progress.setObjectName("setup_progress")
        self.progress_vertical_layout.addWidget(self.setup_progress)
        self.login_to_whatsapp_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_to_whatsapp_label.sizePolicy().hasHeightForWidth())
        self.login_to_whatsapp_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.login_to_whatsapp_label.setFont(font)
        self.login_to_whatsapp_label.setStyleSheet("background-color: #FFC426;\n"
"border-width: 5px 5px 5px 0px;\n"
"border-style: solid;\n"
"border-color: #FFC426;")
        self.login_to_whatsapp_label.setScaledContents(True)
        self.login_to_whatsapp_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.login_to_whatsapp_label.setObjectName("login_to_whatsapp_label")
        self.progress_vertical_layout.addWidget(self.login_to_whatsapp_label)
        self.import_contact_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_contact_label.sizePolicy().hasHeightForWidth())
        self.import_contact_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.import_contact_label.setFont(font)
        self.import_contact_label.setScaledContents(True)
        self.import_contact_label.setObjectName("import_contact_label")
        self.progress_vertical_layout.addWidget(self.import_contact_label)
        self.type_your_message_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_your_message_label.sizePolicy().hasHeightForWidth())
        self.type_your_message_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.type_your_message_label.setFont(font)
        self.type_your_message_label.setScaledContents(True)
        self.type_your_message_label.setObjectName("type_your_message_label")
        self.progress_vertical_layout.addWidget(self.type_your_message_label)
        self.attachment_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attachment_label.sizePolicy().hasHeightForWidth())
        self.attachment_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.attachment_label.setFont(font)
        self.attachment_label.setScaledContents(True)
        self.attachment_label.setObjectName("attachment_label")
        self.progress_vertical_layout.addWidget(self.attachment_label)
        self.finalize_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finalize_label.sizePolicy().hasHeightForWidth())
        self.finalize_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.finalize_label.setFont(font)
        self.finalize_label.setScaledContents(True)
        self.finalize_label.setObjectName("finalize_label")
        self.progress_vertical_layout.addWidget(self.finalize_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.progress_vertical_layout.addItem(spacerItem)
        self.instruction_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        self.instruction_label.setFont(font)
        self.instruction_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.instruction_label.setScaledContents(True)
        self.instruction_label.setOpenExternalLinks(True)
        self.instruction_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.instruction_label.setObjectName("instruction_label")
        self.progress_vertical_layout.addWidget(self.instruction_label)
        self.horizontalLayout.addLayout(self.progress_vertical_layout)
        spacerItem1 = QtWidgets.QSpacerItem(130, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.main_vertical_layout = QtWidgets.QVBoxLayout()
        self.main_vertical_layout.setContentsMargins(-1, 0, -1, -1)
        self.main_vertical_layout.setSpacing(0)
        self.main_vertical_layout.setObjectName("main_vertical_layout")
        self.main_layout = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_layout.sizePolicy().hasHeightForWidth())
        self.main_layout.setSizePolicy(sizePolicy)
        self.main_layout.setObjectName("main_layout")
        self.gridLayout = QtWidgets.QGridLayout(self.main_layout)
        self.gridLayout.setObjectName("gridLayout")
        self.whatsapp_image = QtWidgets.QLabel(self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whatsapp_image.sizePolicy().hasHeightForWidth())
        self.whatsapp_image.setSizePolicy(sizePolicy)
        self.whatsapp_image.setText("")
        self.whatsapp_image.setPixmap(QtGui.QPixmap(image_path))
        self.whatsapp_image.setScaledContents(False)
        self.whatsapp_image.setAlignment(QtCore.Qt.AlignCenter)
        self.whatsapp_image.setWordWrap(True)
        self.whatsapp_image.setOpenExternalLinks(False)
        self.whatsapp_image.setObjectName("whatsapp_image")
        self.gridLayout.addWidget(self.whatsapp_image, 0, 0, 1, 1)
        self.whatspp_login_button = QtWidgets.QPushButton(self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whatspp_login_button.sizePolicy().hasHeightForWidth())
        self.whatspp_login_button.setSizePolicy(sizePolicy)
        self.whatspp_login_button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(32)
        self.whatspp_login_button.setFont(font)
        self.whatspp_login_button.setStyleSheet("background-color:\"#076FD9\";\n"
"color:\"#FFFFFF\";")
        self.whatspp_login_button.setAutoDefault(False)
        self.whatspp_login_button.setDefault(False)
        self.whatspp_login_button.setFlat(False)
        self.whatspp_login_button.setObjectName("whatspp_login_button")
        self.gridLayout.addWidget(self.whatspp_login_button, 1, 0, 1, 1)
        self.whatsapp_status_label = QtWidgets.QLabel(self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whatsapp_status_label.sizePolicy().hasHeightForWidth())
        self.whatsapp_status_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.whatsapp_status_label.setFont(font)
        self.whatsapp_status_label.setScaledContents(True)
        self.whatsapp_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.whatsapp_status_label.setObjectName("whatsapp_status_label")
        self.gridLayout.addWidget(self.whatsapp_status_label, 2, 0, 1, 1)
        self.main_vertical_layout.addWidget(self.main_layout)
        self.base_bar = QtWidgets.QHBoxLayout()
        self.base_bar.setContentsMargins(430, 15, 20, 10)
        self.base_bar.setSpacing(30)
        self.base_bar.setObjectName("base_bar")
        spacerItem2 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.base_bar.addItem(spacerItem2)
        self.next_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(14)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("background-color:\"#112288\";\n"
"color:\"#FFFFFF\";")
        self.next_button.setObjectName("next_button")
        self.base_bar.addWidget(self.next_button)
        self.main_vertical_layout.addLayout(self.base_bar)
        self.main_vertical_layout.setStretch(0, 50)
        self.horizontalLayout.addLayout(self.main_vertical_layout)
        self.horizontalLayout.setStretch(2, 30)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_to_whatsapp_label.setText(_translate("MainWindow", "Login to WhatsApp"))
        self.import_contact_label.setText(_translate("MainWindow", "Import Contacts"))
        self.type_your_message_label.setText(_translate("MainWindow", "Type your Message"))
        self.attachment_label.setText(_translate("MainWindow", "Attachment"))
        self.finalize_label.setText(_translate("MainWindow", "Finalize and Review"))
        self.instruction_label.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.pcenthusiast.tech/post/how-to-use-our-whatsapp-message-blaster\"><span style=\" text-decoration: underline; color:#0000ff;\">Instruction Manual</span></a></p></body></html>"))
        self.whatspp_login_button.setText(_translate("MainWindow", "\n"
"Connect WhatsApp account\n"
""))
        self.whatsapp_status_label.setText(_translate("MainWindow", "You are not logged in to WhatsApp"))
        self.next_button.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

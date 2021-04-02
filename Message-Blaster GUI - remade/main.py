# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-20, 2, 261, 506))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.progress_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.progress_vertical_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.progress_vertical_layout.setContentsMargins(30, 20, 0, 30)
        self.progress_vertical_layout.setSpacing(30)
        self.progress_vertical_layout.setObjectName("progress_vertical_layout")
        self.setup_progress = QtWidgets.QProgressBar(self.verticalLayoutWidget)
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
        self.setup_progress.setProperty("value", 24)
        self.setup_progress.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.setup_progress.setTextVisible(False)
        self.setup_progress.setObjectName("setup_progress")
        self.progress_vertical_layout.addWidget(self.setup_progress)
        self.login_to_whatsapp_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
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
        self.login_to_whatsapp_label.setObjectName("login_to_whatsapp_label")
        self.progress_vertical_layout.addWidget(self.login_to_whatsapp_label)
        self.import_contact_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_contact_label.sizePolicy().hasHeightForWidth())
        self.import_contact_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.import_contact_label.setFont(font)
        self.import_contact_label.setObjectName("import_contact_label")
        self.progress_vertical_layout.addWidget(self.import_contact_label)
        self.type_your_message_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_your_message_label.sizePolicy().hasHeightForWidth())
        self.type_your_message_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.type_your_message_label.setFont(font)
        self.type_your_message_label.setObjectName("type_your_message_label")
        self.progress_vertical_layout.addWidget(self.type_your_message_label)
        self.attachment_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attachment_label.sizePolicy().hasHeightForWidth())
        self.attachment_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.attachment_label.setFont(font)
        self.attachment_label.setObjectName("attachment_label")
        self.progress_vertical_layout.addWidget(self.attachment_label)
        self.finalize_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finalize_label.sizePolicy().hasHeightForWidth())
        self.finalize_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(18)
        self.finalize_label.setFont(font)
        self.finalize_label.setObjectName("finalize_label")
        self.progress_vertical_layout.addWidget(self.finalize_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.progress_vertical_layout.addItem(spacerItem)
        self.instruction_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        self.instruction_label.setFont(font)
        self.instruction_label.setObjectName("instruction_label")
        self.progress_vertical_layout.addWidget(self.instruction_label)
        self.whatsapp_container = QtWidgets.QGroupBox(self.centralwidget)
        self.whatsapp_container.setEnabled(True)
        self.whatsapp_container.setGeometry(QtCore.QRect(250, 0, 701, 451))
        self.whatsapp_container.setStyleSheet("")
        self.whatsapp_container.setTitle("")
        self.whatsapp_container.setObjectName("whatsapp_container")
        self.login_whatsapp_button = QtWidgets.QPushButton(self.whatsapp_container)
        self.login_whatsapp_button.setGeometry(QtCore.QRect(100, 180, 500, 130))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(32)
        self.login_whatsapp_button.setFont(font)
        self.login_whatsapp_button.setObjectName("login_whatsapp_button")
        self.login_status_label = QtWidgets.QLabel(self.whatsapp_container)
        self.login_status_label.setGeometry(QtCore.QRect(164, 350, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(16)
        self.login_status_label.setFont(font)
        self.login_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_status_label.setObjectName("login_status_label")
        self.label = QtWidgets.QLabel(self.whatsapp_container)
        self.label.setGeometry(QtCore.QRect(160, 50, 391, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logos/whatsapp/WhatsApp_Logo_5/WhatsApp_Logo_5 - Copy.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 450, 701, 59))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.base_bar = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.base_bar.setContentsMargins(430, 15, 20, 10)
        self.base_bar.setSpacing(30)
        self.base_bar.setObjectName("base_bar")
        self.back_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(14)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.base_bar.addWidget(self.back_button)
        self.next_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(14)
        self.next_button.setFont(font)
        self.next_button.setObjectName("next_button")
        self.base_bar.addWidget(self.next_button)
        self.import_contacts_container = QtWidgets.QGroupBox(self.centralwidget)
        self.import_contacts_container.setGeometry(QtCore.QRect(249, -1, 701, 451))
        self.import_contacts_container.setTitle("")
        self.import_contacts_container.setObjectName("import_contacts_container")
        self.import_contacts_button = QtWidgets.QPushButton(self.import_contacts_container)
        self.import_contacts_button.setGeometry(QtCore.QRect(100, 180, 500, 130))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(32)
        self.import_contacts_button.setFont(font)
        self.import_contacts_button.setObjectName("import_contacts_button")
        self.import_contacts_status_label = QtWidgets.QLabel(self.import_contacts_container)
        self.import_contacts_status_label.setGeometry(QtCore.QRect(164, 350, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(16)
        self.import_contacts_status_label.setFont(font)
        self.import_contacts_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.import_contacts_status_label.setObjectName("import_contacts_status_label")
        self.excel_image = QtWidgets.QLabel(self.import_contacts_container)
        self.excel_image.setGeometry(QtCore.QRect(164, 49, 391, 111))
        self.excel_image.setText("")
        self.excel_image.setPixmap(QtGui.QPixmap("logos/excel.png"))
        self.excel_image.setScaledContents(True)
        self.excel_image.setObjectName("excel_image")
        self.message_container = QtWidgets.QGroupBox(self.centralwidget)
        self.message_container.setGeometry(QtCore.QRect(249, -1, 701, 451))
        self.message_container.setTitle("")
        self.message_container.setObjectName("message_container")
        self.scrollArea = QtWidgets.QScrollArea(self.message_container)
        self.scrollArea.setGeometry(QtCore.QRect(19, 19, 671, 421))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidget = QtWidgets.QWidget()
        self.scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 669, 419))
        self.scrollAreaWidget.setObjectName("scrollAreaWidget")
        self.message_input_textbox = QtWidgets.QTextEdit(self.scrollAreaWidget)
        self.message_input_textbox.setGeometry(QtCore.QRect(-1, -1, 672, 422))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        self.message_input_textbox.setFont(font)
        self.message_input_textbox.setObjectName("message_input_textbox")
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.attachment_container = QtWidgets.QGroupBox(self.centralwidget)
        self.attachment_container.setGeometry(QtCore.QRect(249, -1, 701, 451))
        self.attachment_container.setTitle("")
        self.attachment_container.setObjectName("attachment_container")
        self.add_attachment_button = QtWidgets.QPushButton(self.attachment_container)
        self.add_attachment_button.setGeometry(QtCore.QRect(100, 140, 500, 130))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(32)
        self.add_attachment_button.setFont(font)
        self.add_attachment_button.setObjectName("add_attachment_button")
        self.attachment_status_label = QtWidgets.QLabel(self.attachment_container)
        self.attachment_status_label.setGeometry(QtCore.QRect(160, 350, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(16)
        self.attachment_status_label.setFont(font)
        self.attachment_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attachment_status_label.setObjectName("attachment_status_label")
        self.supported_formats_label = QtWidgets.QLabel(self.attachment_container)
        self.supported_formats_label.setGeometry(QtCore.QRect(30, 360, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(10)
        self.supported_formats_label.setFont(font)
        self.supported_formats_label.setObjectName("supported_formats_label")
        self.music_image = QtWidgets.QLabel(self.attachment_container)
        self.music_image.setGeometry(QtCore.QRect(50, 30, 81, 81))
        self.music_image.setText("")
        self.music_image.setPixmap(QtGui.QPixmap("logos/Music.png"))
        self.music_image.setScaledContents(True)
        self.music_image.setObjectName("music_image")
        self.video_image = QtWidgets.QLabel(self.attachment_container)
        self.video_image.setGeometry(QtCore.QRect(180, 30, 81, 81))
        self.video_image.setText("")
        self.video_image.setPixmap(QtGui.QPixmap("logos/Video.png"))
        self.video_image.setScaledContents(True)
        self.video_image.setObjectName("video_image")
        self.text_image = QtWidgets.QLabel(self.attachment_container)
        self.text_image.setGeometry(QtCore.QRect(310, 30, 81, 81))
        self.text_image.setText("")
        self.text_image.setPixmap(QtGui.QPixmap("logos/Text.png"))
        self.text_image.setScaledContents(True)
        self.text_image.setObjectName("text_image")
        self.picture_image = QtWidgets.QLabel(self.attachment_container)
        self.picture_image.setGeometry(QtCore.QRect(440, 30, 81, 81))
        self.picture_image.setText("")
        self.picture_image.setPixmap(QtGui.QPixmap("logos/Image.png"))
        self.picture_image.setScaledContents(True)
        self.picture_image.setObjectName("picture_image")
        self.zip_image = QtWidgets.QLabel(self.attachment_container)
        self.zip_image.setGeometry(QtCore.QRect(550, 30, 91, 81))
        self.zip_image.setText("")
        self.zip_image.setPixmap(QtGui.QPixmap("logos/zip.png"))
        self.zip_image.setScaledContents(True)
        self.zip_image.setObjectName("zip_image")
        self.finalize_container = QtWidgets.QGroupBox(self.centralwidget)
        self.finalize_container.setGeometry(QtCore.QRect(249, -1, 701, 451))
        self.finalize_container.setTitle("")
        self.finalize_container.setObjectName("finalize_container")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.finalize_container)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 922, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.customized_summary = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.customized_summary.setContentsMargins(16, 0, 8, 0)
        self.customized_summary.setSpacing(16)
        self.customized_summary.setObjectName("customized_summary")
        self.customized_login_name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customized_login_name.sizePolicy().hasHeightForWidth())
        self.customized_login_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(22)
        self.customized_login_name.setFont(font)
        self.customized_login_name.setText("")
        self.customized_login_name.setObjectName("customized_login_name")
        self.customized_summary.addWidget(self.customized_login_name)
        self.customized_contacts_file = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customized_contacts_file.sizePolicy().hasHeightForWidth())
        self.customized_contacts_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(22)
        self.customized_contacts_file.setFont(font)
        self.customized_contacts_file.setText("")
        self.customized_contacts_file.setObjectName("customized_contacts_file")
        self.customized_summary.addWidget(self.customized_contacts_file)
        self.customized_message = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customized_message.sizePolicy().hasHeightForWidth())
        self.customized_message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(22)
        self.customized_message.setFont(font)
        self.customized_message.setObjectName("customized_message")
        self.customized_summary.addWidget(self.customized_message)
        self.customized_attachment_name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customized_attachment_name.sizePolicy().hasHeightForWidth())
        self.customized_attachment_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(22)
        self.customized_attachment_name.setFont(font)
        self.customized_attachment_name.setText("")
        self.customized_attachment_name.setObjectName("customized_attachment_name")
        self.customized_summary.addWidget(self.customized_attachment_name)
        self.send_button = QtWidgets.QPushButton(self.finalize_container)
        self.send_button.setGeometry(QtCore.QRect(100, 290, 500, 130))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(32)
        self.send_button.setFont(font)
        self.send_button.setObjectName("send_button")
        self.verticalLayoutWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.whatsapp_container.raise_()
        self.import_contacts_container.raise_()
        self.message_container.raise_()
        self.attachment_container.raise_()
        self.finalize_container.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.login_whatsapp_button.setText(_translate("MainWindow", "Connect WhatsApp Account"))
        self.login_status_label.setText(_translate("MainWindow", "You are not currently logged in to WhatsApp"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.import_contacts_button.setText(_translate("MainWindow", "Import Excel file with Contacts"))
        self.import_contacts_status_label.setText(_translate("MainWindow", "Excel file currently not imported"))
        self.add_attachment_button.setText(_translate("MainWindow", "Add your Attachment file"))
        self.attachment_status_label.setText(_translate("MainWindow", "Attachment not added"))
        self.supported_formats_label.setText(_translate("MainWindow", "Supported formats:\n"
"jpg, gif, png\n"
"mp3, mp4, avi, zip\n"
"pdf, doc, docx, ppt, pptx\n"
"xlsb, xlsx"))
        self.customized_message.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.send_button.setText(_translate("MainWindow", "Send →"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

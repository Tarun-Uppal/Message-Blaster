import whatsapp
import excel_reader as excel
import os

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5 import QtWidgets

(contacts, numbers) = excel.read_file(os.path.dirname(__file__) + r'\Contacts.xlsx')

def dialog():
    whatsapp.sender(numbers, contacts, os.path.dirname(__file__) + r'\Sale.mp4', "Dear (name)(new_line)(new_line)Over 50+ international products on sale at reasonable prices, visit www.edutess.com/shop/ to buy now")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.showMaximized() 
    w.setWindowTitle('Whatsapp Message Blaster')

    btn = QPushButton(w)
    btn.setText('Start Sending Messages')
    btn.move(0,0)
    btn.setGeometry(0, 700, 1200, 50)
    btn.show()
    btn.clicked.connect(dialog)

    
    w.show()
    sys.exit(app.exec_())

# def main():
#     # whatsapp.whatsapp_reset()
#     # whatsapp.whatsapp_login()
#     (contacts, numbers) = excel.read_file(os.path.dirname(__file__) + r'\Contacts.xlsx')
#     whatsapp.sender(numbers, contacts, os.path.dirname(__file__) + r'\Sale.mp4', "Dear (name)(new_line)(new_line)Over 50+ international products on sale at reasonable prices, visit www.edutess.com/shop/ to buy now")
    
# main()
    

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit
from PyQt5 import QtWidgets

button_colour = "#005A82"
bkground_colour = "White"
button_2_color = "#00478C"
width = None
height = None
width_border = None
height_border = None



def main():
    global height_border, width, height, width_border
    app = QApplication(sys.argv)
    w = QWidget()
    w.showMaximized() 
    w.setStyleSheet("background-color:" + bkground_colour)
    w.setWindowTitle('Whatsapp Message Blaster')
    
    desktop = QtWidgets.QDesktopWidget().screenGeometry()
    height = desktop.height()
    width = desktop.width()
    height_border = (height / 100) * 5
    width_border = (width / 100) * 5

    login_to_whatsapp_button(w)
    excel_file_choser_button(w)
    excel_file_choser_button1(w)
    switch1(w)
    start_sending_messages_button(w)
    textbox(w, "YEllow", 100, 100, 100, 100)
    
    w.show()
    sys.exit(app.exec_())
    
def start_sending_messages_button(w):
    btn = QPushButton(w)
    btn.setText('Start Sending Messages')
    btn.setGeometry(int((width - width_border) / 2), int(height_border / 2), int((width - width_border) / 2), int((height - height_border) / 10))
    btn.setStyleSheet("background-color:"+button_colour)
    btn.show()
    btn.clicked.connect(start_sending_messages)
    
def login_to_whatsapp_button(w):
    btn = QPushButton(w)
    btn.setText('Login to whatsapp')
    btn.setGeometry(int(width_border / 2), int(height_border / 2), int((width - width_border) / 2), int((height - height_border) / 10))
    btn.setStyleSheet("background-color:"+button_colour)
    btn.show()
    btn.clicked.connect(login_to_whatsapp)
    
def excel_file_choser_button1(w):
    btn = QPushButton(w)
    btn.setText('Choose Excel File')
    btn.setGeometry(int(width_border / 2), int((height_border / 2) + ((height - height_border) / 10)), int((width - width_border) / 2), int((height - height_border) / 10))
    btn.setStyleSheet("background-color:"+button_colour)
    btn.show()
    btn.clicked.connect(excel_file_choser)

def excel_file_choser_button(w):
    btn = QLabel(w)
    btn.setText('INFOOOOOOOOOOOOOOOOOOOOOOOO')
    btn.setGeometry(500,500, int((width - width_border) / 2), int((height - height_border) / 10))
    btn.setStyleSheet("background-color:"+button_colour)
    btn.show()
    # btn.clicked.connect(excel_file_choser)
    
def switch1(w):
    button = QPushButton("Toggle", w) 
    button.setGeometry(200, 150, 100, 40) 
    button.setCheckable(True) 
    button.setStyleSheet("background-color:" + button_2_color) 
    button.show() 
    button.clicked.connect(switch) 
    if button.isChecked(): 
        button.setStyleSheet("background-color:" + button_colour) 
    else: 
        button.setStyleSheet("background-color:" + button_2_color) 
        
def textbox(w, text, x, y, size_x, size_y):
     textbox = QLineEdit(w)
     textbox.setGeometry(x, y, size_x, size_y)
     textbox.setText(text)
      
    
def switch(button):
    print("switch")
    
def excel_file_choser():
    print("excel_file_choser")

def login_to_whatsapp():
    print("login_to_whatsapp")
    
def start_sending_messages():
    print("start_sending_messages")
    
main()
    

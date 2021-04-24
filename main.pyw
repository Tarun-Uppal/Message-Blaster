# imports all the views
import views.whatsapp_login as whatsapp_login_view 
import views.import_contacts as import_contacts_view
import views.type_message as type_message_view 
import views.attachment as attachment_view
import views.finalize_review as finalize_review_view

# imports all the things required for pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets

# imports all the os functions
import os
# imports all the system functions
import sys

# imports all the the functions required by the gui
import gui_functions
# imports multithreading
import threading
# imports all the functiosn related to time
import time
sys_exit = False

# initializes a bunch of random varibles
current_window = 1
app = None
MainWindow = None
ui = None
progress = 0
attachment_gone = False
base_path = os.path.dirname(os.path.abspath(__file__))


def main(): 
    global app, MainWindow
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    use_views()
    
    app.aboutToQuit.connect(stuff)
    sys.exit(app.exec_())

def stuff():
    global sys_exit
    if gui_functions.login_status == True:
        thread = threading.Thread(target=gui_functions.whatsapp.whatsapp_reset)
        thread.start()
        
    sys_exit = True
    sys.exit()
    
def progress_bar_async():
    global ui, progress
    progress1 = 0
    if gui_functions.login_status == True:
        progress1 += 25
    if gui_functions.contacts_status == True:
        progress1 += 25
    if gui_functions.message != None:
        progress1 += 25
    if attachment_gone == True:
        progress1 += 25
        
    if progress <= progress1:
        progress = progress1
        ui.setup_progress.setValue(progress)
    
def use_views():
    global current_window, app, MainWindow, ui
    
    if current_window == 1:
        whatsapp_login()
    if current_window == 2:
        import_contacts()
    if current_window == 3:
        type_message()
        ui.type_message.setPlainText(gui_functions.message)
    if current_window == 4:
        attachment()
    if current_window == 5:
        finalize_review()
        
    progress_bar_async()
    MainWindow.show()
    
def whatsapp_login():
    global ui, app, MainWindow, base_path
    
    ui = whatsapp_login_view.Ui_MainWindow()
    ui.setupUi(MainWindow, resource_path('logos\Whatsapp.png'))  
    
    thread = threading.Thread(target=whatsapp_login_async)
    thread.start()
    
    ui.whatspp_login_button.clicked.connect(gui_functions.login_info)
    ui.next_button.clicked.connect(next_view)
    

def whatsapp_login_async():
    global ui, current_window, sys_exit
    
    while True:
        if current_window == 1:
            if gui_functions.login_status == True:
                ui.whatsapp_status_label.setText("You are logged in as " + gui_functions.user_name)
                progress_bar_async()
            elif gui_functions.login_status == False:
                ui.whatsapp_status_label.setText("You are not logged in to WhatsApp")
            time.sleep(0.001)
        elif sys_exit == True:
            return
        else:
            break
    progress_bar_async()
        
def import_contacts():
    global ui, app, MainWindow
    
    ui = import_contacts_view.Ui_MainWindow()
    ui.setupUi(MainWindow, resource_path('logos\excel.png'))
    
    thread = threading.Thread(target=import_contacts_async)
    thread.start()
    
    ui.import_contacts_button.clicked.connect(gui_functions.excel_button)    
    ui.next_button.clicked.connect(next_view)
    ui.back_button.clicked.connect(previous_view)
    
    
def import_contacts_async():
    global ui, current_window, sys_exit
    while True:
        if current_window == 2:
            if gui_functions.contacts_path != None:
                file = gui_functions.contacts_path.split('/')
                length = len(file) - 1
                ui.contacts_status_label.setText("Your contacts filename is " + file[length])
                progress_bar_async()
        elif sys_exit == True:
            return
        else:
            break
        time.sleep(0.001)
    
def type_message():
    global ui, app, MainWindow
    
    ui = type_message_view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    ui.next_button.clicked.connect(next_view)
    ui.back_button.clicked.connect(previous_view)
    
def attachment():
    global ui, app, MainWindow, attachment_gone, base_path
    
    ui = attachment_view.Ui_MainWindow()
    
    ui.setupUi(MainWindow, resource_path('logos\Image.png'), resource_path('logos\Music.png'), 
               resource_path('logos\Zip.png'), resource_path('logos\Video.png'), resource_path('logos\Text.png'))
    
    thread = threading.Thread(target=attachment_async)
    thread.start()
    attachment_gone = True
    ui.attachment_button.clicked.connect(gui_functions.attachment_button)
    ui.next_button.clicked.connect(next_view)
    ui.back_button.clicked.connect(previous_view)

def attachment_async():
    global ui, current_window, sys_exit
    
    while True:
        if current_window == 4:
            if gui_functions.attachment_path != None:
                file = gui_functions.attachment_path.split('/')
                length = len(file) - 1
                ui.attachment_status_label.setText("Your attachment filename is " + file[length])
                progress_bar_async()
        elif sys_exit == True:
            return
        else:
            break
        time.sleep(0.001)
        
        
def finalize_review():
    global ui, app, MainWindow
    
    ui = finalize_review_view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    if gui_functions.user_name != None:
        ui.finalize_login_label.setText("You are logged in to WhatsApp as \'" + gui_functions.user_name + "\'")
    
    if gui_functions.attachment_path != None:
        file = gui_functions.attachment_path.split('/')
        length = len(file) - 1
        ui.finalize_attachment_label.setText("Your attachment filename is \'" + file[length] + "\'")
    
    if gui_functions.message != None:
        ui.finalize_message_label.setText("Your message is \n" + gui_functions.message)
    
    if gui_functions.contacts_path != None:
        file = gui_functions.contacts_path.split('/')
        length = len(file) - 1
        ui.finalize_contacts_label.setText("Your contacts filename is \'" + file[length] + "\'")
        
    ui.start_sending_messages.clicked.connect(gui_functions.sender_button)
    ui.back_button.clicked.connect(previous_view)

def next_view():
    global current_window
    if current_window == 3:
        store_message()
        
    current_window += 1
    use_views()
    
    
def previous_view():
    global current_window
    if current_window == 3:
        store_message()
        
    current_window -= 1
    use_views()
    
def store_message():
    global ui
    if ui.type_message.toPlainText() != '':
        gui_functions.message = ui.type_message.toPlainText()
        progress_bar_async()
        
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

        
main()

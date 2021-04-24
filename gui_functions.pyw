# imports all the whatsapp message functions
import whatsapp

# imports all the os functions
import os

# imports the multithreading functions
import threading

import excel_reader as excel
# imports all the things required for pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

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
user_name = None

def login_info():
    global _translate, login_status
    
    thread = threading.Thread(target=login_whatsapp)
    thread.start()

def login_whatsapp():
    global _translate, login_status, user_name
    
    val = whatsapp.whatsapp_login_and_get_name()
    if val != False:
        login_status = True
        user_name = val
    else:
        login_status = False
        user_name = 'null'
        
        
def excel_button():
    global contacts_path, _translate, contacts_status
    
    while True:
        filename = QFileDialog.getOpenFileName()
        contacts_path1 = filename[0]
        if contacts_path1 != '':
            filename = contacts_path1.split('.')
            try:
                if filename[1] == 'xlsx' or filename[1] == 'xlsb':
                    val = excel.read_file(contacts_path1)
                    if val == None:
                        continue
                    else:
                        contacts_status = True
                        contacts_path = contacts_path1
                        break
            except IndexError:
                break
        else:
            break

def attachment_button():
    global attachment_path, _translate, attachment_status, attachment_choice  
    
    while True:
        filename = QFileDialog.getOpenFileName()
        try:
            attachment_path1 = filename[0]
            if attachment_path1 != '':
                extension = attachment_path1.split('.')[1]
                valid_extensions = ['xlsb', 'xlsx', 'doc', 'docx', 'ppt', 'pptx', 'pdf', 'jpeg', 'gif', 'png','mp3', 'mp4', 'avi', 'zip']
                if extension.lower() in valid_extensions:
                    attachment_status = True
                    attachment_path = attachment_path1
                    break
            else:
                break
        except IndexError:
            break
            
def sender_button():
    global message, contacts_path, attachment_path, message_status, attachment_status, contacts_status, login_status
    global attachment_choice, message_choice, attachment_first, message_choice, attachment_choice

    attachment_first = True
    if message == None:
        message_choice = False
    else:
        message_choice = True
        
    if attachment_path == None:
        attachment_choice = False
    else:
        attachment_choice = True
    
    if contacts_status == True and login_status == True:
        thread = threading.Thread(target=send_message)
        thread.start()
	    
def send_message():
    global message, contacts_path, attachment_path, message_status, attachment_status, contacts_status, login_status
    global attachment_choice, message_choice, attachment_first, message_choice, attachment_choice
    
    (contacts, numbers) = excel.read_file(contacts_path)
    whatsapp.sender(numbers, contacts, attachment_path, message, attachment_first)

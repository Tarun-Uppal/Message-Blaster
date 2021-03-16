import whatsapp
import excel_reader as excel
import os

def main():
    # whatsapp.whatsapp_reset()
    # whatsapp.whatsapp_login()
    (contacts, numbers) = excel.read_file(os.path.dirname(__file__) + r'\Contacts.xlsx')
    whatsapp.sender(numbers, contacts, os.path.dirname(__file__) + r'\Sale.mp4')
    
main()
    

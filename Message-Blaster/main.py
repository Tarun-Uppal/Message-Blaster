import whatsapp
import excel_reader as excel
import os

def main():
    # whatsapp.whatsapp_reset()
    # whatsapp.whatsapp_login()
    (contacts, numbers) = excel.read_file(os.path.dirname(__file__) + r'\Contacts.xlsx')
    whatsapp.sender(numbers, contacts, os.path.dirname(__file__) + r'\Sale.mp4', "Dear (name)(new_line)(new_line)Over " 
                    + "50+ international products on sale at reasonable prices, visit www.edutess.com/shop/ to buy now", 
                    False)
    
main()

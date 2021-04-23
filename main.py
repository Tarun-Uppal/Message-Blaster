import whatsapp
import excel_reader as excel
import os

def main():
    while True:
        var1 = whatsapp.whatsapp_login_and_get_name()
        var1 = True
        var = excel.read_file(os.path.dirname(__file__) + r'\Contacts.xlsx')
        if var == None or var1 == False:
            continue
        else:
            (contacts, numbers) = var
            whatsapp.sender(numbers, contacts,  os.path.dirname(__file__) + r'\Contacts.xlsx', "Wassup {name}", False)
            break
        break
    
main()

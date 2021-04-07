import whatsapp
import excel_reader as excel
import os

def main():
    while True:
        # whatsapp.whatsapp_reset()
        # var1 = whatsapp.whatsapp_login()
        var1 = True
        var = excel.read_file(os.path.dirname(__file__) + r'\Contacts.xlsx')
        if var == None or var1 == False:
            continue
        else:
            (contacts, numbers) = var
            whatsapp.sender(numbers, contacts, True,  os.path.dirname(__file__) + r'\Sale.mp4', True, 
                            "Dear (name)(new line)(new line)Over 50+ international products on sale at reasonable"
                            + " prices, visit www.edutess.com/shop/ to buy now", 
                            False)
            break
        # print(whatsapp.get_user_name())
        # whatsapp.whatsapp_reset()
        break
    # whatsapp.whatsapp_reset()
    
main()

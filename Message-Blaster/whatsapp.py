# imports all the things that could happen
from selenium.webdriver.support import expected_conditions as EC
# gets all the actions that the bot can do
from selenium.webdriver.common.action_chains import ActionChains  
# the webdriver wait
from selenium.webdriver.support.ui import WebDriverWait
# imports the options
from selenium.webdriver.chrome.options import Options
# imports the options for selenium
from selenium.common import exceptions 
# imports the keyboard and text part of selenium
from selenium.webdriver.common.keys import Keys 
# imports the webdriver 
from selenium import webdriver  
# imports os for the directory management
import os
# random imports
import re
# imports time
import time
# imports selenium
import selenium


# chrome path driver
chrome_path = os.path.dirname(__file__) + r'\chromedriver.exe'
# link for whatsapp web
Link = "https://web.whatsapp.com/"
# stores the browser
browser = None

# send messages and attachments
def sender(numbers, contacts, attachment_path, message1, first_attachment):
    """
    sends the contacts the message
    """
    message1 = message1.replace('(new line)', '\n')
    # the number of numbers to send the message to
    numbers_size = len(numbers)
    # sets the starting point
    i = 0   
    # makes a loop
    while True: 
        # gets the phone number form the database  
        number = numbers[i]
        # checks if the number is invaild
        if isValid(910000000000+number == False) or len(str(number)) != 10:
            print(number)
        # otherwise
        else:
            open_whatsapp()
            # generates the personalized message
            message = message1.replace('(name)', contacts[i])
            # generates the link
            link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(910000000000+number)
            # sends the generated link to the browser
            browser.get(link)
            if first_attachment == True:
                # sends the attachment
                send_attachment(attachment_path)
                # sends the message
                send_message(message)
            else:
                # sends the message
                send_message(message)
                # sends the attachment
                send_attachment(attachment_path)
            # waits for 1 second
            time.sleep(1)
            # exits the browser
            browser.quit()
            
        # checks if the array is over
        if i == numbers_size - 1:
            break
        # increments
        i += 1
        
def send_message(message):
    while True:
        try:
            # trys to find the browser box message
            input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            # goes through all the letters in the message
            for ch in message:
                # if the char is a new line then adds a new line
                if ch == "\n":
                    ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    # otherwise it sends the letters to the the textbox
                    input_box.send_keys(ch)
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
        # except Exception as e:
        #     print("Failed to send message exception: ", e)
        #     return
    # once the message is over it sends it
    input_box.send_keys(Keys.ENTER)
    print("Message sent successfully")
    

def send_attachment(file_path):
    global wait, browser, selenium, exceptions
    while True:
        try:
            attachment_box = browser.find_element_by_xpath('//div[@title = "Attach"]')
            attachment_box.click()
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
        except selenium.common.exceptions.UnexpectedAlertPresentException as e:
            continue
    while True:
        try:
            image_box = browser.find_element_by_xpath(
                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys(file_path)
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
            
    # action = ActionChains(browser) 
    while True:
        try:
            image_box = browser.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div')
            image_box.click()
            # ActionChains(browser).click(image_box).perform()
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
        except selenium.common.exceptions.ElementNotInteractableException as e:
            continue
    time.sleep(1)
    print("File sent")
    
def open_whatsapp():
    """
    logs into whatsapp
    """
    global wait, browser
    chrome_options = Options() 
    chrome_options.add_argument('--user-data-dir=' + os.path.dirname(__file__) + r'\Whatsapp_Data')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 60)
    
def whatsapp_login():
    """
    logs into whatsapp
    """
    global wait, browser
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=' + os.path.dirname(__file__) + r'\Whatsapp_Data')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 60)
    browser.get(Link)
    browser.maximize_window()
    while True:
        try:
            stuff = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span')
            browser.quit()
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
            
def whatsapp_reset():
    global wait, browser
    chrome_options = Options()
    chrome_options.add_argument("headless")
    chrome_options.add_argument('--user-data-dir=' + os.path.dirname(__file__) + r'\Whatsapp_Data')
    browser = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    wait = WebDriverWait(browser, 60)
    browser.get(Link)
    browser.maximize_window()
    while True:
        try:
            options = browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]')
            options.click()
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
        
    while True:
        try:
            options = browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[7]')
            options.click()
            break
        except exceptions.NoSuchElementException as e:
            time.sleep(1)
            
    browser.quit()
    
def isValid(s):
    """
    validates the number
    """
    # casts the number into a string
    s = str(s)
    # stores the pattern
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    # validates the pattern and returns thue if it is valid otherwise false
    if (Pattern.match(s)) and len(s) == 12: 
        return True
    else:
        return False

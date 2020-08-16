from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import datetime
from connectToSql import *

# https://stackoverflow.com/questions/51933480/how-to-send-media-files-on-whatsapp-programmatically-using-click-to-chat-feature/51935096
# https://stackoverflow.com/questions/49831933/eliminate-entering-qr-whatsapp-web-automated-by-selenium-java
contact_example = "אמא"
text = "Hey, this message was sent using Selenium"
path_to_chromedriver = os.path.join(os.getcwd(), "chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=data")

driver = webdriver.Chrome(executable_path=path_to_chromedriver, options=options)
# driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
# input()
print("Logged In")
# inp_xpath_search = "//div[@title='Search or start new chat']"
# input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
# input_box_search.click()
INPUT = {
    'צרף אותי': 'רישום',
}


_SELECTORS = {
        'firstrun': "#wrapper",
        'qrCode': "img[alt=\"Scan me!\"]",
        'qrCodePlain': "div[data-ref]",
        'mainPage': ".app.two",
        'chatList': ".infinite-list-viewport",
        'messageList': "#main > div > div:nth-child(1) > div > div.message-list",  # didn't work
        'message-in': "div.message-in",  #"#main > div > div:nth-child(1) > div > div>div.message-in"
        'message-all': "div > span.selectable-text",
        'unreadMessageBar': "#main > div > div:nth-child(1) > div > div.message-list > div.msg-unread",
        'searchBar': ".input",
        'searchCancel': ".icon-search-morph",
        'chats': ".infinite-list-item",
        'chatBar': 'div.input',
        'sendButton': 'button.icon:nth-child(3)',
        'LoadHistory': '.btn-more',
        'UnreadBadge': '.icon-meta',
        'UnreadChatBanner': '.message-list',
        'ReconnectLink': '.action',
        'WhatsappQrIcon': 'span.icon:nth-child(2)',
        'QRReloader': 'div[data-ref] > span > div'
    }


def get_contact():
    time.sleep(5)
    try:
        # input_box = driver.find_element_by_class_name("_3FRCZ copyable-text selectable-text")
        input_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    except:
        input_box = driver.find_element_by_xpath("//div[text()='Search or start new chat']")
    input_box.click()
    time.sleep(2)
    return input_box


def pick_contact(input_box, contact_name):
    input_box.send_keys(contact_name)
    time.sleep(2)
    input_box.send_keys(Keys.ENTER)
    time.sleep(2)


def click_on_send_file_button():
    sending_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    sending_box.click()
    time.sleep(2)


def send_file():  # only after click_on_send_file_button
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    driver.find_element_by_css_selector("input[type='file']").send_keys(os.path.join(os.getcwd(), "sms.jpeg"))
    time.sleep(1)
    driver.find_element_by_css_selector("span[data-icon='send']").click()
    time.sleep(2)


def send_message(answer):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').click()
    for line in answer.split('\n'):
        ActionChains(driver).send_keys(line).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    ActionChains(driver).send_keys(Keys.RETURN).perform()


def send_text(text):
    sending_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    sending_box.click()
    sending_box.send_keys(Keys.ENTER)
    sending_box.send_keys(text)
    time.sleep(2)
    sending_box.send_keys(Keys.ENTER)


def get_contacts():
    path = '//*[@id="pane-side"]'
    contact_path = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span'
    time.sleep(5)
    print(driver.find_element_by_xpath(contact_path).text)
    for person in driver.find_elements_by_class_name('_3ko75 _5h6Y_ _3Whw5'):
        print(person.text)

    for person in driver.find_elements_by_xpath(contact_path):
        # title = person.find_element_by_xpath('div/div/div/div/div/div')
        # company = person.find_element_by_xpath('.//div[@class="company"]/a').text
        print(person.get_attribute('innerHTML'))
        print(person.text)


def find_all_unread():
    time.sleep(6)
    contact_object = get_contact()
    pick_contact(contact_object, contact_example)
    # content = driver.find_element_by_css_selector('.chat.unread')
    # content.click()
    # input_form = driver.find_element_by_css_selector('.pluggable-input-placeholder')
    # input_form.send_keys(str(datetime.now()), Keys.RETURN)
    for content in driver.find_elements_by_css_selector(_SELECTORS['message-in']):
        print(content.find_element_by_css_selector(_SELECTORS['message-all']).text)
        print(content.get_attribute('innerHTML'))


def get_last_message_of_contact_object_by_click(contact_object):
    contact_object.click()
    time.sleep(2)
    return driver.find_elements_by_css_selector(_SELECTORS['message-in'])[-1].text


def get_last_message_of_contact_object_after_click():
    time.sleep(2)
    # in_messages = driver.find_elements_by_css_selector(_SELECTORS['message-in'])
    in_messages = driver.find_elements_by_css_selector("div[class*='message-in']")
    print("in_messages: ", in_messages)
    count = 0
    while len(in_messages) == 0:
        if count >= 20:
            break
        time.sleep(1)
        count += 1
        in_messages = driver.find_elements_by_css_selector("div[class='_2hqOq message-in focusable-list-item']")
        if len(in_messages) > 0:
            break
        else:
            print("waiting for file to download...")
    return in_messages[-1].text



def return_list_of_unread_contacts():
    # https://www.softwaretestinghelp.com/css-selector-selenium-locator-selenium-tutorial-6/
    # find by substring in css selector
    unread = []
    time.sleep(3)
    for elem in driver.find_elements_by_css_selector("span[aria-label*='unread messages']"):
        # print(elem.get_attribute('innerHTML'))
        # elem.click()
        unread.append(elem)
    # unread.append(driver.find_elements_by_css_selector("span[aria-label*='unread messages']"))
    print("len of unread contacts: ", len(unread))
    unread.append(driver.find_elements_by_css_selector("span[aria-label*='unread message']")[0])
    print("len of unread contacts: ", len(unread))
    return unread

#list_of_unread_contacts = return_list_of_unread_contacts()
#for con in list_of_unread_contacts:
#    con_message = get_last_message_of_contact_object_by_click(con)
#    print(con_message)

time.sleep(4)
input_box = get_contact()
time.sleep(2)
pick_contact(input_box, "שלמהxplace")
time.sleep(3)
text = get_reshum(INPUT["צרף אותי"])
send_message(text)
#last_message = get_last_message_of_contact_object_after_click()
#if 'צרף אותי' in last_message:
#    text = get_reshum(INPUT["צרף אותי"])
#    time.sleep(2)
#    send_text("*Greetings from ,%0a %0a M/s. me %0a %0a")
#else:
#    print("last message: ", last_message)

#driver.quit()
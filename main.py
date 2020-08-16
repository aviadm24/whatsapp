from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
# https://stackoverflow.com/questions/51933480/how-to-send-media-files-on-whatsapp-programmatically-using-click-to-chat-feature/51935096
# https://stackoverflow.com/questions/49831933/eliminate-entering-qr-whatsapp-web-automated-by-selenium-java
contact = "אמא"
text = "Hey, this message was sent using Selenium"
path_to_chromedriver = os.path.join(os.getcwd(), "chromedriver")

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=\data")

driver = webdriver.Chrome(executable_path=path_to_chromedriver, options=options)
# driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
# inp_xpath_search = "//div[@title='Search or start new chat']"
# input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
# input_box_search.click()
try:
    # input_box = driver.find_element_by_class_name("_3FRCZ copyable-text selectable-text")
    input_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
except:
    input_box = driver.find_element_by_xpath("//div[text()='Search or start new chat']")
input_box.click()
time.sleep(2)
input_box.send_keys(contact)
time.sleep(2)
input_box.send_keys(Keys.ENTER)
time.sleep(2)
print(input_box)
sending_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
sending_box.click()
time.sleep(2)

driver.find_element_by_css_selector("span[data-icon='clip']").click()
driver.find_element_by_css_selector("input[type='file']").send_keys(os.path.join(os.getcwd(), "sms.jpeg"))
time.sleep(1)
driver.find_element_by_css_selector("span[data-icon='send']").click()

time.sleep(2)
sending_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
sending_box.click()
sending_box.send_keys(Keys.ENTER)
sending_box.send_keys(text)
time.sleep(2)
sending_box.send_keys(Keys.ENTER)
# driver.quit()
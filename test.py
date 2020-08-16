from webwhatsapi import WhatsAPIDriver
#  https://stackoverflow.com/questions/29846087/microsoft-visual-c-14-0-is-required-unable-to-find-vcvarsall-bat#comment-91095944
# need virtualstudio setuptools for webwhatsapi
import os

# driver = WhatsAPIDriver(client="chrome", chrome_options=[])
path_to_driver = os.path.join(os.getcwd(), "geckodriver.exe")
driver = WhatsAPIDriver(exe)
chats = driver.get_all_chats()
print(chats)
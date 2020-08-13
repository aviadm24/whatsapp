from webwhatsapi import WhatsAPIDriver
import os
import time
path_to_geckodriver = os.path.join(os.getcwd(), "geckodriver")
driver = WhatsAPIDriver(extra_params={"executable_path": path_to_geckodriver})
# print(driver.get_unread())
time.sleep(7)
print(driver.get_all_chats())
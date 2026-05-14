import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(3)
driver.close()                          ## close command only close the current window(parent window)



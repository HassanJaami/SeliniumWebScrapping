import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Sending value to search
driver=webdriver.Chrome()
driver.get("https://www.python.org")

element=driver.find_element(By.XPATH, """//*[@id="id-search-field"]""")
print(element.get_attribute('type'))
# element.clear()
element.send_keys("Python_Tutorial")
element.send_keys(Keys.RETURN)
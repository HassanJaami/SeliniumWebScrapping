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

try:


    # Create a Chrome WebDriver with the service
    driver = webdriver.Chrome()

    # Navigate to the YouTube video URL
    url = ("https://foodtank.com/news/category/sustainable-agriculture/")
    driver.get(url)

    elems=driver.find_elements(By.CSS_SELECTOR, """.single_category_title""")
    print(len(elems))
    for i in elems:
        print(i.text)

    # ... do other actions on the page if needed ...

    # Close the WebDriver when done
    driver.quit()

except WebDriverException as e:
    print(f"An error occurred: {e}")








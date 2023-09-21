import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select












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








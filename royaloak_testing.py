# -*- coding: utf-8 -*-
"""


@author: shank
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.royaloakindia.com/"
driver.get(url)

time.sleep(3)

search_input_box = driver.find_element(By.XPATH, "//input[@placeholder='Enter Keyword or Item']")
search_input_box.send_keys("chair")
time.sleep(3)
search_input_box.send_keys(Keys.RETURN)
time.sleep(3)


product = driver.find_element(By.XPATH, "//a[normalize-space()='Royaloak Texas American Rocking Chair']")
product.click()
time.sleep(3)

add_cart = driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']")
add_cart.click()
time.sleep(5)

proceed_cart=driver.find_element(By.XPATH,  "//img[@src='https://www.royaloakindia.com/media/royaloakindia/images/shopping-cart.png']")
proceed_cart.click()
time.sleep(3)

proceed_cart1=driver.find_element(By.XPATH,  "//span[normalize-space()='View and Edit Cart']")
proceed_cart1.click()
time.sleep(10)

driver.quit()

from re import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

import time
import os

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

options = Options()
options.headless = True

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get('https://python.org')

driver.maximize_window()

search_input = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')
search_input.send_keys('django')

button_submit = driver.find_element(By.ID, 'submit')
button_submit.click()

driver.save_screenshot('python.org1.png')
driver.find_element(By.TAG_NAME, 'body').screenshot('python.org2.png')

func = lambda arg: driver.execute_script('return document.body.parentNode.scroll' + arg)

driver.set_window_size( func("Width"), func("Height") )
driver.find_element(By.TAG_NAME, 'body').screenshot('python.org3.png')

#time.sleep(5)
driver.quit()


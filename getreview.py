from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time
querys ="swift"

url = "https://www.cardekho.com/"
driver= webdriver.Firefox("C:/Users/arpan/Downloads/geckodriver-v0.32.2-win64")
   
def get_(querys,driver, delay,class_name, url=url,):
    # Finding the search box 
    driver.get(url)
    time.sleep(delay)
    box = driver.find_element(By.XPATH, '//*[@id="cardekhosearchtext"]')

    # Type the search query in the search box

    box.send_keys(querys)

    # Pressing enter
    box.send_keys(Keys.ENTER)
    time.sleep(delay)
    driver.execute_script('\
            window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(delay)
    box = driver.find_element(By.XPATH, '//*[@id="rf01"]/div[1]/div/nav/div[2]/div/ul/li[6]/a').click()
    time.sleep(delay)
image_urls =  get_(querys,driver, 20,"product-image-photo",url,)
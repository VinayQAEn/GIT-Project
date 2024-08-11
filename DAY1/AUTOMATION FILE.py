import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
os.getcwd()
location = "/Users/riyabakoria/PycharmProjects/pythonProject/Organic Automation"

def chrome_setup():
    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Chrome(options=ops)
    driver.implicitly_wait(10)
    return driver

def Safari_setup():
    preferences = {"download.default_directory":location}
    ops = webdriver.SafariOptions()
    ops.add_argument("prefs")
    driver = webdriver.Safari(options=ops)
    driver.implicitly_wait(10)
    return driver


def chrome_setup1():
    preferences = {"download.default_directory":"/Users/riyabakoria/PycharmProjects/pythonProject/Pack1","plugin.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=ops)
    return driver

# driver = chrome_setup()
# driver = Safari_setup()
driver = chrome_setup1()
driver.get("https://freetestdata.com/document-files/pdf/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='post-81']/div/div/section[3]/div/div[1]/div/section[1]/div/div[2]/div/div/div/div/a/span/span").click()
time.sleep(5)









































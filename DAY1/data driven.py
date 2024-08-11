import time

import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from DAY1 import XLutilities
from selenium import webdriver
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()
file = "/Users/riyabakoria/Downloads/Calculator.xlsx"

workbook = openpyxl.load_workbook(file)

sheet = workbook["Sheet1"]

Row = XLutilities.get_rowcount(file,"Sheet1")

for r in range(2,Row+1):
    principal = XLutilities.readdata(file,"Sheet1",r,1)
    Rateofinterest = XLutilities.readdata(file,"Sheet1",r,2)
    period1 = XLutilities.readdata(file,"Sheet1",r,3)
    period2 = XLutilities.readdata(file,"Sheet1",r,4)
    frequency = XLutilities.readdata(file,"Sheet1",r,5)
    Exp_maturity = XLutilities.readdata(file,"Sheet1",r,6)

    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principal)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(Rateofinterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(period1)
    period2_drp = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    period2_drp.select_by_visible_text(period2)
    frequency_drp = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequency_drp.select_by_visible_text(frequency)
    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    actual_maturity = driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text
    # Validation
    if float(Exp_maturity) == float(actual_maturity):
        XLutilities.writedata(file,"Sheet1",r,8,"PASSED")
        XLutilities.green_fill(file,"Sheet1",r,8)
    else:
        XLutilities.writedata(file,"Sheet1",r,8,"FAILED")
        XLutilities.red_fill(file,"Sheet1",r,8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()









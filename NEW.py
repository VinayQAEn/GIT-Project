import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='form-group']//input[@name='name']").send_keys("Kumar")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("kumar@gmail.com")
driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("12344565")
driver.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()
Gender_box = Select(driver.find_element(By.XPATH,"//select[@id='exampleFormControlSelect1']"))
Gender_box.select_by_visible_text("Male")
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[7]/input").send_keys("13/02/1998")
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

msg = driver.find_element(By.XPATH,"//strong[normalize-space()='Success!']").text

assert "Success" in msg
time.sleep(10)
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# try:
#     driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()
# except Exception as e:
#     print(f"Exception :{str(e)}")
# from DAY1 import XLutilities
# file = "/Users/riyabakoria/Downloads/Calculator.xlsx"
# row = XLutilities.get_rowcount(file,'Sheet1')
# for r in range(2,row+1):
#     pricipal =  XLutilities.readdata(file,"Sheet1",r,1)
#     rateofinterest = XLutilities.readdata(file,"Sheet1",r,2)
#     period1 = XLutilities.readdata(file,"Sheet1",r,3)
#     period2 = XLutilities.readdata(file,"Sheet1",r,4)
#     frequency = XLutilities.readdata(file,"Sheet1",r,5)
#     exp_maturity = XLutilities.readdata(file,"Sheet1",r,6)
#
#     driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pricipal)
#     driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofinterest)
#     driver.find_element(By.XPATH,"//input[@id='tenure'] ").send_keys(period1)
#     Period2_drp = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
#     Period2_drp.select_by_visible_text(period2)
#     Frequenct_drp = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
#     Frequenct_drp.select_by_visible_text(frequency)
#     driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
#     actual_maturity = driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text
#
#     if float(actual_maturity) == float(exp_maturity):
#         XLutilities.writedata(file,'Sheet1',r,8,"PASSED")
#         XLutilities.green_fill(file,"Sheet1",r,8)
#     else:
#         XLutilities.writedata(file, 'Sheet1', r, 8, "FAILED")
#         XLutilities.red_fill(file, "Sheet1", r, 8)
#     driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Vinay")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("kumar@gmail.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1233445678")
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("Mr John Smith. 132, My Street,"
                                                                      " Kingston, New York 12401.")
Male_radio = driver.find_element(By.XPATH, "//input[@id='male']")
Male_radio.click()
print(Male_radio.is_selected())
print(Male_radio.is_enabled())
print(Male_radio.is_displayed())
Female_radio = driver.find_element(By.XPATH, "//input[@id='female']")
Female_radio.click()
print(Female_radio.is_displayed())
print(Female_radio.is_enabled())
print(Female_radio.is_selected())
checkboxes = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and contains(@id,'day')]")
for i in range(len(checkboxes)):
    checkboxes[i].click()

for check in checkboxes:
    check.click()

for i in range(len(checkboxes) - 2, len(checkboxes)):
    checkboxes[i].click()

for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()

for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()


country_box = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
country_box.select_by_visible_text("India")

country_drp = country_box.options
for country in country_drp:
    if country.text == "United States":
        country.click()
colors_box = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))
colors_box.select_by_visible_text("Green")

color_drp = colors_box.options
for color in color_drp:
    if color.text == "Green":
        color.click()

Date_box = driver.find_element(By.XPATH, "//input[@id='datepicker']")
Date_box.click()
year = "1996"
month = "January"
date = "30"

while True:
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    mn = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    if yr == year and mn == month:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

Dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for Date in Dates:
    if Date.text == date:
        Date.click()

opencart_link = driver.find_element(By.XPATH, "//a[normalize-space()='open cart']")
opencart_link.click()
print(driver.title)
driver.back()
driver.refresh()
orangehrm_link = driver.find_element(By.XPATH, "//a[normalize-space()='orange HRM']")
orangehrm_link.click()
print(driver.title)
driver.back()
driver.refresh()
Home_link = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
Home_link.click()
print(driver.title)
postatom_link = driver.find_element(By.XPATH, "//a[normalize-space()='Posts (Atom)']")
postatom_link.click()
WindowsIDS = driver.window_handles
parent_id = WindowsIDS[0]
child_id = WindowsIDS[1]
driver.switch_to.window(parent_id)
print(driver.title)
NoofRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
Noofcoulumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))
print(NoofRows)
print(Noofcoulumns)

Data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(Data)


for r in range(2, NoofRows + 1):
    for c in range(1, Noofcoulumns + 1):
        Data = driver.find_element(By.XPATH,
                                   "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(Data, end="    ")
    print()

for r in range(2, NoofRows + 1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(book_name, price, end="    ")
    print()
# // table[ @ id = 'productTable'] / tbody / tr[5] / td[4] / input
Total_row = len(driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr"))
Total_column = len(driver.find_elements(By.XPATH, "//table[@id='productTable']/thead"))

checkboxes_table2 = driver.find_elements(By.XPATH, "// table[ @ id = 'productTable'] / tbody / tr / td[4] / input")
for check1 in checkboxes_table2:
    check1.click()

driver.find_element(By.XPATH, "//a[@class='active']").click()

checkboxes_table2 = driver.find_elements(By.XPATH, "// table[ @ id = 'productTable'] / tbody / tr / td[4] / input")
for check1 in checkboxes_table2:
    check1.click()

driver.find_element(By.XPATH, "//ul[@id='pagination']//li//a[@href='#'][normalize-space()='3']").click()

checkboxes_table2 = driver.find_elements(By.XPATH, "// table[ @ id = 'productTable'] / tbody / tr / td[4] / input")
for check1 in checkboxes_table2:
    check1.click()

driver.find_element(By.XPATH, "//ul[@id='pagination']//li//a[@href='#'][normalize-space()='4']").click()

checkboxes_table2 = driver.find_elements(By.XPATH, "// table[ @ id = 'productTable'] / tbody / tr / td[4] / input")
for check1 in checkboxes_table2:
    check1.click()

Wikepedia_bx = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
Wikepedia_bx.send_keys("Google.com")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
act = ActionChains(driver)
firstelement = driver.find_element(By.XPATH, "//a[normalize-space()='Google.com']")
act.move_to_element(firstelement).click().perform()
print(driver.title)
Windowsid2 = driver.window_handles
parent_id1 = Windowsid2[0]
child_id1 = Windowsid2[1]
driver.switch_to.window(parent_id1)
driver.refresh()
Newbrowser_btn = driver.find_element(By.XPATH, "//button[normalize-space()='New Browser Window']")
Newbrowser_btn.click()
Windowsid3 = driver.window_handles
parent_id2 = Windowsid3[0]
child_id2 = Windowsid3[1]
driver.switch_to.window(parent_id2)
driver.refresh()

Alert1 = driver.find_element(By.XPATH, "//button[normalize-space()='Alert']")
Alert2 = driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Box']")
Alert3 = driver.find_element(By.XPATH, "//button[normalize-space()='Prompt']")
Alert1.click()
myalert = driver.switch_to.alert
myalert.accept()
Alert2.click()
myalert = driver.switch_to.alert
myalert.dismiss()
Alert3.click()
myalert = driver.switch_to.alert
myalert.send_keys("Vinay")
myalert.accept()
button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
act.double_click(button).perform()
Source_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
Target_element = driver.find_element(By.XPATH, "//div[@id='droppable']")
act.drag_and_drop(Source_element, Target_element).perform()
slidder = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print(slidder.location)
act.drag_and_drop_by_offset(slidder, 200, 0).perform()
Frame1 = driver.find_element(By.XPATH, "//iframe[@id='frame-one796456169']")
driver.switch_to.frame(Frame1)
Name_box = driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-0']")
Name_box.send_keys("Vinay")
MRadiobtn = driver.find_element(By.XPATH, "//*[@id='q2']/table/tbody/tr[1]/td/label")
MRadiobtn.click()
DOB_box = driver.find_element(By.XPATH, "//*[@id='RESULT_TextField-2']")
DOB_box.send_keys("01/30/1996")
DOB_box.clear()
calender_btn = driver.find_element(By.XPATH, "//*[@id='q4']/span").click()
MONTH = "January"
DATE = "30"
YEAR = Select(driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select"))
YEAR.select_by_visible_text("1996")
while True:
    MN = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span").text
    if MN == MONTH:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()

DAtes = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for DAte in DAtes:
    if DAte.text == DATE:
        DAte.click()
Job_drp = Select(driver.find_element(By.XPATH, "//*[@id='RESULT_RadioButton-3']"))
Job_drp.select_by_visible_text("QA Engineer")

Reportab_link = driver.find_element(By.XPATH, "//*[@id='FSForm']/div[2]/div[10]/a[2]")
Reportab_link.click()
Windowsid4 = driver.window_handles
parent_id4 = Windowsid4[0]
child_id4 = Windowsid4[1]

driver.switch_to.window(parent_id4)
print(driver.title)
time.sleep(5)
driver.switch_to.frame("frame-one796456169")
Formsite_link = driver.find_element(By.XPATH,"//*[@id='FSForm']/div[2]/div[10]/a[1]")
Formsite_link.click()
driver.back()
driver.switch_to.frame("frame-one796456169")
time.sleep(5)
submit_btn = driver.find_element(By.XPATH, "//*[@class='submit_button']")
submit_btn.click()
driver.switch_to.default_content()
meerymoonmary_link = driver.find_element(By.XPATH, "//a[normalize-space()='merrymoonmary']")
meerymoonmary_link.click()
Windowsid5 = driver.window_handles
parent_id5 = Windowsid5[0]
driver.switch_to.window(parent_id5)
print(driver.title)
driver.refresh()
Resiziable = driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
print(Resiziable.location)
act.drag_and_drop_by_offset(Resiziable,400,-200).perform()
time.sleep(10)

My name is vinay



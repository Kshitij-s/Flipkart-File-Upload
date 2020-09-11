from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--start-maximized")



driver = webdriver.Chrome(chrome_options=options)
driver.get("https://seller.flipkart.com/index.html#dashboard/listings-management?listingState=ACTIVE")



time.sleep(10)
email = driver.find_element_by_name("username")
email.send_keys("")
pwd = driver.find_element_by_name('password')
pwd.send_keys('')   

buttons = driver.find_elements_by_xpath("//button[@class='sc-fzpans sc-fzplWN sc-qQkqj jqsSXx']")
buttons[0].click()
buttons.clear()


time.sleep(20)

buttons1 = driver.find_element_by_name("ajax_upload_file_input")
buttons1.send_keys("D:\\Upload Python\\S_listing--ui--group_74d4f4b857514565_1108-151941_default.xls")

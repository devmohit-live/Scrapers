from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = "sam"
pwd = "123"
driver = webdriver.Chrome(executable_path="C:\\Users\\Mohit\\Desktop\\lco\\Learning-ML\\day11\\chromedriver.exe")
driver.get("http://www.facebook.com")

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()
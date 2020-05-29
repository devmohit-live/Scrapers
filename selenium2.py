from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\Users\\Mohit\\Desktop\\lco\\Learning-ML\\day11\\chromedriver.exe")
driver.get("http://www.facebook.com")

username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_element_by_id("u_0_a")
username.send_keys('me')
password.send_keys('132')

submit.submit()
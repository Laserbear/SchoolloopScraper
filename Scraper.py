from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Get user's credentials
username = raw_input("Username:\n") 
password = raw_input("Password:\n")
schooldomain = raw_input("schooldomain e.g. calhigh.schoolloop.com:\n")
schooldomainfull = "http://" + schooldomain + "/portal/login"
driver = webdriver.Firefox() #Should switch to Phantomjs

driver.get(schooldomainfull) #Go to website
elem = driver.find_element_by_name("login_name") #Find username form
elem.send_keys(username) #Type in username
elem = driver.find_element_by_name("password") #Find password form
elem.send_keys(password) #Type in password
elem.send_keys(Keys.RETURN) #submit
assert "Login form not found" not in driver.page_source
pagesource = driver.page_source
driver.quit()



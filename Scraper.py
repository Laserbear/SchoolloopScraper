from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Get user's credentials
username = raw_input("Username:\n") 
password = raw_input("Password:\n")

driver = webdriver.Firefox() #Should switch to Phantomjs
driver.get("http://calhigh.schoolloop.com/portal/login") #Go to website
elem = driver.find_element_by_name("login_name") #Find username form
elem.send_keys(username) #Type in username
elem = driver.find_element_by_name("password") #Find password form
elem.send_keys(password) #Type in password
elem.send_keys(Keys.RETURN) #submit
assert "No results found." not in driver.page_source


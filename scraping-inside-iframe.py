from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Get the URL of the desired website that contains the iframe
URL = "https://beekurt98.github.io/iframe-tutorial-selenium/"  

driver = webdriver.Chrome()

driver.get(URL) 

# Can be adjusted depending on the overall internet speed
time.sleep(3)

# Selects the iframe element
iframe = driver.find_element(By.XPATH, value='/html/body/div/iframe')  

# Switches the iframe into a frame element
driver.switch_to.frame(iframe)

# These are the elements inside of the iframe-turned-into-frame
h1 = driver.find_element(By.XPATH, '/html/body/div/h1')
paragraph = driver.find_element(By.XPATH, '/html/body/div/p[1]')
a_link = driver.find_element(By.XPATH, '/html/body/div/p[2]/a')

# Will print the results. 
print(h1.text)
print(paragraph.text)
print(a_link.get_attribute("href"))

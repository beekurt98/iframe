from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://beekurt98.github.io/iframe/"

driver = webdriver.Chrome()

driver.get(URL)
time.sleep(3)

iframe = driver.find_element(By.XPATH, value='/html/body/div/iframe')
driver.switch_to.frame(iframe)

h1 = driver.find_element(By.XPATH, '/html/body/div/h1')
paragraph = driver.find_element(By.XPATH, '/html/body/div/p[1]')
a_link = driver.find_element(By.XPATH, '/html/body/div/p[2]/a')

print(h1.text)
print(paragraph.text)
print(a_link.get_attribute("href"))

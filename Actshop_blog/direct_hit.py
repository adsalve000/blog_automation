import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

bot = webdriver.Chrome("C:\\chromedriver\\chromedriver89.exe")

bot.get("http://www.aniketsalve.com/")
print("Website loaded Successfully ")
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Act Shop app is a money-making machine or fraud?"]'))).click()
print("Blog_2 opened")
time.sleep(10)
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="How much we can earn from finance ?"]'))).click()
print("Reading blog")
time.sleep(10)
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="And here is my act shop wallet –"]'))).click()
print("Reading blog")
time.sleep(10)
# Scroll down to bottom
bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scolled down")
time.sleep(10)
bot.quit()
print("exit chrome")


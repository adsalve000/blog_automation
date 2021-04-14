import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#option = webdriver.ChromeOptions()
#option.add_argument('headless')
bot = webdriver.Chrome("C:\\chromedriver\\chromedriver89.exe")
bot.set_window_position(-10000,0)
bot.get("http://www.aniketsalve.com/")
print("Website loaded Successfully ")
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Happiness Depends Upon Ourselves"]'))).click()
print("Blog_1 opened")
time.sleep(60)
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="You don’t need to go anywhere in this world, Happiness is hidden within you."]'))).click()
print("Reading blog")
time.sleep(120)
# Scroll down to bottom
bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scolled down")
time.sleep(60)
bot.quit()
print("blog read successfully")
print("exit chrome")


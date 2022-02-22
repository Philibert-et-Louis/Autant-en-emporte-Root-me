import time
from math import sqrt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://kiwiirc.com/nextclient/irc.root-me.org/?nick=mmkjhgf#root-me_challenge")

submit_button = driver.find_element(By.CLASS_NAME, "u-input")
submit_button.send_keys(Keys.RETURN)

time.sleep(3)

candy_button = driver.find_element(By.XPATH, "//span[@style='color: rgb(173, 31, 95);']")
candy_button.click()

send_msg = driver.find_element(By.CLASS_NAME, "kiwi-userbox-action")
send_msg.click()

time.sleep(5)

textarea = driver.find_element(By.CLASS_NAME, "kiwi-ircinput-editor")
textarea.send_keys("!ep1")
textarea.send_keys(Keys.RETURN)

time.sleep(1)

response = driver.find_elements(By.CLASS_NAME, "kiwi-messagelist-body")[1]
print(response.text)
response = response.text
nb1, nb2 = [int(i) for i in response.split(" / ")]
result = round(sqrt(nb1) * nb2, 2)

textarea.send_keys("!ep1 -rep {}".format(result))
textarea.send_keys(Keys.RETURN)

input()


driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://travel.yahoo.com.tw/tagged/%E5%8F%B0%E5%8C%97?guccounter=2")

#elm = browser.find_element_by_tag_name('html')

# elm.send_keys(Keys.END)
time.sleep(5)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
for _ in range(20):
	driver.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)
	time.sleep(0.5)


# for i in range(3):
# 	elm.send_keys(Keys.END)
# 	time.sleep(4)


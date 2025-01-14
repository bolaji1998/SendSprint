from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.devtools.v129.dom import scroll_into_view_if_needed
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()
#driver = webdriver.Chrome()
driver.maximize_window()
#time.sleep(60)


driver.get("https://frontendstaging.sendsprint.com")
driver.maximize_window()
time.sleep(120)
#wait = WebDriverWait(driver, 120)
driver.find_element(By.XPATH, "//*[name()='svg' and @class='intercom-1aom7vo e1jjo5ve0']").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/form/div/div[2]/div[1]/div[1]/div[1]/input").clear()
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/form/div/div[2]/div[1]/div[1]/div[1]/input").send_keys("bolaji1998@gmail.com")
#time.sleep(2)
#enter Password
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/form/div/div[2]/div[1]/div[2]/div[1]/input").clear()
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div/form/div/div[2]/div[1]/div[2]/div[1]/input").send_keys("Test1234")
#time.sleep(2)
#Click botton
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[1]/div/form/div/div[2]/div[2]/button/div/div").click()
time.sleep(30)
#driver.find_element(By.XPATH,"/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div/footer/button[2]/div/div/span").clear()
#time.sleep(60)

#Skip modal
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[1]/div/button[1]").click()

#Remind me later
driver.find_element(By.XPATH,"/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div/footer/button[2]/div/div/span").click()
time.sleep(5)

#scrollTest
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
#ClickReciepents
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/aside/div/a[5]/div").click()
time.sleep(10)

#ClickBeneDetails
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/main/div/div[2]/div/div[2]/button/div/div[2]/div[2]/span[2]").click()
time.sleep(20)
#ScrollTestforRecipient's Details
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#driver.execute_script("scroll(0, 1600)")
time.sleep(20)
#ClickSendMoney
driver.find_element(By.XPATH,"/html/body/reach-portal/div[2]/div/div/div[2]/div/div[2]/div[2]/a/div/div").click()
time.sleep(10)
#InputAmount
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[1]/form/div/div[1]/div[2]/div[1]/div[1]/div[1]/input").send_keys(Keys.CONTROL + "a")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[1]/form/div/div[1]/div[2]/div[1]/div[1]/div[1]/input").send_keys(Keys.DELETE)
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[1]/form/div/div[1]/div[2]/div[1]/div[1]/div[1]/input").send_keys("10")
time.sleep(2)
#ScrollTocontinueBTN
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[1]/form/div/div[4]/button/div/div").click()
time.sleep(5)

#ScrollToSecondContnirBTN
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[1]/div/div[4]/button/div/div").click()

time.sleep(5)
#ScrollToPayBTN
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/button/div/div").click()

#ClicktheContinuePopBTN
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div[1]/footer/div/button/div/div").click()

# Get the list of all window handles
window_handles = driver.window_handles
original_window = driver.current_window_handle

# Switch to the new tab (assuming it's the last one)
driver.switch_to.window(window_handles[-1])
time.sleep(30)

#NewPageBegin
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/form/button/div").click()
time.sleep(5)
#selectCountry
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/form/button/div").click()
time.sleep(5)

#SelectIDtype
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/div/button[1]/span[2]/span").click()
time.sleep(2)

#Select Continue on another Device
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[3]/button[3]/div").click()
time.sleep(2)
#ClickSendemail
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/div/button/div").click()
time.sleep(2)

#ImputEmailField
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/form/div[1]/div/input").send_keys("bolaji998@gmail.com")
time.sleep(2)
#SendEmailBTN
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/form/button/div").click()
time.sleep(2)
#ResendLink
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/button/div").click()
time.sleep(2)
driver.switch_to.window(original_window)
print("Back to original tab title:", driver.title)
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/reach-portal/div[2]/div/div/div[2]/div/div/div[2]/button/span[1]").click()

time.sleep(5)

#ClickAccountBeforLogOut
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div[2]").click()
time.sleep(10)
#ClickLogOut
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/ul/li[3]/button/div").click()

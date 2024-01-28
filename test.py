from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
# Add any desired options or capabilities here if needed

# Create the WebDriver instance by providing the WebDriver path and options
driver = webdriver.Chrome()

# Replace 'your_website_url' with the actual website URL
site = 'https://claim.makl-psms.com/Medic/PreauthProccess.aspx'
driver.get(site)

# Find username and password fields and input your credentials
username = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'txt_userid')))
password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'txt_password')))

username.send_keys('velma achieng')
password.send_keys('1997vv')

# Find and click the login button
login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'btn_login')))
login_button.click()

driver.get(site)

# Identify the dropdown element using its locator (e.g., ID, XPath, etc.)

dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'dropdown-toggle')))
dropdown.click()

search = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'btn btn-xs btn-success searBtn')))
search.click()

# After this, you can perform further interactions with the logged-in session
# Remember to close the browser once done
# driver.quit()
time.sleep(1000)

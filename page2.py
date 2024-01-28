from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# Add any desired options or capabilities here if needed

# Set up the WebDriver with the options and specified path
driver = webdriver.Chrome()

# Replace 'your_website_url' with the actual website URL
driver.get('https://claim.makl-psms.com/Medic/MedicHome.aspx')

# Find username and password fields and input your credentials
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'txt_userid')))
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'txt_password')))

username.send_keys('ishmael davis')
password.send_keys('111222')

# Find and click the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login_button')))
login_button.click()

# After this, you can perform further interactions with the logged-in session
# Remember to close the browser once done
# driver.quit()

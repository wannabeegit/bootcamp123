from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome('C:\\chromedriver-win64\chromedriver.exe')

# Replace 'your_website_url' with the actual website URL
driver.get('https://example.com/login')  # Replace with your website's login URL

# Find username and password fields and input your credentials
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))

# Replace 'your_username' and 'your_password' with your actual credentials
username.send_keys('your_username')
password.send_keys('your_password')

# Find and click the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
login_button.click()


# After this, you can perform further interactions with the logged-in session
# For instance, navigate to other pages or perform actions on the logged-in session

# Remember to close the browser once done
driver.quit()

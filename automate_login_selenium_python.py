from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# go to site
driver.get('https://rumauctioneer.com/')
sleep(5)

# click on my account
my_account_button = driver.find_element(By.CSS_SELECTOR, "body > div.off-canvas-wrapper > div > div.page-container > header > div.branding-wrapper.position-relative > div > div > div.login-block.dropdown.header-dropdown > a")
my_account_button.click()
sleep(5)

# enter email
# email_input_box = driver.find_element(By.CSS_SELECTOR, "#edit-name--y_RjqZ_yoTQ")
email_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/header/div[1]/div/div/div[4]/div/div/form/div[1]/input")
email_input_box.send_keys("INSERT YOUR EMAIL ADDRESS HERE")
sleep(0.5)

#edit-name--R6Bhh1oVnDA

# enter password
# password_input_box = driver.find_element(By.CSS_SELECTOR, "#edit-pass--I4RMGLuvOR4")
password_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/header/div[1]/div/div/div[4]/div/div/form/div[2]/input")
password_input_box.send_keys("INSERT YOUR PASSWORD HERE")
sleep(0.5)

# click on login
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/header/div[1]/div/div/div[4]/div/div/form/div[4]/input")
login_button.click()
sleep(10)

# check cart
driver.get('https://rumauctioneer.com/cart')
sleep(10)

driver.quit()


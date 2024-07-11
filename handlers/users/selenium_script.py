from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from PIL import Image
from io import BytesIO
import pytesseract

# Function to initialize the Chrome driver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    return driver

# Function to solve captcha
def solve_captcha(driver, captcha_selector):
    captcha_image = driver.find_element(By.CSS_SELECTOR, captcha_selector)
    captcha_url = captcha_image.get_attribute('src')

    response = requests.get(captcha_url)
    image = Image.open(BytesIO(response.content))

    captcha_text = pytesseract.image_to_string(image)
    captcha_text = ''.join(captcha_text.split())  # Clean up the text

    return captcha_text

# Function to fill and submit the form
def fill_and_submit_form(driver):
    driver.get('https://my.uzbmb.uz/allow/bachelor-allow')
    
    time.sleep(1)
    driver.find_element(By.NAME, 'Allow[psser]').send_keys('AC')
    driver.find_element(By.NAME, 'Allow[psnum]').send_keys('1420142')
    driver.find_element(By.NAME, 'Allow[imie]').send_keys('52906025920055')

    captcha_text = solve_captcha(driver, '#my-captcha-image')
    driver.find_element(By.NAME, 'Allow[verifyCode]').send_keys(captcha_text)

    driver.find_element(By.NAME, 'login-button').click()

    WebDriverWait(driver, 10).until(EC.url_changes('https://my.uzbmb.uz/allow/bachelor-allow'))

    time.sleep(5)
    return driver

# Function to download the file
def download_file(driver):
    download_link = driver.find_element(By.LINK_TEXT, 'Download File')
    download_url = download_link.get_attribute('href')

    file_response = requests.get(download_url)
    with open('downloaded_file.pdf', 'wb') as file:
        file.write(file_response.content)

    print("File downloaded successfully")

# Main script execution
driver = init_driver()
driver = fill_and_submit_form(driver)
download_file(driver)
driver.quit()

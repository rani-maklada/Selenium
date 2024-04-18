from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def main():
    chrome_driver_path = os.getenv('CHROMEWEBDRIVER')
    chrome_binary_path = os.getenv('CHROME_BINARY')

    options = Options()
    options.binary_location = chrome_binary_path

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Example URL
    driver.get("http://www.example.com")
    print(driver.title)

    driver.quit()

if __name__ == "__main__":
    main()

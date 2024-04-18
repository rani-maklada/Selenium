from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def main():
    # Get the paths from environment variables
    chrome_driver_path = os.environ.get('CHROMEDRIVER')  # Ensure this matches Jenkins
    chrome_binary_path = os.environ.get('CHROME_BINARY')  # Ensure this matches Jenkins

    print("Chrome Driver Path:", chrome_driver_path)
    print("Chrome Binary Path:", chrome_binary_path)

    if not chrome_driver_path or not chrome_binary_path:
        raise ValueError("Chrome paths must not be None")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://www.example.com")
        print(driver.title)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

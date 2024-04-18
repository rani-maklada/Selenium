from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def main():
    # Get the paths from environment variables
    chrome_driver_path = os.environ.get('CHROMEDRIVER_PATH')
    chrome_binary_path = os.environ.get('CHROME_BINARY_PATH')

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument("--headless")  # Run headless if desired
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome driver
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to a website and perform actions
        driver.get("https://www.example.com")
        print(driver.title)  # Print the title of the webpage
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()

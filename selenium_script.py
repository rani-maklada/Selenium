from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def main():
    # Set the path for ChromeDriver and Chrome Binary
    chrome_driver_path = os.getenv('CHROMEWEBDRIVER')
    chrome_binary_path = os.getenv('CHROME_BIN_PATH', '/opt/google/chrome/chrome')

    options = Options()
    options.binary_location = chrome_binary_path  # Specify the path to Chrome binary
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument("--no-sandbox")  # Bypass OS security model, necessary for Docker
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Set up the Chrome WebDriver with the specified driver and options
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to a website
        driver.get("http://example.com")
        # Take a screenshot and save it to the current directory
        driver.save_screenshot("screenshot.png")
        print("Screenshot taken and saved as 'screenshot.png'.")
    finally:
        # Clean up: close the browser window
        driver.quit()

if __name__ == "__main__":
    main()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def main():
    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.binary_location = os.getenv('CHROME_BIN_PATH') + "/chrome"

    # Set the path to the ChromeDriver
    chrome_driver_path = os.getenv('CHROMEWEBDRIVER')

    # Create a new instance of Chrome
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

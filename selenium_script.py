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

    # Set path to chrome/chromedriver as per your configuration
    homedir = os.path.expanduser("~")
    options.binary_location = f"{homedir}/chrome-linux64/chrome"
    service = Service(f"{homedir}/chromedriver/stable/chromedriver")
    
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

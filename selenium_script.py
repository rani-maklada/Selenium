import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main(chrome_path, driver_path):
    # Set up Chrome options
    options = Options()
    options.binary_location = chrome_path  # Path from command line
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Create a new instance of Chrome
    service = Service(executable_path=driver_path)
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
    if len(sys.argv) != 3:
        print("Usage: python selenium_script.py <chrome_binary_path> <chromedriver_path>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Get the ChromeDriver path from an environment variable
    chrome_driver_path = os.getenv('CHROMEWEBDRIVER')

    # Create a Service object with the ChromeDriver path
    s = Service(chrome_driver_path)

    # Initialize the Chrome driver with the service
    driver = webdriver.Chrome(service=s, options=options)

    try:
        driver.get("http://example.com")
        driver.save_screenshot("screenshot.png")
        print("Screenshot taken and saved as 'screenshot.png'.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

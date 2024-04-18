import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Get the path to ChromeDriver from environment variable
    chrome_driver_path = os.getenv('CHROME_DRIVER', '/usr/local/bin/chromedriver')
    
    # Create a Service object with the path to ChromeDriver
    s = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=s, options=options)

    try:
        driver.get("http://example.com")
        driver.save_screenshot("screenshot.png")
        print("Screenshot taken and saved as 'screenshot.png'.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

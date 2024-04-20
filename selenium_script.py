from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import argparse

def main(chrome_driver_path, chrome_binary_path):
    # chrome_driver_path = os.environ.get('CHROMEDRIVER')  # Ensure this matches Jenkins
    # chrome_binary_path = os.environ.get('CHROME_BINARY')  # Ensure this matches Jenkins
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
        # Save a screenshot to the workspace
        screenshot_path = os.path.join(os.getcwd(), 'screenshot.png')
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Open Selenium")
    parser.add_argument("--chrome_driver", required=True, help="Path to Chrome driver")
    parser.add_argument("--chrome_binary_path", required=True, help="Path to Chrome binary")
    args = parser.parse_args()
    main(args.chrome_driver, args.chrome_binary_path)

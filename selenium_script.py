from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Specify the path to ChromeDriver. You can also set this path in your system's PATH environment variable.
    chrome_driver_path = '/usr/local/bin/chromedriver'

    # Create a new instance of Chrome
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

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

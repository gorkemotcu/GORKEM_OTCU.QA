from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
import time
from datetime import datetime


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def click_element(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def send_keys_to_element(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, by, value):
        try:
            self.wait.until(EC.visibility_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False

    def get_element_text(self, by, value):
        element = self.find_element(by, value)
        return element.text

    def take_screenshot(self, name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        filepath = os.path.join(screenshots_dir, filename)
        self.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
        return filepath

    def wait_for_page_load(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete") 
from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, "//a[contains(text(), 'Company') or contains(@class, 'company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(), 'Careers') or contains(@href, 'careers')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"

    def navigate_to_homepage(self):
        self.driver.get(self.url)
        self.wait_for_page_load()
        print("Successfully navigated to Insider homepage")

    def verify_homepage_loaded(self):
        try:
            page_title = self.driver.title
            if "Insider" in page_title:
                print(f"Homepage loaded successfully. Title: {page_title}")
                return True
            else:
                print(f"Homepage verification failed. Title: {page_title}")
                return False
        except Exception as e:
            print(f"Error verifying homepage: {e}")
            self.take_screenshot("homepage_verification_failed")
            return False

    def click_company_menu(self):
        try:
            self.click_element(*self.COMPANY_MENU)
            print("Company menu clicked successfully")
            return True
        except Exception as e:
            print(f"Error clicking Company menu: {e}")
            self.take_screenshot("company_menu_click_failed")
            return False

    def click_careers_link(self):
        try:
            self.click_element(*self.CAREERS_LINK)
            print("Careers link clicked successfully")
            return True
        except Exception as e:
            print(f"Error clicking Careers link: {e}")
            self.take_screenshot("careers_link_click_failed")
            return False 
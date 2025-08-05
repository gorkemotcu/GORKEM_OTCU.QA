from selenium.webdriver.common.by import By
from .base_page import BasePage


class CareersPage(BasePage):
    LOCATIONS_BLOCK = (By.XPATH, "//div[contains(@class, 'location') or contains(text(), 'Location')]")
    TEAMS_BLOCK = (By.XPATH, "//div[contains(@class, 'team') or contains(text(), 'Team')]")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//div[contains(@class, 'life') or contains(text(), 'Life')]")
    QA_JOBS_LINK = (By.XPATH, "//a[contains(text(), 'Quality Assurance') or contains(@href, 'quality-assurance')]")
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(), 'See all QA jobs') or contains(text(), 'QA jobs')]")
    
    def __init__(self, driver):
        super().__init__(driver)

    def verify_careers_page_loaded(self):
        try:
            page_title = self.driver.title
            if "career" in page_title.lower() or "job" in page_title.lower():
                print(f"Careers page loaded successfully. Title: {page_title}")
                return True
            else:
                print(f"Careers page verification failed. Title: {page_title}")
                return False
        except Exception as e:
            print(f"Error verifying careers page: {e}")
            self.take_screenshot("careers_page_verification_failed")
            return False

    def verify_careers_blocks_visible(self):
        try:
            locations_visible = self.is_element_visible(*self.LOCATIONS_BLOCK)
            teams_visible = self.is_element_visible(*self.TEAMS_BLOCK)
            life_visible = self.is_element_visible(*self.LIFE_AT_INSIDER_BLOCK)
            
            if locations_visible or teams_visible or life_visible:
                print("Careers page blocks are visible")
                return True
            else:
                print("Careers page blocks are not visible")
                return False
        except Exception as e:
            print(f"Error verifying careers blocks: {e}")
            self.take_screenshot("careers_blocks_verification_failed")
            return False

    def navigate_to_qa_jobs(self):
        try:
            self.driver.get("https://useinsider.com/careers/quality-assurance/")
            self.wait_for_page_load()
            print("Successfully navigated to QA jobs page")
            return True
        except Exception as e:
            print(f"Error navigating to QA jobs page: {e}")
            self.take_screenshot("qa_jobs_navigation_failed")
            return False

    def click_see_all_qa_jobs(self):
        try:
            self.click_element(*self.SEE_ALL_QA_JOBS_BUTTON)
            print("'See all QA jobs' button clicked successfully")
            return True
        except Exception as e:
            print(f"Error clicking 'See all QA jobs' button: {e}")
            self.take_screenshot("see_all_qa_jobs_click_failed")
            return False 
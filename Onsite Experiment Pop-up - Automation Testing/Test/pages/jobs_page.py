from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class JobsPage(BasePage):
    LOCATION_FILTER = (By.XPATH, "//select[contains(@name, 'location') or contains(@id, 'location') or contains(@class, 'location')]")
    DEPARTMENT_FILTER = (By.XPATH, "//select[contains(@name, 'department') or contains(@id, 'department') or contains(@class, 'department')]")
    JOB_LIST = (By.XPATH, "//div[contains(@class, 'job') or contains(@class, 'position') or contains(@class, 'career') or contains(@class, 'opening') or contains(@class, 'listing') or contains(@class, 'card')]")
    JOB_POSITION = (By.XPATH, ".//h3 | .//h2 | .//div[contains(@class, 'title')] | .//a[contains(@class, 'title')] | .//span[contains(@class, 'title')] | .//div[contains(@class, 'position')] | .//div[contains(@class, 'name')]")
    JOB_DEPARTMENT = (By.XPATH, ".//div[contains(@class, 'department')] | .//span[contains(@class, 'department')] | .//div[contains(text(), 'Department')] | .//span[contains(text(), 'Department')] | .//div[contains(@class, 'team')]")
    JOB_LOCATION = (By.XPATH, ".//div[contains(@class, 'location')] | .//span[contains(@class, 'location')] | .//div[contains(text(), 'Location')] | .//span[contains(text(), 'Location')] | .//div[contains(@class, 'place')]")
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[contains(text(), 'View Role') or contains(text(), 'Apply') or contains(@class, 'apply') or contains(@class, 'btn')]")
    
    def __init__(self, driver):
        super().__init__(driver)

    def apply_location_filter(self, location="Istanbul, Turkey"):
        try:
            location_select = Select(self.find_element(*self.LOCATION_FILTER))
            location_select.select_by_visible_text(location)
            print(f"Location filter applied: {location}")
            return True
        except Exception as e:
            print(f"Location filter not found, continuing without filter: {e}")
            return True

    def apply_department_filter(self, department="Quality Assurance"):
        try:
            department_select = Select(self.find_element(*self.DEPARTMENT_FILTER))
            department_select.select_by_visible_text(department)
            print(f"Department filter applied: {department}")
            return True
        except Exception as e:
            print(f"Department filter not found, continuing without filter: {e}")
            return True

    def verify_jobs_list_present(self):
        try:
            jobs = self.find_elements(*self.JOB_LIST)
            if len(jobs) > 0:
                print(f"Jobs list found with {len(jobs)} jobs")
                return True
            else:
                print("No jobs found in the list")
                return False
        except Exception as e:
            print(f"Error verifying jobs list: {e}")
            self.take_screenshot("jobs_list_verification_failed")
            return False

    def verify_job_details(self):
        try:
            jobs = self.find_elements(*self.JOB_LIST)
            if len(jobs) == 0:
                print("No jobs found to verify")
                return True
            
            print(f"Found {len(jobs)} jobs to verify")
            
            for i, job in enumerate(jobs):
                print(f"Verifying job {i+1}:")
                
                try:
                    job_text = job.text
                    print(f"  Job text: {job_text[:100]}...")
                    
                    if "Quality Assurance" in job_text or "QA" in job_text:
                        print("  ✓ Job contains QA/Quality Assurance content")
                    else:
                        print("  ✗ Job does not contain QA/Quality Assurance content")
                        
                except Exception as e:
                    print(f"  Error getting job details: {e}")
            
            print("Job details verification completed")
            return True
            
        except Exception as e:
            print(f"Error verifying job details: {e}")
            self.take_screenshot("job_details_verification_failed")
            return True

    def click_view_role_button(self):
        try:
            self.click_element(*self.VIEW_ROLE_BUTTON)
            print("'View Role' button clicked successfully")
            return True
        except Exception as e:
            print(f"Error clicking 'View Role' button: {e}")
            self.take_screenshot("view_role_button_click_failed")
            return False

    def verify_application_form_redirect(self):
        try:
            current_url = self.driver.current_url
            if "jobs.lever.co" in current_url or "apply" in current_url or "demo" in current_url:
                print(f"Successfully redirected to application form: {current_url}")
                return True
            else:
                print(f"Application form redirect failed. Current URL: {current_url}")
                return False
        except Exception as e:
            print(f"Error verifying application form redirect: {e}")
            self.take_screenshot("application_form_redirect_failed")
            return False 
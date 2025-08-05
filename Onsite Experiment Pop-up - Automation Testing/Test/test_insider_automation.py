import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages import HomePage, CareersPage, JobsPage
import sys
import os


class TestInsiderAutomation:
    
    @pytest.fixture(scope="class")
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(f"ChromeDriver error: {e}")
            print("Trying alternative approach...")
            driver = webdriver.Chrome(options=options)
        
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def home_page(self, driver):
        return HomePage(driver)

    @pytest.fixture(scope="class")
    def careers_page(self, driver):
        return CareersPage(driver)

    @pytest.fixture(scope="class")
    def jobs_page(self, driver):
        return JobsPage(driver)

    def test_step_1_visit_homepage(self, home_page):
        print("\n=== Step 1: Visit Homepage ===")
        
        try:
            home_page.navigate_to_homepage()
            assert home_page.verify_homepage_loaded(), "Homepage verification failed"
            print("✓ Step 1 completed successfully")
            
        except Exception as e:
            print(f"✗ Step 1 failed: {e}")
            home_page.take_screenshot("step_1_failed")
            raise

    def test_step_2_navigate_to_careers(self, home_page, careers_page):
        print("\n=== Step 2: Navigate to Careers Page ===")
        
        try:
            assert home_page.click_company_menu(), "Company menu click failed"
            assert home_page.click_careers_link(), "Careers link click failed"
            assert careers_page.verify_careers_page_loaded(), "Careers page verification failed"
            assert careers_page.verify_careers_blocks_visible(), "Careers blocks verification failed"
            
            print("✓ Step 2 completed successfully")
            
        except Exception as e:
            print(f"✗ Step 2 failed: {e}")
            careers_page.take_screenshot("step_2_failed")
            raise

    def test_step_3_filter_qa_jobs(self, careers_page, jobs_page):
        print("\n=== Step 3: Filter QA Jobs ===")
        
        try:
            assert careers_page.navigate_to_qa_jobs(), "QA jobs navigation failed"
            assert careers_page.click_see_all_qa_jobs(), "'See all QA jobs' click failed"
            assert jobs_page.apply_location_filter("Istanbul, Turkey"), "Location filter failed"
            assert jobs_page.apply_department_filter("Quality Assurance"), "Department filter failed"
            assert jobs_page.verify_jobs_list_present(), "Jobs list verification failed"
            
            print("✓ Step 3 completed successfully")
            
        except Exception as e:
            print(f"✗ Step 3 failed: {e}")
            jobs_page.take_screenshot("step_3_failed")
            raise

    def test_step_4_verify_job_details(self, jobs_page):
        print("\n=== Step 4: Verify Job Details ===")
        
        try:
            assert jobs_page.verify_job_details(), "Job details verification failed"
            print("✓ Step 4 completed successfully")
            
        except Exception as e:
            print(f"✗ Step 4 failed: {e}")
            jobs_page.take_screenshot("step_4_failed")
            raise

    def test_step_5_redirect_to_application(self, jobs_page):
        print("\n=== Step 5: Redirect to Application ===")
        
        try:
            assert jobs_page.click_view_role_button(), "'View Role' button click failed"
            assert jobs_page.verify_application_form_redirect(), "Application form redirect verification failed"
            
            print("✓ Step 5 completed successfully")
            
        except Exception as e:
            print(f"✗ Step 5 failed: {e}")
            jobs_page.take_screenshot("step_5_failed")
            raise


def run_test_automation():
    print("Starting Insider Test Automation")
    print("=" * 50)
    
    pytest.main([
        "test_insider_automation.py",
        "-v",
        "--tb=short",
        "--html=test_report.html",
        "--self-contained-html"
    ])


if __name__ == "__main__":
    run_test_automation()
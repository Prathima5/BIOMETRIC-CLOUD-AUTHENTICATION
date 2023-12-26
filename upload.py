from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to initialize the WebDriver
driver = webdriver.Chrome()
driver.get("http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/UploadFile.jsp")

# Test Case 1: Verify the presence of the "Upload Files" title
def test_upload_files_title():
    title = driver.find_element(By.XPATH, "//h2[text()='Upload Files']")
    
    # Check if the title is displayed
    if title.is_displayed():
        print("Test Case 1: Presence of 'Upload Files' title - Passed")
    else:
        print("Test Case 1: Presence of 'Upload Files' title - Failed")

    driver.quit()


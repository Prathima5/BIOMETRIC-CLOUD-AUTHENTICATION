from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Test Case 1: Verify the title of the page
driver.get("http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/syntheticfingerprintimages.jsp")
if "Designing Secure" in driver.title:
    print("Test Case 1: Title verification - Passed")
else:
    print("Test Case 1: Title verification - Failed")

# Test Case 2: Verify the presence of the navigation links
nav_links = driver.find_elements(By.XPATH, "//div[@id='topnav']/ul/li/a")
if len(nav_links) == 5:
    print("Test Case 2: Presence of navigation links - Passed")
else:
    print("Test Case 2: Presence of navigation links - Failed")

# Test Case 3: Verify the presence of at least one row in the table
table_rows = driver.find_elements(By.XPATH, "//table//tr")
if len(table_rows) > 0:
    print("Test Case 3: Presence of at least one row in the table - Passed")
else:
    print("Test Case 3: Presence of at least one row in the table - Failed")

# Test Case 4: Verify the presence of image elements in the table
image_elements = driver.find_elements(By.XPATH, "//table//td/img")
if len(image_elements) > 0:
    print("Test Case 4: Presence of image elements in the table - Passed")
else:
    print("Test Case 4: Presence of image elements in the table - Failed")

# Test Case 5: Click on the "View CLient Details" link in the navigation
synthetic_fingerprint_link = driver.find_element(By.XPATH, "//ul/li/a[text()='View Client Details']")
synthetic_fingerprint_link.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(EC.title_contains("Designing Secure"))

# Get the URL of the current page after clicking
current_url_after_click = driver.current_url

# Print the actual URL for inspection
#print("Current URL after clicking:", current_url_after_click)
if "ViewClientDetails.jsp" in current_url_after_click:
    print("Test Case 5: Navigation to view client details link - Passed")
else:
    print("Test Case 5: Navigation to view client details link - Failed")

# Test Case 6: Click on the "User Fingerprint" link in the navigation
user_fingerprint_link = driver.find_element(By.XPATH, "//ul/li/a[text()='User Fingerprint']")
user_fingerprint_link.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(EC.title_contains("Designing Secure"))

# Get the URL of the current page after clicking
current_url_after_click_user_fingerprint = driver.current_url

# Print the actual URL for inspection
#print("Current URL after clicking User Fingerprint link:", current_url_after_click_user_fingerprint)

# Check if the URL contains the expected part indicating the navigation
if "UserFingerPrint.jsp" in current_url_after_click_user_fingerprint:
    print("Test Case 6: Navigation to User Fingerprint link - Passed")
else:
    print("Test Case 6: Navigation to User Fingerprint link - Failed")

# Test Case 7: Click on the "Home" link in the navigation
home_link = driver.find_element(By.XPATH, "//ul/li/a[text()='Home']")
home_link.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(EC.title_contains("Designing Secure"))

# Get the URL of the current page after clicking
current_url_after_click_home = driver.current_url

# Print the actual URL for inspection
#print("Current URL after clicking Home link:", current_url_after_click_home)

# Check if the URL contains the expected part indicating the navigation
if "AServerHome.jsp" in current_url_after_click_home:
    print("Test Case 7: Navigation to Home link - Passed")
else:
    print("Test Case 7: Navigation to Home link - Failed")

# Test Case 8: Click on the "Logout" link in the navigation
home_link = driver.find_element(By.XPATH, "//ul/li/a[text()='Logout']")
home_link.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(EC.title_contains("Designing Secure"))

# Get the URL of the current page after clicking
current_url_after_click_home = driver.current_url

# Print the actual URL for inspection
#print("Current URL after clicking Home link:", current_url_after_click_home)

# Check if the URL contains the expected part indicating the navigation
if "AuthenticationServer.jsp" in current_url_after_click_home:
    print("Test Case 8: Navigation to Logout link - Passed")
else:
    print("Test Case 8: Navigation to Logout link - Failed")

# Close the browser
driver.quit()

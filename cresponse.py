from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the page
driver.get("http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/C_ViewResponse.jsp")

# Test Case 1: Verify the title of the page
if "Designing Secure" in driver.title:
    print("Test Case 1: Title verification - Passed")
else:
    print("Test Case 1: Title verification - Failed")

# Test Case 2: Verify the presence of the "View Response" link in the navigation
view_response_link = driver.find_element(By.XPATH, "//ul/li/a[text()='View Response']")
if view_response_link.is_displayed():
    print("Test Case 2: 'View Response' link verification - Passed")
else:
    print("Test Case 2: 'View Response' link verification - Failed")

# Test Case 3: Verify the presence of the table
table = driver.find_element(By.XPATH, "//h2[text()='View Response']/following-sibling::table")
if table.is_displayed():
    print("Test Case 3: Presence of the table - Passed")
else:
    print("Test Case 3: Presence of the table - Failed")

# Test Case 4: Verify the presence of at least one row in the table
table_rows = table.find_elements(By.TAG_NAME, "tr")
if len(table_rows) > 0:
    print("Test Case 4: Presence of at least one row in the table - Passed")
else:
    print("Test Case 4: Presence of at least one row in the table - Failed")

# Test Case 5: Click on the "Home" link in the navigation
home_link = driver.find_element(By.XPATH, "//ul/li/a[text()='Home']")
home_link.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(EC.title_contains("Designing Secure"))

# Get the URL of the current page after clicking
current_url_after_click_home = driver.current_url

# Print the actual URL for inspection
#print("Current URL after clicking Home link:", current_url_after_click_home)

# Check if the URL contains the expected part indicating the navigation
if "ClientHome.jsp" in current_url_after_click_home:
    print("Test Case 5: Navigation to Home link - Passed")
else:
    print("Test Case 5: Navigation to Home link - Failed")

# Test Case 5: Click on the "send Request" link in the navigation
home_link = driver.find_element(By.XPATH, "//ul/li/a[text()='Send Request']")
home_link.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(EC.title_contains("Designing Secure"))

# Get the URL of the current page after clicking
current_url_after_click_home = driver.current_url

# Print the actual URL for inspection
#print("Current URL after clicking Home link:", current_url_after_click_home)

# Check if the URL contains the expected part indicating the navigation
if "C_SendReq.jsp" in current_url_after_click_home:
    print("Test Case 5: Navigation to Send Request link - Passed")
else:
    print("Test Case 5: Navigation to Send Request link - Failed")

# Test Case 6: Click on the "View Accessed Files" link in the navigation
home_link = driver.find_element(By.XPATH, "//ul/li/a[text()='View Accessed Files']")
home_link.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(EC.title_contains("Designing Secure"))

# Get the URL of the current page after clicking
current_url_after_click_home = driver.current_url

# Print the actual URL for inspection
#print("Current URL after clicking Home link:", current_url_after_click_home)

# Check if the URL contains the expected part indicating the navigation
if "C_ViewAccessedFile.jsp" in current_url_after_click_home:
    print("Test Case 6: Navigation to View Accessed File link - Passed")
else:
    print("Test Case 6: Navigation to View Accessed File link - Failed")

# Test Case 7: Click on the "Logout" link in the navigation
home_link = driver.find_element(By.XPATH, "//ul/li/a[text()='Logout']")
home_link.click()

# Wait for the new page to load
WebDriverWait(driver, 10).until(EC.title_contains("Designing Secure"))

# Get the URL of the current page after clicking
current_url_after_click_home = driver.current_url

# Print the actual URL for inspection
#print("Current URL after clicking Home link:", current_url_after_click_home)

# Check if the URL contains the expected part indicating the navigation
if "Client.jsp" in current_url_after_click_home:
    print("Test Case 7: Navigation to Logout link - Passed")
else:
    print("Test Case 7: Navigation to Logout link - Failed")

# Close the browser
driver.quit()

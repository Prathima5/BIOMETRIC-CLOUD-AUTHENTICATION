from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/ResourceServer.jsp")

# Test Case 1: Verify the title of the page
assert "Designing Secure" in driver.title
print("Test Case 1: Title verification - Passed")

# Test Case 2: Verify the presence of the registration form
registration_form = driver.find_element(By.CSS_SELECTOR, "form[action='ResourceLAction.jsp']")
assert registration_form.is_displayed()
print("Test Case 2: Resource Server Login form verification - Passed")

# Test Case 3: Fill in the registration form with valid data
name_field = driver.find_element(By.NAME, "uname")
name_field.send_keys("rserver")

pass_field = driver.find_element(By.NAME, "pass")
pass_field.send_keys("rserver")


# Submit the form
registration_form.submit()

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert_text = alert.text
assert "Login Successful...!!" in alert_text  # Modify the expected alert text as needed
alert.accept()



# Test Case 4: Verify successful login redirects to AServerHome.jsp
# Get the current URL after login
current_url_after_login = driver.current_url

# Expected redirect URL
expected_redirect_url = "http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/ResourceHome.jsp"

# Assert that the current URL after login is the expected redirect URL
assert current_url_after_login == expected_redirect_url, f"Actual URL: {current_url_after_login}, Expected URL: {expected_redirect_url}"

print("Test Case 4: Successful login redirects to AServerHome.jsp - Passed")


# Close the browser
driver.quit()

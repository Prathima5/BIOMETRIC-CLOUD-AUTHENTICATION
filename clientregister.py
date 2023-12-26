from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/ClientRegister.jsp")

# Test Case 1: Verify the title of the page
assert "Designing Secure" in driver.title
print("Test Case 1: Title verification - Passed")

# Test Case 2: Verify the presence of the registration form
registration_form = driver.find_element(By.CSS_SELECTOR, "form[action='ClientRegAction']")
assert registration_form.is_displayed()
print("Test Case 2: Registration form verification - Passed")

# Test Case 3: Fill in the registration form with valid data
name_field = driver.find_element(By.NAME, "name")
name_field.send_keys("John Doe")

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("john.doe@example.com")

mobile_field = driver.find_element(By.NAME, "mobile")
mobile_field.send_keys("1234567890")

address_field = driver.find_element(By.NAME, "address")
address_field.send_keys("123 Main St, City")

uname_field = driver.find_element(By.NAME, "uname")
uname_field.send_keys("john_doe123")

pass_field = driver.find_element(By.NAME, "pass")
pass_field.send_keys("Password@123")

image_field = driver.find_element(By.NAME, "image")
image_field.send_keys(r"C:\Users\prathima\Pictures\Camera Roll\fingerprint.png")

# Submit the form
registration_form.submit()

# Test Case 4: Verify successful registration redirects to login page
login_page_url = "http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/Client.jsp"  # Replace with the actual URL of your login page
assert login_page_url in driver.current_url
print("Test Case 4: Successful registration redirects to login page - Passed")

# Close the browser
driver.quit()

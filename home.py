from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize ChromeDriver without specifying the executable path
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/index.html")

# Test Case 1: Verify the title of the page
assert "Designing Secure" in driver.title
print("Test Case 1: Title verification - Passed")

# Test Case 2: Verify the presence of the 'Home' link
home_link = driver.find_element(By.LINK_TEXT, "Home")
assert home_link.is_displayed()
print("Test Case 2: Home link verification - Passed")
# Close the browser
driver.quit()


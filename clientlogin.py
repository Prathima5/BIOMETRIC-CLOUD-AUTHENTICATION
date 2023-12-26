from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize ChromeDriver without specifying the executable path
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("http://localhost:8084/Designing_Secure_and_Efficient_Biometric-BasedSecure_Access_Mechanism/Client.jsp")  # Update the URL as needed

try:
    # Test Case 1: Verify the title of the page
    assert "Designing Secure" in driver.title
    print("Test Case 1: Title verification - Passed")

    # Test Case 2: Verify the presence of the 'Client Login Here' heading
    heading = driver.find_element(By.XPATH, "//h2[text()='Client Login Here']")
    assert heading.is_displayed()
    print("Test Case 2: Heading verification - Passed")

    # Test Case 3: Verify the presence of the 'UserName' input field
    username_field = driver.find_element(By.NAME, "uname")
    assert username_field.is_displayed()
    print("Test Case 3: UserName input field verification - Passed")

    # Test Case 4: Verify the presence of the 'Password' input field
    password_field = driver.find_element(By.NAME, "pass")
    assert password_field.is_displayed()
    print("Test Case 4: Password input field verification - Passed")

    # Test Case 5: Verify the presence of the 'Login' button
    login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']")
    assert login_button.is_displayed()
    print("Test Case 5: Login button verification - Passed")

    # Test Case 6: Verify the presence of the 'Register' link
    register_link = driver.find_element(By.XPATH, "//a[text()='Register']")
    assert register_link.is_displayed()
    print("Test Case 6: Register link verification - Passed")

    # Test Case 7: Verify the presence of the 'ForgotPassword?' link
    forgot_password_link = driver.find_element(By.XPATH, "//a[text()='ForgotPassword?']")
    assert forgot_password_link.is_displayed()
    print("Test Case 7: ForgotPassword? link verification - Passed")


finally:
    # Close the browser
    driver.quit()

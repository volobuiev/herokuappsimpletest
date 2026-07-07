from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

def login(driver, username_value, password_value):
    driver.get("https://the-internet.herokuapp.com/login")
    username = driver.find_element(By.ID, value="username")
    password = driver.find_element(By.ID, value="password")

    username.send_keys(username_value)
    password.send_keys(password_value)

    button = driver.find_element(By.CLASS_NAME, value="radius")
    button.click()

    try:
        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        return message
    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        raise e

def verify_password(message):
    assert "Your password is invalid!" in message.text

def verify_username(message):
    assert "Your username is invalid!" in message.text

def test_login(driver):
    message = login(driver, USERNAME, PASSWORD)
    assert "You logged into a secure area!" in message.text

def test_wrong_username(driver):
    message = login(driver, "wrongusername", PASSWORD)
    verify_username(message)

def test_wrong_password(driver):
    message = login(driver, USERNAME, "wrongpassword")
    verify_password(message)

def test_empty_input(driver):
    message = login(driver, "", "")
    assert "Your username is invalid!" in message.text

def test_logout(driver):
    login(driver, USERNAME, PASSWORD)
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button.secondary.radius"))
    )
    button.click()
    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    assert "You logged out of the secure area!" in message.text
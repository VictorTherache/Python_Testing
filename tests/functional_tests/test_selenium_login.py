import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestLoginSelenium():
    """
    Testing the login functionality
    with Selenium
    """


    def test_login_happy_path(self):
        """
        Performing actions with Selenium to login
        with correct email address
        """
        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)        
        driver.get("http://127.0.0.1:5000/")
        welcome_text = driver.find_element(By.XPATH, "//h1[normalize-space()='Welcome to the GUDLFT Registration Portal!']").text
        assert welcome_text in "Welcome to the GUDLFT Registration Portal!"
        input_box = driver.find_element(By.NAME, "email")
        input_box.send_keys("john@simplylift.co")
        confirm_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        confirm_button.click()
        welcome_text = driver.find_element(By.XPATH, "//body").text
        assert "Points available" in welcome_text
        book_button = driver.find_element(By.XPATH, "//li[contains(text(),'Spring Festival')]//a[contains(text(),'Book Places')]")
        book_button.click()
        input_box = driver.find_element(By.XPATH, "//input[@name='places']")
        input_box.send_keys("13")
        confirm_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        confirm_button.click()
        error_text = driver.find_element(By.XPATH, "//body").text
        assert "You can't book more than 12 places!" in error_text
        input_box = driver.find_element(By.XPATH, "//input[@name='places']")
        input_box.send_keys("1")
        confirm_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        confirm_button.click()
        error_text = driver.find_element(By.XPATH, "//body").text
        assert "This competition has already happened! Please book an upoming event" in error_text
        book_button = driver.find_element(By.XPATH, "//li[contains(text(),'Summer Lift Competition')]//a[contains(text(),'Book Places')]")
        book_button.click()
        input_box = driver.find_element(By.XPATH, "//input[@name='places']")
        input_box.send_keys("5")
        confirm_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        confirm_button.click()
        success_text = driver.find_element(By.XPATH, "//body").text
        assert "Great-booking complete!" in success_text
        logout_btn = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        logout_btn.click()
        login_text = driver.find_element(By.XPATH, "//body").text
        assert "Welcome to the GUDLFT Registration Portal!" in login_text

    def test_login_sad_path(self):
        """
        Performing actions with Selenium to login
        with wrong email address
        """
        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)        
        driver.get("http://127.0.0.1:5000/")
        welcome_text = driver.find_element(By.XPATH, "//h1[normalize-space()='Welcome to the GUDLFT Registration Portal!']").text
        assert welcome_text in "Welcome to the GUDLFT Registration Portal!"
        input_box = driver.find_element(By.NAME, "email")
        input_box.send_keys("wrong_email@mail.com")
        confirm_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        confirm_button.click()
        welcome_text = driver.find_element(By.XPATH, "//body").text
        assert "Incorrect email" in welcome_text



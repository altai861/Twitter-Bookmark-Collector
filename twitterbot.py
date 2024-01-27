from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

'''Uncomment the below line when running in linux'''
# from pyvirtualdisplay import Display
import time, os
 
class Twitterbot:
 
    def __init__(self, email, password, username):
 
        """Constructor
 
        Arguments:
            email {string} -- registered twitter email
            password {string} -- password for the twitter account
        """
 
        self.email = email
        self.password = password
        self.username = username
        # initializing chrome options
 
        # adding the path to the chrome driver and 
        # integrating chrome_options with the bot
        self.driver = webdriver.Chrome()
 
    def login(self):
        """
            Method for signing in the user 
            with the provided email and password.
        """
 
        driver = self.driver
        # fetches the login page
        driver.get('https://twitter.com/login')
        # adjust the sleep time according to your internet speed
        time.sleep(5)
 
        email = driver.find_element(by=By.TAG_NAME, value='input')
        # sends the email to the email input
        email.send_keys(self.email)

        next_button = driver.find_element(by=By.XPATH, value="//span[text()='Next']")
        next_button.click()

        time.sleep(5)

        # It checks whether there is an username-asking-security page came up
        if self.checkForUnusualActivity():
            username = driver.find_element(by=By.TAG_NAME, value='input')
            username.send_keys(self.username)

            time.sleep(5)

            second_next_button = driver.find_element(by=By.XPATH, value="//span[text()='Next']")
            second_next_button.click()
        
        time.sleep(5)

        password = driver.find_element(by=By.XPATH, value="//input[@name='password']")
        password.send_keys(self.password)

        login_button = driver.find_element(by=By.XPATH, value="//span[text()='Log in']")
        login_button.click()

        time.sleep(15)

        

    # When logging in twitter, sometimes, asked to prompt username because of unusual activity.
    def checkForUnusualActivity(self):
        driver = self.driver
        try:
            unusual_text = driver.find_element(by=By.XPATH, value="//span[text()='There was unusual login activity on your account. To help keep your account safe, please enter your phone number or username to verify it’s you.']")
        except NoSuchElementException:
            return False
        return True
    
    def goToBookMarks(self):
        driver = self.driver
        others_button = driver.find_element(by=By.XPATH, value="//span[text()='More']")

        others_button.click()

        time.sleep(5)

        bookmarks_button = driver.find_element(by=By.XPATH, value="//span[text()='Bookmarks']")

        bookmarks_button.click()

        time.sleep(7)

 
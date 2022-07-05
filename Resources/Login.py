from selenium.webdriver.support.ui import WebDriverWait
import browser
from selenium.webdriver.support import expected_conditions as EC


class Login:
    @staticmethod
    def navigate_to_pdds(url):
        browser.initBrowser()
        browser.goto(url)

    @staticmethod
    def input_username_and_password(username, password):
        globalBrowser = browser.getBrowser()
        usernameField = (globalBrowser.find_element(by="id", value="txtUserName"))
        passwordField = (globalBrowser.find_element(by="id", value="txtPassword"))
        usernameField.send_keys(username)
        passwordField.send_keys(password)

    @staticmethod
    def login_button_click():
        # Get the login button and click login
        globalBrowser = browser.getBrowser()
        loginBTN = globalBrowser.find_element(by="id", value="aLogin")
        wait = WebDriverWait(globalBrowser, 5).until(EC.element_to_be_clickable(loginBTN))
        wait.click()

    @staticmethod
    def validate_login(matchTitle):
        globalBrowser = browser.getBrowser()
        getTitle = globalBrowser.title
        return getTitle == matchTitle


from selenium import webdriver

browser = None


def initBrowser():
    # set options
    global browser
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Open Chrome Browser
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()



def getBrowser():
    global browser
    return browser


def goto(value):
    """
    Implementing load web page functionality
    Loads a web page in the current browser session.
    :param value: URL
    :return:
    """
    global browser
    # maximize_window()
    # delete_cookies()
    browser.get(value)


def close_test_browser():
    global browser
    browser.close()

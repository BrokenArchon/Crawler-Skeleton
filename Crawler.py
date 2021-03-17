from bs4 import BeautifulSoup

class Crawler():
    web_driver = None

    def __init__(self, custom_web_driver):
        self.web_driver = custom_web_driver

    def run(self):
        result = None

        browser = self.web_driver.getChromeBrowser('path_to_driver/chromedriver', True)
        browser.get('https://www.us-proxy.org')
        browser.page_source
        browser.quit()

        return result
import os
import logging
from bs4 import BeautifulSoup
from selenium import webdriver

class SeleniumWrapper:

    proxies = []

    def getChromeBrowser(self, webdriver_path, using_proxie = False):

        options = webdriver.ChromeOptions()

        options.add_experimental_option(
            'prefs',
            {
                'profile.managed_default_content_settings.images': 2,
                'permissions.default.stylesheet': 2
            }
        )

        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless') # hide browser

        seleniumLogFolder = '{0}/seleniumlog'.format(os.path.dirname(os.path.realpath(__file__)))

        if using_proxie:

            if not self.proxies:

                self.getProxiesFromFPL(webdriver.Chrome(
                    executable_path = webdriver_path,
                    chrome_options = options,
                    service_log_path = seleniumLogFolder
                ))

            proxie = self.proxies.pop()
            logging.info('Using http proxie server: {0}'.format(proxie))
            options.add_argument('--proxy-server={0}'.format(proxie))

        return webdriver.Chrome(
            executable_path = webdriver_path,
            chrome_options = options,
            service_log_path = seleniumLogFolder,
        )

    def getProxiesFromFPL(self, browser):

        # This method get proxies from Free Proxy List web site
        proxie_provider = 'https://www.us-proxy.org/'

        try:
            browser.get(proxie_provider)

            if browser.page_source:

                page = BeautifulSoup(browser.page_source, 'html.parser')
                browser.quit()

                proxies_table = page.find(id = 'proxylisttable')

                for row in proxies_table.tbody.find_all('tr'):

                    self.proxies.append(
                        'http://{0}:{1}'.format(row.find_all('td')[0].string, row.find_all('td')[1].string)
                    )

            else:
                logging.info('Proxy service is not availeble')

        except Exception as e:
            browser.quit()
            logging.error(str(e))
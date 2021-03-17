import Crawler
import CustomHelper
from CustomWebDriver import SeleniumWrapper

def main():
    CustomHelper.initiateLogger()
    custom_web_driver = SeleniumWrapper()
    crawler = Crawler(custom_web_driver)

    cr_data = crawler.run()

    # CustomHelper.saveAsFile(cr_data)

if __name__ == '__main__':
    main()

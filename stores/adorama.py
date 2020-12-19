from stores.stores import Store
import bs4
import requests


class Adorama(Store):

    def __init__(self):
        self.storeName = "Adorama"
        self.OOS_MSG = "Temporarily not available"

    def findTitle(self, browser):
        # To do. Not able to find the title
        return super().findTitle(browser)

    def checkInventory(self, url, browser):
        super().printUrl(url)
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        browser.get(url)
        # res.raise_for_status()
        # soup = bs4.BeautifulSoup(res.text, "lxml")
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        # soup.select
        if ((self.OOS_MSG in soup.text) or ("sold out" in soup.text)):
            print(self.storeName + " OOS XXX ")
            return False
        else:
            print(self.storeName + " *** HAS it")
            return True
# elem = soup.select_one('#XBRRT00001B_btn')
# elem.text == "\r\n    Temporarily not available\r\n    \r\n"
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# https://stackoverflow.com/questions/50454896/access-denied-while-scraping-a-website-with-selenium-in-python

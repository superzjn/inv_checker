from stores.stores import Store


class Newegg(Store):

    def __init__(self):
        self.storeName = "NewEgg"
        self.OOS_MSG = "SOLD OUT"

    def findTitle(self, browser):
        return super().findTitle(browser)

    def checkInventory(self, url, browser):
        super().printUrl(url)
        browser.get(url)
        elem = browser.find_element_by_id(
            'ProductBuy')
        if (elem.text == self.OOS_MSG):
            super().printOosMsg(browser)
            return False
        else:
            super().printInStoreMsg(browser)
            return True

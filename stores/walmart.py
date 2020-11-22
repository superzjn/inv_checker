from stores.stores import Store


class Walmart(Store):

    def __init__(self):
        self.storeName = "Walmart"
        self.OOS_MSG = "Add to cart"

    def findTitle(self, browser):
        return super().findTitle(browser)

    def checkInventory(self, url, browser):
        super().printUrl(url)
        browser.get(url)

        if (self.OOS_MSG not in browser.page_source):
            super().printOosMsg(browser)
            return False
        else:
            super().printInStoreMsg(browser)
            return True

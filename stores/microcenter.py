from stores.stores import Store


class MicroCenter(Store):

    def __init__(self):
        self.storeName = "MicroCenter"
        self.OOS_MSG = "\'inStock\':\'False\'"

    def findTitle(self, browser):
        return super().findTitle(browser)

    def checkInventory(self, url, browser):
        super().printUrl(url)
        browser.get(url)

        if (self.OOS_MSG in browser.page_source):
            super().printOosMsg(browser)
            return False
        else:
            super().printInStoreMsg(browser)
            return True

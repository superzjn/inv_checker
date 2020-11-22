from stores.stores import Store


class Bestbuy(Store):

    def __init__(self):
        self.storeName = "BestBuy"
        self.OOS_MSG = "Sold Out"

    def findTitle(self, browser):
        return browser.find_element_by_class_name('sku-title').text

    def checkInventory(self, url, browser):
        super().printUrl(url)
        browser.get(url)
        elem = browser.find_element_by_class_name(
            'fulfillment-add-to-cart-button')
        if (elem.text == self.OOS_MSG):
            super().printOosMsg(browser)
            return False
        else:
            super().printInStoreMsg(browser)
            return True

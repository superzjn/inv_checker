from stores.stores import Store


class Target(Store):

    def __init__(self):
        self.storeName = "Target"
        self.OOS_MSG = "Sold Out"  # not in use

    def findTitle(self, browser):
        return super().findTitle(browser)

    def checkInventory(self, url, browser):
        super().printUrl(url)
        browser.get(url)
        browser.implicitly_wait(10)

        try:
            elem = browser.find_element_by_xpath(
                "//button[contains(text(),'Ship it')]")
            super().printInStoreMsg(browser)
            return True

        except Exception as exc:
            super().printOosMsg(browser)
            return False

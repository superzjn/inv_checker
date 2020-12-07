from stores.stores import Store


class BHPhotoVideo(Store):

    def __init__(self, url):
        self.storeName = "BHPhotoVideo"
        self.OOS_MSG = "Notify When Available"
        self.url = url

    def findTitle(self, browser):
        return super().findTitle(browser)

    def checkInventory(self, url, browser):
        super().printUrl(url)
        browser.get(url)
        # elem = browser.find_element_by_xpath(
        #     "//button[contains(text(),'Notify When Available')]")
        # if (elem.text == self.OOS_MSG):
        if (self.OOS_MSG in browser.page_source):
            super().printOosMsg(browser)
            return False
        else:
            super().printInStoreMsg(browser)
            return True
